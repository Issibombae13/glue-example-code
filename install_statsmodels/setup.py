from setuptools import setup

setup(name="install_statsmodels",
        version="0.1",
        packages=['install_statsmodels'],
        install_requires=['statsmodels==0.9.0', 'pandas==0.25.1', 's3fs==0.4.2']
    )

