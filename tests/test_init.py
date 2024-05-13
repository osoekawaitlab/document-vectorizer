import re

import oldv


def test_oldv_has_version() -> None:
    assert hasattr(oldv, "__version__")
    assert re.match(r"\d+\.\d+\.\d+", oldv.__version__)
