# Obsidian Workflow

The TS-LLM Knowledge Stack integrates with [Obsidian](https://obsidian.md/) for efficient knowledge management and note-taking.

## Overview

Obsidian is a powerful knowledge base that works on top of a local folder of plain text Markdown files. This workflow leverages Obsidian's features for:

- Note-taking and documentation
- Bi-directional linking
- Graph visualization
- Plugin ecosystem

## Setup

### 1. Install Obsidian

Download and install Obsidian from [obsidian.md](https://obsidian.md).

### 2. Open Vault

Open the repository as an Obsidian vault:

1. Launch Obsidian
2. Click "Open folder as vault"
3. Navigate to your repository directory
4. Select the folder

### 3. Configure Settings

Recommended settings for the TS-LLM workflow:

```yaml
# .obsidian/config.yml
theme: dark
baseFontSize: 16
showLineNumber: true
spellcheck: true
```

## Core Features

### Bi-directional Links

Create connections between notes using `[[wikilinks]]`:

```markdown
This concept is related to [[Knowledge Graphs]] and [[LLM Integration]].

See also: [[Build Pipeline]] for implementation details.
```

### Tags

Organize notes with tags:

```markdown
#concept #machine-learning #typescript

This note discusses TypeScript in ML contexts.
```

### Graph View

Visualize your knowledge network:

::::{grid} 2

:::{grid-item-card} Local Graph
Shows connections to current note
:::

:::{grid-item-card} Global Graph
Shows entire knowledge network
:::

::::

## Recommended Plugins

### Essential Plugins

1. **Dataview** - Query and display note metadata
2. **Templater** - Advanced template functionality
3. **Excalidraw** - Embedded drawings
4. **Calendar** - Daily notes management

### Installation

```bash
# Plugins are installed via Obsidian's Community Plugins
# Settings > Community Plugins > Browse
```

## Note Templates

### Concept Template

```markdown
---
type: concept
tags: [concept]
created: {{date}}
---

# {{title}}

## Definition

Brief definition of the concept.

## Related Concepts

- [[Related Concept 1]]
- [[Related Concept 2]]

## References

1. Source 1
2. Source 2

## Notes

Additional notes and observations.
```

### Document Template

```markdown
---
type: document
author: 
date: {{date}}
tags: [document]
---

# {{title}}

## Summary

Brief summary of the document.

## Key Points

- Point 1
- Point 2
- Point 3

## Connections

Related documents and concepts:
- [[Document 1]]
- [[Concept 1]]
```

## Dataview Queries

Use Dataview to create dynamic lists:

```markdown
## Recent Notes

\`\`\`dataview
LIST
FROM ""
SORT file.mtime DESC
LIMIT 10
\`\`\`

## Notes by Tag

\`\`\`dataview
TABLE file.tags as Tags, file.mtime as Modified
WHERE contains(file.tags, "#concept")
SORT file.mtime DESC
\`\`\`
```

## Daily Notes

### Setup Daily Notes

Configure daily notes in Obsidian settings:

- Format: `YYYY-MM-DD`
- Location: `daily/`
- Template: Use daily note template

### Daily Note Template

```markdown
---
date: {{date}}
type: daily
---

# {{date:YYYY-MM-DD}}

## Tasks

- [ ] Task 1
- [ ] Task 2

## Notes

### Meetings


### Ideas


### Questions


## Links

Created: [[]]
Referenced: [[]]
```

## Integration with Build Pipeline

### Export Notes

Export Obsidian notes to the build pipeline:

```bash
# Export notes to pipeline format
python scripts/export_obsidian.py --vault ./vault --output ./data
```

### Sync Knowledge Graph

Sync Obsidian graph with the knowledge graph:

```bash
# Sync bidirectionally
python scripts/sync_graph.py --source obsidian --target knowledge_graph
```

## Best Practices

:::{tip}
**Naming Conventions**
- Use clear, descriptive note titles
- Avoid special characters in filenames
- Use sentence case for readability
:::

:::{tip}
**Linking Strategy**
- Link liberally but meaningfully
- Create index notes for major topics
- Use tags for classification, links for relationships
:::

:::{tip}
**Maintenance**
- Regular review of orphaned notes
- Update broken links
- Archive outdated notes
:::

## Workflow Examples

### Research Workflow

1. **Capture** - Create daily note with observations
2. **Process** - Create concept notes from daily notes
3. **Connect** - Link related concepts
4. **Review** - Weekly review of new connections
5. **Publish** - Export to documentation

### Project Workflow

1. **Plan** - Create project overview note
2. **Tasks** - Break down into task notes
3. **Progress** - Update daily notes with progress
4. **Document** - Create documentation from notes
5. **Archive** - Move completed projects to archive

## Troubleshooting

### Common Issues

**Sync conflicts**
```bash
# Resolve sync conflicts
git checkout --theirs conflicted_file.md
```

**Broken links**
- Use "Detect broken links" in Obsidian
- Run link checker: `python scripts/check_links.py`

**Performance issues**
- Exclude build directories in `.obsidian/config`
- Limit Dataview queries

## Advanced Features

### Custom CSS

Customize appearance with CSS snippets:

```css
/* .obsidian/snippets/custom.css */
.markdown-preview-view {
    font-family: 'Inter', sans-serif;
}

.tag {
    background-color: #4a5568;
    color: #f7fafc;
    border-radius: 3px;
    padding: 2px 6px;
}
```

### Templater Scripts

Automate with Templater:

```javascript
// Templates/scripts/auto-link.js
module.exports = async (tp) => {
    const note = tp.file.title;
    // Auto-link related notes
    const related = await findRelated(note);
    return related.map(r => `- [[${r}]]`).join('\n');
}
```

## See Also

- {doc}`knowledge_graphs` - Understanding knowledge graph structure
- {doc}`build_pipeline` - How notes feed into the pipeline
- {doc}`repository_structure` - Repository organization
