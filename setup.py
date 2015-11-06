try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Sends Bay Area daily tides and currents via SMS',
    'author': 'Etienne Pelletier',
    'author_email': 'epelletier@twilio.com',
    'version': '0.1',
    'install_requires': [
          'flask',
          'twilio',
          'requests',
      ],
    'scripts': [],
    'name': 'tidesandcurrents'
}


setup(**config)