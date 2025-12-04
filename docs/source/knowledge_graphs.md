# Knowledge Graphs

Knowledge graphs are the core data structure in the TS-LLM Knowledge Stack, representing entities and their relationships.

## Overview

A knowledge graph is a structured representation of information that captures:

- **Entities**: Objects, concepts, or things
- **Relationships**: Connections between entities
- **Attributes**: Properties of entities and relationships

## Structure

### Entity Types

::::{grid} 2

:::{grid-item-card} Concepts
Abstract ideas and theories
:::

:::{grid-item-card} Documents
Papers, articles, and notes
:::

:::{grid-item-card} People
Authors, researchers, contributors
:::

:::{grid-item-card} Projects
Software projects and repositories
:::

::::

## Visualization

Below is an interactive visualization of the knowledge graph:

```{raw} html
<div style="width: 100%; height: 600px; border: 1px solid #ddd; margin: 20px 0;">
    <iframe 
        src="https://example.com/knowledge-graph-visualization" 
        width="100%" 
        height="100%" 
        frameborder="0"
        style="border: none;">
    </iframe>
</div>
```

:::{note}
The interactive visualization above shows real-time data from the knowledge graph. You can zoom, pan, and click on nodes to explore relationships.
:::

## Graph Schema

```{mermaid}
graph TD
    A[Document] -->|authored_by| B[Person]
    A -->|contains| C[Concept]
    C -->|related_to| D[Concept]
    A -->|part_of| E[Project]
    E -->|uses| F[Technology]
```

## Building Knowledge Graphs

### Automated Construction

Knowledge graphs can be built automatically from various sources:

```python
from knowledge_graph import GraphBuilder

builder = GraphBuilder()
builder.add_source('documents/*.md')
builder.add_source('data/*.json')
graph = builder.build()
```

### Manual Curation

For precise control, manually define entities and relationships:

```python
from knowledge_graph import Entity, Relationship

# Create entities
doc = Entity(type='document', name='Research Paper')
author = Entity(type='person', name='John Doe')

# Create relationship
rel = Relationship(
    source=doc,
    target=author,
    type='authored_by'
)

graph.add(doc, author, rel)
```

## Querying Knowledge Graphs

### Basic Queries

Query the knowledge graph using various methods:

```python
# Find all documents by an author
docs = graph.query(
    entity_type='document',
    relationship='authored_by',
    target='John Doe'
)

# Get neighbors of a concept
neighbors = graph.neighbors('Machine Learning')
```

### Advanced Queries

Use graph traversal for complex queries:

```python
# Find all concepts related to a document's concepts
result = graph.traverse(
    start='document_id',
    path=['contains', 'related_to'],
    max_depth=2
)
```

## Integration with LLM

Knowledge graphs enhance LLM capabilities:

::::{grid} 2

:::{grid-item-card} Retrieval Augmented Generation
Use graph data to provide context to LLMs
:::

:::{grid-item-card} Semantic Search
Navigate the graph using natural language
:::

:::{grid-item-card} Knowledge Completion
Infer missing relationships using LLMs
:::

:::{grid-item-card} Entity Extraction
Automatically extract entities from text
:::

::::

## Export and Import

### Export Formats

Export knowledge graphs in various formats:

```bash
# Export as JSON
python -m knowledge_graph export --format json output.json

# Export as RDF
python -m knowledge_graph export --format rdf output.rdf

# Export as GraphML
python -m knowledge_graph export --format graphml output.graphml
```

### Import Data

Import from external sources:

```bash
# Import from JSON
python -m knowledge_graph import data.json

# Import from CSV
python -m knowledge_graph import --format csv entities.csv
```

## Best Practices

:::{tip}
**Design Principles**
- Keep entity types consistent
- Use clear, descriptive relationship names
- Document custom attributes
- Regular validation and cleanup
:::

:::{warning}
**Performance Considerations**
- Index frequently queried attributes
- Limit graph depth in queries
- Use caching for repeated queries
:::

## See Also

- {doc}`build_pipeline` - How knowledge graphs are built
- {doc}`obsidian_workflow` - Using Obsidian for graph curation
- {doc}`api_reference/index` - API documentation
