
## Introduction

ToolScan is a comprehensive benchmark designed to help evaluate common error patterns identified in large language models (LLMs) during tool use tasks.
 1. **Holistic Dataset**: ToolScan incorporates 10 distinct environments and 30 different tasks to comprehensively understand the generalist ability of LLM agents, which is built upon LLM's extensive knowledge base and exceptional scenario comprehension.
 2. **Multi-round Intercation**: ToolScan provides multi-round interaction between agents and environment, which is necessary to reflect the evolutionary nature of human intelligence, which continuously receives information and adapts towards the environment.
 3. **Error Quantification Platform**: Recognizing the brittleness of tool calls, where slight changes to arguments, missing arguments, or incorrect calls can lead to drastically different and incorrect results, ToolScan establishes a robust error quantification platform. This platform is crucial for identifying and catching output errors effectively.

<div align="left">


## 🚀 Quick Start 

Here we provide a quick start guide to evaluate LLM agents on ToolScan within 30 minutes. 

### Setup Environment

<details>

**Step 1. Create a conda environment**
```shell
conda create -n ${YOUR_ENV_NAME} python=3.8.13  # python version should be 3.8.13
conda activate ${YOUR_ENV_NAME}
```

**Step 2. Git clone this repo**


**Step 3. Download the data from huggingface**
```shell
# Download the data and move it to the project root dir
cd toolscan
pip install -r requirements.txt
```


### Setup Environment Variables in `toolscan/.env`
Environment Variables needed for ToolScan include:
```
PROJECT_PATH = {path to project}/ToolScan

ANTHROPIC_API_KEY=...
OPENAI_API_KEY=...


MOVIE_KEY=...

```
<details>
<summary>
Click to expand API key setup procedures.
</summary>

**Variables 1: API keys for Tool tasks**

Since API keys for **Tool** tasks are private, we do not provide them in this repo.

Please follow this detailed [guide](./toolscan/pages/keys.md) to get API keys for **Tool** tasks.


**Variables 3: API keys for Proprietary models**

**⚠️ You don't need to setup API keys for models you don't want to use.**

If you use OpenAI models, please put your API keys in `.env` file.
```shell
OPENAI_API_TYPE="open_ai"
OPENAI_API_KEY=${YOUR_OPENAI_API_KEY}
```

If you use Anthropic models, please put your API keys in `.env` file.
```shell
ANTHROPIC_API_KEY=${YOUR_ANTHROPIC_API_KEY}
```
</details>


#### Local log files
In addition to online results viewing, local logs are automatically stored in `{log_path}`. In WebArena, we additionally support more detailed trajectory files, including web page screenshots and network traffic records.
<details>
  <summary>
    Log file organization: 
  </summary>

```
{log_path}
├── results                    # detailed example-wise logs for each task
│  ├── model-name     
│  │  ├── logs
│  │  │  ├── task_data
│  │  ├── ...
│  ├── ...
├── all_results.txt         # overall metrics for each task
└── ...              
```
</details>


## Data
Not yet released.
```
data
├── total
│   └── test.jsonl
```

</details>


## Evaluation Details
### Evaluation Preparation

#### Internet Access
For regions with Internet restrictions, please make sure that the machine can access the Internet.

You can check whether you have network issues by observing the output during the execution process.

### Running Proprietary Models
In this section, we provide a script to evaluate the closed-source models on each task.

Please do not forget to set the environment variables (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`) before running the following commands.


We provide a quick start script to evaluate the `gpt-3.5-turbo-0613`.

```shell
python ToolScan/evaluation.py \
    --PROJECT_PATH /export/home/ToolScan/
    --cfg-path toolscan/configs/main_results_all_tasks.yaml \
    --task-data total \
    --model gpt-3.5-turbo-0613 \
    --log_path ./results/gpt-3.5-turbo-0613 \
```
Parameters:
- `--PROJECT_PATH`: 
- `--cfg-path`: The relative path of the config file, please refer to `toolscan/configs/main_results_all_tasks.yaml` for more details.
- `--task-data`: The data folder to be evaluated 
- `--model`: The LLM to be evaluated. We provide some LLM models, including:
  - `gpt-3.5-turbo`
  - `gpt-3.5-turbo-16k`
  - `gpt-4`
  - `text-davinci-003`
  - `claude2`
- `log_path`: Path to save logs, as specified [here](#check-and-analyze-results).


### Running Open-source Models
In ToolScan, we have pre-supported the following 8 open-source models, by default we use `vLLM` to speed up inference.
  - `llama2-13b`
  - `llama2-34b`
  - `codellama-13b`
  - `codellama-34b`
  - `vicuna-13b-16k`
  - `lemur-70b`
  - `deepseek-67b`
  - `mistral-7b`

> Please refer to `toolscan/configs/main_results_all_tasks.yaml` for more details about these models.

```
