# rag_pipeline/embeddings.py

from langchain.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    """
    Initialise et retourne un moteur d'embedding HuggingFace.
    """
    print(" Initialisation du modèle d'embedding HuggingFace...")
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        print(" Embeddings prêt.")
        return embeddings
    except Exception as e:
        raise RuntimeError(f" Erreur lors de l'initialisation du modèle d'embedding : {e}")

def embed_docs(docs):
    """
    Génère les embeddings à partir d'une liste de documents avec clé 'context'.
    Retourne une liste de vecteurs.
    """
    print(" Génération des embeddings pour les documents...")

    if not docs or not isinstance(docs, list):
        raise ValueError(" Liste de documents vide ou invalide")

    texts = []
    for doc in docs:
        context = doc.get("context")
        if not context:
            raise ValueError(f" Document invalide (manque le champ 'context') : {doc}")
        texts.append(context)

    embeddings = get_embeddings()

    try:
        vectors = embeddings.embed_documents(texts)
        print(f" {len(vectors)} embeddings générés.")
        return vectors
    except Exception as e:
        raise RuntimeError(f" Erreur lors de la génération des embeddings : {e}")
