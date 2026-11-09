Generate an HTML research report from the notes below, for product and engineering leads. It must be readable asynchronously; do not make a slide deck.

Output requirements:
- Save to {artifact_dir}.
- Use a restrained, research-style visual look.
- Do not dress up opinions that have no numbers as KPIs.

Research notes:
- Multi-agent collaboration failures are usually not a model-capability problem but a context-boundary and handoff-contract problem.
- Observation 1: when a task has no explicit artifact owner, several agents re-read the same set of files.
- Observation 2: when review looks only at the final diff and not the trace, many process errors stay hidden.
- Observation 3: the most stable teams split work into explorer, worker and reviewer, and require each role to output structured evidence.
- Recommendation: build a small trace eval first, then consider more complex autonomous scheduling.
