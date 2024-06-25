# Readme

- Install: `sudo apt install python3-venv`
- Create environment: `python3 -m venv venv`
- Start environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Start local Browserless docker container: `docker run -d --rm --name browserless -p 3000:3000 browserless/chrome`
- Create `.env` file: `cp .env.example .env`
- Start application: `python3 main.py`
- Stop environment: `deactivate`

## Todo

- Test
  - Prompts
    - [ ] 'Differences between the neighborhoods in sudoeste and octogonal'

## References

- [Github - JayZeeDesign/researcher-gpt](https://github.com/JayZeeDesign/researcher-gpt/blob/main/app.py)
- [Github - mickymultani/jsonQueryRAG](https://github.com/mickymultani/jsonQueryRAG/)
