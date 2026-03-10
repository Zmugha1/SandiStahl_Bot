# Sandy Bot POC

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Sandy Bot - Coaching Assistant POC**
> 
> Client Profiles | Pipeline Visualizer | Coaching Assistant | Post Call Analysis

## Overview

Sandy Bot is a proof-of-concept coaching assistant built on the MLDLC Governance Framework. It provides client profile management, pipeline visualization, AI coaching assistance, and post-call analysis capabilities.

## Quick Start

### Deploy to Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io)
2. Click **"New app"**
3. Select: `Zmugha1/SandiStahl_Bot`
4. Branch: `feature/sandy-bot-poc`
5. Main file path: `app/main.py`
6. Add `OPENAI_API_KEY` in the app secrets
7. Click **"Deploy"**

### Local Development

```bash
# Clone repository
git clone https://github.com/Zmugha1/SandiStahl_Bot.git
cd SandiStahl_Bot

# Switch to Sandy Bot branch
git checkout feature/sandy-bot-poc

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key to .streamlit/secrets.toml
# OPENAI_API_KEY = "your-key-here"

# Run Streamlit app
streamlit run app/main.py
```

## Repository Structure

```
SandiStahl_Bot/
├── app/
│   ├── pages/
│   │   ├── 18_Client_Profiles.py      # Client profile management
│   │   ├── 19_Pipeline_Visualizer.py  # Pipeline visualization
│   │   ├── 20_Coaching_Assistant.py   # AI coaching assistant
│   │   └── 21_Post_Call_Analysis.py   # Post-call analysis
│   └── main.py
├── src/
│   ├── coaching/                      # Sandy Bot coaching module
│   │   ├── client.py
│   │   ├── client_memory.py
│   │   ├── pipeline_monitor.py
│   │   └── compartment.py
│   └── prompts/
│       └── coaching_prompts.py
├── schemas/
│   └── client_profile.json
├── .streamlit/
│   └── secrets.toml                   # Local dev (add OPENAI_API_KEY)
└── requirements.txt
```

## Sandy Bot Components

| Component | Description |
|-----------|-------------|
| Client Profiles | Manage client profiles and compartments |
| Pipeline Visualizer | Visualize coaching pipeline stages |
| Coaching Assistant | AI-powered coaching conversations |
| Post Call Analysis | Analyze calls and generate insights |

## Upstream

This POC is based on [MLDLC Governance Framework](https://github.com/Zmugha1/mldlc-governance-framework). To sync upstream changes:

```bash
git fetch upstream
git merge upstream/main
```

## License

MIT License - see [LICENSE](LICENSE) file.
