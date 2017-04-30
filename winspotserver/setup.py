from setuptools import setup

setup(
    name='winspotserver',
    version= '1.0.0',
    author ='Odysseas Lamtzidis',
    url = 'https://github.com/OdysLam/spotify-local-http-api',
    packages=['winspotservice'],
    include_package_data=True,
    install_requires=['flask']
)