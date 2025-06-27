# :money_with_wings: :chart_with_upwards_trend: Stock Market Agentic Chatbot :bar_chart: :technologist:

* ### _A production grade conversational assistant that ingests and understands financial documents.Built with Retrieval-Augmented Generation (RAG),it allows users to upload PDFs files,process them into a vector database (Pinecone),and interact via natural language to receive contextual,AI-powered answers about the stock market._
* ### _This project combines real-time data, semantic retrieval, and agentic reasoning to offer a smart, domain-specific assistant for financial analytics._

![banner-6-1](https://github.com/user-attachments/assets/12578004-6ce9-4a80-8b08-a12f3ef1eafb)



## 👨‍💻Techniques Used :arrow_forward:

* ### Backend (FastAPI) :arrow_right:

               >  Exposes endpoints for document upload (/upload) and user queries (/query).

               >  Each query is processed via a GraphBuilder which invokes a LangGraph-based RAG workflow.

* ### Data Ingestion :arrow_right:  

               > File Handling: Uses tempfile to safely handle uploaded documents.

               > Parsing: Supports .pdf with PyPDFLoader and .docx with Docx2txtLoader.

               > Chunking: Splits large texts into semantic chunks via RecursiveCharacterTextSplitter.

               > Embedding: Encodes text with GoogleGenerativeAIEmbeddings (via LangChain).

               > Vector Store: Indexes chunks in Pinecone with UUIDs as IDs.

* ### Retrieval Tools :arrow_right:

               > Retriever_tool: Retrieves top-k chunks with threshold-based similarity filtering.

               > PolygonFinancials: Integrates real-time financial market data from Polygon.io.

               > TavilySearch: (optionally) enables enhanced web search via Tavily API.

* ### LLM and Graph :arrow_right:

               > Groq-hosted LLM: Uses ChatGroq from langchain-groq to answer questions based on retrieved context.

               > LangGraph: Controls the query lifecycle and memory structure.

               > Prompt Templates: Custom prompt design ensures responses are grounded in retrieved data.

* ### Frontend (Streamlit) :arrow_right:

               >  Sidebar upload for document ingestion.

               >  Real-time chat interface with bot response display.

               >  Uses st.session_state to preserve chat history.

               >  Shows detailed error handling and feedback for every interaction.

## 🧠 Libraries & Technologies :arrow_forward:

* __FastAPI__: Web framework for serving chat and upload endpoints.

* __Streamlit__: User interface for upload and chat.

* __LangChain__: Framework for chaining LLM and retrieval.

* __LangGraph__: Agent workflow handler for managing graph-based LLM interactions.

* __Pinecone__: Vector database to store and retrieve semantic chunks.

* __Google Generative AI Embeddings__: Text-to-vector embedding model.

* __ChatGroq__: Groq-powered inference engine for LLMs.

* __Polygon Financials__: Real-time market data as a LangChain tool.

* __TavilySearch__: External web search augmentation tool.
  
![Screenshot_25-6-2025_234736_localhost](https://github.com/user-attachments/assets/3f13957d-8023-45d4-865b-89b7d4f5517d)
