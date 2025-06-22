

Projet RAG :

Démarrage : 

Lancer un environnement virtuel : 
source path/to/rag-env/bin/activate
 
Lancer le script bash d’installation LLM :
./download.sh
(au besoin faire : dos2unix download_LLM.sh puis chmod +x download.sh)

Lancer l'image PostgreSQL : 
docker run --name my-postgres \
  -e POSTGRES_PASSWORD=pass \
  -p 5432:5432 \
  -d pgvector/pgvector:pg16

Executer : 
python3 main.py


Structure du projet :
Securité/
├── requirements.txt
├── main.py
├── rag_pipeline/
│   ├── __init__.py
│   ├── loader.py
│   ├── embeddings.py
│   ├── database.py
│   ├── retriever.py
│   ├── LLM.py
│   └── qa.py
└── README.txt
