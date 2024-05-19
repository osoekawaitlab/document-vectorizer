from oldv.document_vectorizers.count_vectorizer import CountVectorizerCore
from oldv.models import Document
from oldv.settings import CountVectorizerSettings


def test_count_vectorizer_serialize() -> None:
    core = CountVectorizerCore.create(
        [
            Document(content="good"),
            Document(content="bye"),
            Document(content="Hello"),
            Document(content="world"),
        ],
        CountVectorizerSettings(),
    )
    serialized = core.serialize()
    core2 = CountVectorizerCore.deserialize(serialized)
    assert core.count_vectorizer.vocabulary_ == core2.count_vectorizer.vocabulary_
