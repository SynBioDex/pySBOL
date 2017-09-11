Testing pySBOL
======================

pySBOL comes with a testing function to check the integrity of the library.
To run the tester, simply execute the following command.

.. code:: python

    import sbol
    sbol.testSBOL()
    
The output tells you whether certain test has been passed or not.

.. code:: python

    testAddComponentDefinition (sbol.unit_tests.TestComponentDefinitions) ... ok
    testCDDisplayId (sbol.unit_tests.TestComponentDefinitions) ... ok
    testRemoveComponentDefinition (sbol.unit_tests.TestComponentDefinitions) ... ok
    testAddSeqence (sbol.unit_tests.TestSequences) ... ok
    testRemoveSequence (sbol.unit_tests.TestSequences) ... ok
    testSeqDisplayId (sbol.unit_tests.TestSequences) ... ok
    testSequenceElement (sbol.unit_tests.TestSequences) ... ok
    testDiscard (sbol.unit_tests.TestMemory) ... ok

    