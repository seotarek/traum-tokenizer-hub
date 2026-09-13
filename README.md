# Traum Tokenizer Hub 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Model%20Hub-yellow.svg)](https://huggingface.co/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Evaluation tools, benchmarking utilities, and CLI analysis for the `traum-tokenizer` model family on Hugging Face.**

Developed by **Tarek Mohamed** ([@seotarek](https://github.com/seotarek))

---

## 📌 Overview

Standard multilingual tokenizers (such as LLaMA or GPT tokenizers) suffer from severe subword fragmentation when processing Arabic text, often requiring **2.5 to 3.8 tokens per word**. This inflates inference latency and API costs significantly.

`traum-tokenizer` addresses this by optimizing byte-pair encodings for Arabic morphology and common dialectal prefixes, achieving a fertility ratio of **~1.35 tokens per word** (up to **50%+ token savings**).

---

## 🚀 Installation & Usage

### 1. Install via pip
```bash
git clone https://github.com/seotarek/traum-tokenizer-hub.git
cd traum-tokenizer-hub
pip install -e .
```

### 2. Run Token Evaluation CLI
```bash
traum-eval "الذكاء الاصطناعي وهندسة البرمجيات والأنظمة الموزعة"
```

Output:
```text
📊 Traum Tokenizer Efficiency Report:
  • Words: 7
  • Characters: 54
  • Generic Tokenizer Tokens: 20
  • Traum Tokenizer Tokens:   9
  • Token Savings:            55.0%
  • Fertility Ratio:          1.29 tokens/word
```

---

## 📜 License
Licensed under the [MIT License](LICENSE).
