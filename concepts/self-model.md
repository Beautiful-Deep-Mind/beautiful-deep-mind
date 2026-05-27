# Self-Model

## Definition

A self-model, as used in BDM, is a structured data representation of a system's own internal state: what topics it has stored knowledge about, what confidence levels attach to stored beliefs, what limitations have been recorded, and what the recent interaction history looks like from the system's perspective.

A self-model is a data structure. It is not self-awareness. It is not consciousness. It is not a subjective sense of existing. It is a record — maintained and queryable — of the system's own knowledge state.

---

## Why It Matters

Systems that lack any representation of their own state cannot reason accurately about what they know and do not know. LLMs, in particular, are known to express confident-sounding outputs even in domains where their knowledge is absent or weak. A self-model that tracks known knowledge gaps, confidence levels, and acknowledged limitations could constrain outputs in uncertain domains, leading to more appropriately hedged and accurate responses.

Beyond uncertainty representation, a self-model enables a form of consistency: the system can consult its self-model before committing to a claim and identify whether that claim conflicts with recorded prior positions.

---

## Possible Software Representation

A minimal self-model in BDM might include:

- **Topic inventory:** A list of topics the system has stored records about, with rough coverage indicators (e.g., high, medium, low, none)
- **Confidence registry:** For key stored beliefs, a confidence score reflecting how well-supported the belief is by stored evidence
- **Limitation log:** A record of explicitly acknowledged gaps, corrections received, and areas where the system has produced inconsistent outputs in the past
- **Interaction summary:** A compact summary of recent interaction patterns — what topics have been discussed, what corrections have been received, what open questions remain

The self-model would be injected into the LLM's context as a structured summary, providing the model with access to a representation of its own state without requiring it to infer that state from scratch each time.

---

## Open Questions

- What is the minimal schema that makes a self-model useful without making it too large to inject into context?
- How should confidence scores be assigned and updated? Rule-based, LLM-assisted, or both?
- How do we prevent self-model drift — where the self-model becomes inaccurate over time because updates are missed or incorrect?
- Is the self-model exposed to the LLM directly (injected into the prompt), used as a filter before prompting, or both?
- What is the risk of the LLM over-relying on the self-model and refusing to engage with topics not represented in it?

---

## Relation to BDM

The self-model layer depends on the memory layer (it is derived from stored records), the learning loop (it is updated by learning events), and reflection (reflection events feed into the limitation log). It feeds into the interface layer by providing structured context about the system's current state for injection into LLM prompts.

The self-model is one of BDM's more novel components — it has analogs in cognitive science (metacognition, self-monitoring) but less clear precedent in current AI system design as a first-class architectural layer.

**Reminder:** possession of a self-model does not make a system self-aware. The self-model is a record of state, not an experience of it.
