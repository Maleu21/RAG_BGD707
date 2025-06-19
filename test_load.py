from datasets import load_dataset

print("🚀 Chargement en cours...")
dataset = load_dataset("neural-bridge/rag-dataset-12000", split="train")
print("✅ Chargé avec succès :", len(dataset), "éléments")
