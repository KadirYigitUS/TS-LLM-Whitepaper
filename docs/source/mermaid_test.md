# Mermaid Diagram Test Page

This page demonstrates Mermaid diagram capabilities in the documentation.

## Flow Charts

### Simple Flow Chart

```{mermaid}
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]
    C --> E[End]
    D --> E
```

### Build Pipeline Flow

```{mermaid}
graph LR
    A[Source Files] --> B[Preprocessing]
    B --> C[Knowledge Graph]
    C --> D[LLM Integration]
    D --> E[Documentation]
    E --> F[Deploy to ReadTheDocs]
```

## Sequence Diagrams

### API Request Flow

```{mermaid}
sequenceDiagram
    participant User
    participant API
    participant Database
    participant LLM
    
    User->>API: Request data
    API->>Database: Query
    Database-->>API: Return results
    API->>LLM: Process with LLM
    LLM-->>API: Enhanced results
    API-->>User: Response
```

## Class Diagrams

### Knowledge Graph Structure

```{mermaid}
classDiagram
    class Entity {
        +String id
        +String type
        +String name
        +Dict attributes
        +get_neighbors()
        +add_relationship()
    }
    
    class Relationship {
        +String id
        +String type
        +Entity source
        +Entity target
        +Dict properties
    }
    
    class Graph {
        +List entities
        +List relationships
        +add_entity()
        +add_relationship()
        +query()
        +traverse()
    }
    
    Entity "1" --> "*" Relationship: has
    Graph "1" --> "*" Entity: contains
    Graph "1" --> "*" Relationship: contains
```

## State Diagrams

### Document Processing States

```{mermaid}
stateDiagram-v2
    [*] --> New
    New --> Processing: Start Processing
    Processing --> Parsed: Parse Complete
    Parsed --> Validated: Validate
    Validated --> Indexed: Index
    Indexed --> Published: Publish
    Published --> [*]
    
    Processing --> Error: Parse Error
    Validated --> Error: Validation Error
    Error --> New: Retry
```

## Entity Relationship Diagrams

### Documentation Database

```{mermaid}
erDiagram
    DOCUMENT ||--o{ SECTION : contains
    DOCUMENT ||--o{ AUTHOR : "written by"
    DOCUMENT ||--o{ TAG : "tagged with"
    SECTION ||--o{ PARAGRAPH : contains
    SECTION ||--o{ CODE_BLOCK : contains
    DOCUMENT {
        string id
        string title
        date created
        date modified
    }
    SECTION {
        string id
        string title
        int order
    }
    AUTHOR {
        string name
        string email
    }
```

## Gantt Charts

### Project Timeline

```{mermaid}
gantt
    title TS-LLM Development Timeline
    dateFormat YYYY-MM-DD
    section Planning
    Requirements Gathering    :done, 2024-01-01, 2024-01-15
    Architecture Design        :done, 2024-01-16, 2024-01-31
    section Development
    Core Framework            :done, 2024-02-01, 2024-03-15
    Knowledge Graph           :active, 2024-03-01, 2024-04-15
    LLM Integration           :2024-04-01, 2024-05-15
    section Documentation
    API Documentation         :2024-04-15, 2024-05-30
    User Guide               :2024-05-01, 2024-06-15
```

## Pie Charts

### Module Distribution

```{mermaid}
pie title Module Code Distribution
    "Core Framework" : 35
    "Knowledge Graph" : 25
    "LLM Integration" : 20
    "Documentation" : 10
    "Tests" : 10
```

## Git Graph

### Branch Strategy

```{mermaid}
gitGraph
    commit id: "Initial"
    branch develop
    checkout develop
    commit id: "Setup docs"
    branch feature/knowledge-graph
    checkout feature/knowledge-graph
    commit id: "Add entities"
    commit id: "Add relationships"
    checkout develop
    merge feature/knowledge-graph
    checkout main
    merge develop tag: "v0.1.0"
    checkout develop
    commit id: "Continue development"
```

## C4 Context Diagram

### System Context

```{mermaid}
C4Context
    title System Context Diagram for TS-LLM Knowledge Stack
    
    Person(user, "User", "Documentation author/reader")
    System(tslm, "TS-LLM System", "Knowledge management and documentation")
    System_Ext(obsidian, "Obsidian", "Note-taking application")
    System_Ext(llm, "LLM API", "Language model service")
    System_Ext(rtd, "ReadTheDocs", "Documentation hosting")
    
    Rel(user, tslm, "Manages knowledge", "Web/CLI")
    Rel(user, obsidian, "Creates notes", "Desktop app")
    Rel(tslm, llm, "Processes text", "API")
    Rel(tslm, obsidian, "Syncs data", "File system")
    Rel(tslm, rtd, "Publishes docs", "Git push")
```

## Testing Mermaid Features

### Advanced Styling

```{mermaid}
graph TB
    A[Input] -->|Data| B(Process)
    B -->|Success| C[Output]
    B -->|Error| D[Log Error]
    
    style A fill:#9f6,stroke:#333,stroke-width:2px
    style B fill:#69f,stroke:#333,stroke-width:2px
    style C fill:#6f9,stroke:#333,stroke-width:2px
    style D fill:#f66,stroke:#333,stroke-width:2px
```

### Subgraphs

```{mermaid}
graph TB
    subgraph "Data Layer"
        A[Raw Data]
        B[Processed Data]
    end
    
    subgraph "Logic Layer"
        C[Business Logic]
        D[Validation]
    end
    
    subgraph "Presentation Layer"
        E[API]
        F[UI]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    D --> F
```

## Interactive Features

:::{note}
If Mermaid diagrams are not rendering:
1. Check that the Mermaid CDN is loaded in `conf.py`
2. Ensure JavaScript is enabled in your browser
3. See {doc}`troubleshooting` for more help
:::

:::{tip}
**Mermaid Tips**
- Use the [Mermaid Live Editor](https://mermaid.live) to test diagrams
- Keep diagrams simple and focused
- Use meaningful node labels
- Consider color coding for different types of nodes
:::

## See Also

- {doc}`build_pipeline` - Pipeline documentation with diagrams
- {doc}`knowledge_graphs` - Knowledge graph visualization
- [Mermaid Documentation](https://mermaid.js.org/) - Official Mermaid docs
