from llmsherpa.readers import LayoutPDFReader
from llama_index.core import VectorStoreIndex, Document
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding


def read_pdf_file(query_text: str) -> str:
    llm = Ollama(model="gemma3", request_timeout=60.0)
    embed = OllamaEmbedding(model_name="mxbai-embed-large")

    llmsherpa_api_url = "http://localhost:5010/api/parseDocument?renderFormat=all"
    pdf_url = "./docs/company_car_policy.pdf"
    pdf_reader = LayoutPDFReader(llmsherpa_api_url)
    doc = pdf_reader.read_pdf(pdf_url)

    index = VectorStoreIndex([], embed_model=embed)
    for chunk in doc.chunks():
        index.insert(Document(text=chunk.to_context_text(), extra_info={}))

    query_engine = index.as_query_engine(llm)

    res = query_engine.query(query_text)
    return str(res)
