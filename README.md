# 📑 Structured JSON Extraction Engine

A robust, enterprise-grade document intelligence platform that transforms raw, unstructured data (like PDF invoices) into strict, type-safe, and validated structured JSON objects. Powered by **Google Gemini**, **Instructor**, **Pydantic**, and **Streamlit**.

---

## 🚀 Key Features

* **Deterministic Schema Enforcement:** Uses Pydantic data blueprints to force the Large Language Model to return 100% predictable JSON structures.
* **Legacy API Adapter Bridge:** Seamlessly intercepts and maps modern data layers to stable enterprise API gateways.
* **Complete PDF Pipeline:** Automates raw document parsing, text extraction buffers, and validation filters.
* **Stateful Storage Tracking:** Automatically records every validation payload, token utilization log, and processing metric inside a structured SQLite ledger.
* **Real-time Analytics Dashboard:** Features a premium administrative monitoring UI for immediate file analysis, line-item itemization tables, and error telemetry flags.

---

## 🏗️ System Architecture

The project implements a clean, decoupled modular layout to isolate computational processing from user interface execution layers:

```text
structured-json-extractor/
├── app/
│   ├── config.py       # Hardened multi-source configurations (.env integration)
│   ├── crud.py         # Database transaction and record operations ledger
│   ├── database.py     # SQLite persistence layer and schema orchestrations
│   ├── errors.py       # Custom platform error tracking exception blocks
│   ├── extractor.py    # Gemini & Instructor structural inference gateway
│   ├── logger.py       # Standard centralized production logger matrices
│   ├── processor.py    # Raw document ingestion and text buffering pipes
│   └── schemas.py      # Pydantic data structure contracts & definitions
├── temp_processing/    # Sandboxed scratchpad tracking file buffers
├── main.py             # Streamlit premium dashboard view orchestration
├── .env                # Protected localized environment keys
└── requirements.txt    # Frozen environment dependency tracks
