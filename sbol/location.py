from identified import Identified
from constants import *
from property import Property
from rdflib import URIRef

class Location(Identified):
    """The Location class specifies the strand orientation of a Component."""
    def __init__(self, type_uri=SBOL_LOCATION, uri=URIRef('example'), orientation=SBOL_ORIENTATION_INLINE):
        super().__init__(type_uri, uri)
        self.orientation = Property(self, SBOL_ORIENTATION, '1', '1', [], orientation)
        self.sequence = Property(self, SBOL_SEQUENCE_PROPERTY, SBOL_SEQUENCE, '0', '1', [])


class Range(Location):
    """A Range object specifies a region via discrete, inclusive start and end positions that correspond to indices
    for characters in the elements String of a Sequence.  Note that the index of the first location is 1,
    as is typical practice in biology, rather than 0, as is typical practice in computer science."""
    def __init__(self, uri=URIRef('example'), start=1, end=2):
        super().__init__(uri=uri)
        self.start = start
        self.end = end

    def precedes(self, comparand):
        if self.end < comparand.start:
            return comparand.start - self.end
        else:
            return 0

    def follows(self, comparand):
        if self.start > comparand.end:
            return comparand.end - self.start
        else:
            return 0

    def adjoins(self, comparand):
        if comparand.end + 1 == self.start:
            return 1
        if self.end + 1 == comparand.start:
            return 1
        return 0

    def contains(self, comparand):
        if self.start <= comparand.start and self.end >= comparand.end:
            return comparand.length()
        else:
            return 0

    def overlaps(self, comparand):
        if self.start == comparand.start and self.end == comparand.end:
            return 0
        elif self.start < comparand.start and self.end < comparand.end and self.end >= comparand.start:
            return self.end - comparand.start + 1
        elif self.start > comparand.start and self.end > comparand.end and self.start <= comparand.end:
            return comparand.end - self.start + 1
        elif comparand.contains(self):
            return comparand.contains(self)
        else:
            return 0

    def length(self):
        return self.end + 1 - self.start

class Cut(Location):
    pass


class GenericLocation(Location):
    pass
