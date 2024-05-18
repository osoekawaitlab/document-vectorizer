import numpy as np

import oldv


def test_oldv_as_module() -> None:
    core = oldv.CountVectorizerCore.create(
        [
            oldv.Document(content=oldv.DocumentContent("good")),
            oldv.Document(content=oldv.DocumentContent("bye")),
            oldv.Document(content=oldv.DocumentContent("Hello")),
            oldv.Document(content=oldv.DocumentContent("world")),
        ],
        oldv.CountVectorizerSettings(),
    )
    dv = oldv.DocumentVectorizerApp(core)
    res = dv.vectorize(oldv.Document(content=oldv.DocumentContent("Hello world")))
    assert isinstance(res, oldv.DocumentVector)
    res2 = dv.vectorize(oldv.Document(content=oldv.DocumentContent("Hello world")))
    assert res == res2
    assert (res.vector.array == np.array([0, 0, 1, 1], dtype=oldv.Scalar)).all()
