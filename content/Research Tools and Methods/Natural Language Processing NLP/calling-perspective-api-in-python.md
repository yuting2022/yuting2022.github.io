---
title: Calling Perspective API in Python
date: 2026-07-09
tags: NLP, Perspective API, Text Classification, Toxicity Detection, Computational Methods
article_class: reading-note
---

Perspective API is a machine-learning-based tool that scores the perceived attributes of a piece of text, such as toxicity, insult, threat, profanity, identity attack, or other forms of potentially harmful language.

This note summarizes how Perspective API works conceptually and how to call it in Python for computational social science research.

<a class="resource-link" href="https://github.com/yuting2022/API_tests/tree/main/Perspective_API">Download the code on GitHub</a>

## What is Perspective API?

Perspective API is a free API that uses machine learning models to score attributes of a comment or text. When a text input is sent to the API, the model returns probability scores indicating how likely readers are to perceive the text as containing a given attribute.

For example, a comment may receive scores for attributes such as:

- toxicity
- severe toxicity
- insult
- profanity
- threat
- identity attack
- sexually explicit content
- likely to reject

The input is text. The output is usually a probability score between **0** and **1**.

## How to interpret the scores

A higher score indicates a greater likelihood that readers would perceive the text as containing a particular attribute.

Importantly, a Perspective score should not be interpreted as an objective measurement of what the text “is.” Rather, it estimates how readers may perceive the text.

For example, a toxicity score of **0.90** does not necessarily mean that a comment is “90% toxic.” It means the model estimates that approximately 9 out of 10 readers would likely perceive the comment as toxic.

## Key characteristics

Perspective API has several practical characteristics that matter for research use:

- It supports multiple languages, including English, Spanish, French, German, Portuguese, and Italian.
- It is hosted through Google Cloud.
- It can be accessed through different programming languages.
- The maximum text size per request is limited, so long documents may need to be split into shorter units.
- API use is subject to quota limits, which should be checked through Google Cloud.

## Prerequisites

Before using Perspective API, you need to:

- have a Google account;
- create or select a Google Cloud project;
- request access to Perspective API;
- enable the API in Google Cloud;
- generate and securely store an API key.

<div class="callout">Do not publish your API key in public code repositories.</div>

## Calling Perspective API in Python

A typical Python workflow includes the following steps:

- import the Google API client library;
- store the API key securely;
- build a Perspective API client;
- define the text input;
- request one or more attributes;
- execute the request and parse the returned scores.

A simplified structure looks like this:

```python
from googleapiclient import discovery
import json

API_KEY = "YOUR_API_KEY"

client = discovery.build(
    "commentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
)

analyze_request = {
    "comment": {"text": "Hello, world!"},
    "requestedAttributes": {"TOXICITY": {}},
}

response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))
```

For real research projects, the API key should be stored securely, for example in an environment variable or a local configuration file that is not uploaded to GitHub.

## Applications

Perspective API is commonly used in moderation and computational text analysis. In industry settings, it can help identify comments that may require review. In academic research, it can be used to study toxic language, harassment, incivility, or other forms of problematic online discourse.

However, Perspective API should not be treated as a perfect or neutral measurement tool. Like all machine learning systems, it can make errors and may perform differently across contexts, groups, languages, and genres of text.

## Research reminders

For academic research, Perspective API is best used with caution.

Some useful practices include:

- validating model scores on a sample of the research corpus;
- avoiding direct interpretation of scores as ground truth;
- comparing Perspective API with other classifiers when possible;
- documenting the attributes, thresholds, and API version used;
- considering the ethical implications of labeling user-generated content.

## Takeaway

Perspective API provides a convenient way to obtain machine-learning-based scores for text attributes such as toxicity or insult. It can be useful for computational social science research, but its outputs should be interpreted as model-based estimates of perceived language attributes rather than objective labels.
