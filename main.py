# main.py

from rag_pipeline import database, embeddings, loader, retriever, qa

def main():
    print(" Démarrage du pipeline RAG...")

    # 1. Charger les documents
    docs = loader.load_data()
    if not docs:
        print(" Aucun document chargé.")
        return

    # 2. Embedding
    embeddings = embeddings.embed_docs(docs)
    if not embeddings or len(embeddings) != len(docs):
        print(" Erreur dans la génération des embeddings.")
        return

    # 3. Stockage dans PostgreSQL
    conn = database.connect()
    database.init_table(conn)
    database.insert_embeddings(conn, docs, embeddings)

    # 4. Interrogation
    query = "Qui a fondé l'empire romain ?"
    top_docs = retriever.search_similar_docs(conn, query)
    if not top_docs:
        print(" Aucun document similaire trouvé.")
        return

    answer = qa.ask_llm(query, top_docs)

    print("\n Réponse finale :", answer)

if __name__ == "__main__":
    main()
