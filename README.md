# LLaMA Demo

The LLaMA demo is the place to experiment with the [LLaMA][llama-paper] language model.

## ☑️ Requirements

Before starting the project make sure these requirements are available:

- [python][python]. For executing the code in this project.
- [git][git]. For versioning your code.

## 🛠️ Setup

### Create a python environment

First create the virtual environment where the service will store all the modules.

#### Using virtualenv

Using the `virtualenv` command, run the following commands:

```bash
# install the virtual env command
pip install virtualenv

# create a new virtual environment
virtualenv -p python ./.venv

# activate the environment (UNIX)
./.venv/bin/activate

# activate the environment (WINDOWS)
./.venv/Scripts/activate

# deactivate the environment (UNIX & WINDOWS)
deactivate
```

#### Using conda

Install [conda][conda], a program for creating python virtual environments. Then run the following commands:

```bash
# create a new virtual environment
conda create --name llama python=3.8 pip

# activate the environment
conda activate llama

# deactivate the environment
deactivate
```

### Install

To install the requirements run:

```bash
pip install -e .
```

### Model weights

Model weights can be requested [here](https://docs.google.com/forms/d/e/1FAIpQLSfqNECQnMkycAp2jP4Z9TFX0cGR4uf7b_fBxjY_OjhJILlKGA/viewform).

#### Convert official LLaMA weights to HF

🤗 implemented the LLaMA model and also provided a script for converting the official LLaMA weights in this PR [#21955](https://github.com/huggingface/transformers/pull/21955).

Taking the official script, to convert the official LLaMA weights to the format that is compatible with 🤗 run the following script:

```bash
python src/utils/convert_llama_weights_to_hf.py \
    --input_dir /path/to/downloaded/llama/weights \
    --model_size 7B \
    --output_dir /output/path
```

We advise to save the model weights in a separate `/models` folder:

```
/models
    /7B
    /13B
    /30B
    /65B
```

### Configuration

The project can be configured using the `.env` file. To configure the project copy the `.env.example` file to `.env` and change the values.

## 🚀 Start the service

To start the service run:

```bash
python scripts/start_demo.py
```

This will start the service on port `7654` or on the port specified in the `.env` file.

To stop the service press `Ctrl+C` in the terminal.

## 📚 Related Papers

**[LLaMA: Open and Efficient Foundation Language Models][llama-paper]**
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample
arXiv, 2023.

**Abstract:**
We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community.

[python]: https://www.python.org/
[conda]: https://www.anaconda.com/
[git]: https://git-scm.com/
[llama-paper]: https://arxiv.org/abs/2302.13971
