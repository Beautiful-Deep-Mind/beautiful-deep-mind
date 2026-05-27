# Glossary

This glossary defines terms used across BDM documentation. Definitions are written to be precise but accessible. Where a term has contested or varied meanings across disciplines, the definition reflects BDM's specific usage.

---

## Attention

In cognitive science, attention is the selective allocation of cognitive resources toward particular stimuli while filtering others out. In machine learning, attention mechanisms compute weighted relevance scores between query elements and memory or input elements, allowing a model to "focus" on the most relevant parts of a sequence. In BDM, attention refers to the process of selecting which stored memories or contextual elements should be surfaced in response to a given input.

---

## BCI (Brain-Computer Interface)

A technology that establishes a direct communication pathway between the brain and an external device, typically reading neural signals (input BCIs), delivering stimulation to the brain (output BCIs), or both (bidirectional BCIs). BDM is not a BCI project. The term appears in the reading list and ethics document for contextual awareness, not as part of BDM's scope.

---

## Cognitive Architecture

A framework that specifies the underlying fixed structures and processes of a cognitive or intelligent system. Examples in cognitive science include ACT-R and SOAR. A cognitive architecture defines what memory types exist, how they interact, how attention operates, and how learning occurs. BDM uses this concept to frame its own layered design — not to replicate any existing cognitive architecture, but to adopt the approach of defining functional layers with clear responsibilities.

---

## Connectome

A comprehensive map of neural connections in a brain or part of a brain. The human connectome is an active area of neuroscience research. BDM does not work with connectomes and does not attempt to simulate or replicate neural connectivity. The term appears here for context and disambiguation.

---

## Consciousness

Consciousness is the subjective experience of being aware — the "what it is like" quality of experience. It is one of the most debated and least understood topics in philosophy, neuroscience, and cognitive science. BDM does not claim to create, simulate, or explain consciousness. The term appears in ethics and glossary documentation to explicitly define what BDM does not pursue.

---

## Continuity

In BDM, continuity refers to the preservation of relevant internal state across sessions, interactions, or time. A system has continuity if information from prior interactions influences current behavior in a structured, retrievable way. Biological memory supports continuity by maintaining representations of past experience. BDM's continuity layer is a software design concern, not a philosophical claim about identity or self.

---

## Episodic Memory

A type of memory that stores records of specific events in context — what happened, when, and under what circumstances. Episodic memory differs from semantic memory (general facts and concepts) by including temporal and contextual metadata. In BDM, episodic memory structures are hypothesized to improve retrieval relevance by allowing the system to distinguish between types of prior interactions.

---

## Internal Context

The accumulated internal state that a system maintains across an interaction or session: what has been said, what has been reasoned about, what commitments have been made, and what uncertainties have been noted. Most current AI systems maintain internal context only within a single context window. BDM treats persistent internal context as a core design requirement.

---

## Learning Loop

A process by which a system updates its internal state based on new information, feedback, or outcomes. In BDM, learning loops do not refer to gradient descent or model training. They refer to structured mechanisms for updating stored beliefs, revising salience scores, flagging contradictions, or recording new episodic events. The learning loop is a design pattern, not a claim about autonomous learning capability.

---

## LLM (Large Language Model)

A neural network model trained on large text corpora that can generate, summarize, classify, and reason about text. Examples include GPT-4, Claude, and Llama. LLMs are BDM's primary research substrate. BDM does not train LLMs; it explores architectures that augment LLMs with memory, reflection, and continuity layers.

---

## Long-Term Memory

Memory that persists over extended periods, potentially indefinitely. In cognitive science, long-term memory encompasses episodic, semantic, and procedural memory. In BDM, long-term memory refers to stored records that persist across sessions and are indexed for retrieval over time.

---

## Memory

The capacity to encode, store, and retrieve information. In BDM, memory is a first-class architectural concern. Memory is not a flat log. It is a structured store with distinct record types, indexing strategies, and retrieval mechanisms. The quality and structure of memory is hypothesized to be a key determinant of system coherence over time.

---

## Neuroplasticity

The brain's ability to reorganize itself by forming new neural connections throughout life. Neuroplasticity underlies learning, memory formation, and recovery from injury. BDM draws conceptual inspiration from the idea that a system's internal state can be modified by experience, but does not model neuroplasticity at a biological level.

---

## Reflection

In BDM, reflection is a structured process by which a system reviews its own prior outputs, checks for consistency, and applies corrections or revisions where needed. Reflection is implemented as a software module, not as philosophical introspection. The hypothesis is that even a simple reflection step can improve consistency across long interactions.

---

## Self-Model

A representation a system maintains of its own state: what it knows, what it does not know, what topics it has engaged with, what its recent outputs have been, and what confidence attaches to its stored beliefs. A self-model is a data structure. It is explicitly not a claim about self-awareness, subjective experience, or consciousness. In BDM, the self-model layer is hypothesized to improve a system's ability to represent uncertainty and acknowledge prior commitments accurately.

---

## Short-Term Memory

Memory that holds a limited amount of information for a brief period, typically seconds to minutes. In cognitive science, working memory is a closely related concept that includes active manipulation of information. In BDM, short-term memory corresponds roughly to the active context window of an LLM during a session.

---

*Terms will be added as the project develops. Definitions reflect BDM usage and may differ from usage in other contexts.*
