from llmsherpa.readers import LayoutPDFReader
from llama_index.core import Document
from llama_index.core import VectorStoreIndex

def readPDFFile(queryText: str) -> str:
    llmsherpa_api_url = "http://localhost:5010/api/parseDocument?renderFormat=all"
    pdf_url = "./docs/company_car_policy.pdf"
    pdf_reader = LayoutPDFReader(llmsherpa_api_url)
    doc = pdf_reader.read_pdf(pdf_url)

    index = VectorStoreIndex([])
    for chunk in doc.chunks():
        index.insert(Document(text=chunk.to_context_text(), extra_info={}))
    query_engine = index.as_query_engine()

    res = query_engine.query(queryText)
    return res
