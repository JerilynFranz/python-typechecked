from ._protocol import Immutable,  ImmutableTypedDict
from ._immutable import is_immutable, is_immutable_typeddict_typehint, is_immutable_data_typehint

__all__ = (
    "Immutable",
    "is_immutable",
    "is_immutable_data_typehint",
    "is_immutable_typeddict_typehint",
    "ImmutableTypedDict",
)
