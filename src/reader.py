from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from transformers.models.auto.tokenization_auto import AutoTokenizer


def read_file(query_text: str) -> str:
    llm = Ollama(model="gemma3", request_timeout=60.0)
    embed = OllamaEmbedding(model_name="mxbai-embed-large")

    Settings.llm = llm

    Settings.tokenizer = AutoTokenizer.from_pretrained("./models/gemma-3-4b-it")

    Settings.embed_model = embed

    documents = SimpleDirectoryReader("./docs").load_data()
    index = VectorStoreIndex.from_documents(
        documents,
    )

    query_engine = index.as_query_engine()
    res = query_engine.query(query_text)

    return str(res)
