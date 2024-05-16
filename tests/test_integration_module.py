import numpy as np

import oldv


def test_oldv_as_module() -> None:
    core = oldv.CountVectorizerCore.create(
        [
            oldv.DocumentContent("good"),
            oldv.DocumentContent("bye"),
            oldv.DocumentContent("Hello"),
            oldv.DocumentContent("world"),
        ],
        oldv.CountVectorizerSettings(),
    )
    dv = oldv.DocumentVectorizerApp(core)
    res = dv.vectorize(oldv.DocumentContent("Hello world"))
    assert isinstance(res, oldv.Vector)
    res2 = dv.vectorize(oldv.DocumentContent("Hello world"))
    assert res == res2
    assert (res.array == np.array([0, 0, 1, 1], dtype=oldv.Scalar)).all()
