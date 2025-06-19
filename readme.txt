

Projet RAG :

Démarrage : 

Lancer l'image PostgreSQL : 
docker run --name my-postgres \
  -e POSTGRES_PASSWORD=pass \
  -p 5432:5432 \
  -d pgvector/pgvector:pg16


Structure du projet :
Securité/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── main.py
├── rag_pipeline/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── embedder.py
│   ├── db.py
│   ├── retriever.py
│   ├── llm.py
│   └── qa.py
└── readme.txt
