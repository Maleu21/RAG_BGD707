# rag_pipeline/qa.py

from langchain.llms import Ollama
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document

def format_prompt(contexts, question):
    """
    Construit un prompt complet pour le LLM.
    """
    context_str = "\n\n".join(contexts)
    return f"""Voici des informations contextuelles :\n\n{context_str}\n\nQuestion : {question}\n\nRéponse :"""

def ask_llm(question, contexts):
    print("💬 Construction du prompt et interrogation du LLM...")

    if not contexts or not question:
        raise ValueError("❌ Contexte ou question manquants")

    # Formatage du prompt
    prompt = format_prompt(contexts, question)

    try:
        # Initialisation du modèle local via Ollama
        llm = Ollama(model="llama2")  # Assure-toi d’avoir téléchargé ce modèle
        print("🤖 Modèle LLM prêt (Ollama + LLaMA2)")

        # Enrobage LangChain (version simple)
        docs = [Document(page_content=prompt)]
        chain = load_qa_chain(llm, chain_type="stuff")

        result = chain.run(input_documents=docs, question=question)
        print("✅ Réponse générée.")
        return result

    except Exception as e:
        raise RuntimeError(f"❌ Erreur lors de l'interrogation du LLM : {e}")
