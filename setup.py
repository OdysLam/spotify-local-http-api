from setuptools import setup

setup(
    name='spot_server',
    version= '1.0.0',
    author ='Odysseas Lamtzidis',
    url = 'https://github.com/OdysLam/spotify-local-http-api',
    packages=['spot_server'],
    include_package_data=True,
    install_requires=['flask']
)