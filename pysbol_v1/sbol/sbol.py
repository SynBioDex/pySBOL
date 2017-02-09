## @package sbol
# A Python wrapper for libSBOLc, a module for reading, writing, and constructing
# genetic designs according to the standardized specifications of the Synthetic Biology Open Language
#
# @file sbol.py
# Implements a high-level, Pythonic interface for the SWIG-Python classes in libsbol
#
# @namespace sbol.sbol
# High level wrappers for libSBOLc
#
# @namespace sbol.libsbol
# Low level SWIG-Python wrappers for libSBOLc
#
# @namespace sbol.sbol_test
# Unit tests

import libsbol
import sys
from cStringIO import StringIO

# SO terms
PROMOTER = "http://purl.obolibrary.org/obo/SO_0000167"
RBS = "http://purl.obolibrary.org/obo/SO_0000552"
CDS = "http://purl.obolibrary.org/obo/SO_0000316"
TERMINATOR = "http://purl.obolibrary.org/obo/SO_0000141"
USER_DEFINED = "http://purl.obolibrary.org/obo/SO_0000001"
DESIGN = "http://purl.obolibrary.org/obo/SO_0000546"
SCAR = "http://purl.obolibrary.org/obo/SO_0001953"

class SBOLError(Exception):     'Problem with SBOL'
class InternalError(SBOLError): 'Encountered a bug'
class URIError(SBOLError):      'Invalid URI'
class PositionError(SBOLError): 'Invalid position'
class StrandError(SBOLError):   'Invalid strand polarity'

__all__ = (
    'SBOLError',
    'InternalError',
    'URIError',
    'PositionError',
    'StrandError',
    'Document',
    'DNASequence',
    'SequenceAnnotation',
    'DNAComponent',
    'Collection' )

## The SBOL print functions use printf() to print directly
# to stdout; this captures that output and returns it for
# use in Python's __str__ methods.
def capture_stdout(fn, *args, **kwargs):
    backup = sys.stdout
    sys.stdout = StringIO()
    fn(*args, **kwargs)
    output = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = backup
    return output


## An array that partly supports Python list-like operations including
# slice indexing.  A proxy for libSBOLc PointerArrays.
# Members of the array may be one type of SBOL core objects (eg, DNAComponents)
# Members of the array may be referenced by numerical index (eg,
# sbol.Document.components[0]). In addition, the array behaves like a dictionary
# indexed by an object's URI
# (eg, sbol.Document.components['http://examples.com/0001']).<br>
# The sbol.Document class contains 4 instances of SBOLObjectArrays that
# each register a core type of SBOL object: DNAComponents, DNASequences,
# SequenceAnnotations, and Collections.  Each instance of a SBOLObjectArray
# is initialized to contain one of these type of objects.  The accessor methods
# specific to the type of object are passed as callback function arguments to
# the SBOLObjectArray constructor.<br>
# Accessor methods used by the SBOLObjectArray conform to the following pattern:
# |Accessor  | Return value                                   | Example callback           |
# |----------|------------------------------------------------|----------------------------|
# |get_uri_fn| Returns the object's URI                       | libsbol.getDNAComponentURI |
# |remove_fn | Remove the object from the array               | libsbol.removeDNAComponent |
# |get_num_fn| Get the num of objects in the array            | libsbol.getNumDNAComponents|
# |get_nth_fn| Get the array element whose index is specified | libsbol.getNthDNAComponent |
# <br>
# Instances of SBOL objects are registered in a Document automatically when
# created and cannot exist independently of a parent Document. Consequently,
# SBOLObjectArrays do not require an "add child to parent" accessor function
# (see SBOLObjectExtendableArray)
class SBOLObjectArray(object):
    ## Construct an SBOLObjectArray
    # @param obj A pointer to the PySBOL object that will own this array.
    # Typically the obj will be the parent Document object.
    # @param get_uri Callback function for retrieving an SBOL object's URI
    # @param remove Callback function that will remove an object from this array
    # @param num Callback function that returns the number of objects in the array
    # @param nth Callback function that returns an object with the specified index
    def __init__(self, obj, get_uri, remove, num, nth):
        ## A pointer to the PySBOL object owns this array.
        self.ptr = obj.ptr
        if isinstance(obj, Document):
            self.doc = obj
        else:
            self.doc = obj.doc

        # Each type of SBOL object has its own array functions,
        # which need to be set for the wrapper to work.
        ## Accessor method used by SBOLObjectArray to retrieve an element object's URI
        self.get_uri_fun = get_uri
        ## Accessor method used by SBOLObjectArray to remove an element object from the array
        self.remove_fn = remove
        ## Accessor method used by SBOLObjectArray to get the number of objects in the array
        self.get_num_fn = num
        ## Accessor method used by SBOLObjectArray to retrieve an object of specified index
        # from array
        self.get_nth_fn = nth

    ## implements 'len(array)'
    def __len__(self):
        return self.get_num_fn(self.ptr)

    ## Checks if key is indices or a URI
    # distinguishes 'array[index]' from 'array[start:end:step]
    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = key.indices( len(self) )
            return [self._getsingle_(n) for n in range(*indices)]
        elif isinstance(key, str):
            # Make a list of URIs for the objects in this array
            uris = [ self.get_uri_fun(self.get_nth_fn(self.ptr, n)) for n in range(self.get_num_fn(self.ptr))]
            # Then search the list for an element matching the key
            ind = uris.index(key)
            ptr = self.get_nth_fn(self.ptr, ind)
            obj = self.doc._proxy(ptr)
            return obj
        else: # assume int-like object
            if key < 0: # indexed from end
                key += len(self)
            return self._getsingle_(key)

    ## implements 'array[index]'
    def _getsingle_(self, index):
        num = self.get_num_fn(self.ptr)
        if index >= num:
            raise IndexError
        ptr = self.get_nth_fn(self.ptr, index)
        obj = self.doc._proxy(ptr)
        return obj

    ## implements 'for obj in array:'
    def __iter__(self):
        num = self.get_num_fn(self.ptr)
        for n in range(num):
            ptr = self.get_nth_fn(self.ptr, n)
            obj = self.doc._proxy(ptr)
            yield obj

    ## implements 'obj in array'
    def __contains__(self, obj):
        for candidate_obj in self:
            if candidate_obj == obj:
                return True
        return False

    ## implements 'print array'
    def __str__(self):
        if len(self) == 0:
            return '[]'
        output = []
        output.append('[')
        for obj in self[:-1]:
            output.append(obj.__repr__())
            output.append(', ')
        output.append(self[-1].__repr__())
        output.append(']')
        return ''.join(output)

    ## implements 'array' (print in the interpreter)
    def __repr__(self):
        return self.__str__()

    ## implements array.remove(obj)
    def remove(self, obj):
        self.remove_fn(self.ptr, obj.ptr)


## The ExtendableSBOLObjectArray contains a list of SBOL objects
# that CAN exist independently of a parent, in contrast to the SBOLObjectArray
# in which a parent-child relationship is mandated.  As a result the
# ExtendableSBOLObjectArray has one extra accessor function compared to
# an SBOLObjectArray, the add_fn, that allows the client user to manually
# add a child object to a parent.
# <br>
# Accessor methods used by the ExtendableSBOLObjectArray conform to the
# following pattern:
# |Accessor  | Return value                             | Example callback                                 |
# |----------|------------------------------------------|--------------------------------------------------|
# |get_uri_fn| Returns the object's  URI                | libsbol.getSequenceAnnotationURI                 |
# |add_fn    | Add this child object to a parent        | libsbol.addSequenceAnnotation                    |
# |remove_fn | Remove the object from the array         | libsbol.removeSequenceAnnotationFromDNAComponent |
# |get_num_fn| Get the num of objects in the array      | libsbol.getNumSequenceAnnotationsFor             |
# |get_nth_fn| Get the array element of specified index | libsbol.getNthSequenceAnnotationFor              |
class ExtendableSBOLObjectArray(SBOLObjectArray):
    ## Construct an ExtendableSBOLObjectArray
    # @param obj A pointer to the PySBOL object that owns this array
    # @param get_uri Callback function for retrieving an SBOL object's URI
    # @param add Callback function that will register this object in a parent's
    # ExtendableSBOLObjectArray
    # @param remove Callback function that will remove an object from this array
    # @param num Callback function that returns the number of objects in the array
    # @param nth Callback function that returns an object with the specified index
    def __init__(self, obj, get_uri, add, remove, num, nth):
        SBOLObjectArray.__init__(self, obj, get_uri, remove, num, nth)
        ## Accessor method used by ExtendableSBOLObjectArray to add a child object
        # to a parent
        self.add_fn = add

    ## implements 'array += obj'
    def __iadd__(self, obj):
        if obj in self:
            raise SBOLError('Duplicate obj %s' % obj)
        self.add_fn(self.ptr, obj.ptr)
        return self

    ## implements 'array.append(obj)'
    def append(self, obj):
        self.__iadd__(obj)

    ## implements 'array += obj_list'
    def __extend__(self, obj_list):
        for obj in obj_list:
            self += obj

## URIToSBOLObjectAssociativeArray
#
#class Precedes(ExtendableSBOLObjectArray):
#    #def __init__(self, doc, uri, get_uri, add, remove, num, nth):
#    #    obj = doc._getSBOLObjectByURI(doc, uri)        
#    #    ExtendableSBOLObjectArray.__init__(self, obj, get_uri, remove, num, nth)
#    
#    def _getSBOLObjectByURI(doc, uri):
#        obj = None         
#        for ann in doc.annotations:
#            if ann.uri == uri:
#                obj = ann
#        return obj
        
## Represents an SBOL document that can be read from or written to a file.
# It also holds a registry of all the SBOL objects in the document,
# so it can be used for iterating through all the objects of a certain kind,
# retrieving the object with a certain URI, checking the type of an object, etc.
# Deleting a Document also deletes the SBOL objects it contains.
# Each SBOL object must be associated with a document, for two main reasons:
# to ensure that its URI is unique, and to make memory management simpler.
# @todo Objects should be able to belong to multiple documents
class Document(object):
    ## Construct a Document
    def __init__(self):
        # create document
        ## Pointer to the encapsulated libSBOLc Document object
        self.ptr = libsbol.createDocument()

        # create sequences array
        fns = (libsbol.getDNASequenceURI,
               libsbol.removeDNASequence,
               libsbol.getNumDNASequences,
               libsbol.getNthDNASequence)
        ## Registers all DNASequence objects in Document
        self.sequences = SBOLObjectArray(self, *fns)

        # create annotations array
        fns = (libsbol.getSequenceAnnotationURI,
               libsbol.removeSequenceAnnotation,
               libsbol.getNumSequenceAnnotations,
               libsbol.getNthSequenceAnnotation)
        ## Registers all SequenceAnnotation objects in Document
        self.annotations = SBOLObjectArray(self, *fns)

        # create components array
        fns = (libsbol.getDNAComponentURI,
               libsbol.removeDNAComponent,
               libsbol.getNumDNAComponents,
               libsbol.getNthDNAComponent)
        ## Registers all DNAComponent objects in Document
        self.components = SBOLObjectArray(self, *fns)

        # create collections array
        fns = (libsbol.getCollectionURI,
               libsbol.removeCollection,
               libsbol.getNumCollections,
               libsbol.getNthCollection)
        ## Registers all Collection objects in Document
        self.collections = SBOLObjectArray(self, *fns)

        # create lists of Python proxy objects to keep them
        # from being garbage collected, and for looking up
        # objects from SWIG pointers
        ## Registers all PySBOL DNASequence wrapper objects in Document
        self._sequences   = []
        ## Registers all PySBOL SequenceAnnotation wrapper objects in Document
        self._annotations = []
        ## Registers all PySBOL DNAComponent wrapper objects in Document
        self._components  = []
        ## Registers all PySBOL Collection wrapper objects in Document
        self._collections = []

    ## Delete this Document and all associated objects, freeing libSBOL memory
    def close(self):
        if self.ptr:
            libsbol.deleteDocument(self.ptr)

    ## Print summary of Document
    def __str__(self):
        return capture_stdout(libsbol.printDocument, self.ptr)

    ## Read an SBOL file
    # @param filename A string containing the full file name
    def read(self, filename):
        libsbol.readDocument(self.ptr, filename)
        # Instantiate python proxy objects for each C object in file
        for i in range(0, libsbol.getNumDNASequences(self.ptr)):
            ptr = libsbol.getNthDNASequence(self.ptr, i)
            uri = libsbol.getDNASequenceURI(ptr)
            seq = DNASequence(self, uri, ptr)
        for i in range(0, libsbol.getNumSequenceAnnotations(self.ptr)):
            ptr = libsbol.getNthSequenceAnnotation(self.ptr, i)
            uri = libsbol.getSequenceAnnotationURI(ptr)
            seq_annotation = SequenceAnnotation(self, uri, ptr)
        for i in range(0, libsbol.getNumDNAComponents(self.ptr)):
            ptr = libsbol.getNthDNAComponent(self.ptr, i)
            uri = libsbol.getDNAComponentURI(ptr)
            component = DNAComponent(self, uri, ptr)
        for i in range(0, libsbol.getNumCollections(self.ptr)):
            ptr = libsbol.getNthCollection(self.ptr, i)
            uri = libsbol.getCollectionURI(ptr)
            collection = SequenceAnnotation(self, uri, ptr)

    ## Write an SBOL file
    # @param filename A string containing the full file name
    def write(self, filename):
        libsbol.writeDocumentToFile(self.ptr, filename)

    ## Total number of objects owned by this Document
    @property
    def num_sbol_objects(self):
        return len(self.sequences)   \
             + len(self.annotations) \
             + len(self.components)  \
             + len(self.collections)

    ## URIs of all object instances owned by this Document
    @property
    def uris(self):
        output = []
        for array in (self._sequences,
                      self._annotations,
                      self._components,
                      self._collections):
            for obj in array:
                output.append(obj.uri)
        return output

    ## Find the Python proxy for an unknown pointer
    def _proxy(self, ptr):
        for array in (self._sequences,
                      self._annotations,
                      self._components,
                      self._collections):
            for obj in array:
                if obj.ptr == ptr:
                    return obj
        return None

## Instances of the DNASequence class contain the actual DNA sequence string.
# This specifies the sequence of nucleotides that comprise the DNAComponent
# being described.
class DNASequence(object):
    ## Constructor for a PySBOL DNASequence. A PySBOL DNASequence wraps a
    # libSBOLc DNASequence.  By default the constructor will instantiate both
    # a libSBOLc object and its wrapper Python object.  However, if a libSBOLc
    # DNASequence already exists, it can be wrapped by specifying the optional
    # argument ptr
    # @param doc The Document to which this sequence will belong
    # @param uri A unique string identifier
    # @param ptr Optional. A SWIGPython-libSBOLc object to be wrapped with
    # this DNASequence
    def __init__(self, doc, uri, ptr=None):
        ## The SWIGPython-libSBOLc object wrapped by this DNASequence object
        self.ptr = None
        if not ptr:
            # create the C object if it doesn't exist already
            self.ptr = libsbol.createDNASequence(doc.ptr, uri)
        else:
            # wrap a C object if it already exists, necessary for input from file
            self.ptr = ptr

        if self.ptr == None:
            raise URIError("Duplicate URI '%s'" % uri)

        # register the Python proxy
        ## the Document to which this sequence object belongs
        self.doc = doc
        self.doc._sequences.append(self)

    ## Clean-up this wrapper and its object
    def __del__(self):
        if self.ptr:
            libsbol.deleteDNASequence(self.ptr)
        self.doc._sequences.remove(self)

    ## Print summary of this DNASequence object
    def __str__(self):
        return capture_stdout(libsbol.printDNASequence, self.ptr, 0)

    ## Print the URI of this DNASequence object
    def __repr__(self):
        return "<%s uri='%s'>" % (self.__class__.__name__, self.uri)

    ## Copy the properties of this DNASequence object to a new DNASequence
    # object.  The new object is automatically assigned its URI based on the
    # self object's URI augmented with the id_modifier
    # @param id_modifier A string of characters added to an object's URI to
    # designate the new object's URI.
    def deepcopy(self, id_modifier):
        copy_ptr = libsbol.copyDNASequence(self.ptr, id_modifier)
        return DNASequence(self.doc, self.uri + id_modifier, copy_ptr)

    ## A string that uniquely identifies a DNASequence instance
    @property
    def uri(self):
        return libsbol.getDNASequenceURI(self.ptr)

    ## This property specifies the sequence of nucleotides that comprise the
    # parent DNAComponent.  The base pairs MUST be represented by a sequence of
    # lowercase characters corresponding to the 5' to 3' order of nucleotides in
    # the DNA segment described, eg. "actg". The string value MUST conform to the
    # restrictions listed below:
    # a. The DNA sequence MUST use the Nomenclature for incompletely specified
    # bases in nucleic acid sequences (Cornish-Bowden 1985). Rules adopted by IUPAC.
    # | Symbol | Meaning            |
    # |--------|--------------------|
    # | a      | a; adenine         |
    # | c      | c; cytosine        |
    # | g      | g; guanine         |
    # | t      | t; thymine         |
    # | m      | a or c             |
    # | r      | a or g             |
    # | w      | a or t             |
    # | s      | c or g             |
    # | y      | c or t             |
    # | k      | g or t             |
    # | v      | a or c or g; not t |
    # | h      | a or c or t; not g |
    # | d      | a or g or t; not c |
    # | b      | c or g or t; not a |
    # | n      | a or c or g or t   |
    # b. Blank lines, spaces, or other symbols must not be included in the sequence text.
    # c. The sequence text must be in ASCII or UTF-8 encoding. For the alphabets used,
    # the two are identical.<br>

    @property
    def nucleotides(self):
        return libsbol.getDNASequenceNucleotides(self.ptr)

    @nucleotides.setter
    def nucleotides(self, value):
        libsbol.setDNASequenceNucleotides(self.ptr, value)

## Analogous to 'a feature' in other systems, the SequenceAnnotation
# indicates information about the parent DNAComponent at the position
# specified by the SequenceAnnotation's location data properties. The
# SequenceAnnotation location CAN be specified by the start and end
# positions of the subComponent, along with the DNA sequence. Alternatively,
# the partial order of SequenceAnnotations along a DNAComponent can be
# specified by indicating the precedes relationship to other SequenceAnnotations.
class SequenceAnnotation(object):
    ## Constructor for a PySBOL SequenceAnnotation. A PySBOL SequenceAnnotation
    # wraps a libSBOLc SequenceAnnotation.  By default the constructor will instantiate
    # both a libSBOLc object and its wrapper Python object.  However, if a libSBOLc
    # SequenceAnnotation already exists, it can be wrapped by specifying the optional
    # argument ptr
    # @param doc The Document to which this annotation will belong
    # @param uri A unique string identifier
    # @param ptr Optional. A SWIGPython-libSBOLc object to be wrapped with
    # this SequenceAnnotation
    def __init__(self, doc, uri, ptr=None):
        ## The SWIGPython-libSBOLc object wrapped by this SequenceAnnotation
        self.ptr = None
        if not ptr:
            # create the C object if it doesn't exist already
            self.ptr = libsbol.createSequenceAnnotation(doc.ptr, uri)
        else:
            # wrap a libSBOLc object if it already exists (most likely due to file import)
            self.ptr = ptr

        if self.ptr == None:
            raise URIError("Duplicate URI '%s'" % uri)

        # register the Python proxy
        ## the Document to which this annotation belongs
        self.doc = doc
        self.doc._annotations.append(self)

        # finish the Python proxy
        self.doc._annotations.append(self)
        fns = (libsbol.getSequenceAnnotationURI,
               libsbol.addPrecedesRelationship,
               libsbol.removePrecedesRelationship,
               libsbol.getNumPrecedes,
               libsbol.getNthPrecedes)
        # This SequenceAnnotation object precedes all the SequenceAnnotation objects
        # whose object references are included in this array property. Thus, the
        # precedes property specifies this annotation's position relative to others
        # that belong to the same parent DNAComponent.  This property can be operated
        # on with Python list operators and slice indexing.
        self.precedes = ExtendableSBOLObjectArray(self, *fns)

    ## Clean-up this wrapper and its object
    def __del__(self):
        if self.ptr:
            libsbol.deleteSequenceAnnotation(self.ptr)
        self.doc._annotations.remove(self)

    ## Print summary of this SequenceAnnotation object
    def __str__(self):
        return capture_stdout(libsbol.printSequenceAnnotation, self.ptr, 0)

    ## Print the URI of this SequenceAnnotation object
    def __repr__(self):
        return "<%s uri='%s'>" % (self.__class__.__name__, self.uri)

    ## Determines if this SequenceAnnotation is upstream (precedes) the object
    # annotation
    # @param object A SequenceAnnotation whose position relative to self is unknown
    # @return True if this SequenceAnnotation is upstream of the object annotation,
    # or False if it is downstream
    def isUpstream(self, object):
        return bool(libsbol.precedes(self.ptr, object.ptr))

    ## A SequenceAnnotation is downstream of the object annotation
    # if the object annotation precedes it
    # @param object A SequenceAnnotation whose position relative to self is unknown
    # @return True if this SequenceAnnotation is downstream of the
    # object annotation, or False if it is upstream
    def isDownstream(self, object):
        return bool(libsbol.precedes(object.ptr, self.ptr))

    ## A string that uniquely identifies a SequenceAnnotation instance
    @property
    def uri(self):
        return libsbol.getSequenceAnnotationURI(self.ptr)

    ## Positive integer coordinate of the position of the first base of the
    # subcomponent on the DNAComponent. As a convention, numerical coordinates in
    # this class use position 1 (not 0) to indicate the initial base pair of a
    # DNA sequence, a convention often used in molecular biology.  The start
    # coordinate is relative to the parent sequence.
    @property
    def start(self):
        start = libsbol.getSequenceAnnotationStart(self.ptr)
        if start == -1:
            return None
        else:
            return start

    ## Positive integer coordinate of the position of the last base of the
    # subcomponent on the DNAComponent. The end coordinate is relative to the
    # parent sequence.
    @property
    def end(self):
        end = libsbol.getSequenceAnnotationEnd(self.ptr)
        if end == -1:
            return None
        else:
            return end

    ## The strand orientation, or direction, of the subComponent's sequence
    # relative to the parent DnaComponent is specified by the strand [+/-].
    # For strand: '+' the sequence of the subComponent is the exact sub-sequence,
    # and for '-' it is the reverse-complement of the parent DnaComponent's sequence
    # in that region.
    @property
    def strand(self):
        polarity = libsbol.getSequenceAnnotationStrand(self.ptr)
        if polarity == libsbol.STRAND_FORWARD:
            return '+'
        elif polarity == libsbol.STRAND_BIDIRECTIONAL:
            return '*'
        elif polarity == libsbol.STRAND_REVERSE:
            return '-'
        else:
            raise InternalError('Got invalid strand polarity %i' % polarity )

    ## This property specifies a child DNAComponent which is nested inside a
    # parent DNAComponent's sequence.  The location data properties contained
    # in a SequenceAnnotation object describe the position of the subcomponent
    # within its parent's sequence.  The sequence of the subcomponent SHOULD be
    # logically consistent its parent's sequence, and logically consistent
    # with the strand value, though the API does not enforce these restrictions.
    @property
    def subcomponent(self):
        ptr = libsbol.getSequenceAnnotationSubComponent(self.ptr)
        return self.doc._proxy(ptr)

    @subcomponent.setter
    def subcomponent(self, subcomponent):
        libsbol.setSequenceAnnotationSubComponent(self.ptr, subcomponent.ptr)

    @start.setter
    def start(self, index):
        if index == None:
            index = -1
        elif index < 0:
            raise PositionError('Negative position %i' % index)
        libsbol.setSequenceAnnotationStart(self.ptr, index)

    @end.setter
    def end(self, index):
        if index == None:
            index = -1
        elif index < 0:
            raise PositionError('Negative position %i' % index)
        libsbol.setSequenceAnnotationEnd(self.ptr, index)

    @strand.setter
    def strand(self, polarity):
        if polarity == '+':
            polarity = libsbol.STRAND_FORWARD
        elif polarity == '*':
            polarity = libsbol.STRAND_BIDIRECTIONAL
        elif polarity == '-':
            polarity = libsbol.STRAND_REVERSE
        else:
            raise StrandError('Invalid polarity %s' % polarity)
        libsbol.setSequenceAnnotationStrand(self.ptr, polarity)

    @subcomponent.setter
    def subcomponent(self, com):
        if com:
            libsbol.setSequenceAnnotationSubComponent(self.ptr, com.ptr)
        else:
            libsbol.setSequenceAnnotationSubComponent(self.ptr, None)

## Instances of the DNAComponent class represent segments of DNA. A component's
# DNA sequence can be annotated using SequenceAnnotation instances, positionally
# defined descriptors of the sequence which specify additional DnaComponent
# instances as subComponents. A DNAComponent MAY specify one DnaSequence
# instance it abstracts. DNAComponent instances MAY be grouped into Collections.
class DNAComponent(object):
    ## Constructor for a PySBOL DNAComponent. A PySBOL DNAComponent wraps a
    # libSBOLc DNAComponent.  By default the constructor will instantiate both
    # a libSBOLc object and its wrapper Python object.  However, if a libSBOLc
    # DNAComponent already exists, it can be wrapped by specifying the optional
    # argument ptr
    # @param doc The Document to which this component will belong
    # @param uri A unique string identifier
    # @param ptr Optional. A SWIGPython-libSBOLc object to be wrapped with
    # this DNAComponent
    def __init__(self, doc, uri, ptr=None):
        ## The SWIGPython-libSBOLc object wrapped by this DNAComponent
        self.ptr = None
        if not ptr:
            # create the C object if it doesn't exist already
            self.ptr = libsbol.createDNAComponent(doc.ptr, uri)
        else:
            # wrap a C object if it already exists, necessary for input from file
            self.ptr = ptr
        if self.ptr == None:
            raise URIError("Duplicate URI '%s'" % uri)

        # register the Python proxy
        ## the Document to which this component belongs
        self.doc = doc
        self.doc._components.append(self)

        # finish the Python proxy
        fns = (libsbol.getSequenceAnnotationURI,
               libsbol.addSequenceAnnotation,
               libsbol.removeSequenceAnnotationFromDNAComponent,
               libsbol.getNumSequenceAnnotationsFor,
               libsbol.getNthSequenceAnnotationFor)

        ## Zero or more values of type SequenceAnnotation. This property links
        # to SequenceAnnotation instances, each of which specifies the position
        # and strand orientation of a DnaComponent that describes a subComponent
        # of this DNA component.
        self.annotations = ExtendableSBOLObjectArray(self, *fns) ## Zero or more values of type SequenceAnnotation.

    ## Clean-up this wrapper and its object
    def __del__(self):
        if self.ptr:
            libsbol.deleteDNAComponent(self.ptr)
        self.doc._components.remove(self)

    ## Print summary of this DNAComponent object
    def __str__(self):
        return capture_stdout(libsbol.printDNAComponent, self.ptr, 0)

    ## Print the URI of this DNAComponent object
    def __repr__(self):
        return "<%s uri='%s'>" % (self.__class__.__name__, self.uri)

    ## Copy a "genetic design".  This DNAComponent and all its children objects
    # are recursively copied. Not fully implemented, does not copy references
    def deepcopy(self, id_modifier):
        copy_ptr = libsbol.copyDNAComponent(self.ptr, id_modifier)
        copy_uri = self.uri + id_modifier
        copy = DNAComponent(self.doc, copy_uri, copy_ptr)
        seq_copy_ptr = libsbol.getDNAComponentSequence(copy_ptr)
        if seq_copy_ptr:
            seq_copy_uri = libsbol.getDNASequenceURI(seq_copy_ptr)
            seq_copy = DNASequence(self.doc, seq_copy_uri, ptr=seq_copy_ptr)
        for i_ann in range(libsbol.getNumSequenceAnnotationsFor(copy.ptr)):
            SA_copy_ptr = libsbol.getNthSequenceAnnotationFor(copy.ptr, i_ann)
            SA_copy_uri = libsbol.getSequenceAnnotationURI(SA_copy_ptr)
            SA_copy = SequenceAnnotation(self.doc, SA_copy_uri, ptr=SA_copy_ptr)
        return copy

    ## This property uniquely identifies the instance, and is intended to be
    # used whenever a reference to the instance is needed, such as when
    # referring to a DNAComponent stored on a server from another location.
    @property
    def uri(self):
        return libsbol.getDNAComponentURI(self.ptr)

    ## The displayId is a human readable identifier for display to users.
    @property
    def display_id(self):
        return libsbol.getDNAComponentDisplayID(self.ptr)

    ## The name of the DNA component is a human-readable string providing
    # the most recognizable identifier used to refer to this DnaComponent.
    # It often confers meaning of what the component is in biological contexts
    # to a human user. A name may be ambiguous, in that multiple, distinct
    # DnaComponents may share the same name. For example, acronyms are
    # sometimes used (eg. pLac-O1) which may have more than one instantiation
    # in terms of exact DNA sequence composition.
    @property
    def name(self):
        return libsbol.getDNAComponentName(self.ptr)

    ## The description is a free-text field that contains text such as a title
    # or longer free-text-based description for users. This text is used to
    # clarify what the DnaComponent is to potential users (eg. engineered Lac
    # promoter, repressible by LacI).
    @property
    def description(self):
        return libsbol.getDNAComponentDescription(self.ptr)

    ## Zero or one DNASequence object. This property specifies the DNA sequence
    # which this DnaComponent object represents.
    @property
    def sequence(self):
        ptr = libsbol.getDNAComponentSequence(self.ptr)
        return self.doc._proxy(ptr)

    @display_id.setter
    def display_id(self, displayid):
        libsbol.setDNAComponentDisplayID(self.ptr, displayid)

    @name.setter
    def name(self, name):
        libsbol.setDNAComponentName(self.ptr, name)

    @description.setter
    def description(self, descr):
        libsbol.setDNAComponentDescription(self.ptr, descr)

    @sequence.setter
    def sequence(self, seq):
        libsbol.setDNAComponentSequence(self.ptr, seq.ptr)

    ## A URI referencing the Sequence Ontology
    @property
    def type(self):
        return libsbol.getDNAComponentType(self.ptr)

    @type.setter
    def type(self, typ):
        return libsbol.setDNAComponentType(self.ptr, typ)

    # TODO: does not copy sublevels contained in SequenceAnnotations
    def move(self, new_doc):
        if self.sequence:
            self.sequence.doc = new_doc
            new_doc._sequences.append(self.sequence)
        libsbol.moveDNAComponent(self.ptr, new_doc.ptr)
        self.doc = new_doc
        new_doc._components.append(self)

## Individual instances of the Collection class represent an organizational
# container which helps users and developers conceptualize a set of
# DNAComponents as a group. Any combination of these instances CAN be added
# to a Collection instance, annotated with a displayID, name, and description
# and be published or exchanged directly.<br>
# For example, a set of restriction enzyme recognition sites, such as the
# components commonly used for BBF RFC 10 BioBricks could be placed into a
# single Collection.  A Collection might contain DNA components used in a
# specific project, lab, or custom grouping specified by the user
class Collection(object):
    ## Constructor for a PySBOL Collection. A PySBOL Collection wraps a
    # libSBOLc Collection.  By default the constructor will instantiate both
    # a libSBOLc object and its wrapper Python object.  However, if a libSBOLc
    # Collection already exists, it can be wrapped by specifying the optional
    # argument ptr
    # @param doc The Document to which this collection will belong
    # @param uri A unique string identifier
    # @param ptr Optional. A SWIGPython-libSBOLc object to be wrapped with
    # this Collection
    def __init__(self, doc, uri, ptr=None):
        ## The SWIGPython-libSBOLc object wrapped by this Collection
        self.ptr = None
        if not ptr:
            # create the C object if it doesn't exist already
            self.ptr = libsbol.createCollection(doc.ptr, uri)
        else:
            # wrap a C object if it already exists
            self.ptr = ptr

        if self.ptr == None:
            raise URIError("Duplicate URI '%s'" % uri)

        # register the Python proxy
        ## the Document to which this Collection object belongs
        self.doc = doc
        self.doc._collections.append(self)

        # finish the Python proxy
        fns = (libsbol.getDNAComponentURI,
               libsbol.addDNAComponentToCollection,
               libsbol.removeDNAComponentFromCollection,
               libsbol.getNumDNAComponentsIn,
               libsbol.getNthDNAComponentIn)
        ## An array of zero or more instances of type DNAComponent which are members
        # of this Collection representing DNA segments for engineering biological
        # systems. For example, standard biological parts, BioBricks, pBAD, B0015,
        # BioBrick Scar, Insertion Element, or any other DNA segment of interest as
        # a building block of biological systems.  This property supports Python
        # list-like operations, slice indexing, as well as indexing by URI.
        self.components = ExtendableSBOLObjectArray(self, *fns)

    ## Clean-up this wrapper and its object
    def __del__(self):
        if self.ptr:
            libsbol.deleteCollection(self.ptr)
        self.doc._collections.remove(self)

    ## Print summary of this Collection object
    def __str__(self):
        return capture_stdout(libsbol.printCollection, self.ptr, 0)

    ## Print the URI of this Collection object
    def __repr__(self):
        return "<%s uri='%s'>" % (self.__class__.__name__, self.uri)

    ## This property uniquely identifies the instance, and is intended to be
    # used whenever a reference to the instance is needed, such as when
    # referring to a Collection stored on a server from another location.
    @property
    def uri(self):
        return libsbol.getCollectionURI(self.ptr)

    ## The displayID is a human-readable identifier for display to users
    @property
    def display_id(self):
        return libsbol.getCollectionDisplayID(self.ptr)

    ## The common name of the Collection is the most recognizable identifier used
    # to refer to this Collection. It SHOULD confer what is contained in the
    # Collection and is often ambiguous (eg, My Bookmarked Parts).
    @property
    def name(self):
        return libsbol.getCollectionName(self.ptr)

    ##  The description is a human-readable, free-text field, that SHOULD provide
    # a hint about why the member DNAComponents are grouped into this Collection.
    @property
    def description(self):
        return libsbol.getCollectionDescription(self.ptr)

    @display_id.setter
    def display_id(self, displayid):
        libsbol.setCollectionDisplayID(self.ptr, displayid)

    @name.setter
    def name(self, name):
        libsbol.setCollectionName(self.ptr, name)

    @description.setter
    def description(self, descr):
        libsbol.setCollectionDescription(self.ptr, descr)

