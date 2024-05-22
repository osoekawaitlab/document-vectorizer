from collections.abc import Sequence
from typing import Optional

import numpy.typing as npt

from oldv.types import Scalar

class SentenceTransformer:
    def __init__(self, model_name_or_path: str, trust_remote_code: bool = False): ...
    def encode(self, sentences: Sequence[str]) -> npt.NDArray[Scalar]: ...
