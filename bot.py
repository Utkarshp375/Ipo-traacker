name: IPO Auto Checker (IST)

on:
  schedule:
    # UTC time mujab 11:30 UTC = IST 5:00 PM (17:00). 
    # Sanje 5 vagya pachi ratra sudhi dar 10 minute e run thase.
    - cron: '30-59/10 11-18 * * *'
  workflow_dispatch:

jobs:
  run-checker:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install requests gspread oauth2client pytz beautifulsoup4

      - name: Run Script
        run: python bot.py
