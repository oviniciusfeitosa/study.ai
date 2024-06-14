# Readme

- Install: `sudo apt install python3-venv`
- Create environment: `python3 -m venv venv`
- Start environment: `source venv/bin/activate`
- Install dependencies: `pip install crewai 'crewai[tools]' duckduckgo-search langchain_community 'unstructured[html]'`
  - Unstructed package:
    - All docs: `pip install "unstructured[all-docs]"`
    - Specific doc: `pip install "unstructured[html]"`
    - Specific docs: `pip install "unstructured[docx,pptx]"`
- Start local Browserless docker container: `docker run -d --rm --name browserless -p 3000:3000 browserless/chrome`
- Create `.env` file: `cp .env.example .env`
- Start application: `python3 main.py`
- Stop environment: `deactivate`