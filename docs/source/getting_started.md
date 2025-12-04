# Getting Started

This guide will help you get started with the TS-LLM Knowledge Stack.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip package manager
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KadirYigitUS/TS-LLM-Whitepaper.git
cd TS-LLM-Whitepaper
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Build the Documentation

```bash
cd docs
make html
```

The documentation will be built in the `docs/build/html` directory.

## Quick Start

### Basic Usage

Here's a simple example to get you started:

```python
import lumache

# Get random ingredients
ingredients = lumache.get_random_ingredients()
print(ingredients)
```

## Next Steps

- Read the {doc}`build_pipeline` to understand the system architecture
- Explore the {doc}`knowledge_graphs` documentation
- Learn about the {doc}`obsidian_workflow`

## Configuration

### Environment Setup

Create a `.env` file in the root directory:

```bash
# Example configuration
DEBUG=true
LOG_LEVEL=info
```

### API Keys

If using LLM features, configure your API keys:

```bash
OPENAI_API_KEY=your_api_key_here
```

:::{warning}
Never commit API keys to version control. Use environment variables or a secure secrets manager.
:::

## Troubleshooting

If you encounter issues during installation, see the {doc}`troubleshooting` guide.
