# Contract Analyzer

**AI-powered employment contract analysis — understand what you're signing before you sign it.**

> **Note:** Contract Analyzer is currently built specifically for **employment contracts**. It is not a general-purpose contract analysis tool.

Contract Analyzer parses employment contracts, retrieves relevant legal context via RAG, and uses an LLM to flag risky clauses, explain them in plain English, and suggest negotiation points. A conversational assistant lets you ask follow-up questions about your specific contract.

---

## Why Contract Analyzer

Employment contracts are full of dense, one-sided legal language. Most people sign without fully understanding clauses around IP assignment, non-competes, termination terms, or confidentiality. Contract Analyzer breaks the contract down clause by clause, scores each one against a curated employment-law knowledge base, and tells you — in plain language — what to watch out for and how to push back.

## Features

- 📄 Upload and parse employment contracts (PDF)
- 🔍 Semantic retrieval against a curated legal knowledge base (FAISS)
- ⚠️ Clause-level risk classification: **Fair / Moderate / Risky**
- 📊 Aggregated overall contract risk score
- 💡 Plain-English explanation for every clause
- ✍️ Employee-oriented negotiation suggestions
- 💬 Conversational Q&A over the analyzed contract
- 📥 Structured, exportable contract reports
- ⚡ FastAPI backend + Streamlit frontend

## How It Works

```
Employment Contract (PDF)
        │
        ▼
Clause Extraction (LLM)
        │
        ▼
Semantic Retrieval (FAISS + knowledge base)
        │
        ▼
Clause-Level Risk Analysis (LLM)
        │
        ▼
Risk Scoring & Aggregation
        │
        ▼
Structured Report Generation
        │
        ▼
Interactive Contract Q&A
```

### Pipeline Stages

1. **Clause Extraction** — the contract is parsed and split into individual clauses.
2. **Semantic Retrieval** — each clause is embedded and matched against a 25-entry employment-law knowledge base to ground the analysis.
3. **LLM Legal Analysis** — each clause is broken down into its **Meaning**, **Risk** classification, a plain-English **Explanation**, and a **Negotiation Tip** (or a note that no negotiation is needed if the clause is already balanced).
4. **Risk Scoring** — individual clause scores roll up into an overall contract risk score and level.
5. **Report Generation** — a structured report with summary, high-attention clauses, and full clause-level detail.
6. **Contract Assistant** — ask natural-language questions about the analyzed contract and get grounded answers.

## Example Output

**Report Summary**

```
Risk Score : 20
Risk Level : Low
Clauses    : 2

Summary
This contract contains 2 analyzed clauses. Overall, the agreement
appears balanced and follows standard employment practices. No
significant legal concerns were identified, though you should
always review the terms carefully before signing.
```

**Per-Clause Breakdown**

Each clause in the report expands into:

```
Clause
  [Full clause text as written in the contract]

Meaning
  [Plain-English restatement of what the clause means]

Risk
  Fair / Moderate / Risky

Explanation
  [Why the clause received this risk classification]

Negotiation Tip
  [Suggested language or approach — or "No negotiation
  needed" if the clause is already balanced]
```

**Contract Assistant**

Once a contract is analyzed, you can ask follow-up questions like *"what are the risky clauses in it?"* and get answers grounded in the actual clause-level report — including which clauses were reviewed, their risk scores, and why they were classified that way.

## Tech Stack

| Layer | Tools |
|---|---|
| Backend | FastAPI, Python |
| Frontend | Streamlit |
| LLM / Orchestration | LangChain, Groq (`llama-4-scout-17b-16e-instruct`), Cerebras (overflow fallback) |
| Embeddings | Hugging Face |
| Vector Store | FAISS |
| Validation | Pydantic |
| Document Processing | PyMuPDF |

## Project Structure

```
ContractAnalyzer/
├── backend/
│   ├── app.py
│   ├── routes.py
│   └── service.py
├── frontend/
│   ├── Home.py
│   ├── Dashboard.py
│   ├── Chat.py
│   └── components.py
├── src/
│   ├── clause_extractor.py
│   ├── rag_chain.py
│   ├── vector_db.py
│   ├── scorer.py
│   ├── report_generator.py
│   ├── question_answer.py
│   ├── prompts.py
│   ├── models.py
│   └── config.py
├── data/
├── requirements.txt
├── README.md
└── .env
```

## Installation

```bash
git clone https://github.com/yourusername/ContractAnalyzer.git
cd ContractAnalyzer

python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

Configure environment variables in `.env`:

```
GROQ_API_KEY=your_groq_api_key
CEREBRAS_API_KEY=your_cerebras_api_key
MODEL_NAME=meta-llama/llama-4-scout-17b-16e-instruct
```

Run the backend:

```bash
uvicorn backend.app:app --reload
```

Run the frontend:

```bash
streamlit run frontend/Home.py
```

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/analyze` | POST | Uploads a contract, returns a full AI-generated risk report |
| `/chat` | POST | Answers natural-language questions grounded in the analyzed contract |

## Roadmap

- [ ] Multi-language contract support
- [ ] Side-by-side comparison of multiple contracts
- [ ] OCR for scanned PDFs
- [ ] Contract version diffing
- [ ] Clause recommendation engine
- [ ] Organization-specific legal knowledge bases
- [ ] Multi-agent workflow via LangGraph
- [ ] Export reports to PDF / Word
- [ ] User authentication and analysis history

## Contributing

Contributions are welcome — fork the repo, create a feature branch, and open a pull request.

## License

MIT License.

---

⭐ If Contract Analyzer is useful to you, consider starring the repo — it helps others find it.
