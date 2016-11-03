import mimetypes
import urlparse
import os

from logging import getLogger

from pylons import config
from ckan.common import json

from ckan import plugins as p
import ckan.lib.helpers as h

try:
    from ckan.lib.datapreview import on_same_domain
except ImportError:
    from ckan.lib.datapreview import _on_same_domain as on_same_domain

ignore_empty = p.toolkit.get_validator('ignore_empty')
boolean_validator = p.toolkit.get_validator('boolean_validator')

log = getLogger(__name__)

TOLOMEO_FORMATS = ['wms', 'wfs']
TOLOMEO_PRESET_FORMATS = ['tolomeo:preset', 'tolomeo', 'webgis']


def get_proxified_service_url(data_dict):
    '''
    :param data_dict: contains a resource and package dict
    :type data_dict: dictionary
    '''
    controller = \
        'ckanext.tolomeo.controllers.service_proxy:ServiceProxyController'
    url = h.url_for(
        action='proxy_service',
        controller=controller,
        id=data_dict['package']['name'],
        resource_id=data_dict['resource']['id'])
    log.debug('Proxified url is {0}'.format(url))
    return url


class GeoViewBase(p.SingletonPlugin):
    '''This base class is for view extensions. '''
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IConfigurable, inherit=True)

    proxy_enabled = False
    same_domain = False

    def update_config(self, config):
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('public', 'ckanext-tolomeo')

        self.proxy_enabled = 'resource_proxy' in config.get('ckan.plugins', '')


class TolomeoView(GeoViewBase):
    p.implements(p.ITemplateHelpers, inherit=True)

    # IResourceView (CKAN >=2.3)
    def info(self):
        return {'name': 'tolomeo_view',
                'title': 'tolomeo',
                'icon': 'map-marker',
                'iframed': True,
                'default_title': p.toolkit._('Tolomeo'),
                }

    def can_view(self, data_dict):
        resource = data_dict['resource']
        format_lower = resource.get('format', '').lower()

        if format_lower in TOLOMEO_FORMATS:
            return True
#            return self.same_domain or self.proxy_enabled
        return False

    def view_template(self, context, data_dict):
        return 'dataviewer/tolomeo.html'

    def setup_template_variables(self, context, data_dict):
        import ckanext.resourceproxy.plugin as proxy
        self.same_domain = data_dict['resource'].get('on_same_domain')
        if self.proxy_enabled and not self.same_domain:
            data_dict['resource']['original_url'] = data_dict['resource'].get('url')
            data_dict['resource']['url'] = proxy.get_proxified_resource_url(data_dict)

    ## ITemplateHelpers
    def get_tolomeo_config(self):
        '''
            Returns a dict with all configuration options related to the
            Tolomeo viewer (ie those starting with 'ckanext.tolomeo.')
        '''
        namespace = 'tolomeo.'
        return dict([(k.replace(namespace, ''), v) for k, v in config.iteritems()
                     if k.startswith(namespace)])

    def get_helpers(self):
        return {
            'get_tolomeo_config' : self.get_tolomeo_config,
        }


class TolomeoPresetView(GeoViewBase):
    p.implements(p.IResourceView, inherit=True)

    # IResourceView (CKAN >=2.3)
    def info(self):
        return {'name': 'tolomeo_preset_view',
                'title': 'tolomeo_preset',
                'icon': 'map-marker',
                'iframed': False,
                'default_title': p.toolkit._('WebGIS Tolomeo'),
                }

    def can_view(self, data_dict):
        resource = data_dict['resource']
        format_lower = resource.get('format', '').lower()

        return format_lower in TOLOMEO_PRESET_FORMATS

    def view_template(self, context, data_dict):
        return 'dataviewer/tolomeo_preset.html'
