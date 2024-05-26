# Ollama

## Install

- **NOTE**: Preference for using an Nvidia graphics card
- install: `curl -fsSL https://ollama.com/install.sh | sh`
- Then access: `http://localhost:11434`

## Run

- Download llama3: `ollama pull llama3`
- Run: `ollama run llama3`
- Watch video card performance: `watch -n 0.5 nvidia-smi`

## OpenWebUI

- Run the WebUI with Docker: `docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main`
- Then access: `http://localhost:8080`
- Click on `Signup`
  - Fill in username and password
  - Acquire administrative privileges

### Use other models

- NOTE: It is also possible to add more than one model to the conversation
- codegemma
  - Downloading codegemma: `ollama pull codegemma`
    - Access the Open Web UI page: `http://localhost:8080`
    - At the top of the page
      - Select the template you would like to use: `codegemma:latest`
- llava
  - Downloading codegemma: `ollama pull llava`
    - Access the Open Web UI page: `http://localhost:8080`
    - At the top of the page
      - Select the model you would like to use: `llava:latest`
    - Click the "+" button and add an image to the conversation
    - Send the prompt and the llava model will be used to analyze the image
