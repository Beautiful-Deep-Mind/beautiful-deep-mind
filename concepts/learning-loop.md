# Learning Loop

## Definition

A learning loop is a mechanism by which a system updates its internal state based on new information, feedback, or outcomes from interaction. In BDM, learning does not refer to gradient descent or model weight updates. It refers to structured modifications to stored data: updating beliefs, revising salience scores, recording new episodic events, propagating corrections from reflection decisions.

---

## Why It Matters

A system that cannot update its internal state is static. It may perform well within a single session, but it cannot improve based on feedback, adapt to new information, or correct prior errors over time. Learning — even in the limited sense of updating stored records — is the mechanism by which a system becomes more accurate and more useful over repeated interactions.

The learning loop is also the mechanism by which BDM's other layers influence each other: reflection decisions feed into memory updates, user feedback updates salience scores, and new episodic events extend the memory store.

---

## Possible Software Representation

The learning loop in BDM would operate as an event-driven update mechanism:

**Triggers for learning:**
- Explicit user feedback (correction, confirmation, or flag)
- Reflection module output (inconsistency detected, revision generated)
- New episodic event at session end
- Scheduled review pass (e.g., salience decay)

**Update types:**
- **Belief update:** modify or replace a stored semantic record when new contradicting information is confirmed
- **Salience update:** increase or decrease the salience score of a memory record based on retrieval frequency or user feedback
- **Episodic append:** write a new episodic record summarizing a completed interaction
- **Inconsistency resolution:** mark contradicting records, archive the superseded version, and promote the revised version

**Logging:**
Every update should be logged: what changed, what triggered the change, when, and what the prior state was. This is non-negotiable for auditability and rollback capability.

---

## Open Questions

- What counts as "feedback" for triggering a learning update? Only explicit corrections, or also implicit signals?
- How do we prevent the learning loop from introducing systematic drift — where early incorrect beliefs propagate and compound?
- What is the rollback mechanism when a learning update is found to be incorrect?
- How do we detect when the learning loop is degrading rather than improving performance?
- Is there a point at which accumulated updates require a full consistency review pass, rather than incremental updates?

---

## Relation to BDM

The learning loop sits at the center of BDM's architecture as the mechanism that keeps all other layers updated. It consumes output from reflection and from the interface layer, and it writes back to the memory layer and the self-model layer. Without the learning loop, BDM would be a read-only system: capable of retrieving and using stored knowledge but unable to update it based on experience.

The learning loop is what makes the system adaptive rather than merely persistent.
