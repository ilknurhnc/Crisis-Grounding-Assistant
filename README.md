# InnerAnchor

InnerAnchor is a context-aware AI grounding assistant designed to help users navigate moments of emotional overwhelm through personalized calming guidance, reflective check-ins, memory-based support, and grounding recommendations.

The project focuses on building a safe and supportive AI system that assists users during stressful or emotionally difficult moments without positioning itself as a therapy or diagnostic tool.

---

# Project Vision

InnerAnchor aims to provide users with:

- Personalized grounding support
- Emotional check-ins
- Context-aware calming guidance
- Memory-based emotional support
- Reflective journaling assistance
- Calming recommendations during difficult moments

The system is designed to remember what has previously helped the user and use that context to generate more personalized support over time.

---

# Core Concept

The user creates a personal emotional support profile containing:

- Calming colors
- Helpful coping mechanisms
- Safe grounding phrases
- Trusted contacts
- Emotional triggers
- Preferred calming activities

During moments of overwhelm, the user can interact with the system through short emotional check-ins such as:

```text
"I feel overwhelmed right now."
"I think I'm starting to panic."
"I feel emotionally exhausted."
```

The AI then generates personalized grounding guidance using:

- User profile data
- Previous emotional check-ins
- Similar past situations
- Context-aware memory retrieval
- Generative AI responses

---

# Project Goals

## Technical Goals

- Learn Generative AI systems
- Build a Retrieval-Augmented Generation (RAG) pipeline
- Implement vector embeddings
- Use semantic memory retrieval
- Work with vector databases
- Build multi-service architecture with Docker Compose
- Design context-aware AI workflows
- Learn AI orchestration patterns

## Product Goals

- Create a meaningful AI-native product
- Focus on real-world emotional support use cases
- Build a calming and thoughtful user experience
- Create personalized AI interactions
- Develop a safe and ethically scoped support system

---

# Important Scope Definition

InnerAnchor is NOT:

- A therapist
- A medical system
- A diagnostic tool
- A crisis intervention replacement
- A mental health authority

InnerAnchor IS:

- A grounding assistant
- A reflective journaling companion
- A personalized calming support system
- A context-aware emotional support tool

The application should encourage users to seek professional support during severe crises or emergencies.

---

# MVP Scope

The first version of the application will include:

## 1. Personal Support Profile

Users can store information such as:

- Calming colors
- Helpful activities
- Grounding techniques
- Safe phrases
- Emotional triggers
- Trusted contacts

Example:

```json
{
  "calming_colors": ["lavender", "soft blue"],
  "helpful_activities": [
    "walking",
    "deep breathing",
    "cold water"
  ],
  "safe_phrases": [
    "This feeling is temporary.",
    "You are safe right now."
  ]
}
```

---

## 2. Emotional Check-ins

Users can describe their current emotional state.

Example:

```text
"I feel extremely anxious right now."
```

---

## 3. Personalized Grounding Responses

The AI generates calming and supportive responses based on:

- Current emotional input
- Stored profile data
- Previous interactions
- Context retrieval

---

## 4. Calming UI Elements

The frontend may include:

- Breathing animations
- Soft color palettes
- Grounding cards
- Visual calming panels
- Guided breathing instructions

---

## 5. Memory-Based Support

The system will eventually remember:

- Previous emotional states
- What previously helped the user
- Recurring stress patterns
- Effective grounding techniques

Example:

```text
"Last time you felt this way, slow breathing and walking helped you calm down."
```

---

# Planned System Architecture

```text
Frontend UI
    ↓
FastAPI Backend
    ↓
Memory & Retrieval Layer
    ↓
Vector Database
    ↓
LLM Provider
```

---

# Planned Services

The project will use a multi-service architecture with Docker Compose.

## Services

- frontend
- backend
- chromadb
- postgres
- llm provider

---

# Planned Technical Stack

## Backend

- Python
- FastAPI

## AI / NLP

- OpenAI API or Gemini API
- Sentence Transformers
- Embeddings
- Retrieval-Augmented Generation (RAG)

## Databases

- ChromaDB
- PostgreSQL

## Frontend

- HTML
- CSS
- JavaScript

## Infrastructure

- Docker
- Docker Compose

---

# Learning Goals

This project is designed as a progression from a traditional NLP classification project toward modern AI systems engineering.

Key learning areas include:

- Generative AI
- RAG systems
- Embeddings
- Semantic search
- Memory systems
- AI orchestration
- Multi-service backend architecture
- Personalized AI workflows
- AI product design
- Ethical AI scoping

---

# Planned Development Phases

## Phase 1 — Core Grounding Assistant

- Basic frontend
- FastAPI backend
- Emotional check-ins
- Personalized grounding responses
- Docker Compose setup

---

## Phase 2 — Memory System

- Journal storage
- Previous check-in history
- Emotional memory retrieval

---

## Phase 3 — RAG Integration

- Embeddings
- ChromaDB
- Semantic similarity search
- Context-aware memory retrieval

---

## Phase 4 — Advanced Grounding UI

- Breathing animations
- Dynamic calming themes
- Interactive grounding visuals

---

## Phase 5 — Personalized Recommendations

- Calming music recommendations
- Video suggestions
- Journaling prompts
- Personalized coping suggestions

---

# Example User Flow

```text
User emotional check-in
        ↓
Profile context retrieval
        ↓
Memory similarity search
        ↓
LLM grounding prompt generation
        ↓
Personalized calming response
        ↓
Frontend grounding UI
```

---

# Future Ideas

Potential future improvements:

- Emotion trend tracking
- Weekly emotional summaries
- Voice-based grounding support
- AI-generated calming visuals
- Emotion-aware recommendation systems
- Multi-session memory
- Reflection insights
- Local LLM support with Ollama

---

# Repository Status

Project planning and architecture phase.
Initial MVP scope and system design are currently being defined.


inneranchor/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── schemas.py
│   │   ├── routes/
│   │   │   ├── profile.py
│   │   │   ├── checkin.py
│   │   │   └── grounding.py
│   │   ├── services/
│   │   │   ├── profile_service.py
│   │   │   ├── memory_service.py
│   │   │   ├── grounding_service.py
│   │   │   ├── recommendation_service.py
│   │   │   └── llm.py
│   │   └── prompts/
│   │       └── grounding_prompt.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── Dockerfile
│
├── data/
│   ├── profiles/
│   ├── journals/
│   ├── chroma/
│   ├── sample_profile.json
│   └── recommendations.json
│
├── docker-compose.yml
├── README.md
└── .gitignore