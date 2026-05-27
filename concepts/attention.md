# Attention

## Definition

Attention is the mechanism by which a system selects which information is most relevant to the current task and allocates processing resources accordingly. In cognitive science, attention is the selective filtering of stimuli from a larger pool of available input. In machine learning, attention mechanisms compute weighted relevance between a query and a set of candidate elements, producing a focused selection of relevant content.

---

## Why It Matters

Memory without attention is nearly useless. A system might store a large number of records, but if it cannot select the right records at the right time, storage confers no benefit. Attention is the retrieval strategy — the mechanism that bridges what is stored and what is currently needed.

In LLM-based systems, attention operates within the context window over input tokens. BDM's attention layer operates at a different level: over a persistent memory store, selecting which stored records should be surfaced and injected into the current interaction context. This is sometimes described as "retrieval-augmented" attention.

---

## Possible Software Representation

In BDM, the attention layer would function as a query processor over the memory store:

1. Receive the current input or task as a query
2. Compute relevance scores for stored memory records against the query
3. Rank and filter records by relevance, recency, or other configurable criteria
4. Return a bounded set of high-relevance records for injection into the downstream context
5. Log the retrieval decision for auditability

Relevance computation might use:
- **Keyword overlap:** simple term matching between query and record content
- **Embedding similarity:** cosine similarity between query and record embeddings
- **Recency weighting:** more recent records receive a relevance boost
- **Salience scoring:** records marked as high-salience by the learning loop are prioritized

---

## Open Questions

- Should the attention layer use a single retrieval strategy or dynamically select among strategies based on query type?
- How do we evaluate retrieval quality without ground truth labels for what is "most relevant"?
- What is the right upper bound on retrieved context to inject — too much adds noise, too little loses important context?
- Should attention filter retrieved records further (e.g., summarize or compress them) before injection?
- How should conflicting retrieved records be handled — injected together, flagged, or filtered?

---

## Relation to BDM

Attention sits between the memory layer and all higher layers. It is responsible for ensuring that the right stored information reaches the right part of the pipeline at the right time. Without effective attention, memory becomes a liability rather than an asset: large, slow, and noisy.

Designing the attention layer well is likely one of the most impactful engineering decisions in the BDM architecture.
