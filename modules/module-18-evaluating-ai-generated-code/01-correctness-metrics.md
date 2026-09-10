# Tutorial 18.1 — Correctness Metrics

**Created by School of AI**

## Objective
Apply **correctness metrics** while keeping the human engineer accountable for correctness.

## Workflow
1. State desired behavior and constraints.
2. Inspect relevant code before prompting.
3. Ask AI for a plan before a large change.
4. Keep the change small enough to review.
5. Read the generated diff.
6. Run tests and static checks.
7. Test failure and edge cases.
8. Review security and data exposure.
9. Refactor only with behavioral evidence.
10. Record what changed and why.

## Verification questions
- Can I explain every important change?
- Did the AI invent an API, file, dependency or requirement?
- What evidence proves behavior?
- What could regress?
- Did permissions or data access change?
- Is the diff larger than necessary?
- Can I roll it back?

## Exercise
Create a small change request, AI prompt, proposed plan, diff review, test evidence and final acceptance decision.

---

**Created by School of AI**
