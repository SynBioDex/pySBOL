__author__ = 'user'

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path, chdir
from sys import maxsize
from sys import version, version_info
# Determine if Windows or Mac
import platform

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

def get_config():
    if maxsize == 2147483647:
        python_interpreter_architecture = 32
    elif maxsize == 9223372036854775807:
        # May not detect Windows x64 (maxsize = 2147483647)!
        python_interpreter_architecture = 64
    else:
        python_interpreter_architecture = 0
    if version_info[0] == 2:
        python_version = 2
    elif version_info[0] == 3:
        python_version = 3
    else:
        python_version = 0
    if platform.system() == 'Darwin':
        platform_system = 'Mac'
    elif platform.system() == 'Windows':
        platform_system = 'Win'
    else:
	    platform_system = 'Linux'
    return (platform_system, python_interpreter_architecture, python_version)

config = get_config()
print("Installing libSBOL binaries for %s %d-bit %s" %(config[0], config[1], version))
# Reconstruct path to binaries based on the system and Python interpreter architecture
package_dir = "%s_%d_%d" %(config[0], config[1], config[2])
print(package_dir)
if config[0] == 'Win':
    chdir(path.join(here,package_dir))
    package_data={
    'sbol': ['examples/*'],
      'sbol.test': ['*.*', 'SBOL2/*.*', 'SBOL2_bp/*.*', 'SBOL2_ic/*.*', 'SBOL2_nc/*.*'],
    'sbol': ['_libsbol.pyd', 'libsbol.py', 'crispr_example.xml']
    }
elif config[0] == 'Mac':
    chdir(path.join(here,package_dir))
    package_data={
      'sbol': ['examples/*'],
      'sbol.test': ['*.*', 'SBOL2/*.*', 'SBOL2_bp/*.*', 'SBOL2_ic/*.*', 'SBOL2_nc/*.*'],
      'sbol': ['_libsbol.so', 'libsbol.py', 'crispr_example.xml']
    }
else:
    chdir(path.join(here, package_dir))
    package_data={
      'sbol': ['examples/*'],
      'sbol.test': ['*.*', 'SBOL2/*.*', 'SBOL2_bp/*.*', 'SBOL2_ic/*.*', 'SBOL2_nc/*.*'],
      'sbol': ['_libsbol.so', 'libsbol.py', 'crispr_example.xml']
    }
	
setup(
    name='pySBOL',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='2.3.3.post1',

    description='A module for reading, writing, and constructing genetic designs according to the standardized specifications of the Synthetic Biology Open Language (SBOL).',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/SynBioDex/pySBOL',

    # Author details
    author='Bryan Bartley',
    author_email='editors@sbolstandard.org',

    # Choose your license
    license='Apache-2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],

    # What does your project relate to?
    keywords='synthetic biology',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages = ['examples'],
    #packages = ['sbol']  # No subdirectory named sbol
    packages=['sbol', 'sbol.test'],
    #packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    #install_requires=['peppercorn'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data=package_data,
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
   # },
      zip_safe = False,
      #include_package_data = True
)
