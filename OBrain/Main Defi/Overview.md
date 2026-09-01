# Overview — Making-A-LLM

## The goal
Build a working **language model from scratch in pure Python**, with **zero ML libraries**.
Every step — tokenizing, vocabulary, embeddings, the forward pass, loss, backprop, training —
is hand-written so Sami understands the machinery, not just the API.

The concrete near-term target: a **next-word predictor**. Given a word, predict the word that
tends to follow it, learned from a small hand-written training corpus.

## Why
Learning. This is Sami teaching himself how LLMs work by building one. Correctness and clarity
of the *mental model* matter more than performance or scale. Small vocab, tiny corpus, readable
code with dense explanatory comments is the house style (see [[from-scratch-llm-playbook]]).

## The corpus
`Assets/training_sentences.py` holds ~10 hand-crafted sentences clustered into themes so a
co-occurrence learner has real signal to find:
- **cooking** — potatoes / tomatoes / soup / bananas / chocolate
- **focus** — chess / ADHD / Red Bull / concentration
- **animals** — dogs / birds / fly / frisbees / bananas

The thematic overlap (bananas appears in cooking *and* animals; fly in animals) is deliberate —
it gives the eventual model ambiguity to resolve.

## Current stage
See [[Home]] → Current stage. Data-prep pipeline complete; model not yet started.

## Links
- Pipeline mechanics → [[Architecture]]
- What to build next → [[from-scratch-llm-playbook]]
