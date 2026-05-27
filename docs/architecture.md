# Conceptual Architecture

This document describes a conceptual architecture for the BDM system. This is not an implementation. No code exists for this architecture yet. The purpose of this document is to define the functional layers that BDM intends to build, clarify their responsibilities and interfaces, and identify open design questions for each layer.

All descriptions here represent design intentions and hypotheses, not implemented behavior.

---

## Overview

BDM's architecture is organized as a set of composable functional layers. Each layer has a distinct purpose and communicates with adjacent layers through defined interfaces. The layered design is intended to keep concerns separated, to allow individual layers to be developed and tested independently, and to make the overall system auditable and modifiable.

```
┌─────────────────────────────────┐
│         Interface Layer         │  ← user/LLM input and output
├─────────────────────────────────┤
│       Context Continuity        │  ← session persistence
├─────────────────────────────────┤
│         Self-Model Layer        │  ← internal state representation
├─────────────────────────────────┤
│          Learning Loop          │  ← belief update, feedback processing
├─────────────────────────────────┤
│         Reflection Layer        │  ← consistency checking, review
├─────────────────────────────────┤
│          Attention Layer        │  ← memory retrieval, context selection
├─────────────────────────────────┤
│           Memory Layer          │  ← storage, indexing, retrieval
└─────────────────────────────────┘
```

---

## Memory Layer

**Purpose:** Store and retrieve structured records of experience, knowledge, and interaction history.

**Possible Responsibilities:**
- Maintain distinct record types: episodic records (timestamped interaction events), semantic records (general facts and concepts), and working memory (active session context)
- Provide a query interface for retrieval by recency, topic, relevance score, or record type
- Manage record expiration, salience decay, and storage limits
- Support update and revision of stored records when new information contradicts prior entries
- Provide an audit log of memory operations

**Open Questions:**
- What schema best captures episodic records without excessive overhead?
- How should salience and relevance be scored — rule-based, embedding-based, or hybrid?
- What is the right retention policy: time-based decay, explicit deletion, or confidence-weighted pruning?
- How should contradictions between stored records be handled — flagged, merged, or replaced?
- At what scale does a flat indexed store become insufficient, requiring vector search or graph structures?

---

## Attention Layer

**Purpose:** Select which stored memories and contextual elements are most relevant to the current input, and surface them for downstream processing.

**Possible Responsibilities:**
- Receive a query (current input, task, or question) and return a ranked set of relevant memory records
- Apply retrieval strategies: recency-weighted, semantic similarity-based, or topic-filtered
- Limit the retrieved context to what can fit within a downstream system's context window
- Maintain a retrieval log for auditability

**Open Questions:**
- Should attention be purely retrieval-based, or should it also filter or summarize retrieved records?
- How should retrieval strategy be selected — fixed, configurable, or adaptive?
- How do we evaluate retrieval quality without ground truth relevance labels?
- What happens when retrieved context is contradictory? Does the attention layer filter, flag, or pass contradictions downstream?

---

## Reflection Layer

**Purpose:** Review prior outputs for consistency, flag divergences, and optionally apply corrections before a final output is produced.

**Possible Responsibilities:**
- Compare a new output candidate against stored prior outputs on the same topic
- Detect explicit contradictions (factual inconsistencies) and implicit inconsistencies (changed stance without justification)
- Produce a reflection report: consistent, inconsistent, or uncertain
- Optionally revise the output to resolve detected inconsistencies
- Log all reflection events for audit

**Open Questions:**
- Should reflection be a blocking step (output is held until review completes) or asynchronous?
- How do we distinguish legitimate updates to prior positions from inconsistencies?
- Can reflection be implemented without an LLM (rule-based), and at what cost in quality?
- At what frequency should reflection run — every output, periodically, or on-demand?
- What is the risk of over-correction: reflection that changes outputs too aggressively?

---

## Learning Loop

**Purpose:** Update stored internal state based on new information, feedback, or outcomes from interaction.

**Possible Responsibilities:**
- Process explicit feedback signals (user corrections, flagged errors) and update relevant memory records
- Adjust salience scores for memory records based on how often they are retrieved or confirmed
- Record new episodic events generated during interaction
- Propagate updates from reflection decisions back into the memory layer
- Maintain a change log of all updates applied

**Open Questions:**
- What counts as feedback? Only explicit corrections, or also implicit signals like follow-up questions?
- How should conflicting updates be resolved — most recent wins, confidence-weighted, or manual?
- How do we prevent the learning loop from introducing systematic drift over time?
- Is there a risk of reinforcing errors if early incorrect beliefs are confirmed by subsequent interactions?

---

## Self-Model Layer

**Purpose:** Maintain a structured representation of the system's own state: what it knows, what it does not know, what topics it has engaged with, and what confidence levels attach to its stored beliefs.

**Possible Responsibilities:**
- Maintain a topic inventory: subjects the system has stored information about
- Track confidence levels for stored beliefs, updated by the learning loop
- Record acknowledged limitations and known gaps
- Provide a summary of self-model state for downstream use (e.g., the LLM can reference it when formulating responses)
- Support introspective queries: "what do I know about X?", "how confident am I about Y?"

**Open Questions:**
- What is the minimal schema for a useful self-model? What must it include, and what is overhead?
- How do confidence levels get assigned and updated in a principled way?
- Is the self-model exposed to the LLM directly (injected into context), or does it operate as a pre-processing filter?
- How do we avoid the self-model becoming inaccurate through drift — representing beliefs the system no longer holds?

**Important Note:** A self-model is a data structure. It does not constitute self-awareness. It does not imply consciousness. It is a record of internal state, not a subjective experience of that state.

---

## Context Continuity Layer

**Purpose:** Preserve relevant internal state across sessions so that a new session begins with access to prior context rather than from a blank state.

**Possible Responsibilities:**
- Serialize and store session state at the end of each interaction
- Restore relevant prior state at the start of a new session, filtered by recency and relevance
- Apply a "cold start" protocol: summarize prior context into a compact representation for injection into a new session
- Manage session boundaries and transitions cleanly
- Support rollback: restoring state to a prior checkpoint if corruption or error is detected

**Open Questions:**
- How much prior context should be restored? Full history vs. a relevance-filtered summary?
- What defines a session boundary? Time-based, topic-based, or explicit user action?
- How do we handle continuity after long gaps (days, weeks) where much prior context may be stale?
- Privacy implications: stored session state may contain sensitive content — how is it protected?

---

## Interface Layer

**Purpose:** Connect all internal layers to external inputs (user messages, API calls) and outputs (generated responses), and to the LLM where applicable.

**Possible Responsibilities:**
- Receive incoming input and route it through the processing pipeline
- Inject retrieved memory context and self-model state into LLM prompts
- Receive LLM outputs and pass them to the reflection layer
- Return final outputs to the user or calling system
- Expose a configuration interface for enabling or disabling layers
- Provide logging and observability hooks for debugging and evaluation

**Open Questions:**
- Should the interface layer be LLM-agnostic (able to swap the underlying model) from the start?
- How should prompt injection of retrieved context be structured — system prompt, user message, or a dedicated format?
- How do we prevent the interface layer from becoming a bottleneck or single point of failure?
- What logging is needed for reproducibility of experiments?

---

*This architecture is conceptual. All layer descriptions represent design intentions. No implementation exists at this stage.*
