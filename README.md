# 🏥 Optum Care Intelligence Agent

## Healthcare Analytics AI Agent

Optum Care Intelligence is a beginner-friendly healthcare analytics agent that allows users to ask questions about structured healthcare data using natural language.

The system converts user questions into analytical SQL queries, validates the queries for security, executes them against a MySQL database, and converts the results into easy-to-understand responses.

---

## 🎯 Project Objective

The goal of this project is to demonstrate how an AI-agent architecture can be applied to healthcare data analytics.

Instead of manually writing SQL queries, users can ask questions such as:

- How many patients are in the dataset?
- What is the average age of patients?
- Which condition is most common?
- What is the readmission rate?
- What is the highest treatment cost?
- Show me the details of patient 101.

The agent processes the question and retrieves the relevant information from the healthcare database.

---

## 🧠 Agent Architecture

```text
                 User
                   │
                   ▼
        Natural Language Question
                   │
                   ▼
          Intent / SQL Generation
                   │
                   ▼
             SQL Validator
                   │
          ┌────────┴────────┐
          │                 │
       Safe Query       Unsafe Query
          │                 │
          ▼                 ▼
       MySQL DB          Blocked
          │
          ▼
       Query Result
          │
          ▼
    Result Interpretation
          │
          ▼
    Natural Language Answer