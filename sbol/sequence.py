from constants import *
from toplevel import *
from deprecated import deprecated

class Sequence(TopLevel):
    """The primary structure (eg, nucleotide or amino acid sequence) of a ComponentDefinition object."""

    def __init__(self, uri="example", elements="", encoding=SBOL_ENCODING_IUPAC,
                 version=VERSION_STRING, type_uri=SBOL_SEQUENCE):
        """Construct a Sequence.

        :param uri: A full URI including a scheme, namespace, and identifier.
        If SBOLCompliance configuration is enabled, then this argument is simply the displayId for the new object
        and a full URI will automatically be constructed.
        :param elements: A string representation of the primary structure of DNA, RNA, protein,
        or a SMILES string for small molecules.
        :param encoding: A URI that describes the representation format used for the elements property.
        Set to SBOL_ENCODING_IUPAC by default
        :param version: An arbitrary version string. If SBOLCompliance is enabled,
        this should be a Maven version string.
        :param type_uri: The RDF type for an extension class derived from this one.
        """
        super().__init__(type_uri, uri, version)

    # The elements property is a REQUIRED String of characters that represents the constituents of a biological
    # or chemical molecule. For example, these characters could represent the nucleotide bases of a molecule of DNA,
    # the amino acid residues of a protein, or the atoms and chemical bonds of a small molecule.
    elements = None

    # The encoding property is REQUIRED and has a data type of URI. This property MUST indicate how the elements
    # property of a Sequence MUST be formed and interpreted. For example, the elements property of a Sequence with an
    # IUPAC DNA encoding property MUST contain characters that represent nucleotide bases, such as a, t, c, and g.
    # The elements property of a Sequence with a Simplified Molecular-Input Line-Entry System (SMILES) encoding,
    # on the other hand, MUST contain characters that represent atoms and chemical bonds, such as C, N, O, and =.
    #
    # It is RECOMMENDED that the encoding property contains a URI from the table below. The terms in the table are
    # organized by the type of ComponentDefinition that typically refer to a Sequence with such an encoding.
    # When the encoding of a Sequence is well described by one of the URIs in the table, it MUST contain that URI.
    # | ComponentDefinition type  | Encoding       | libSBOL Symbol              | URI                                              |
    # | :------------------------ | :--------------| :-------------------------- | :----------------------------------------------- |
    # | DNA, RNA                  | IUPAC DNA, RNA | SBOL_ENCODING_IUPAC         | http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html |
    # | Protein                   | IUPAC Protein  | SBOL_ENCODING_IUPAC_PROTEIN | http://www.chem.qmul.ac.uk/iupac/AminoAcid/      |
    # | Small Molecule            | SMILES         | SBOL_ENCODING_SMILES        | http://www.opensmiles.org/opensmiles.html        |
    encoding = None

    def assemble(self, composite_sequence=""):
        """Calculates the complete sequence of a high-level Component from the sequence of its subcomponents.

        Prior to assembling the the complete sequence, you must assemble a template design by calling
        ComponentDefinition::assemble for the ComponentDefinition that references this Sequence.

        :param composite_sequence: Typically no value for the composite sequence should be specified by the user.
        This parameter is used to hold the composite sequence as it is passed to function calls
        at a higher-level of the recursion stack.
        :return: The complete sequence of a high-level Component.
        """
        raise NotImplementedError("Not yet implemented")

    def compile(self):
        """Synonomous with Sequence::assemble.

        Calculates the complete sequence of a high-level Component from the sequence of its subcomponents.
        Prior to assembling the the complete sequence, you must assemble a template design by calling
        ComponentDefinition::assemble for the ComponentDefinition that references this Sequence.

        :return:
        """
        raise NotImplementedError("Not yet implemented")

    def __len__(self):
        """

        :return: The length of the primary sequence in the elements property.
        """
        raise NotImplementedError("Not yet implemented")

    @deprecated(version='3.0.0', reason='Use len(sequence) instead')
    def length(self):
        """

        :return: The length of the primary sequence in the elements property.
        """
        return len(self)

    def synthesize(self, clone_id):
        """

        :param clone_id: A URI for the build, or displayId if working in SBOLCompliant mode.
        :return:
        """
        raise NotImplementedError("Not yet implemented")