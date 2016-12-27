Testing pySBOL
======================

pySBOL comes with a testing function to check the integrity of the library.
To run the tester, simply execute the following command.

.. code:: python

    import sbol
    sbol.testSBOL()
    
The output tells you whether certain test has been passed or not.

.. code:: python

    test_round_trip (sbol.unit_tests.TestRoundTrip) ... Setting up
    ok