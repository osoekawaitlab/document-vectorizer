from typing import TypeAlias

import numpy as np
import numpy.typing as npt
from oltl import BaseBytes, NonEmptyStringMixIn

Scalar: TypeAlias = np.float32


class Vector(BaseBytes):
    """A vector of scalars.

    This class is a wrapper around a byte buffer that contains a sequence of
    scalars. The scalars are stored in the buffer in a contiguous manner.

    >>> vector = Vector.from_array(np.array([1.0, 2.0, 3.0], dtype=Scalar))
    >>> vector.array
    array([1., 2., 3.], dtype=float32)

    """

    @property
    def array(self) -> npt.NDArray[Scalar]:
        return np.frombuffer(self, dtype=Scalar)

    @classmethod
    def from_array(cls, array: npt.NDArray[Scalar]) -> "Vector":
        return cls(array.tobytes())


class DocumentContent(NonEmptyStringMixIn):
    """The content of a document.

    The content of a document is a non-empty string.

    """

    pass


class PickleBytes(BaseBytes):
    """A byte buffer that contains a pickled object.

    This class is a wrapper around a byte buffer that contains a pickled object.

    """

    pass
