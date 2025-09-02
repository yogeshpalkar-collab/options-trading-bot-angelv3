# Options Trading Bot (Angel One) - Self-contained SmartApi Version

## Features
- ✅ Bundles SmartApi inside the project with patched __init__.py
- ✅ No dependency on PyPI smartapi-python
- ✅ Clean import: from SmartApi.smartConnect import SmartConnect
- ✅ Works on Render without import errors

## Setup
1. pip install -r requirements.txt
2. streamlit run options_trading_bot_angel.py

## Deployment (Render)
- Build Command:
  ```bash
  pip install -r requirements.txt
  ```
- Start Command:
  ```bash
  streamlit run options_trading_bot_angel.py --server.port 10000 --server.address 0.0.0.0
  ```
