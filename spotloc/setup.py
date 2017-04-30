from setuptools import setup

setup(
    name='spotloc',
    version= '1.0.0',
    author ='Odysseas Lamtzidis',
    url = 'https://github.com/OdysLam/spotify-local-http-api',
    packages=['spotloc'],
    include_package_data=True,
    install_requires=['flask']
)