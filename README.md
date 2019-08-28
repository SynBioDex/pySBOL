# SBOL 3.0.0

**SBOL** is a pure Python implementation of the SBOL standard [Synthetic Biology Open Language (SBOL)](http://www.sbolstandard.org/) - 
an open standard for the representation of *in silico* biological designs. It draws from [libSBOL](https://github.com/SynBioDex/libSBOL)
and [pySBOL](https://github.com/SynBioDex/pySBOL).

## INSTALLATION

This library is currently under development. To test it out, follow these steps:
1) Clone this repository.
2) (From top-level directory) `pip install -e .`
3) Open a python3 interpreter, and import sbol3.

## TESTING

SBOL comes with a testing function to check the integrity of the library. To run the unit tests, simply execute the following command.
```python
import sbol3
sbol3.testSBOL()
```
SBOL also comes with a suite of 'round-trip' tests to verify that serialization and deserialization of SBOL files works correctly.
To run the round-trip tests, execute the following command.
```python
import sbol3
sbol3.testRoundTrip()
```

## DOCUMENTATION

To be updated.

## ACKNOWLEDGEMENTS

To be updated.

<p align="center">
  <img src="./logo.jpg" height="100" />
</p>
