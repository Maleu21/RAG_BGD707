# rag_pipeline/retriever.py

from langchain.embeddings import HuggingFaceEmbeddings
import numpy as np

VECTOR_DIM = 384  # Doit correspondre à celui défini dans db.py

def embed_query(text):
    print("Embedding de la requête utilisateur...")
    try:
        embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector = embedder.embed_query(text)
        return vector
    except Exception as e:
        raise RuntimeError(f"Erreur dans l'embedding de la requête : {e}")

def search_similar_docs(conn, query, k=3):
    print(f"Recherche des {k} documents les plus proches de la requête...")
    
    vector = embed_query(query)
    vector_str = "[" + ",".join([str(x) for x in vector]) + "]"

    try:
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT context
                FROM rag_documents
                ORDER BY embedding <-> %s
                LIMIT %s
            """, (vector_str, k))
            rows = cur.fetchall()

        results = [row[0] for row in rows]
        print(f"{len(results)} documents similaires récupérés.")
        return results
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la recherche vectorielle : {e}")
