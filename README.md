# Structured JSON Extraction Engine
An enterprise-grade document intelligence platform transforming unstructured PDF invoices into validated, type-safe JSON objects via schema-enforced LLM orchestration. 🛠️

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

---

⚠️ **CRITICAL SECURITY WARNING:** This application processes untrusted document uploads and handles sensitive financial financial records. Do not upload live production financial datasets to environments utilizing public AI models. All extracted files are cached locally in the configured staging area; modify the storage retention configuration properties to comply with local data privacy policies before deploying to public staging clusters.

---

![Demo](demo.gif) ## Overview
This platform ingests raw digital PDF documents, extracts their textual layouts, and converts them into structured JSON schemas using LLM-guided orchestration. Built primarily for accounts payable teams, data automation pipelines, and engineering teams, it provides deterministic parsing of chaotic documents like invoices. By combining strict data validation contracts with automated storage telemetry, it eliminates manual structural mapping and data entry overhead.

## Features
* Extracts raw string streams from complex multi-page PDF documents cleanly.
* Forces large language models to return deterministic, structural payloads matching predefined models.
* Bridges modern application codebases with legacy backend API routing gateways using customized client adapters.
* Logs complete processing sessions, runtime telemetry data, and structural JSON fields inside a centralized relational registry.
* Provides a premium reactive administrative portal for file processing, data evaluation tables, and parsing status streams.

## Tech Stack
| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **User Interface** | Streamlit | Powers the reactive metrics dashboard and file upload gateway views. |
| **Inference Wrapper** | Instructor | Controls strict structural output matching data blueprints. |
| **AI Model Platform** | Google Gemini | Handles entity resolution and text context evaluation matching metrics. |
| **Data Validation** | Pydantic | Enforces runtime structural formatting, precision bounds, and field types. |
| **Persistence Layer** | SQLite & SQLAlchemy | Records system telemetry metrics, token tracking data, and JSON outputs. |

## Project Structure
```text
structured-json-extractor/
├── app/
│   ├── config.py       # Manages file configurations, absolute paths, and environment validation.
│   ├── crud.py         # Executes structured transactional reads and inserts into database logs.
│   ├── database.py     # Initializer layer for the engine and the logging schemas.
│   ├── errors.py       # Definitions of custom domain exceptions isolating processing layers.
│   ├── extractor.py    # Gateway adapting legacy client wrappers to structured extraction modes.
│   ├── logger.py       # Configuration file managing standardized console and error logs.
│   ├── processor.py    # Manages filesystem reads and extracts text arrays from PDF instances.
│   └── schemas.py      # Declarations of Pydantic models mapping targets and total fields.
├── temp_processing/    # Temporary workspace tracking raw document chunks safely.
├── main.py             # Entrypoint managing view elements and presentation layouts.
├── .env                # Local protected configuration credentials.
└── requirements.txt    # Frozen list of package versions.
