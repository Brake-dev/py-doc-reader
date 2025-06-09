import os
import pathlib

from llama_index.core import Settings, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from transformers.models.auto.tokenization_auto import AutoTokenizer
import pymupdf4llm

PATH = "./docs/pdf/"


def read_pdf_file(query_text: str) -> str:
    llm = Ollama(model="gemma3", request_timeout=60.0)
    embed = OllamaEmbedding(model_name="mxbai-embed-large")

    index = VectorStoreIndex([], embed_model=embed)

    Settings.llm = llm
    Settings.tokenizer = AutoTokenizer.from_pretrained("./models/gemma-3-4b-it")
    Settings.embed_model = embed

    llama_reader = pymupdf4llm.LlamaMarkdownReader()

    obj = os.scandir(PATH)

    for entry in obj:
        if entry.is_file() and "pdf" in entry.name:
            pdf_path = f"{PATH}{entry.name}"
            doc = llama_reader.load_data(pdf_path)

            for d in doc:
                index.insert(d)

    query_engine = index.as_query_engine()
    res = query_engine.query(query_text)

    return str(res)


def write_to_md():
    md_text = pymupdf4llm.to_markdown("./docs/pdf/1910.13461v1.pdf")
    pathlib.Path("output.md").write_bytes(md_text.encode())
