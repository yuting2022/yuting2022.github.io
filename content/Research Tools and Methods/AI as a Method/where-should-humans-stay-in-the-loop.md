---
title: Where Should Humans Stay in the Loop? A Five-Stage Framework for AI-Assisted Social Science
date: 2026-08-21
tags: AI, Research Methods, LLMs, Human-AI Collaboration, Social Science
article_class: reading-note
---

Large language models are rapidly becoming part of the social scientist's methodological toolkit. Researchers now use them to annotate political texts, generate experimental stimuli, simulate respondents, discover patterns in large corpora, write code, and even reproduce published studies.

The usual debate asks a simple question: **How much should researchers rely on AI?**

I think that is the wrong question.

AI does not play the same epistemic role at every stage of research. A model that is useful for brainstorming a possible explanation may be wholly inappropriate for validating a measurement. A model that performs remarkably well at classifying thousands of political messages may still introduce systematic errors that invalidate downstream statistical inference.

<div class="callout"><strong>A better question:</strong> What kind of human judgment does each stage of research require, and what role should AI be allowed to play within it?</div>

I propose thinking about AI-assisted research as a five-stage process:

<div class="power-flow"><div><strong>1. Theory formation</strong><span>concepts · definitions · theoretical commitments</span></div><b>↓</b><div><strong>2. Hypothesis discovery</strong><span>patterns · anomalies · conjectures</span></div><b>↓</b><div><strong>3. Analytical execution</strong><span>models · prompts · data · methodological architecture</span></div><b>↓</b><div><strong>4. Validation</strong><span>benchmarks · measurement error · inference</span></div><b>↓</b><div><strong>5. Research reproduction</strong><span>automation · replication · scientific responsibility</span></div></div>

Across these stages, the appropriate division of labor between humans and AI changes. AI can participate throughout the research process, but its capacity to perform a task should not be confused with **epistemic authority** over the decisions that task involves.

## 1. Theory Formation: AI Can Search, but It Cannot Commit

At the earliest stage of research, AI is already extremely useful.

A researcher entering an unfamiliar literature can ask a language model to identify relevant concepts, map adjacent fields, compare competing definitions, or surface possible connections across disciplines. Models can process an amount of information that would take a human researcher far longer to review manually.

They may also help identify recurring patterns or places where existing explanations seem incomplete.

But there is an important distinction between **finding information** and **forming a concept**.

A model may tell us that scholars define “political polarization” in several different ways. It can summarize those definitions, compare measurement strategies, and point out tensions among them. What it cannot do on the researcher's behalf is determine what polarization *should mean in this particular study* and why that conceptualization is theoretically appropriate.

That decision requires what I think of as **interpretive commitment**.

Concept formation in social science is not simply an information-retrieval problem. Researchers must choose among competing understandings of the world, determine which distinctions matter, and specify how an abstract phenomenon becomes observable. In political communication especially, concepts such as ideology, bias, polarization, populism, and misinformation are historically situated and theoretically contested (Reese, 2023).

AI can widen the field of possibilities.

Humans still have to decide which possibility is worth defending.

<div class="callout"><strong>General rule:</strong> Use AI generously for theoretical exploration, but cautiously for theoretical adjudication.</div>

The reason humans remain central here is not that AI lacks information. It is that theory requires judgment about meaning.

## 2. Hypothesis Discovery: Pattern Recognition Is Not Scientific Discovery

The distinction becomes even sharper when researchers move from concepts to hypotheses.

AI is increasingly capable of detecting patterns that humans might overlook. Models can identify latent relationships within large textual datasets, surface unusual clusters, and generate candidate explanations. Recent work suggests that AI systems can assist with forms of concept and hypothesis discovery by identifying interpretable structures in complex data (Movva et al., 2025).

That is important.

But discovering a statistical regularity is not the same as recognizing a scientific problem.

Many consequential research questions begin with something more difficult to formalize: an observation that does not fit existing expectations.

A political behavior that should have disappeared but persists.

A theory that works for one group but suddenly fails for another.

A communication pattern that contradicts what the literature tells us should happen.

Scientific discovery often depends on recognizing such **anomalies** and deciding that they should not be dismissed as noise.

This is where the difference between pattern matching and scientific interpretation becomes particularly important.

A simplified version of scientific discovery might look like:

<div class="callout"><strong>conjecture → deduction → experiment → revision → new conjecture</strong></div>

The critical step is **revision**.

When evidence conflicts with expectations, researchers may need to reconsider their assumptions, redefine concepts, or develop an entirely different explanation. By contrast, contemporary AI systems are generally strongest within an already legible hypothesis space. They can extend, combine, and recombine patterns encoded in existing data, but this is different from deciding that the existing space itself is inadequate (Ding & Li, 2025).

This does not make AI useless for discovery. Quite the opposite.

<div class="callout"><strong>Treat AI-generated hypotheses as structured conjectures rather than scientific conclusions.</strong></div>

Let the model generate possibilities. Let it make surprising associations. Let it propose explanations that initially seem implausible.

Then ask the human researcher to do the epistemically harder work: determining whether the surprise is meaningful.

## 3. Analytical Execution: The Question Is Not Which Model Is “Best”

Once a project reaches analysis, AI's role becomes much more substantial.

LLMs can classify political messages, position political actors ideologically, analyze frames and sentiment, generate experimental stimuli, process multilingual data, and simulate respondents. In some annotation tasks, their performance can rival or exceed crowd workers (Gilardi et al., 2023; Le Mens & Gallego, 2025).

At this stage, researchers may therefore be tempted to ask:

**Which model gives me the highest accuracy?**

But model performance alone is an insufficient criterion for methodological choice.

A proprietary model may provide excellent performance while changing silently over time. An open-weight model may offer better reproducibility and privacy while requiring considerably more infrastructure. A model that performs well in English may behave differently in German, Chinese, or a low-resource language. A classifier that works for relatively objective categories may struggle with socially constructed concepts such as empathy, grievance, extremity, or ideological identity (Ziems et al., 2024; Urman & Makhortykh, 2025).

The methodological question is therefore not simply which model is strongest.

<div class="callout"><strong>Which combination of model, prompting strategy, data, and validation procedure best matches the theoretical object I am trying to measure?</strong></div>

This is where human involvement changes form.

During theory formation, humans provide conceptual judgment.

During analysis, humans increasingly provide **methodological architecture**.

The researcher decides what the model is allowed to do, what information it receives, how prompts are constructed, whether outputs are aggregated across repeated runs, which model version is used, and how uncertainty will be documented.

This becomes especially important because AI systems introduce two challenges that conventional research workflows were not designed around: **prompt brittleness** and **model drift**. Small changes in wording or ordering can change model outputs. Proprietary models can also be updated without researchers knowing exactly what changed (Bail, 2024; Linegar et al., 2023).

For AI-assisted research, documenting prompts, model versions, sampling parameters, and validation procedures is not administrative detail.

It is part of the method.

## 4. Validation: 90% Accuracy May Still Be Wrong Enough

Validation may be the most important—and most underestimated—stage of AI-assisted social science.

Researchers commonly evaluate an AI annotation system by comparing its labels with human-coded data. If agreement is sufficiently high, they conclude that the model is reliable and proceed to use its predictions as variables in subsequent analysis.

But there are actually **two different validation problems**.

The first is familiar:

**Are the AI-generated labels accurate?**

The second is more consequential:

**Do the errors in those labels distort the statistical conclusions we eventually draw?**

These are not the same question.

Imagine an AI classifier that achieves 90% accuracy when identifying a political communication category. That sounds excellent.

But suppose its remaining errors are not random. Perhaps the model is slightly more likely to misclassify messages written by one ideological group, messages about race, or messages using a particular rhetorical style.

If those errors correlate with variables central to the research question, they can propagate through regression models and distort statistical inference.

Research using design-based supervised learning demonstrates exactly this problem: even highly accurate AI annotations can produce severely misleading confidence intervals when prediction errors systematically correlate with theoretically relevant variables. Combining a smaller set of expert human annotations with model predictions can help correct this measurement error (Rister Portinari Maranca et al., 2025).

<div class="callout"><strong>High predictive accuracy does not automatically imply valid inference.</strong></div>

The unit of validation should therefore not be the model alone.

It should be the **entire research pipeline**.

Researchers need to ask not merely whether AI “gets the labels right,” but how its mistakes are distributed and whether those mistakes matter for the substantive conclusions being drawn.

This is also why human oversight is especially important at the validation stage.

Humans are not simply proofreading an AI system.

They are constructing the benchmark against which claims about the social world become credible.

## 5. Research Reproduction: Automation Changes What Becomes Scarce

AI may have its clearest advantages in the later, more procedural stages of research.

Tasks involved in reproduction—locating replication materials, reconstructing computational environments, running existing models, and checking outputs—are often tedious but relatively well structured. Recent work shows that AI-assisted workflows can automate substantial parts of replication when appropriate materials are available (Xu & Yang, 2026).

This is an exciting possibility.

But automation also creates a paradox.

If AI dramatically lowers the cost of producing research, then producing *more research* becomes easier.

Producing *important research* does not necessarily become easier.

Recent evidence from a large-scale analysis of scientific papers illustrates this tension: scientists adopting AI tools may increase their individual productivity and impact while scientific exploration becomes more concentrated at the collective level (Hao et al., 2026).

The implication is not that researchers should avoid AI.

It is that automation changes what becomes scarce.

When coding becomes easier, coding skill becomes less differentiating.

When literature retrieval becomes easier, retrieving literature becomes less differentiating.

When statistical workflows can be partially automated, executing those workflows becomes less differentiating.

What becomes more valuable are the activities that remain difficult to automate:

**asking consequential questions, recognizing anomalies, making theoretical distinctions, exercising critical judgment, and imagining explanations that do not yet exist.**

In an AI-assisted scientific ecosystem, human creativity may become more—not less—important.

## Hallucination Is Not Always the Same Kind of Problem

This stage-dependent perspective also changes how we should think about familiar AI limitations.

Consider hallucination.

The standard response is straightforward: hallucinations are errors and should therefore be eliminated.

That is obviously correct when a model is retrieving factual information or producing a measurement that must correspond to empirical reality.

But in an exploratory stage, the answer may be more complicated.

Scientific discovery has never depended on uninterrupted correctness. Researchers routinely entertain conjectures that eventually turn out to be false. A strange AI-generated connection may therefore sometimes function as a creative prompt (Zhang et al., 2025).

The key is not whether the output is wrong.

The key is **what the researcher is using it for**.

During brainstorming, conceptual exploration, or hypothesis generation, an unexpected model output might be valuable precisely because it pushes the researcher outside an obvious path.

During operationalization, annotation, or validation, the same behavior becomes a methodological threat.

So instead of asking:

**Does this model hallucinate?**

Researchers should also ask:

**At this particular stage of research, what are the consequences if it does?**

## AI Reasoning Should Be Treated as Conjecture, Not Explanation

The same principle applies when LLMs explain their own reasoning.

Chain-of-thought prompting and related techniques can produce detailed rationales for why a model reached a particular conclusion. Those explanations may appear transparent and persuasive.

But they should not automatically be treated as faithful accounts of the underlying decision process. Model-generated rationales can be inconsistent with outputs and can themselves contain invented or unstable reasoning.

A more interesting approach is to use those explanations instrumentally.

For example, Peng et al. (2025) asked a multimodal LLM to explain credibility judgments about visual content, extracted candidate features from those explanations, and then validated the features against human judgments. Instead of accepting the model's explanation as ground truth, they used it as a source of empirically testable possibilities.

<div class="callout"><strong>LLM reasoning is most useful when treated as something to test, not something to trust.</strong></div>

## Perhaps “Human–AI Collaboration” Is the Wrong Metaphor

All of this leads to a deeper question.

We routinely describe the emerging research environment as one of **human–AI collaboration**.

But collaboration is a surprisingly strong word.

Genuine collaboration implies some combination of shared goals, mutual understanding, reciprocal adaptation, and common ground. Contemporary AI systems can assist, accelerate, simulate, and automate research activities, but they do not bear scholarly responsibility for the knowledge they help produce (Shah & Tamine, 2026).

They do not decide which scientific questions are socially important. They do not defend a conceptual choice to reviewers. They do not carry accountability when an analysis harms a population or produces a misleading conclusion.

Researchers do.

That asymmetry matters.

Perhaps the goal, then, should not be to determine the optimal percentage of “human” versus “AI” participation in research.

It should be to design research systems in which the capabilities of AI are used where they are epistemically productive, while responsibility remains clearly located where it belongs.

## The Framework at a Glance

<div class="framework-scroll"><table class="framework-table"><thead><tr><th>Research stage</th><th>Productive role for AI</th><th>Irreplaceable human role</th></tr></thead><tbody><tr><td><strong>Theory formation</strong></td><td>Search, comparison, conceptual exploration</td><td>Meaning-making and theoretical commitment</td></tr><tr><td><strong>Hypothesis discovery</strong></td><td>Pattern detection and conjecture generation</td><td>Anomaly recognition and explanation</td></tr><tr><td><strong>Analytical execution</strong></td><td>Classification, generation, simulation, scaling</td><td>Methodological architecture and contextual judgment</td></tr><tr><td><strong>Validation</strong></td><td>Supporting evaluation and diagnostics</td><td>Ground-truth construction and inferential accountability</td></tr><tr><td><strong>Research reproduction</strong></td><td>Automation and computational replication</td><td>Scientific judgment and responsibility</td></tr></tbody></table></div>

The central principle is simple:

<div class="callout"><strong>The fact that AI can perform a research task does not mean that it should control the epistemic decision embedded in that task.</strong></div>

AI can participate across the entire scientific process.

But the appropriate role of the human changes from stage to stage—and understanding those differences may be more important than deciding whether researchers should use AI at all.

## Selected References

Bail, C. A. (2024). Can generative AI improve social science? *Proceedings of the National Academy of Sciences, 121*(21), e2314021121.

Ding, A. W., & Li, S. (2025). Generative AI lacks the human creativity to achieve scientific discovery from scratch. *Scientific Reports, 15*, 9587.

Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences, 120*(30), e2305016120.

Hao, Q., Xu, F., Li, Y., & Evans, J. (2026). Artificial intelligence tools expand scientists' impact but contract science's focus. *Nature*.

Le Mens, G., & Gallego, A. (2025). Positioning political texts with large language models by asking and averaging. *Political Analysis, 33*(3), 274–282.

Linegar, M., Kocielnik, R., & Alvarez, R. M. (2023). Large language models and political science. *Frontiers in Political Science, 5*, 1257092.

Movva, R., Peng, K., Garg, N., Kleinberg, J., & Pierson, E. (2025). Sparse autoencoders for hypothesis generation. *arXiv preprint arXiv:2502.04382*.

Peng, Y., Qian, S., Lu, Y., & Shen, C. (2025). Large language model-informed feature discovery improves prediction and interpretation of credibility perceptions of visual content. *arXiv preprint arXiv:2504.10878*.

Reese, S. D. (2023). Writing the conceptual article: A practical guide. *Digital Journalism, 11*(7), 1195–1210.

Rister Portinari Maranca, A., Chung, J., Hinck, M., Wolsky, A. D., Egami, N., & Stewart, B. M. (2025). Correcting the measurement errors of AI-assisted labeling in image analysis using design-based supervised learning. *Sociological Methods & Research, 54*(3), 984–1016.

Shah, C., & Tamine, L. (2026). Why “human-AI collaboration” obscures what actually happens in information seeking. *Journal of the Association for Information Science and Technology*. Advance online publication.

Urman, A., & Makhortykh, M. (2025). The silence of the LLMs: Cross-lingual analysis of guardrail-related political bias and false information prevalence in ChatGPT, Google Bard (Gemini), and Bing Chat. *Telematics and Informatics, 96*, 102211.

Xu, Y., & Yang, L. Y. (2026). Scaling reproducibility: An AI-assisted workflow for large-scale replication and reanalysis. *arXiv preprint arXiv:2602.16733*.

Zhang, Y., Khan, S. A., Mahmud, A., Yang, H., Lavin, A., Levin, M., et al. (2025). Advancing the scientific method with large language models: From hypothesis to discovery. *arXiv preprint arXiv:2505.16477*.

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics, 50*(1), 237–291.
