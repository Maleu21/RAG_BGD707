# main.py

from rag_pipeline import data_loader, embedder, db, retriever, qa

def main():
    print("🚀 Démarrage du pipeline RAG...")

    # 1. Charger les documents
    docs = data_loader.load_data()
    if not docs:
        print("❌ Aucun document chargé.")
        return

    # 2. Embedding
    embeddings = embedder.embed_docs(docs)
    if not embeddings or len(embeddings) != len(docs):
        print("❌ Erreur dans la génération des embeddings.")
        return

    # 3. Stockage dans PostgreSQL
    conn = db.connect()
    db.init_table(conn)
    db.insert_embeddings(conn, docs, embeddings)

    # 4. Interrogation
    query = "Qui a fondé l'empire romain ?"
    top_docs = retriever.search_similar_docs(conn, query)
    if not top_docs:
        print("❌ Aucun document similaire trouvé.")
        return

    answer = qa.ask_llm(query, top_docs)

    print("\n🤖 Réponse finale :", answer)

if __name__ == "__main__":
    main()
