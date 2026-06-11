
# JsonForge

An enterprise-grade document intelligence platform transforming unstructured PDF invoices into validated, type-safe JSON objects via LLM-powered extraction with schema validation. 🛠️

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()



⚠️ **CRITICAL SECURITY WARNING:** This application processes untrusted document uploads and handles sensitive financial financial records. Do not upload live production financial datasets to environments utilizing public AI models. All extracted files are cached locally in the configured staging area; modify the storage retention configuration properties to comply with local data privacy policies before deploying to public staging clusters.
## Screenshots

![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

---

## Overview
This platform ingests raw digital PDF documents, extracts their textual layouts, and converts them into structured JSON schemas using LLM-guided orchestration. Built primarily for accounts payable teams, data automation pipelines, and engineering teams, it provides deterministic parsing of chaotic documents like invoices. By combining strict data validation contracts with automated storage telemetry, it eliminates manual structural mapping and data entry overhead.

---

## Features

| | |
| :--- | :--- |
| **🎯 Schema Enforcement**<br>Forces large language models to return deterministic, structural JSON payloads matching strict target data blueprints. | **🔌 Legacy Adapter Bridge**<br>Bridges modern application codebases with legacy backend API routing gateways using customized client adapters. |
| | |
| **📄 Complete PDF Pipeline**<br>Extracts raw string streams from complex multi-page PDF documents cleanly without formatting loss. | **📊 Relational Registry**<br>Logs complete processing sessions, runtime telemetry data, and structural JSON fields inside a centralized database. |
| | |

--- 


## Demo

Insert gif or link to demo

---

## Project Structure

```text
structured-json-extractor/
├── app/
│   ├── config.py         # Type-safe environment and app configuration settings.
│   ├── crud.py           # Database persistence operations for logged extractions.
│   ├── database.py       # SQLAlchemy database engine connection initialization.
│   ├── errors.py         # Centralized pipeline exception handling and error definitions.
│   ├── extractor.py      # Core Gemini orchestration engine for structured parsing.
│   ├── init_db.py        # Database schema initialization script.
│   ├── logger.py         # Centralized structured logging infrastructure.
│   ├── models.py         # Relational database models for transactional tracking.
│   ├── processor.py      # Raw document layer processing and text extraction engine.
│   └── schemas.py        # Strict Pydantic models defining the extraction contracts.
├── .env.example          # Security environment configuration blueprint file.
├── .gitignore            # Specifying untracked workspace files to exclude from git.
├── main.py               # Main Streamlit dashboard interface entry point.
├── README.md             # Project documentation hub.
└── requirements.txt      # Python dependencies.
```

---

## Prerequisites

| System Layer | Requirements & Blueprint Configuration |
| :--- | :--- |
| **🐍 Engine Core** | **Python 3.10 \| 3.11** |
| | ↳ *Note: 3.12+ causes strict Pydantic/Instructor wheel initialization blocks.* |
| **🎨 Schema Contract** | **Pydantic v2 Blueprint Structure** |
| | ↳ *Core validation models built with strict precision type checks.* |
| **🔑 Inference Key** | **Google AI Studio API Key** |
| | ↳ *Active token mapped to route through `models/gemini-1.5-flash-latest`.* |
## Environment Variables



| Variable | Required | Description |
| :--- | :--- | :--- |
| `GOOGLE_API_KEY` | **Yes** | Developer access token required to authenticate pipeline requests with the Google Gemini ecosystem. |
| | | ↳ *Target Core routing engine mapping path: `models/gemini-1.5-flash-latest`* |
| `DATABASE_URL` | No | Optional relational database connection string for telemetry tracking. |
| | | ↳ *Defaults to a local, automatically generated SQLite instance (`sqlite:///jsonforge.db`) if left unconfigured.* |

---


## Configuration Blueprint 


Create a local configuration file named `.env` in the root directory of your project workspace and inject your operational tokens as shown below:

```bash
# ==============================================================================
# JSONFORGE RUNTIME ENVIRONMENT CONFIGURATION BLUEPRINT
# ==============================================================================

# Google AI Studio Developer Token (Required)
# Secure your access token at: [https://aistudio.google.com/](https://aistudio.google.com/)
GOOGLE_API_KEY=AIzaSyYourActualGeminiStudioTokenPatternHere

# Centralized Telemetry Database Engine Connection String (Optional)
# Leave blank or unconfigured to automatically fallback to local SQLite storage
DATABASE_URL=sqlite:///jsonforge.db
```
---

## 🚀 Quickstart (Local)



1. **Repository Workspace Setup**

```bash
git clone [https://github.com/chhavi03/structured-json-extractor.git](https://github.com/chhavi03/structured-json-extractor.git)
cd structured-json-extractor
```

2. **Set up a virtual environment**
```bash
# Initialize the virtual environment infrastructure
python -m venv venv

# Activate the workspace tracking layers
# On macOS / Linux:
source venv/bin/activate

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Windows (Command Prompt):
.\venv\Scripts\activate.bat
```

3. **Install dependencies**

```bash
# Ensure pip is operating on the latest security wheels
python -m pip install --upgrade pip

# Process the pinned framework dependency manifest
pip install -r requirements.txt
```

4. **Configuration Layer Provisioning**

```bash
# Instantiate your runtime environment variables mapping file
cp .env.example .env
```
⚠️ Action Required: Open the newly generated .env file using your favorite text editor and paste your verified Google AI Studio API key into the GOOGLE_API_KEY field before continuing.

5. **Launch the Local Interactive Dashboard**

```bash
streamlit run main.py
```

After initialization completes successfully, your primary browser tab will launch to track the web interface directly at:

- `http://localhost:8501`

---

## 🧠 How It Works


Structured JSON Extractor orchestrates a deterministic parsing pipeline by fusing large language model intelligence with runtime schema enforcement. When an unstructured file or raw data stream is ingested, the system feeds the textual data layers into a processing matrix. Instead of allowing open-ended, chaotic text generation, the core extraction engine uses an internal validation matrix powered by Pydantic v2 and Instructor. 

This contract layer intercepts data streams flowing from the Google Gemini core framework (`gemini-1.5-flash-latest`), forcing the predictive outputs to conform perfectly to your predefined application data schemas. If raw outputs deviate from the target validation blocks, automated error boundaries handle the pipeline exceptions gracefully. Validated, type-safe data schemas are then stored sequentially using an integrated SQLAlchemy CRUD persistence infrastructure, and real-time operational logs are instantly displayed on the local Streamlit visual deck.
## 👤 Author

- Chhavi Tokhi - https://github.com/chhavi03/CURA
