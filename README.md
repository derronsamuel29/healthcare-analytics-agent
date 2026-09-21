# 🏥 Healthcare Analytics Agent

### Natural-language healthcare analytics using Python, SQL, MySQL and Streamlit

![Healthcare Analytics Agent Dashboard](Screenshot%202026-09-18%20172355.png)

---

## 📌 Overview

The **Healthcare Analytics Agent** is an interactive analytics application that allows users to ask questions about healthcare data using natural language instead of manually writing SQL queries.

The system interprets the user's question, generates an analytical SQL query, validates the query for security, retrieves data from MySQL, and converts the result into an easy-to-understand response.

This project demonstrates how **data analytics, SQL, Python, and AI-agent concepts** can be combined into a practical healthcare analytics workflow.

---

## 🎯 Project Objective

The goal of this project is to demonstrate how an AI-agent-style architecture can be applied to healthcare data analytics.

The current version uses a rule-based natural-language-to-SQL layer, with a modular architecture designed to support future LLM integration.

Instead of writing SQL manually, users can ask questions such as:

- How many patients are in the dataset?
- What is the average age of patients?
- Which condition is most common?
- What is the readmission rate?
- What is the highest treatment cost?
- How many patients over 65 were readmitted?
- Show me the details of patient 101.

The agent processes the question and retrieves the relevant analytical information from the healthcare database.

---

## 🧠 How the Agent Works

```text
User Question
      │
      ▼
Natural Language Processing
      │
      ▼
SQL Generation
      │
      ▼
SQL Security Validation
      │
      ▼
MySQL Database
      │
      ▼
Query Result
      │
      ▼
Result Interpretation
      │
      ▼
Natural Language Answer


| Technology    | Purpose                                 |
| ------------- | --------------------------------------- |
| Python        | Agent logic and application development |
| MySQL         | Healthcare data storage and querying    |
| SQL           | Data analysis and aggregation           |
| Streamlit     | Interactive dashboard                   |
| Python-dotenv | Environment variable management         |


📊 Dataset

The project uses a structured healthcare patient dataset containing 984 patient records.

The dataset includes information such as:

Patient ID
Age
Gender
Condition
Medication
Admission date
Discharge date
Patient state
Length of stay
Readmission
Outcome
Satisfaction
Insurance claims
Treatment cost
📈 Analytics Capabilities

The agent can answer questions related to:

👥 Patient Analytics
Total number of patients
Patient demographic information
Individual patient details
Average patient age
Gender distribution
🏥 Healthcare Analytics
Most common conditions
Readmission analysis
Patient outcomes
Length of stay
Patient satisfaction
💰 Financial Analytics
Average treatment cost
Highest treatment cost
Treatment cost by condition
Insurance claim analysis
📍 Geographic Analytics
Patient distribution by state

🔐 SQL Security

The project includes an SQL validation layer that restricts database operations to analytical SELECT queries.

Commands such as:
INSERT
UPDATE
DELETE
DROP
ALTER
TRUNCATE
CREATE
REPLACE
GRANT
REVOKE

📂 Project Structure
healthcare-analytics-agent/
│
├── app.py
├── agent.py
├── ai_sql_generator.py
├── database.py
├── result_interpreter.py
├── schema.py
├── sql_validator.py
├── README.md
├── .gitignore
└── Screenshot 2026-09-18 172355.png

File Responsibilities

app.py
Streamlit dashboard and user interface.

agent.py
Controls the overall agent workflow.

ai_sql_generator.py
Converts supported natural-language questions into SQL queries.

database.py
Handles the MySQL database connection and query execution.

sql_validator.py
Checks generated SQL queries before execution.

result_interpreter.py
Converts database results into readable responses.

schema.py
Contains the healthcare database schema information used by the agent.

🚀 How to Run
1. Clone the repository
git clone https://github.com/derronsamuel29/healthcare-analytics-agent.git
2. Navigate into the project
cd healthcare-analytics-agent
3. Install dependencies
pip install mysql-connector-python streamlit python-dotenv
4. Configure environment variables
Create a .env file:
MYSQL_PASSWORD=your_mysql_password
Keep .env private and never upload database credentials to GitHub.
5. Set up MySQL
Create the database:
CREATE DATABASE optum_healthcare;
Create the patient_records table and import the healthcare dataset.
6. Start the Streamlit application
streamlit run app.py

💡 Example Questions
Try asking:
How many patients are in the dataset?
What is the average age?
What is the average treatment cost?
Which condition is most common?
What is the readmission rate?
How many patients over 65 were readmitted?
What is the highest treatment cost?
Show me the details of patient 101.

🔮 Future Improvements

Possible future versions could include:

LLM-powered natural-language SQL generation
More advanced conversational memory
Automated data visualization
Voice-based analytics
Advanced anomaly detection
Role-based access control
More healthcare datasets
Cloud deployment
Advanced query validation
⚠️ Disclaimer

This project is intended for healthcare data analytics and educational purposes.

It does not provide medical diagnosis, treatment recommendations, or clinical decision-making.

👨‍💻 Author

Derron Samuel

BSc Computer Data Science and Data Analytics Engineering

Interested in:

Data Analytics · Data Science · SQL · Python · AI

⭐ If you found this project interesting, feel free to explore the repository and connect with me.
