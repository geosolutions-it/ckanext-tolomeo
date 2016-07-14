from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='ckanext-tolomeo',
    version=version,
    description='CKAN Tolomeo ResourceView',
    long_description=''' ''',
    classifiers=[],
    keywords='',
    author='Emanuele Tajariol (GeoSolutions)',
    author_email='etj@geo-solutions.it',
    url='http://github.com/geosolutions-it/ckanext-tolomeo',
    license='GPL3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
    [ckan.plugins]
    tolomeo_view=ckanext.tolomeo.plugin:TolomeoView
    ''',

)
