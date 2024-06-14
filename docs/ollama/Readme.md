# Ollama

## Install

- **NOTE**: Preference for using an Nvidia graphics card
- Download and install: `curl -fsSL https://ollama.com/install.sh | sh`
  - Open `/etc/systemd/system/ollama.service`
  - Then add `Environment="OLLAMA_HOST=0.0.0.0"` below `[Service]`
  - Save it
  - Reload systemd and restart Ollama: `sudo systemctl daemon-reload; sudo systemctl restart ollama`
- Then access: `http://localhost:11434`

## Run

- Download llama3: `ollama pull llama3`
- Download phi3: `ollama pull phi3`
- Run: `ollama run llama3`
- Watch video card performance: `watch -n 0.5 nvidia-smi`

## Commands

- Benchmark
  - llm_benchmark
    - Install: `pip install llm-benchmark`
    - Send systeminfo and benchmark results to a remote server: `llm_benchmark run`
    - Do not send systeminfo and benchmark results to a remote server: `llm_benchmark run --no-sendinfo`
    - Benchmark run on explicitly given the path to the ollama executable: 
      - Custom path: `llm_benchmark run --ollamabin=~/code/ollama/ollama`
      - Dynamic path: `llm_benchmark run --ollamabin=$(which ollama)`
    - References
      - [Benchmark Throughput Performance with running local large language models (LLMs) via ollama](https://llm.aidatatools.com/)
      - [Github - ollama-benchmark](https://github.com/aidatatools/ollama-benchmark)

## OpenWebUI

- Options to run the WebUI with Docker:
  - Basic: `docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main`
    - Then access: `http://localhost:8080`
  - With bundled Ollama support
    - `docker run -d -p 9999:8080 -v ollama:/root/.ollama -v /opt/www/open-webui/open-webui/data:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama`
  - Using NVIDIA GPU: `docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda`
    - Then access: `http://localhost:3000`
  - Store data in another folder:
    - (*) You can set another folder to store data like `/opt/www/open-webui/open-webui/data`, e.g.
    - Use the command: `docker run -d -p 9999:8080 --add-host=host.docker.internal:host-gateway -e OLLAMA_BASE_URL=http://host.docker.internal:11434 -v /opt/www/open-webui/open-webui/data:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main`
    - Then access: `http://localhost:9999`
  - Using an alias:
    - Open your profile or aliases preference: `vim ~/.sh_aliases`
    - Add the aliases:
      - To start webui: `alias startWebui="docker run -d -p 9999:8080 --add-host=host.docker.internal:host-gateway -e OLLAMA_BASE_URL=http://host.docker.internal:11434 -v /opt/www/open-webui/open-webui/data:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main ; echo 'open http://localhost:9999'"`
      - To stop webui: `alias stopWebui="docker rm -f open-webui"`
    - Source yout profile or aliases: `source ~/.sh_aliases`
    - Then start Open Webui: `webui`
- Click on `Signup`
  - Fill in username and password
  - Acquire administrative privileges

### Use other models

- NOTE: It is also possible to add more than one model to the conversation
- **codegemma**
  - Downloading codegemma: `ollama pull codegemma`
    - Access the Open Web UI page: `http://localhost:8080`
    - At the top of the page
      - Select the template you would like to use: `codegemma:latest`
- **llava**
  - Downloading codegemma: `ollama pull llava`
    - Access the Open Web UI page: `http://localhost:8080`
    - At the top of the page
      - Select the model you would like to use: `llava:latest`
    - Click the "+" button and add an image to the conversation
    - Send the prompt and the llava model will be used to analyze the image

## Stable Diffusion

- Install dependencies: `sudo apt install -y make build-essential libssl-dev zlib-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git`
- Install pyenv: `curl https://pyenv.run | bash`
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

## Stable Diffusion + Open Webui

- In the directory `/opt/www/stablediff` now run the shell script `webui.sh` with the command: `./webui.sh --listen --api`
- Access the Web UI: `http://localhost:8080`
- Settings > Images: Set to `AUTOMATIC1111 Base URL`: `http://127.0.01:7860`
- Click on the refresh button next to the field
- Click on `Save`
- Now when a prompt is answered in OpenUI, an icon will appear to generate an image of the prompt

## Documents + Open Webui

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

## AnythingLLM vs Open Webui

- [Official site](https://useanything.com/)
- [Github](https://github.com/Mintplex-Labs/anything-llm)

- Tutorials
  - Videos
    - [x] [Unleash the power of Local LLM's with Ollama x AnythingLLM](https://www.youtube.com/watch?v=IJYC6zf86lU)
    - [ ] [AnythingLLM Cloud: Fully LOCAL Chat With Docs (PDF, TXT, HTML, PPTX, DOCX, and more)](https://www.youtube.com/watch?v=SP-Y_9OEaFg)

## References

- [Hosting an AI chatbot with Ollama and Open WebUI](https://community.hetzner.com/tutorials/ai-chatbot-with-ollama-and-open-webui)
- [Ollama - FAQ](https://github.com/ollama/ollama/blob/main/docs/faq.md)
