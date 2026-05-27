# Roadmap

This roadmap describes the intended phases of BDM development. It is not a commitment schedule. Timelines are not fixed. Each phase depends on the findings of the previous one. The goal is to make progress in a disciplined sequence, from documentation to prototyping to experimentation.

---

## Phase 0 — Documentation and Conceptual Foundation

**Status: In progress**

### Goal
Establish a clear, well-documented conceptual foundation before writing any application code. Define what BDM is, what it is not, and what it intends to explore. Create a research vocabulary, an ethical framework, and an initial architecture.

### Expected Outputs
- Complete repository documentation (README, manifesto, theory, glossary, ethics)
- Conceptual architecture definition
- Initial research hypotheses
- Experiment designs (pre-implementation)
- Reading list organized by relevant domain

### Limitations
- No working software yet
- All architectural descriptions are conceptual
- No empirical validation of any hypothesis
- Direction may change significantly as the conceptual work matures

---

## Phase 1 — Memory Model Prototype

### Goal
Implement a minimal persistent memory system that can store, retrieve, and index structured episodic records. Evaluate whether structured memory improves retrieval relevance compared to flat log storage.

### Expected Outputs
- A working memory store with episodic and semantic record types
- A retrieval interface (query by recency, relevance, or topic)
- Basic evaluation metrics for retrieval quality
- A documented set of findings and limitations

### Limitations
- Memory will be small-scale (no large-scale vector database required initially)
- Retrieval quality metrics will be preliminary
- No reflection or self-model integration in this phase
- Implementation language TBD (likely Python)

---

## Phase 2 — Reflection and Learning Loop

### Goal
Design and implement a reflection module that reviews prior outputs for consistency. Implement a lightweight learning loop that updates stored beliefs or salience scores based on new information or corrections.

### Expected Outputs
- A reflection module that can compare new outputs to stored prior outputs
- A basic consistency-checking mechanism
- A belief update mechanism that modifies stored records
- Evaluation of whether reflection reduces detectable inconsistencies

### Limitations
- Reflection will be rule-based or LLM-assisted, not autonomous
- "Learning" in this phase means updating stored data, not retraining models
- Consistency metrics will be manually defined and limited in scope
- Risk of over-correction: reflection that modifies too aggressively may reduce coherence

---

## Phase 3 — Self-Model and Continuity Model

### Goal
Implement a lightweight self-model: a structured record of the system's known topics, confidence levels, recent interaction history, and acknowledged limitations. Implement a continuity layer that preserves this self-model across sessions.

### Expected Outputs
- A self-model schema and storage mechanism
- A continuity layer that serializes and restores internal state across sessions
- Evaluation of whether access to a self-model improves uncertainty representation
- Documentation of what the self-model does and does not represent

### Limitations
- Self-model is a data structure, not self-awareness
- Continuity depends on the memory model from Phase 1 being stable
- Cross-session continuity introduces privacy considerations (see docs/ethics.md)
- The self-model may be too coarse to capture meaningful state distinctions

---

## Phase 4 — Integration with LLMs

### Goal
Integrate the memory model, reflection module, and self-model with a large language model as a research substrate. Evaluate whether augmenting an LLM with these layers produces measurably more coherent and consistent behavior over extended interactions.

### Expected Outputs
- An end-to-end pipeline: input → memory retrieval → LLM → reflection → memory update
- Evaluation of coherence and consistency metrics across multi-session interactions
- Comparison against a baseline LLM without augmentation
- Open publication of architecture, prompts, and evaluation results

### Limitations
- LLM API costs and rate limits will constrain experiment scale
- Evaluation of coherence is partly subjective; automated metrics are imperfect
- Results will be specific to the LLM used; generalizability is uncertain
- Integration complexity may introduce bugs that are difficult to isolate

---

## Phase 5 — Experiments, Evaluation, and Open-Source Collaboration

### Goal
Run a structured set of experiments drawn from research/experiments.md. Publish results. Open the project to external contributors. Evaluate the project's hypotheses against empirical findings and revise or retire hypotheses as needed.

### Expected Outputs
- Published experiment results (including negative results)
- Open-source release of prototype code with documentation
- Revised hypothesis document based on findings
- Contributor guidelines and open issues for community engagement
- A clear statement of what has been learned and what remains open

### Limitations
- Results may not generalize beyond the specific systems tested
- Community contributions introduce coordination overhead
- Some original hypotheses may be falsified — this is expected and desirable
- The project may pivot based on what is learned in Phases 1–4

---

*This roadmap is a working document. It will be updated as the project progresses.*
