---
name: why-chain
description: Interrogate a claim or a previous response by asking "why is that true?" and "how do we know?" repeatedly until every step bottoms out in a measured fact, a definition, or an admitted unknown. Flags circular reasoning (a claim that restates its own evidence), unsupported steps, and coined labels used as if they were explanations. Use when the user says "why-chain this", "keep asking why", or challenges a rule as circular.
---

# why-chain

Take the claim (or the last response) and run this loop in plain English, no coined labels:

1. **State the claim in one sentence.** If it was a rule ("trust fast answers"), restate it as a claim about the world ("answers produced quickly are right more often than answers produced slowly").
2. **Ask: why is that true?** Write the reason in one sentence.
3. **Ask of the reason: how do we know?** Name the evidence: a measured number and where it came from, a study with a citation, a definition, or "not known."
4. **Check for circularity.** If the reason restates the claim in other words, or the evidence is the claim itself, say so: "this is circular as stated." Then find the non-circular version: what would the claim have to say to be testable, and does the evidence test it?
5. **Repeat 2–4 on each reason** until every branch ends in one of: a measured fact (with the number and where it came from), a definition, an explicit unknown.
6. **Report the chain** as a short indented list. Mark each leaf as FACT / DEFINITION / UNCHECKED / UNKNOWN / CIRCULAR. Then give the corrected claim if the original didn't survive.

Rules:
- Real terms only, defined where used. No invented labels.
- A leaf that says "the literature says" must carry a citation or become UNKNOWN.
- A citation recalled from memory and not checked in this session is UNCHECKED, not FACT. If the claim matters, check it with the research-verify agent before relying on it.
- Distinguish "consistent with" from "shown by" at every step. A number counts as FACT only when the comparison it implies is actually in the data.
- Keep each line under about twenty words.
- **Validity check, not only provenance.** (Added after a real error: a correctly sourced fact sitting inside an invalid inference.) For any claim of the form "X is (or is not) evidence for Y," ask first: is X more expected if Y is true than if Y is false, by any margin? If yes, X is evidence for Y, however weak; a rival explanation lowers the ratio but does not zero it. Never load Y with an extra prediction it does not make and then score its absence against Y. Say "weak evidence" when the ratio is modestly above one, and "not evidence" only when X is equally expected either way.

Example of the loop on "our new AI grader is accurate":
- Claim: the grader's scores match what a careful person would score.
- Why: it gave sensible-looking scores on the ten samples we tried. FACT that we looked; consistent with accuracy, not shown by it.
- Circularity check: "sensible-looking" was judged by the person who built it and expects it to work. CIRCULAR as stated.
- How would we know: score a set of samples by hand and compare. UNKNOWN until done.
- Testable version: on 40 hand-checked samples, the grader agrees with the hand check on at least 38.
- Corrected claim: the grader is untested. Check 40 samples by hand before trusting any number it produces.
