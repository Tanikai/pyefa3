from setuptools import setup
import pyefa

setup(name='pyefa',
	version=pyefa.__version__,
	description='Python-Bindings for online train connection APIs.',
	author='Nils Martin Klünder',
	author_email='nomoketo@nomoketo.de',
	url='https://github.com/NoMoKeTo/pyefa',
	packages=['pyefa'],
	license='Apache',
	classifiers=[
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Intended Audience :: Developers',
		'Programming Language :: Python',
		'License :: OSI Approved :: Apache Software License'],
	install_requires=['beautifulsoup4', 'colorama'],
	)
