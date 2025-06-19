#!/bin/bash

echo "📥 Installation d'Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

echo "✅ Vérification de l'installation..."
ollama --version || { echo "❌ Ollama non installé correctement."; exit 1; }

echo "🚀 Démarrage du serveur Ollama..."
ollama serve > /dev/null 2>&1 &

# Attente que le serveur réponde
echo "⏳ Attente du serveur..."
sleep 5

echo "📦 Téléchargement du modèle léger phi3:mini..."
ollama pull phi3:mini

echo "✅ Modèle téléchargé et prêt."
