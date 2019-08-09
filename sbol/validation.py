import re
from sbolerror import SBOLError, SBOLErrorCode
from identified import *

def is_alphanumeric_or_underscore(c):
    i = ord(c)
    if i >= 48 and i <= 57:
        return True
    if i >= 65 and i <= 90:
        return True
    if i >= 97 and i <= 122:
        return True
    if i == 95:
        return True
    return False


def is_not_alphanumeric_or_underscore(c):
    return not is_alphanumeric_or_underscore(c)


def sbolRule10101(sbol_obj, arg):
    """An SBOL document MUST declare the use of the following XML namespace: http://sbols.org/v2#."""
    # TODO
    raise NotImplementedError("Not yet implemented")


def sbolRule10102(sbol_obj, arg):
    """An SBOL document MUST declare the use of the following XML namespace: http://www.w3.org/1999/02/22-rdf-syntax-ns#."""
    # TODO
    raise NotImplementedError("Not yet implemented")


def sbol_rule_10202(sbol_obj, arg):
    """The identity property of an Identified object MUST be globally unique."""
    if not isinstance(sbol_obj, Identified) or not isinstance(arg, str):
        # Not applicable
        raise TypeError('Inappropriate types passed to sbol_rule_10202')
    # if sbol_obj.doc is not None:
    #     #     if sbol_obj.doc.
    raise NotImplementedError("Not yet implemented")


# The displayId property of an Identified object is OPTIONAL and MAY contain a String that MUST
# be composed of only alphanumeric or underscore characters and MUST NOT begin with a digit.
def sbol_rule_10204(sbol_obj, arg):
    """The displayId property of an Identified object is OPTIONAL and MAY contain a String that MUST
    be composed of only alphanumeric or underscore characters and MUST NOT begin with a digit.
    """
    # TODO
    raise NotImplementedError("Not yet implemented")


# The definition property MUST NOT refer to the same ComponentDefinition as the one that contains the
# ComponentInstance. Furthermore, ComponentInstance objects MUST NOT form a cyclical chain of references
# via their definition properties and the ComponentDefinition objects that contain them. For example, consider
# the ComponentInstance objects A and B and the ComponentDefinition objects X and Y.The reference chain "X
# contains A, A is defined by Y, Y contains B, and B is defined by X" is cyclical


def libsbol_rule_1(sbol_obj, arg):
    """Print a test message"""
    print("Testing internal validation rules")


def libsbol_rule_2(sbol_obj, arg):
    """Validate XSD date-time format"""
    # Implementation note: re.match only matches the beginning part of the string;
    # re.search returns True if any part of the string matches the pattern.
    # Since the intention is to match the entire string, I needed to use '^' and '$'.
    date_time_1 = re.compile("^([0-9]{4})-([0-9]{2})-([0-9]{2})([A-Z])?$")
    date_time_2 = re.compile("^([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})([.][0-9]+)?[A-Z]?$")
    date_time_3 = re.compile("^([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})([.][0-9]+)?[A-Z]?([\\+|-]([0-9]{2}):([0-9]{2}))?$")
    datetime_match_1 = re.search(date_time_1, arg) is not None
    datetime_match_2 = re.search(date_time_2, arg) is not None
    datetime_match_3 = re.search(date_time_3, arg) is not None
    if not datetime_match_1 or not datetime_match_2 or not datetime_match_3:
        raise SBOLError(SBOLErrorCode.SBOL_ERROR_NONCOMPLIANT_VERSION,
                        "Invalid datetime format. Datetimes are based on XML Schema dateTime datatype. "
                        "For example 2016-03-16T20:12:00Z")


def libsbol_rule_3(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_4(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_5(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_6(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_8(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_9(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_10(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_11(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_12(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_13(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_14(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_15(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_16(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_17(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_18(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_20(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")


def libsbol_rule_21(sbol_obj, arg):
    raise NotImplementedError("Not yet implemented")

