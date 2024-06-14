# Benchmark

- Install: `sudo apt install python3-venv`
- Create environment: `python3 -m venv venv`
- Start environment: `source venv/bin/activate`
- Install: `pip install -r requirements.txt`
- Before running benchmarks, make sure your Ollama model server is running: `ollama serve`
- Run: `python benchmark.py --verbose --prompts "What is the sky blue?" "Write a report on the financials of Nvidia"`

## References

- [Benchmark Throughput Performance with running local large language models (LLMs) via ollama](https://llm.aidatatools.com/)
- [LLM Benchmark (ollama only)](https://github.com/MinhNgyuen/llm-benchmark)
- [Benchllama](https://github.com/srikanth235/benchllama)