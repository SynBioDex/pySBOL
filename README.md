# pySBOL 2.1.0

**pySBOL2** is a SWIG-Python wrapper around [libSBOL](https://github.com/SynBioDex/libSBOL), a module for reading, writing, and constructing genetic designs according to the standardized specifications of the [Synthetic Biology Open Language (SBOL)](http://www.sbolstandard.org/).  

## INSTALLATION

### Using Python
Python by default comes with package installer. Follow the steps below to install pySBOL2. If you have Windows, and would like to try our Windows binary installers, check [Using Installer for Windows](https://github.com/SynBioDex/pysbol2#Using-Installer-for-Windows) section.
1 - [Download the source code of latest release here](https://github.com/SynBioDex/pysbol2/releases/latest) and extract it.
If you would like to try out our latest snapshot, use [git](https://git-scm.com/) and type following command in the console or terminal which will clone the source under pysbol2 folder.
```
git clone https://github.com/SynBioDex/pysbol2.git
```
2 - Open your console or terminal. Go to package's root directory and Run the installer script by using the following command line. This will install pySBOL2 to the Python release associated with the console or terminal you are using.
```
python setup.py install
```
**If you are having problems, make sure your console/terminal is associated and associated with the right Python environment you wish to use.**
3 - Test the pySBOL2 by importing it in Python.
```
import sbol
print(sbol.__version__)
```
**If you have trouble importing the module with the setup script, check to see if there are multiple Python installations on your machine and also check the output of the setup script to see which version of Python is the install target. You can also test the module locally from inside the Mac_OSX/sbol or Win_32/sbol folders.**

### Using Installer for Windows

We provide binary installers for Windows users only. Currently, we support Python 2.7 and Python 3.5 for both 32 bit and 64 bit architecture.
Simply [download the installers](https://github.com/SynBioDex/pysbol2/releases/latest) and execute it to install it. Installer will look for your local Python distributions.
**Be sure to use the installers with the same Python version and architecture with the one installed in your local machine!**

## ACKNOWLEDGEMENTS

pySBOL2 is brought to you by Bryan Bartley, Kiri Choi, and SBOL Developers.

Current support for the development of pySBOL is generously provided by the NSF through the [Synthetic Biology Open Language Resource](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1355909) collaborative award.

<p align="center">
  <img src="./logo.jpg" height="100" />
</p>
