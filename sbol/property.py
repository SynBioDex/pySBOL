from rdflib import URIRef, Literal

class Property():
    """Member properties of all SBOL objects are defined using a Property object.

    The Property class provides a generic interface for accessing SBOL objects.
    At a low level, the Property class converts SBOL data structures into RDF triples.
    """

    def __init__(self, property_owner, type_uri, lower_bound, upper_bound, validation_rules, initial_value=None):
        """Construct a Property.

        :param property_owner: All Property objects must have a pointer back to their parent SBOLObject.
        :param type_uri: An RDF hash URI for this property, consisting of a namespace followed by an identifier.
        For example, Properties of SBOLObjects use URIs of the form http://sbols.org/v2#somePropertyName,
        where the identifier somePropertyName determines the appearance of XML nodes in an SBOL file.
        Alternatively, annotations in a custom namespace can be provided using a similarly formed hash URI
        in another namespace.
        :param lower_bound:
        :param upper_bound:
        :param validation_rules: A vector of externally defined ValidationRules.
        The vector contains pointers to functions which correspond to the validation rules listed in the appendix
        of the formal SBOL specification document.  ValidationRules are automatically checked every time a setter
        or adder method is called and when Documents are read and written.
        :param initial_value: The initial value of the Property (int, str, float supported)
        """
        self._sbol_owner = property_owner
        self._rdf_type = type_uri
        self._lowerBound = lower_bound
        self._upperBound = upper_bound
        self._validation_rules = []
        self._validation_rules = validation_rules
        self._values = []
        self._values.append(initial_value)

    def getTypeURI(self):
        """

        :return: URI representing the predicate.
        """
        return self._rdf_type

    def getOwner(self):
        """

        :return: The owner of this Property.
        """
        return self._sbol_owner

    @property
    def value(self):
        return self.get()

    @value.setter
    def value(self, new_value):
        self.set(new_value)

    def get(self):
        if len(self._values) == 0:
            return None
        else:
            return self._values[len(self._values)-1]

    def set(self, new_value):
        # TODO perform validation prior to setting the value
        if len(self._values) == 0:
            self._values.append(new_value)
        else:
            self._values[len(self._values)-1] = new_value

    def add(self, new_value):
        """Appends the new value to a list of values, for properties that allow it."""
        raise NotImplementedError("Not yet implemented")

    def remove(self, index=0):
        """Remove a property value."""
        raise NotImplementedError("Not yet implemented")

    def clear(self):
        """Clear all property values."""
        raise NotImplementedError("Not yet implemented")

    def write(self):
        """Write property values."""
        subject = self._sbol_owner.identity.get()
        predicate = self._rdf_type
        if len(self._values) > 0:
            obj = self._values[0]
        else:
            obj = None
        print('Subject: ' + subject)
        print('Predicate: ' + predicate)
        print('Object: ' + obj)

    def find(self, query):
        """Check if a value in this property matches the query."""
        raise NotImplementedError("Not yet implemented")

    def getLowerBound(self):
        return self._lowerBound

    def getUpperBound(self):
        return self._upperBound

    def validate(self, arg):
        if arg is None:
            # NOTE: Original libSBOL code has commented-out code for this case.
            raise TypeError("arg cannot be None")
        for validation_rule in self._validation_rules:
            validation_rule(self._sbol_owner, arg)

    def __contains__(self, item):
        if self.find(item) != None:
            return True
        else:
            return False

    def _isHidden(self):
        raise NotImplementedError("Not yet implemented")

