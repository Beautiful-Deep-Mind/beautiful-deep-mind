# Reading List

This document organizes relevant literature by category. It is a starting structure, not a complete bibliography. Specific titles and authors will be added as the project develops. The goal here is to define which areas of literature are relevant to BDM and why.

---

## Neuroscience

**Why it matters for BDM:**
Neuroscience provides the empirical grounding for the cognitive concepts BDM draws on — memory, attention, learning, and continuity. BDM does not model the brain at a biological level, but understanding what we know about biological memory systems (e.g., the role of the hippocampus in episodic memory) informs which software abstractions are worth exploring and which are oversimplifications.

**Key areas to cover:**
- Memory consolidation and the role of sleep
- Hippocampus and episodic memory formation
- Prefrontal cortex and working memory
- Synaptic plasticity and long-term potentiation
- Attention networks (dorsal and ventral)
- Default mode network and self-referential processing

---

## Cognitive Science

**Why it matters for BDM:**
Cognitive science bridges neuroscience and computation. It provides functional models of cognition — how memory, attention, and reasoning work at a level of abstraction that can inform software design. Classic cognitive architectures (ACT-R, SOAR, CLARION) are directly relevant to BDM's layered design approach.

**Key areas to cover:**
- Working memory models (Baddeley's multi-component model)
- Dual-process theory (fast vs. slow reasoning)
- Cognitive load and resource allocation
- Schema theory and knowledge representation
- Metacognition and self-monitoring
- ACT-R and SOAR architectures

---

## Artificial Intelligence

**Why it matters for BDM:**
AI research — particularly in natural language processing, memory-augmented networks, and agent architectures — provides the technical tools and patterns BDM will use. Understanding the current state of the art in AI is necessary to situate BDM's contribution and avoid reinventing existing solutions.

**Key areas to cover:**
- Transformer architecture and attention mechanisms
- Retrieval-augmented generation (RAG)
- Memory-augmented neural networks (e.g., Neural Turing Machine, Differentiable Neural Computer)
- Long-context language models
- Tool-use and agentic LLM systems
- Prompt engineering and in-context learning

---

## Cognitive Architectures

**Why it matters for BDM:**
Cognitive architecture research has decades of work on how to design structured, modular systems that model aspects of intelligent behavior. This is the most directly relevant area for BDM's architectural design. Understanding prior work prevents BDM from repeating mistakes and helps identify what is genuinely novel.

**Key areas to cover:**
- ACT-R (Anderson et al.) — procedural and declarative memory
- SOAR (Laird et al.) — problem solving and learning
- CLARION (Sun) — implicit and explicit processing
- Global Workspace Theory (Baars) — attention and conscious access
- Predictive processing frameworks (Clark, Friston)
- Comparison of cognitive architecture approaches

---

## Consciousness Studies

**Why it matters for BDM:**
BDM explicitly does not pursue consciousness. But to avoid making accidental claims about consciousness, or to avoid building systems that are deceptively anthropomorphic, the team needs a clear understanding of what consciousness is proposed to be, what theories exist, and why they are contested. Avoiding a claim requires understanding it.

**Key areas to cover:**
- Global Workspace Theory (Baars, Dehaene)
- Integrated Information Theory (Tononi)
- Higher-order theories of consciousness
- The "hard problem" of consciousness (Chalmers)
- Philosophical zombie thought experiments and their implications
- Criticisms of AI consciousness claims

---

## Brain-Computer Interfaces

**Why it matters for BDM:**
BCI research addresses the interface between biological neural systems and external computational systems. BDM is not a BCI project, but BCI literature raises relevant questions about data representation, signal interpretation, and the ethics of systems that interact closely with cognitive processes.

**Key areas to cover:**
- Non-invasive BCI (EEG-based systems)
- Invasive BCI (electrode arrays, neural implants)
- Motor prosthetics and communication BCIs
- Current limitations in signal decoding
- Privacy and consent in neural data
- Long-term safety of implanted devices

---

## Memory and Learning

**Why it matters for BDM:**
This is the most directly relevant domain for BDM's core technical focus. Understanding how memory works, how it degrades, how learning updates it, and how retrieval operates is essential for designing BDM's memory and learning loop layers.

**Key areas to cover:**
- Spaced repetition and memory consolidation
- Forgetting curves (Ebbinghaus)
- Reconstructive memory and memory errors
- Transfer learning and its limits
- Continual learning in neural networks (catastrophic forgetting)
- Knowledge graphs and semantic memory representation
- Vector databases and embedding-based retrieval

---

## Ethics of Neurotechnology

**Why it matters for BDM:**
Neurotechnology ethics addresses questions of consent, privacy, autonomy, and identity that arise when software interacts closely with cognitive processes or cognitive data. Even though BDM does not currently work with neural data, the ethical frameworks developed in this field are relevant to BDM's responsible research commitments.

**Key areas to cover:**
- Neurorights and proposed legal frameworks
- Mental privacy and cognitive liberty
- Informed consent in cognitive research
- The ethics of memory manipulation or augmentation
- Power asymmetries in neurotechnology
- Dual-use risks in cognitive enhancement research

---

## Philosophy of Mind

**Why it matters for BDM:**
Philosophy of mind provides the conceptual tools for thinking carefully about consciousness, intentionality, self-reference, and identity — concepts that BDM's work touches but cannot resolve. Reading philosophy of mind helps the project maintain conceptual precision and avoid making claims that are philosophically incoherent.

**Key areas to cover:**
- Functionalism and the multiple realizability argument
- Physicalism and its variants
- The intentionality of mental states (Brentano, Searle)
- The Chinese Room argument (Searle) and its responses
- Personal identity and continuity (Locke, Parfit)
- Extended mind thesis (Clark, Chalmers)
- Philosophy of artificial intelligence

---

*Specific book and paper recommendations will be added as the project progresses. Contributors are welcome to suggest readings in any category via issues.*
