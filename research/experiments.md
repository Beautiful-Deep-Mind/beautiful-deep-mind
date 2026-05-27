# Experiment Designs

This document contains initial experiment designs for BDM research. Each experiment is linked to one or more hypotheses from `hypotheses.md`. These are pre-implementation designs — no experiments have been run yet.

All experiments are in a planning phase. Designs will be updated as the project moves from conceptual phase to prototype.

---

## E1 — Simple Memory Persistence

**Related Hypothesis:** H1 (Persistent memory improves interaction continuity)

**Goal:**
Establish whether a memory-augmented system recalls prior interaction content more accurately than a baseline, and whether this recall produces measurably more coherent responses.

**Method:**
1. Design a set of multi-turn, multi-session interaction scripts. Each script includes facts, preferences, or commitments established in early sessions that are relevant to later sessions.
2. Run each script against two systems: a baseline LLM with no persistent memory, and a memory-augmented variant with an episodic memory store.
3. In each late session, ask questions that require reference to content from early sessions.
4. Evaluate responses for: correct reference to prior content, absence of contradictions, and reduction in user re-explanation burden.

**Expected Observation:**
The memory-augmented system will correctly reference prior session content in a meaningful percentage of cases where the baseline does not. The memory-augmented system will produce fewer contradictions of prior commitments.

**Possible Failure Modes:**
- Retrieval quality is too low: the memory store contains the relevant record, but retrieval does not surface it
- Retrieval quality is too high in the wrong direction: irrelevant prior context is retrieved and inserted, confusing the system
- The evaluation criteria are too subjective to produce reliable measurements
- The memory store grows stale: old records conflict with updated knowledge

**Ethical/Safety Notes:**
If this experiment uses real user data, data handling policies must be established before the experiment begins. Test interactions should use synthetic or consenting participant data only.

---

## E2 — Episodic Memory Retrieval

**Related Hypothesis:** H5 (Episodic memory improves distinction between facts, events, and interactions)

**Goal:**
Evaluate whether an episodic memory schema — records with temporal and contextual metadata — produces better retrieval precision across different query types than a flat log.

**Method:**
1. Construct a test dataset containing three types of stored records: general facts, time-bound event records, and prior interaction records.
2. Design a query set covering all three record types.
3. Run queries against both a flat log and an episodic schema.
4. Measure retrieval precision: were the correct record types returned for each query type?

**Expected Observation:**
Episodic schema will outperform flat log on queries that require temporal or contextual discrimination (event and interaction queries). Performance on general fact queries may be comparable.

**Possible Failure Modes:**
- Record type assignment is inconsistent: some records are miscategorized, degrading the benefit of the episodic schema
- Retrieval strategy does not exploit the episodic metadata: flat and episodic stores perform the same because the retrieval logic treats them identically
- The query set does not include genuinely discriminating cases

**Ethical/Safety Notes:**
No specific concerns for a synthetic dataset experiment. If real interaction data is used, standard data handling applies.

---

## E3 — Reflection Before Response

**Related Hypothesis:** H2 (Reflection loops improve reasoning consistency)

**Goal:**
Evaluate whether a pre-output reflection step reduces the rate of detectable inconsistencies across a structured multi-session interaction.

**Method:**
1. Design a set of interaction scripts with built-in opportunities for inconsistency: the same factual question asked in different forms, position questions repeated after several turns, and value-laden questions where drift might occur.
2. Run scripts against: (a) a baseline LLM, (b) an LLM with a reflection module that compares outputs to stored prior outputs before finalizing.
3. Score outputs for inconsistency: explicit contradictions (factual), and implicit inconsistencies (position drift without justification).

**Expected Observation:**
The reflection-augmented system will produce a lower rate of explicit contradictions. Implicit inconsistency rates may also be lower but are harder to measure.

**Possible Failure Modes:**
- Reflection module latency makes the system impractical for interactive use
- Reflection module generates false positives: flags legitimate position updates as inconsistencies
- Reflection module generates false negatives: misses genuine inconsistencies because comparison is too shallow
- The intervention changes output style in ways that affect readability, not just consistency

**Ethical/Safety Notes:**
No specific concerns for a synthetic test dataset. If human evaluators assess output quality, a brief review ethics protocol should be documented.

---

## E4 — Belief Update

**Related Hypothesis:** H3 (Self-model improves uncertainty representation), H2 (Reflection loops improve consistency)

**Goal:**
Evaluate whether a system with a belief update mechanism — the ability to revise stored beliefs when new contradicting information is provided — produces outputs that correctly reflect the updated state.

**Method:**
1. Seed the memory store with a set of stored beliefs.
2. Provide explicit corrections or contradictory information in subsequent interactions.
3. Query the system on topics covered by the original and updated beliefs.
4. Evaluate whether responses reflect the updated belief, the original belief, or ambiguity between the two.

**Expected Observation:**
After a belief update, the system will respond consistently with the updated belief rather than the original. Responses should acknowledge the update where relevant.

**Possible Failure Modes:**
- The update mechanism writes the new belief but retrieval still returns the old one
- The update mechanism overwrites the old belief without recording that a revision occurred, losing audit trail
- The system correctly updates one representation of a belief but not all related ones, leading to partial inconsistency

**Ethical/Safety Notes:**
Belief update mechanisms must be auditable. Any implementation should log both the original and updated belief, the trigger for the update, and the timestamp. Unlogged belief updates in a real system would be a significant safety concern.

---

## E5 — Self-State Tracking

**Related Hypothesis:** H3 (Self-model improves uncertainty representation)

**Goal:**
Evaluate whether a system with a self-model — a structured record of what it knows and does not know — produces more accurate uncertainty statements than a baseline without one.

**Method:**
1. Construct a test set of questions: some within the system's known knowledge base, some clearly outside it, and some at the boundary.
2. Run questions against a baseline LLM and a self-model-augmented version.
3. Evaluate responses for: appropriate hedging in uncertain domains, inappropriate confidence in areas of known limitation, and correct refusal to answer in areas where no relevant knowledge is stored.

**Expected Observation:**
The self-model-augmented system will express appropriate uncertainty more consistently, particularly in domains not represented in its stored knowledge.

**Possible Failure Modes:**
- The self-model is too coarse: it tracks topic coverage at a level too high to provide useful uncertainty signals
- The self-model is stale: it reflects prior state accurately but has not been updated with recent additions or deletions
- The underlying LLM's confidence calibration is so poor that the self-model signal is insufficient to override it

**Ethical/Safety Notes:**
No specific concerns for a synthetic experiment. In a deployed setting, misleading uncertainty representations (either over- or under-confident) have real consequences for user trust. This must be addressed before any real-world use.

---

## E6 — Continuity Across Sessions

**Related Hypothesis:** H4 (Context continuity is necessary for long-term adaptive behavior)

**Goal:**
Evaluate whether a continuity layer — preserving and restoring session state across interactions — enables adaptive behavior that a stateless system cannot produce.

**Method:**
1. Design a multi-session protocol in which the user provides feedback across several sessions that should shift the system's behavior (e.g., repeatedly correcting a specific type of response, establishing a preference, or building up a shared context).
2. Run the protocol against a stateless baseline and a continuity-augmented version.
3. Evaluate whether the continuity-augmented system's behavior shifts in the expected direction across sessions, while the baseline does not.

**Expected Observation:**
The continuity-augmented system will show behavioral adaptation in response to accumulated session history. The stateless baseline will not.

**Possible Failure Modes:**
- The continuity layer restores context but the system does not use it to adapt behavior
- Restored context is too large or too noisy to be useful: the system's performance degrades rather than improves
- The adaptation is superficial: the system mentions prior context but does not genuinely change its outputs
- Long-gap sessions (days between sessions) cause the restored context to be misleading or stale

**Ethical/Safety Notes:**
Cross-session state persistence introduces meaningful privacy implications. Any implementation must document clearly what is stored, for how long, and how it can be deleted. This applies even to test environments.

---

*Experiment designs will be updated as implementation proceeds. Results, including failures, will be recorded in this document or a linked results file.*
