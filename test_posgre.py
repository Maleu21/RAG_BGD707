# test_postgres_connexion.py

import psycopg

# Exemple de configuration (à adapter)
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "pass"
}


try:
    print("Tentative de connexion à PostgreSQL...")
    conn = psycopg.connect(**DB_CONFIG)
    print("✅ Connexion réussie !")
    conn.close()
except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
