# Karpathy Zero to Hero

Personal workspace for following Andrej Karpathy's Neural Networks: Zero to Hero material.

## Layout

```text
.
├── 01-micrograd/          # scalar autograd and backpropagation
├── 02-makemore/           # character-level language model basics
├── 03-mlp/                # MLP language model
├── 04-batchnorm/          # activations, gradients, batch normalization
├── 05-wavenet/            # WaveNet-style character model
├── 06-gpt-from-scratch/   # transformer / GPT implementation
├── 07-tokenization/       # tokenizer notes and experiments
├── notes/                 # written study notes
├── notebooks/             # exploratory notebooks
├── scripts/               # utility scripts
└── data/                  # local datasets, ignored by git except .gitkeep files
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

Check the local environment:

```bash
python scripts/check_env.py
```

## Workflow

1. Watch the relevant video section.
2. Reproduce the code in the matching lesson directory.
3. Keep scratch exploration in `notebooks/`.
4. Move durable notes into `notes/`.
5. Keep downloaded datasets or generated artifacts under `data/`.

## Progress

- [ ] 01 Micrograd
- [ ] 02 Makemore
- [ ] 03 MLP
- [ ] 04 BatchNorm
- [ ] 05 WaveNet
- [ ] 06 GPT from Scratch
- [ ] 07 Tokenization
