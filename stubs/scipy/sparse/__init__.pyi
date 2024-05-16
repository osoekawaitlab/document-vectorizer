import numpy.typing as npt

from oldv.types import Scalar

class csr_matrix:
    def toarray(self) -> npt.NDArray[Scalar]: ...
