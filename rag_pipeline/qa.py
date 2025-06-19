# rag_pipeline/qa.py

from langchain_community.llms import Ollama  # ✅ nouveau chemin
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
        # Initialisation d’Ollama avec le modèle local phi3:mini
        llm = Ollama(model="phi3:mini", base_url="http://localhost:11434")  # ✅ clair et compatible
        print("🤖 Modèle LLM prêt (Ollama + phi3:mini)")

        # Enrobage LangChain (chaîne simple)
        docs = [Document(page_content=prompt)]
        chain = load_qa_chain(llm, chain_type="stuff")

        result = chain.run(input_documents=docs, question=question)
        print("✅ Réponse générée.")
        return result

    except Exception as e:
        raise RuntimeError(f"❌ Erreur lors de l'interrogation du LLM : {e}")
