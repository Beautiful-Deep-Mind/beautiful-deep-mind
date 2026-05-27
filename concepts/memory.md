# Memory

## Definition

Memory is the capacity to encode, store, and retrieve information. In cognitive science, memory is not a single system but a collection of functionally distinct processes and structures with different characteristics: duration, capacity, encoding mechanisms, and retrieval modes.

---

## Why It Matters

Memory is the foundation of continuity. Without the ability to retain information from prior experience, a system cannot adapt, maintain consistency, or build on prior knowledge. In biological systems, memory enables identity, learning, and goal-directed behavior across time. In software systems, memory is typically either absent (stateless computation) or undifferentiated (flat logs or simple key-value stores).

BDM's core hypothesis is that the structure of memory matters, not just its presence. Distinguishing episodic records from semantic facts, indexing by relevance and recency, and managing retention policies are hypothesized to produce qualitatively better retrieval behavior than flat storage.

---

## Possible Software Representation

A BDM memory store would likely include:

- **Episodic records:** Structured entries capturing specific interaction events, with fields for timestamp, topic tags, salience score, and a summary of what occurred
- **Semantic records:** General facts and concepts, stored with source attribution, confidence level, and a last-verified timestamp
- **Working memory buffer:** A short-lived, high-priority context window containing the most recent interaction state, flushed to episodic records at session end

Retrieval would support multiple query modes:
- Recency-weighted: return the most recent records
- Relevance-weighted: return records most similar to the current query, using embedding-based or keyword-based similarity
- Type-filtered: return only episodic, only semantic, or only working memory records

---

## Open Questions

- What is the minimal schema for an episodic record that is both informative and computationally tractable?
- How should salience scores be assigned and updated over time?
- What retention policy prevents unbounded growth without losing important records?
- How should contradictions between stored records be resolved?
- Is embedding-based retrieval necessary from the start, or can simpler keyword indexing suffice for initial prototypes?

---

## Relation to BDM

Memory is the first layer in BDM's architecture and the prerequisite for all other layers. Attention retrieves from memory. Reflection compares against memory. The learning loop updates memory. The self-model summarizes memory state. Context continuity persists memory across sessions.

Everything in BDM depends on the quality of the memory layer. It is the highest-priority component for Phase 1 development.
