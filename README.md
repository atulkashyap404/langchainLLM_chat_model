# LangchainLLM_Chat_Modes

LangchainLLM_Chat_Modes is a project that demonstrates the integration of Langchain with OpenAI to create various chat modes using large language models (LLMs).

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The LangchainLLM_Chat_Modes project leverages OpenAI's powerful language models to create different chat modes for various applications. Whether you need a conversational agent for customer support, a creative writing assistant, or an educational tutor, this project provides a flexible framework to build upon.

## Features

- **Multiple Chat Modes**: Supports various chat modes such as customer support, creative writing, and educational tutoring.
- **Easy Integration**: Simple integration with OpenAI's API and Langchain.
- **Extensible**: Easily extendable to add more chat modes or customize existing ones.
- **Configurable**: Customizable configurations for different use cases.

## Installation

To get started, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/yourusername/langchainLLM_chat_modes.git
cd langchainLLM_chat_modes
pip install -r requirements.txt
```
## Usage

- Set up OpenAI API key: Obtain your OpenAI API key from the OpenAI website.
- Run the application: Start the application with the following command:
```bash
python main.py
```
- Select Chat Mode: Choose the desired chat mode from the available options and start interacting with the LLM.

  ##Configuration

  - Configuration settings can be modified in the config.yaml file. Here, you can specify different parameters such as API keys, chat mode settings, and more.

  - Example config.yaml:

    
    openai:
  api_key: 'your_openai_api_key_here'

chat_modes:
  - mode: 'customer_support'
    description: 'Handles customer support queries'
  - mode: 'creative_writing'
    description: 'Assists with creative writing tasks'
  - mode: 'educational_tutor'
    description: 'Provides educational tutoring'

##Contributing
- We welcome contributions to enhance the project! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
      - Fork the repository.
      - Create a new branch: git checkout -b feature-branch-name
      - Make your changes and commit them: git commit -m 'Add some feature'
      - Push to the branch: git push origin feature-branch-name
      - Open a pull request.
