Getting Started with SBOL
=============================

This beginner’s guide introduces the basic principles of pySBOL for new users. For more comprehensive documentation about the API, refer to documentation about specific classes and methods for detailed information about the API. For more detail about the SBOL standard, visit `sbolstandard.org <http://sbolstandard.org>`_ or'refer to the `specification document <http://sbolstandard.org/downloads/specifications/specification-data-model-2-0-1/>`_.

-------------------------
Creating an SBOL Document
-------------------------

In a previous era, engineers might sit at a drafting board and draft a design by hand. The engineer's drafting sheet in LibSBOL is called a Document. The Document serves as a container, initially empty, for SBOL data objects. All file I/O operations are performed on the Document to populate it with SBOL objects representing design elements. Usually the first step is to create an SBOLDocument in which to put your objects. This can be done by calling the Document constructor.  The read and write methods are used for reading and writing files in SBOL format.

.. code:: python

    doc = Document()
    doc.read("CRISPR_example.xml")
    print (len(Document))
    doc.write("CRISPR_example.xml")
.. end

Reading a Document will wipe any existing contents clean before import. However, you can import objects from multiple files into a single Document object using `Document.append() <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.libsbol.Document.append>`_. This can be advantageous when you want to integrate multiple ComponentDefinitions from multiple files into a single design, for example.

A Document may contain different types of SBOL objects, including ComponentDefinitions, ModuleDefinitions, Sequences, SequenceAnnotations, and Models. These objects are collectively referred to as Top Level objects because they can be referenced directly from a Document. The total count of objects contained in a Document is determined using the ``len`` function.

In order to review the ComponentDefinitions contained in a Document, use a Python iterator:

.. code:: python

    for cd in doc.componentDefinitions:
       print cd
.. end

This will print the unique identity of each object (see the next section). Similarly, you can iterate through `Document.moduleDefinitions() <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.libsbol.Document.getModuleDefinition>`_, `Document.sequences() <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.libsbol.Document.getSequence>`_, 
`Document.sequenceAnnotations() <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.libsbol.SequenceAnnotation>`_, and `Document.models() <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.libsbol.Document.getModel>`_.

--------------------------
Creating SBOL Data Objects
--------------------------

Both structural and functional details of biological designs can be described with SBOL data objects.  The principle classes for describing the structure and primary sequence of a design are ComponentDefinitions, Components, and Sequences, SequenceAnnotations.  The principle classes for describing the function of a design are ModuleDefinitions, Modules, and Interactions. In the official SBOL specification document, these classes and their properties are represented as a special kind of box diagram. Each box represents a record of data thats describe a particular kind of SBOL object. For example, following is the diagram for a ComponentDefinition which will be referred to in later sections.

.. figure:: ../component_definition_uml.png
    :align: center
    :figclass: align-center

When a new object is created, it must be assigned a unique identity, or uniform resource identifier (URI). A typical URI consists of a scheme, a namespace, and an identifier, although other forms of URI's are allowed.  In this tutorial, we use URI's of the type ``http://sys-bio.org/my_design``, where the scheme is indicated by ``http://``, the namespace is ``sys-bio.org`` and the identifier is ``my_design``.

Objects can be created by calling their respective constructors. The following constructs a ModuleDefinition:

.. code:: python

    crispr_template = ModuleDefinition('http://sys-bio.org/CRISPRTemplate')
.. end

LibSBOL provides a few global configuration options that make URI construction easy. The first configuration option allows you to specify a default namespace for new object creation. If the default namespace is set, then only an identifier needs to be passed to the constructor.  This identifier will be automatically appended to the default namespace. Setting the default namespace is like signing your homework and claims ownership of an object.

.. code:: python

    setHomespace("http://sys-bio.org")
    crispr_template = ModuleDefinition("CRISPRTemplate")
    print (crispr_template.identity.get())
.. end

Another configuration option enables automatic construction of SBOL-compliant URIs. These URIs consist of a namespace, an identifier, AND a Maven version number. In addition, SBOL-compliance simplifies autoconstruction of certain types of SBOL objects, as we will see later.  LibSBOL operates in SBOL-compliant mode by default. However, some power users will prefer to operate in "open-world" mode and provide the full raw URI when constructing objects. To disable URI construction, SBOL-compliance use ``setOption('sbol_compliant_uris', 'False')``.

Some constructors have required fields. In the specification document, required fields are indicated as properties with a cardinality of 1 or more.  For example, a ComponentDefinition (see the UML diagram above) has only one required field, the type, which specifies the molecular type of a component.  Arguments to a constructor are always determined by whether the official SBOL specification document indicates if it is required.  Required fields SHOULD be specified when calling a constructor.  If they are not, then they will be assigned default values.  The following creates a protein component. If the BioPAX term for protein were not specified, then the constructor would create a ComponentDefinition of DNA by default.

.. code:: python

    cas9 = ComponentDefinition("Cas9", BIOPAX_PROTEIN)
.. end

Notice the type is specified using a predefined constant. The ``ComponentDefinition.types`` property is one of many SBOL properties that use standard ontology terms as property values.  The ``ComponentDefinition.types`` property uses the Sequence Ontology to be specific.  Many commonly used ontological terms are provided by libSBOL as predefined constants in the `constants.h <https://github.com/SynBioDex/libSBOL/blob/develop/source/constants.h>`_ header.  See the help page for the `sbol.ComponentDefinition <https://pysbol2.readthedocs.io/en/latest/API.html#sbol.libsbol.ComponentDefinition>`_ class or other specific class to find a table that lists the available terms.

----------------------------
Adding Objects to a Document
----------------------------

In some cases a developer may want to use SBOL objects as intermediate data structures in a computational biology workflow.  In this case the user is free to manipulate objects independently of a Document.  However, if the user wishes to write out a file with all the information contained in their object, they must first add it to the Document.  This is done using a templated add method.

.. code:: python

    doc.addModuleDefinition(crispr_template)
    doc.addComponentDefinition(cas9)
.. end

Only TopLevel objects need to be added to a Document. These top level objects include ComponentDefinitions, ModuleDefinitions, Sequences, Models. Child objects are automatically associated with the parent object's Document.

---------------------------------------------
Getting, Setting, and Editing Optional Fields
---------------------------------------------

Objects may also include optional fields.  These are indicated in UML as properties having a cardinality of 0 or more. Except for the molecular type field, all properties of a ComponentDefinition are optional.  Optional properties can only be set after the object is created. The following code creates a DNA component which is designated as a promoter:

.. code:: python

    target_promoter = ComponentDefinition('TargetPromoter', BIOPAX_DNA, '1.0.0')
    target_promoter.roles.set(SO_PROMOTER)
.. end

All properties have a set and a get method. To view the value of a property:

.. code:: python

    print(target_promoter.roles.get())
.. end

This returns the string ``http://identifiers.org/so/SO:0000167`` which is the Sequence Ontology term for a promoter.

Note also that some properties support a list of values.  A property with a cardinality indicated by an asterisk symbol indicates that the property may hold an arbitrary number of values.  For example, a ComponentDefinition may be assigned multiple roles.  Calling ``set`` on a method always overwrites the first value of a property, while the ``add`` method always appends a value to the end of a list.

.. code:: python

    target_promoter.roles.add(SO "0000568")
.. end

----------------------------------
Creating and Editing Child Objects
----------------------------------

Some SBOL objects can be composed into hierarchical parent-child relationships.  In the specification diagrams, these relationshipss are indicated by black diamond arrows.  In the UML diagram above, the black diamond indicates that ComponentDefinitions are parents of SequenceAnnotations.  Properties of this type can be modified using the add method and passing the child object as the argument.

.. code:: python

    point_mutation = SequenceAnnotation("PointMutation");
    target_promoter.annotations.add(point_mutation);
.. end

If you are operating in SBOL-compliant mode, you may prefer to take a shortcut:

.. code:: python

    target_promoter.annotations.create("PointMutation");
.. end

The create method captures the construction and addition of the SequenceAnnotation in a single function call. Another advantage of the create method is the construction of SBOL-compliant URIs. If operating in SBOL-compliant mode, you will almost always want to use the create method.  The create method ALWAYS takes one argument--the URI of the new object. All other values are initialized with default values. You can change these values after object creation, however. When operating in open-world mode, it is preferable to follow the first example and use the constructor and add method.

-----------------------------------------
Creating and Editing Reference Properties
-----------------------------------------

Some SBOL objects point to other objects by way of references. For example, ComponentDefinitions point to their corresponding Sequences. Properties of this type should be set with the URI of the related object.

.. code:: python

    eyfp_gene = ComponentDefinition("EYFPGene", BIOPAX_DNA);
    seq = Sequence("EYFPSequence", "atgnnntaa", SBOL_ENCODING_IUPAC);
    eyfp_gene.sequences.set(seq.identity.get());
.. end

--------------------------------------
Iterating and Indexing List Properties
--------------------------------------

Some properties can contain multiple values or objects. Additional values can be specified with the add method.  In addition you may iterate over lists of objects or values.

.. code:: python

    # Iterate through objects (black diamond properties in UML)
    for p in cas9_complex_formation.participations:
        print(p)
        print(p.roles.get())

    # Iterate through references (white diamond properties in UML)
    for role in reaction_participant.roles.begin():
        print(role)
.. end

Numerical indexing of lists works as well:

.. code:: python

    for i_participation in range(0, len(cas9_complex_formation.participations)):
        print(cas9_complex_formation.participations[i_participation])
.. end

This concludes the basic methods for manipulating SBOL data structures. Now that you're familiar with these basic methods, you are ready to learn about libSBOL's high-level design interface for synthetic biology. See `SBOL Examples <https://pysbol2.readthedocs.io/en/latest/sbol_examples.html>`_.