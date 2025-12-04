# API Reference

This section contains the API documentation for the TS-LLM Knowledge Stack.

## Overview

The API is organized into the following modules:

```{toctree}
:maxdepth: 2

modules
```

## Quick Reference

### Core Modules

::::{grid} 2

:::{grid-item-card} lumache
Main module for recipe generation
:::

:::{grid-item-card} knowledge_graph (planned)
Knowledge graph operations
:::

:::{grid-item-card} pipeline (planned)
Build pipeline components
:::

:::{grid-item-card} obsidian (planned)
Obsidian integration utilities
:::

::::

## Module Documentation

The API documentation is automatically generated from Python docstrings using Sphinx autodoc.

See the {doc}`modules` page for detailed API documentation of all modules.

## Usage Examples

### Basic Example

```python
import lumache

# Get random ingredients
ingredients = lumache.get_random_ingredients()
print(ingredients)
# Output: ['shells', 'gorgonzola', 'parsley']
```

### With Kind Parameter

```python
import lumache

try:
    ingredients = lumache.get_random_ingredients(kind=['vegetables'])
    print(ingredients)
except lumache.InvalidKindError as e:
    print(f"Error: {e}")
```

## Type Hints

The API uses Python type hints for better IDE support and documentation:

```python
from typing import Optional, List

def get_random_ingredients(kind: Optional[List[str]] = None) -> List[str]:
    """
    Return a list of random ingredients as strings.
    
    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    pass
```

## Contributing

When adding new API functions:

1. Include comprehensive docstrings
2. Use type hints
3. Add examples in docstrings
4. Update this API reference

## See Also

- {doc}`../getting_started` - Getting started guide
- {doc}`../build_pipeline` - Understanding the pipeline
- {doc}`../troubleshooting` - Common issues
