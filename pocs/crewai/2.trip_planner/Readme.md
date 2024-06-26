# Readme

- Install: `sudo apt install python3-venv`
- Create environment: `python3 -m venv venv`
- Start environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
  - Unstructed package:
    - All docs: `pip install "unstructured[all-docs]"`
    - Specific doc: `pip install "unstructured[html]"`
    - Specific docs: `pip install "unstructured[docx,pptx]"`
- Start
  - Create `.env` file: `cp .env.example .env`
  - Lock poetry dependencies: `poetry lock`
  - Install poetry dependencies: `poetry install`
  - Start local Browserless docker container: `docker run -d --rm --name browserless -p 3000:3000 browserless/chrome`
  - Start application: `poetry run trip_planner_crew`
- Stop environment: `deactivate`
