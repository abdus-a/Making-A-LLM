# ADR-0001 — Pure Python, no ML libraries

**Status:** accepted · **Date:** 2026-07-14 (documenting an existing, standing choice)

## Context
This is a learning build. Sami wants to understand how an LLM works at the level of the actual
arithmetic, not how to call a framework.

## Decision
Build everything in **pure Python with no ML libraries** (no numpy, torch, tensorflow). Where a
Python built-in would hide the mechanism we're trying to learn, hand-roll it too:
- `make_lowercase` does ASCII math instead of `str.lower()`
- `tokenize` walks characters instead of `str.split()`
- `build_vocabulary` dedupes with a nested loop instead of `set()`

## Consequences
- ➕ Maximum transparency; every step is inspectable and explainable.
- ➕ Forces real understanding of embeddings, softmax, backprop.
- ➖ Slow and unscalable — acceptable, since scale is a non-goal.
- ➖ We re-implement known-solved things; that IS the point here.

## Revisit when
Sami explicitly shifts the goal from *learning the internals* to *building something performant*.
Until then this decision holds and overrides any instinct to "just use numpy."
