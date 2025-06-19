# rag_pipeline/data_loader.py
from datasets import load_dataset as hf_load_dataset

def load_data():
    print("📦 Chargement du dataset depuis Hugging Face...")
    dataset = hf_load_dataset("neural-bridge/rag-dataset-12000", split="train")
    docs = [{"context": row["context"]} for row in dataset if "context" in row]
    print(f"✅ {len(docs)} documents chargés.")
    return docs
