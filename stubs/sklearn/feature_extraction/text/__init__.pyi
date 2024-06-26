from collections.abc import Sequence

import numpy.typing as npt
import scipy.sparse as sp

class CountVectorizer:
    def __init__(self, analyzer: str, dtype: npt.DTypeLike): ...
    def fit(self, corpus: Sequence[str]) -> None: ...
    def transform(self, text: Sequence[str]) -> sp.csr_matrix: ...
    @property
    def vocabulary_(self) -> dict[str, int]: ...
