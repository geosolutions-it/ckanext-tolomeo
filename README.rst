=======================================================================
ckanext-tolomeo - Geospatial viewer for CKAN resources based on Tolomeo
=======================================================================

This extension contains a view plugin to display geospatial resources in CKAN (>2.3).

You can find more info on Tolomeo at http://tolomeogis.comune.prato.it/ .

------------------------
Development Installation
------------------------

To install ckanext-tolomeo for development:

1. Clone the source::

    cd /usr/lib/ckan/default/src
    git clone https://github.com/geosolutions-it/ckanext-tolomeo.git

2. Activate your CKAN virtual environment, for example::

    . /usr/lib/ckan/default/bin/activate

3. Install the ckanext-geoview Python package into your python virtual environment::

    cd ckanext-tolomeo
    python setup.py develop

4. Update the list of plugins adding this one. Edit the ``.ini`` file and add::

    ckan.plugins = ... tolomeo_view
    ckan.views.default_views = ... tolomeo_view

5. In the ``.ini`` file add the configuration needed for Tolomeo; e.g.::

    tolomeo_preset = Cerco
    tolomeo_base_url = http://www.opendatanetwork.it/tolomeo

6. Restart CKAN.

7. Add the views to all the dataset containing WMS resources::

    paster --plugin=ckan views create    --config=/etc/ckan/default/production.ini


----------------
Other extensions
----------------

This extension follows the structure of ckanext-geoview_, which offers views for a wider range of formats.

.. _ckanext-spatial: https://github.com/ckan/ckanext-spatial
.. _ckanext-geoview: https://github.com/ckan/ckanext-geoview
