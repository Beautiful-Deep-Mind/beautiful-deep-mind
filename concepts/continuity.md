# Continuity

## Definition

Continuity, in BDM's context, refers to the preservation of relevant internal state across sessions, interactions, or time. A system has continuity if information from prior interactions can influence current behavior in a structured, retrievable, and auditable way.

Continuity does not mean perfect memory of everything. It means that relevant prior state is accessible, not lost, when a new session begins.

---

## Why It Matters

Without continuity, each session is a fresh start. The system cannot reference prior commitments, build on prior exchanges, correct errors from past interactions, or accumulate knowledge over time. This is a fundamental limitation for any system intended to be useful across multiple sessions or over extended periods.

Continuity is also the property that most closely connects BDM's design to the cognitive question that originally motivated the project: how does a mind maintain a coherent sense of context and identity over time? In biological systems, this is supported by memory consolidation, long-term potentiation, and the persistence of episodic records. In BDM, continuity is a software design decision.

Importantly, continuity is not the same as immutability. A system with good continuity can update, revise, and forget — but it does so in a structured, principled way rather than by losing state arbitrarily.

---

## Possible Software Representation

BDM's context continuity layer would be responsible for:

1. **Session serialization:** At the end of each session, serialize the active state of the memory store, self-model, and interaction summary to durable storage
2. **Session restoration:** At the start of a new session, load the persisted state and inject a compressed summary of prior context into the current session
3. **Cold start protocol:** When starting after a long gap, produce a "resumption brief" — a compact summary of the most relevant prior state — rather than attempting to inject full history
4. **Staleness management:** Mark records as stale after configurable time thresholds, so that old information is not presented as current
5. **Rollback support:** Maintain checkpoints so that corrupted or degraded state can be restored to a prior known-good point

The continuity layer is a persistence and restoration layer. It does not generate new knowledge — it ensures that existing knowledge survives session boundaries.

---

## Open Questions

- How much prior context should be restored at session start? Full history is impractical; too little defeats the purpose
- How should the system handle long gaps (days, weeks) between sessions where much prior context may be stale or irrelevant?
- What defines a session boundary? Time-based, topic-based, explicit user action, or a combination?
- How should the continuity layer interact with the privacy requirement that users can inspect and delete stored state?
- What happens when the memory store grows very large over many sessions — how should it be compressed or pruned without losing critical context?

---

## Relation to BDM

Continuity is the layer that makes BDM's memory, self-model, and learning loop useful across time rather than just within a single session. Without continuity, all other layers reset at session end. With continuity, the system accumulates experience, maintains consistency over time, and exhibits adaptive behavior that a stateless system cannot.

Continuity is also where privacy and safety concerns are most acute: what is stored, how it is protected, and how it can be deleted are design questions that must be resolved in parallel with the technical implementation.
