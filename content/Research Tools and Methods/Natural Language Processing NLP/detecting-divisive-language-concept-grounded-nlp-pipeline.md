---
title: Detecting Divisive Language: A Concept-Grounded NLP Pipeline
date: 2026-07-09
tags: NLP, Text Classification, Political Polarization, Computational Social Science, LLMs
---

This note introduces an NLP pipeline I developed with collaborators for detecting divisive language in polarized social media discourse.

The paper was published in the **Proceedings of the Twentieth International AAAI Conference on Web and Social Media (ICWSM 2026)**. The paper can be read and downloaded here:

<a class="resource-link" href="https://ojs.aaai.org/index.php/ICWSM/article/view/42796">Read/download the paper</a>

## What problem does this tool address?

Political polarization is often studied computationally through indirect proxies such as toxicity, hate speech, profanity, or negative sentiment. However, these signals do not necessarily capture the kind of identity-based antagonism that makes discourse polarizing.

The core idea of this project is that polarizing discourse is not simply “toxic” or “negative.” Instead, it often works by explaining political or social disagreement through group-based identities.

We conceptualize this as **divisive language**: language that attributes political or social disagreement to group-based identities.

## Why divisive language?

The paper argues that existing NLP approaches often rely on adjacent but imperfect constructs, such as toxicity or sentiment. These constructs can miss polarizing discourse that appears humorous, neutral, or non-abusive, while also capturing harmful language that is not necessarily polarizing.

Divisive language focuses more directly on how discourse creates or reinforces group boundaries.

In the paper, divisive language is operationalized through two observable signals:

- the presence of identifiable social groups;
- the attribution of outcomes, often negative ones, to those group identities.

## How the pipeline works

The pipeline separates **concept-level supervision** from **high-throughput classification**.

Rather than asking a small classifier to learn an abstract theoretical construct directly from limited labeled data, the pipeline uses a staged process.

### Stage 1: Definition-grounded synthetic annotation

A large proprietary LLM is prompted with a detailed definition of divisive language. It produces both a natural-language analysis and a categorical label.

This stage is designed to make the supervision signal explicitly grounded in the theoretical definition.

### Stage 2: Instruction-tuned LLM for scalable label generation

An open-source instruction-following model is fine-tuned on the LLM-labeled data. It then generates labels for a much larger unlabeled corpus.

This stage transfers the concept-aligned decision boundary from a powerful model to a more scalable annotation process.

### Stage 3: Lightweight classifier training

A RoBERTa-based classifier is trained on the large pseudo-labeled dataset. The goal is to produce a model that is efficient enough for large-scale computational analysis.

## Why this matters methodologically

This project treats LLMs not only as classifiers, but as **methodological intermediaries**. They help translate an abstract social science construct into structured supervision signals that can later be distilled into smaller models.

For computational social science, this is useful because many important constructs are not reducible to surface keywords. They require conceptual interpretation before they can be scaled.

## Main takeaway

This pipeline shows that divisive language can be modeled as a distinct, computable linguistic construct. It offers a way to study polarization beyond toxicity, sentiment, or hate-speech frameworks.
