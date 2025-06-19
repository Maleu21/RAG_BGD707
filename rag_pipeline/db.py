# rag_pipeline/db.py

import psycopg
import numpy as np

DB_CONFIG = {
    "host": "127.0.0.1",
    "dbname": "postgres",
    "user": "postgres",
    "password": "pass"  # ← c’est celui que tu avais mis dans `docker run`
}



VECTOR_DIM = 384  # à ajuster selon le modèle d'embedding utilisé

def connect():
    try:
        print("🔗 Connexion à la base de données PostgreSQL...")
        conn = psycopg.connect(**DB_CONFIG)
        print("✅ Connexion établie.")
        return conn
    except Exception as e:
        raise RuntimeError(f"❌ Échec de la connexion à PostgreSQL : {e}")

def init_table(conn):
    print("🛠️ Création de la table (si inexistante)...")
    try:
        with conn.cursor() as cur:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS rag_documents (
                    id SERIAL PRIMARY KEY,
                    context TEXT,
                    embedding VECTOR({VECTOR_DIM})
                );
            """)
            conn.commit()
        print("✅ Table prête.")
    except Exception as e:
        raise RuntimeError(f"❌ Erreur lors de la création de la table : {e}")

def insert_embeddings(conn, docs, embeddings):
    print(f"📥 Insertion de {len(docs)} documents dans la base...")
    try:
        with conn.cursor() as cur:
            for doc, vector in zip(docs, embeddings):
                context = doc.get("context", "")
                if not context or not vector:
                    print("⚠️ Document ou vecteur vide, ignoré.")
                    continue
                vector_str = "[" + ",".join([str(x) for x in vector]) + "]"
                cur.execute(
                    "INSERT INTO rag_documents (context, embedding) VALUES (%s, %s)",
                    (context, vector_str)
                )
            conn.commit()
        print("✅ Insertion terminée.")
    except Exception as e:
        raise RuntimeError(f"❌ Erreur lors de l'insertion des embeddings : {e}")
