# document-vectorizer

`oldv` is an application that allows you to convert a document into a vector. The vector is a list of numbers that represents the document and you can use it to measure the similarity between documents and so on.

## Environment

- Python 3.10.x

## Installation

```bash
pip install git+https://github.com/osoekawaitlab/document-vectorizer
```

## Usage

There are three ways to use `oldv`.

### Use as a python module

There is `oldv.DocumentVectorizerApp` which is an interface class to use `oldv`.

```python
from oldv import DocumentVectorizerApp, Document
from oldv.settings import DocumentVectorizerAppSettings

settings = DocumentVectorizerAppSettings(document_vectorizer_settings={"type": "ALL_MINI_LM"})
app = DocumentVectorizerApp.create(settings=settings)
res = app.vectorize(Document(content="This is a pen."))
print(res.vector.array) # [-1.46203572e-02  4.90227267e-02...]
```

This code will output the vector of the document "This is a pen.".
For more information about the settings, see the [settings](#settings) section.

### Use as a command line tool

You can use `oldv` as a command line tool.

```bash
OLDV_DOCUMENT_VECTORIZER_SETTINGS__TYPE=ALL_MINI_LM oldv vectorize "This is a pen." output.json
```

This command will output the vector of the document "This is a pen." to `output.json`.
Settings can be passed as environment variables. For more information about the settings, see the [settings](#settings) section.


### Use as a REST API

REST API server is also available.

```bash
OLDV_DOCUMENT_VECTORIZER_SETTINGS__TYPE=ALL_MINI_LM uvicorn oldv.interfaces.api.main:app
```

This command will start a REST API server. You can access the server at `http://localhost:8000/docs`.


## Settings

There are several settings that can be used to customize the behavior of `oldv`.

### Available settings

#### `DocumentVectorizerAppSettings`

- `document_vectorizer_settings`: `DocumentVectorizerSettings`
    - Settings for the internal vectorizer.

#### `DocumentVectorizerSettings`

- `type`: `Literal["ALL_MINI_LM"] | Literal["NOMIC_EMBED_TEXT"]`
    - The type of the document vectorizer to use.
    - `ALL_MINI_LM`: Use `ALL_MINI_LM` document vectorizer.
    - `NOMIC_EMBED_TEXT`: Use `NOMIC_EMBED_TEXT` document vectorizer.

### Environment variables

You can pass settings as environment variables.

- `OLDV_DOCUMENT_VECTORIZER_SETTINGS__TYPE`: `Literal["ALL_MINI_LM"] | Literal["NOMIC_EMBED_TEXT"]`
    - The type of the document vectorizer to use.
    - `ALL_MINI_LM`: Use `ALL_MINI_LM` document vectorizer.
    - `NOMIC_EMBED_TEXT`: Use `NOMIC_EMBED_TEXT` document vectorizer.
