from collections.abc import Sequence

import numpy.typing as npt

from oldv.types import Scalar

class SentenceTransformer:
    def __init__(self, model_name_or_path: str): ...
    def encode(self, sentences: Sequence[str]) -> npt.NDArray[Scalar]: ...
