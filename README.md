# Prompt Chaining with Groq LLM

This project demonstrates the concept of **Prompt Chaining**, where a complex task is broken down into multiple smaller prompts. Each prompt performs a specific task, and its output is passed as input to the next prompt.

Instead of asking the LLM to perform everything in a single prompt, we create a sequence of prompts that work together to achieve the final result.

---

## What is Prompt Chaining?

Prompt Chaining is an LLM workflow pattern in which the output of one prompt becomes the input for another prompt.

It is useful when a task involves multiple reasoning steps that can be separated into smaller, well-defined stages.

**Workflow:**

```
Resume
   │
   ▼
Extract Candidate Skills
   │
   ▼
Job Description
   │
   ▼
Extract Required Skills
   │
   ▼
Compare Skills
   │
   ▼
Generate Match Score & Verdict
```

---

## Project Objective

The goal of this project is to understand how Prompt Chaining works by building a simple Resume Screening application.

The application performs three sequential LLM calls:

1. Extract skills from the candidate's resume.
2. Extract required skills from the job description.
3. Compare both skill sets and generate a match score with a hiring verdict.

Each step is handled by an independent prompt.

---

## Tech Stack

- Python
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv

---

## Prompt Chain Breakdown

### Step 1 – Resume Skill Extraction

The first prompt extracts only the candidate's technical skills from the resume.

**Input**

- Resume

**Output**

```
Python, FastAPI, MySQL, Docker, REST APIs, Git
```

---

### Step 2 – Job Description Skill Extraction

The second prompt extracts only the required skills from the Job Description.

**Input**

- Job Description

**Output**

```
Python, FastAPI, PostgreSQL, Docker, AWS, REST APIs
```

---

### Step 3 – Skill Matching

The third prompt receives the outputs of the previous two prompts and compares them.

It generates:

- Match Score (0–100)
- Hiring Verdict

Example:

```
Match Score: 83

Verdict:
Candidate is a good fit for the role but lacks AWS and PostgreSQL experience.
```

---

## Prompt Chain Flow

```
               Resume
                  │
                  ▼
      Prompt 1: Extract Skills
                  │
                  ▼
        Candidate Skills
                  │
                  │
                  │
Job Description   │
        │         │
        ▼         │
Prompt 2: Extract Skills
        │
        ▼
   JD Skills
        │
        ▼
Prompt 3: Compare Skills
        │
        ▼
 Match Score + Verdict
```

---

## Why Prompt Chaining?

Compared to using a single large prompt, Prompt Chaining offers several advantages:

- Breaks complex tasks into smaller, manageable steps.
- Produces more structured and reliable outputs.
- Makes debugging easier.
- Allows reuse of intermediate outputs.
- Improves modularity and maintainability.
- Makes prompts easier to modify independently.

---

## Learning Outcomes

Through this project, you will understand:

- What Prompt Chaining is.
- How to design sequential LLM workflows.
- How to pass outputs between prompts.
- Writing effective system and user prompts.
- Using the Groq API for multiple LLM calls.
- Building modular AI applications.

---

Learning Generative AI concepts through hands-on projects.
