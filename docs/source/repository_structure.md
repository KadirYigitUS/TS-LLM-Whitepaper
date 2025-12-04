# Repository Structure

This document describes the organization and structure of the TS-LLM Knowledge Stack repository.

## Directory Layout

```
TS-LLM-Whitepaper/
├── docs/                      # Documentation source
│   ├── source/               # Sphinx source files
│   │   ├── _static/         # Static assets (images, CSS, JS)
│   │   ├── _templates/      # Custom Sphinx templates
│   │   ├── api_reference/   # API documentation
│   │   ├── conf.py          # Sphinx configuration
│   │   └── *.md             # Documentation pages
│   ├── build/               # Built documentation (generated)
│   ├── Makefile             # Build automation
│   └── requirements.txt     # Documentation dependencies
├── scripts/                  # Utility scripts
├── tests/                   # Test suite
├── .readthedocs.yaml        # ReadTheDocs configuration
├── pyproject.toml           # Project metadata
└── README.rst               # Project README
```

## Key Directories

### Documentation (`docs/`)

The documentation directory contains all Sphinx-related files:

::::{grid} 2

:::{grid-item-card} source/
Markdown and RST source files
:::

:::{grid-item-card} build/
Generated HTML output
:::

:::{grid-item-card} _static/
Images, CSS, JavaScript
:::

:::{grid-item-card} _templates/
Custom Jinja2 templates
:::

::::

### Source Files (`docs/source/`)

| File | Purpose |
|------|---------|
| `index.md` | Main landing page |
| `getting_started.md` | Installation and setup guide |
| `build_pipeline.md` | Build system documentation |
| `knowledge_graphs.md` | Knowledge graph documentation |
| `obsidian_workflow.md` | Obsidian integration guide |
| `repository_structure.md` | This file |
| `troubleshooting.md` | Common issues and solutions |
| `conf.py` | Sphinx configuration |

### Scripts Directory

```
scripts/
├── build.sh              # Build automation
├── deploy.sh             # Deployment script
├── export_obsidian.py    # Export Obsidian notes
└── sync_graph.py         # Sync knowledge graph
```

## Configuration Files

### Sphinx Configuration (`docs/source/conf.py`)

Main configuration for Sphinx documentation:

```python
project = 'TS-LLM Knowledge Stack'
extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_autodoc_typehints',
    'sphinx_design',
    # ... more extensions
]
```

### ReadTheDocs Configuration (`.readthedocs.yaml`)

Configuration for ReadTheDocs builds:

```yaml
version: "2"

build:
  os: "ubuntu-22.04"
  tools:
    python: "3.10"

python:
  install:
    - requirements: docs/requirements.txt

sphinx:
  configuration: docs/source/conf.py
```

### Project Metadata (`pyproject.toml`)

Python project configuration:

```toml
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "lumache"
# ... project metadata
```

## File Naming Conventions

### Documentation Files

- Use lowercase with underscores: `getting_started.md`
- Descriptive names: `knowledge_graphs.md` not `kg.md`
- Consistent extensions: `.md` for Markdown, `.rst` for reStructuredText

### Python Modules

- Lowercase with underscores: `knowledge_graph.py`
- Test files: `test_knowledge_graph.py`
- Package initialization: `__init__.py`

## Build Artifacts

The following directories contain generated files and should not be committed:

```
docs/build/          # Generated documentation
__pycache__/         # Python bytecode cache
*.pyc                # Compiled Python files
.pytest_cache/       # Pytest cache
htmlcov/             # Coverage reports
dist/                # Distribution packages
```

:::{note}
These directories are listed in `.gitignore` and excluded from version control.
:::

## Adding New Content

### Adding a Documentation Page

1. Create a new `.md` file in `docs/source/`:

```bash
touch docs/source/new_page.md
```

2. Add content using Markdown:

```markdown
# New Page Title

Content goes here...
```

3. Add to table of contents in `index.md`:

```markdown
\`\`\`{toctree}
new_page
\`\`\`
```

### Adding API Documentation

1. Create Python module with docstrings:

```python
def function_name(param1, param2):
    """
    Brief description.
    
    Args:
        param1: Description
        param2: Description
        
    Returns:
        Description of return value
    """
    pass
```

2. Generate API docs:

```bash
cd docs
make api
```

### Adding Static Assets

Place files in `docs/source/_static/`:

```
_static/
├── images/
│   └── diagram.png
├── css/
│   └── custom.css
└── js/
    └── custom.js
```

Reference in documentation:

```markdown
![Diagram](_static/images/diagram.png)
```

## Dependencies

### Documentation Dependencies

Listed in `docs/requirements.txt`:

```
sphinx>=7.1.2
sphinx-rtd-theme>=1.3.0
myst-parser>=2.0.0
sphinx-copybutton>=0.5.2
sphinx-autodoc-typehints>=1.24.0
sphinx-design>=0.5.0
```

### Python Dependencies

Listed in `pyproject.toml` or `requirements.txt`.

## Build Process

### Local Build

```bash
# Build HTML documentation
cd docs
make html

# View in browser
open build/html/index.html
```

### Clean Build

```bash
# Remove build artifacts
make clean

# Rebuild from scratch
make html
```

### API Documentation

```bash
# Generate API reference
make api

# Build with API docs
make html
```

## Version Control

### Branches

- `main` - Stable release branch
- `develop` - Development branch
- `feature/*` - Feature branches
- `fix/*` - Bug fix branches

### Commit Messages

Follow conventional commits:

```
type(scope): description

- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes
- refactor: Code refactoring
- test: Test additions/changes
- chore: Build process updates
```

## Continuous Integration

### GitHub Actions

Workflows in `.github/workflows/`:

- `docs.yml` - Build and deploy documentation
- `tests.yml` - Run test suite
- `lint.yml` - Code quality checks

### ReadTheDocs

Automatic builds on:
- Push to `main` branch
- Pull request creation
- Tagged releases

## Best Practices

:::{tip}
**Organization**
- Keep related files together
- Use clear, descriptive names
- Document complex structures
- Maintain consistent conventions
:::

:::{tip}
**Documentation**
- Update docs with code changes
- Include examples and diagrams
- Link related documentation
- Keep README up to date
:::

:::{warning}
**Version Control**
- Don't commit build artifacts
- Don't commit sensitive data
- Use `.gitignore` effectively
- Review changes before committing
:::

## See Also

- {doc}`build_pipeline` - Understanding the build process
- {doc}`getting_started` - Setting up your environment
- {doc}`troubleshooting` - Common issues and solutions
