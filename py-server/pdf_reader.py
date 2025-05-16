import os

from llmsherpa.readers import LayoutPDFReader
from llama_index.core import VectorStoreIndex, Document
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

PATH = "./docs/"


def read_pdf_file(query_text: str) -> str:
    llm = Ollama(model="gemma3", request_timeout=60.0)
    embed = OllamaEmbedding(model_name="mxbai-embed-large")

    llmsherpa_api_url = "http://localhost:5010/api/parseDocument?renderFormat=all"
    pdf_reader = LayoutPDFReader(llmsherpa_api_url)
    index = VectorStoreIndex([], embed_model=embed)

    obj = os.scandir(PATH)
    files = []

    for entry in obj:
        if entry.is_file() and "pdf" in entry.name:
            files.append(entry.name)

    for f in files:
        pdf_url = f"{PATH}{f}"
        doc = pdf_reader.read_pdf(pdf_url)

        for chunk in doc.chunks():
            index.insert(Document(text=chunk.to_context_text(), extra_info={}))

    query_engine = index.as_query_engine(llm)

    res = query_engine.query(query_text)
    return str(res)
