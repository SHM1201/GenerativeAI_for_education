# GenerativeAI_for_education

This was a project for the course Generative AI WiSe'25 at Saarland University. This project focused on making LLMs for example GPT-4o-mini and Phi-3-mini usable in the educational settings where these models could be used as AI Tutors for students, say, learning to program. How this would work is that an LLM would analyze a buggy code written by a student and generate the repairs for that program that best align with the student's code and generate relevant and concise hints for the student to ponder upon. 

Worked with the INTROPYNUS dataset and applied prompt engineering techniques such as Zero-shot Chain of Thought and supervised finetuning with LoRA to improve the models outputs.

## Metrics
Quality metrics for program repair: RPass (binary) examines whether the repaired program
passes all test cases, signifying a successful fix. REdit (non-negative number) captures the token-level
edit distance between the buggy and the repaired program, with a smaller edit distance reflecting
that the repaired program is better aligned with the learner’s buggy program.

Quality metrics for hint generation: HCorrect (binary) captures whether the
generated hint provides correct information for resolving issues in the buggy program. HInformative
(binary) captures whether the generated hint provides useful information to help the learner resolve
bug(s). HConceal (binary) captures that the information in the generated hint is not too detailed,
so the learner would also have to reason about implementing the fixes. HComprehensible (binary)
captures whether the generated hint is easy to understand, presented in a readable format, and does
not contain redundant information. The overall quality of the generated hint is measured by HGood
(binary) that takes the value of 1 (good quality) when all the four attributes are rated as 1.

References:
1. Victor-Alexandru Padurean and Adish Singla. Benchmarking Generative Models on Computational
Thinking Tests in Elementary Visual Programming. In NeurIPS (Datasets and Benchmarks
Track), 2024. Paper link: https://openreview.net/pdf?id=q2WT19Ciad.

2. Tung Phung, Victor-Alexandru Padurean, Anjali Singh, Christopher Brooks, José Cambronero,
Sumit Gulwani, Adish Singla, and Gustavo Soares. Automating Human Tutor-Style Programming
Feedback: Leveraging GPT-4 Tutor Model for Hint Generation and GPT-3.5 Student Model
for Hint Validation. In LAK, 2024. Paper link: https://dl.acm.org/doi/pdf/10.1145/
3636555.3636846.

3. Nachiket Kotalwar, Alkis Gotovos, and Adish Singla. Hints-In-Browser: Benchmarking Language
Models for Programming Feedback Generation. In NeurIPS (Datasets and Benchmarks
Track), 2024. Paper link: https://openreview.net/pdf?id=JRMSC08gSF.
