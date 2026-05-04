from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document


class RAGRetriever:
    """Domain-agnostic RAG retriever backed by FAISS."""

    def __init__(self, embedding_model: str = "paraphrase-multilingual-MiniLM-L12-v2"):
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
        self.vectorstore: FAISS | None = None

    def build(self, texts: list[str]) -> None:
        docs = [Document(page_content=t) for t in texts]
        self.vectorstore = FAISS.from_documents(docs, self.embeddings)

    def save(self, path: str) -> None:
        if self.vectorstore:
            self.vectorstore.save_local(path)

    def load(self, path: str) -> None:
        self.vectorstore = FAISS.load_local(path, self.embeddings, allow_dangerous_deserialization=True)

    def retrieve(self, query: str, k: int = 3) -> list[str]:
        if not self.vectorstore:
            return []
        docs = self.vectorstore.similarity_search(query, k=k)
        return [d.page_content for d in docs]
