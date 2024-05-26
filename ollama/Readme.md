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

## Stable Diffusion

- install dependencies: `sudo apt install -y make build-essential libssl-dev zlib-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git`
- install pyenv: `curl https://pyenv.run | bash`
- Add to your profile (~/.bashrc or ~/.profile):

  ```env
    export PYENV_ROOT="$HOME/.pyenv"
    [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
  ```

- Test pyenv: `pyenv -h`
- Install python 3.10: `pyenv install 3.10`
- Make python 3.10 the default: `pyenv global 3.10`
- Create directory for stable diffusion: `mkdir -p /opt/www/stablediff; cd /opt/www/stablediff`
- Download stable diffusion shell script: `wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh`
- Make the shell script executable: `chmod +x webui.sh`
- Run: `./webui.sh`
- After downloading it will be running at `http://127.0.01:7860`
  - Generate images by texts

## Stable Diffusion + OpenUI

- In the directory `/opt/www/stablediff` now run the shell script `webui.sh` with the command: `./webui.sh --listen --api`
- Access the Web UI: `http://localhost:8080`
- Settings > Images: Set to `AUTOMATIC1111 Base URL`: `http://127.0.01:7860`
- Click on the refresh button next to the field
- Click on `Save`
- Now when a prompt is answered in OpenUI, an icon will appear to generate an image of the prompt

## Documents + WebUI

- Access the Web UI: `http://localhost:8080`
- In the "Documents" side tab, add any document, for example, `document.txt`.
- Now when creating a new chat use `#document.txt`
  - Select the document
  - Write the prompt using the document as a reference

## Local AI + Obsidian notes

- Go to obsidian > Settings > Community plugins > Search for "BMO"
- Select `BMO Chatbot` and install and enable
- Access obsidian > Settings > Community plugins > `BMO Chatbot` > Click on the settings button
  - In the `Ollama connection` section > Ollama REST API URL > fill in `http://127.0.0.1:11434`
  - Now in the `Profiles > General > Model` section select the desired model
- Now a tab for `BMO` will appear on the right side allowing you to chat with the chatbot within Obsidian
  - Commands
    - `/help` - possible commands
    - `/ref on` - activates reference to the open document
    - `/ref off` - disables reference to the open document
