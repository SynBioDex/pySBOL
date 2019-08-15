__version__ = '3.0.0'

# NOTE: I have to manually specify 'sbol3'. Why?
from sbol3.document import Document
from sbol3.componentdefinition import ComponentDefinition
from sbol3.moduledefinition import ModuleDefinition
from sbol3.sequence import Sequence

# NOTE: I have to manually include all of these, which is quite a pain.
__all__ = ['Document', 'ComponentDefinition', 'ModuleDefinition', 'Sequence']
