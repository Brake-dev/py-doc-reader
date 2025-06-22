from typing import List
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from transformers.models.auto.tokenization_auto import AutoTokenizer
from pydantic import BaseModel
from pydantic_core import from_json

PATH = "./docs/md/"

QUERY_TEXT = """ Extract the subtitles from a request for proposal document and generate common questions related to those subtitles that someone responding to the document might have.

    Return a structured list of titles and questions based on the schema.
 """


class DocSchema(BaseModel):
    title: str
    questions: List[str]


class DocListSchema(BaseModel):
    topics: List[DocSchema]


def get_structured_output_from_doc() -> DocListSchema:
    llm = Ollama(model="gemma3", request_timeout=60.0)
    sllm = llm.as_structured_llm(output_cls=DocListSchema)

    embed = OllamaEmbedding(model_name="mxbai-embed-large")

    Settings.llm = sllm

    Settings.tokenizer = AutoTokenizer.from_pretrained("./models/gemma-3-4b-it")

    Settings.embed_model = embed

    documents = SimpleDirectoryReader(PATH).load_data()
    index = VectorStoreIndex.from_documents(
        documents,
    )

    query_engine = index.as_query_engine()
    res = query_engine.query(QUERY_TEXT)

    doc_list = DocListSchema.model_validate(from_json(str(res)))

    return doc_list
