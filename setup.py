from setuptools import setup, find_packages

setup(
    name="traum-tokenizer-hub",
    version="0.1.0",
    description="Tooling, benchmarks, and CLI evaluation for the traum-tokenizer model family.",
    author="Tarek Mohamed",
    author_email="seotarek@gmail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "traum-eval=traum_tokenizer.cli:main",
        ],
    },
    python_requires=">=3.8",
)
