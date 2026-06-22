from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="flintapi",
    version="0.1.0",
    author="FlintAPI",
    author_email="support@flintapi.ai",
    description="One API key for 25+ Chinese LLMs — OpenAI-compatible client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moozechen/flintapi",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["openai>=1.0.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="llm, api, chinese, deepseek, qwen, kimi, glm, minimax, openai, chatgpt",
)
