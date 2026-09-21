import streamlit as st
from agent import run_agent
from database import run_query


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Optum Care Intelligence",
    page_icon="🏥",
    layout="wide"
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🏥 Optum Care Intelligence")
st.markdown(
    "### Healthcare Analytics AI Agent"
)

st.markdown(
    """
    Explore healthcare data using natural-language questions.
    The agent converts analytical questions into SQL, validates
    the query, retrieves data from MySQL, and returns an
    easy-to-understand response.
    """
)

st.divider()


# ---------------------------------------------------------
# HEALTHCARE OVERVIEW
# ---------------------------------------------------------

st.markdown("## 📊 Healthcare Overview")

try:

    total_patients = run_query("""
        SELECT COUNT(*)
        FROM patient_records;
    """)[0][0]

    average_age = run_query("""
        SELECT ROUND(AVG(Age), 2)
        FROM patient_records;
    """)[0][0]

    average_cost = run_query("""
        SELECT ROUND(AVG(Total_Cost), 2)
        FROM patient_records;
    """)[0][0]

    average_satisfaction = run_query("""
        SELECT ROUND(AVG(Satisfaction), 2)
        FROM patient_records;
    """)[0][0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Total Patients",
            f"{total_patients:,}"
        )

    with col2:
        st.metric(
            "🎂 Average Age",
            f"{average_age} years"
        )

    with col3:
        st.metric(
            "💰 Average Treatment Cost",
            f"₹{average_cost:,.0f}"
        )

    with col4:
        st.metric(
            "⭐ Average Satisfaction",
            f"{average_satisfaction}"
        )

except Exception as error:

    st.error(
        f"Unable to load overview metrics: {error}"
    )


st.divider()


# ---------------------------------------------------------
# CONDITION ANALYSIS
# ---------------------------------------------------------

st.markdown("## 🏥 Patient Condition Analysis")

try:

    condition_data = run_query("""
        SELECT
            `Condition`,
            COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY `Condition`
        ORDER BY patient_count DESC;
    """)

    condition_names = [
        row[0] for row in condition_data
    ]

    condition_counts = [
        row[1] for row in condition_data
    ]

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown("#### Patients by Condition")

        st.bar_chart(
            data={
                "Condition": condition_names,
                "Patients": condition_counts
            },
            x="Condition",
            y="Patients"
        )

    with col2:

        st.markdown("#### Condition Summary")

        for name, count in condition_data:

            st.write(
                f"**{name}** — {count} patients"
            )

except Exception as error:

    st.error(
        f"Unable to load condition data: {error}"
    )


# ---------------------------------------------------------
# STATE ANALYSIS
# ---------------------------------------------------------

st.markdown("## 📍 Geographic Patient Analysis")

try:

    state_data = run_query("""
        SELECT
            Patient_State,
            COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY Patient_State
        ORDER BY patient_count DESC;
    """)

    states = [
        row[0] for row in state_data
    ]

    selected_state = st.selectbox(
        "Select a state",
        ["All States"] + states
    )

    if selected_state == "All States":

        filtered_data = state_data

        st.info(
            f"The dataset contains patients from "
            f"{len(states)} states."
        )

    else:

        filtered_data = [
            row for row in state_data
            if row[0] == selected_state
        ]

        patient_count = filtered_data[0][1]

        st.info(
            f"{selected_state} has "
            f"{patient_count} patients in the dataset."
        )

    st.bar_chart(
        data={
            "State": [
                row[0] for row in filtered_data
            ],
            "Patients": [
                row[1] for row in filtered_data
            ]
        },
        x="State",
        y="Patients"
    )

except Exception as error:

    st.error(
        f"Unable to load state data: {error}"
    )


# ---------------------------------------------------------
# READMISSION ANALYSIS
# ---------------------------------------------------------

st.markdown("## 🔄 Readmission Analysis")

try:

    readmission_data = run_query("""
        SELECT
            Readmission,
            COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY Readmission;
    """)

    total_records = sum(
        row[1] for row in readmission_data
    )

    readmitted_count = 0

    for row in readmission_data:

        if str(row[0]).lower() == "yes":

            readmitted_count = row[1]

    if total_records > 0:

        readmission_rate = (
            readmitted_count / total_records
        ) * 100

    else:

        readmission_rate = 0

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🔄 Readmission Rate",
            f"{readmission_rate:.2f}%"
        )

    with col2:

        st.metric(
            "🔁 Readmitted Patients",
            f"{readmitted_count:,}"
        )

    st.bar_chart(
        data={
            "Readmission Status": [
                row[0] for row in readmission_data
            ],
            "Patients": [
                row[1] for row in readmission_data
            ]
        },
        x="Readmission Status",
        y="Patients"
    )

except Exception as error:

    st.error(
        f"Unable to load readmission data: {error}"
    )


# ---------------------------------------------------------
# PATIENT OUTCOMES
# ---------------------------------------------------------

st.markdown("## 📈 Patient Outcomes")

try:

    outcome_data = run_query("""
        SELECT
            Outcome,
            COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY Outcome
        ORDER BY patient_count DESC;
    """)

    st.bar_chart(
        data={
            "Outcome": [
                row[0] for row in outcome_data
            ],
            "Patients": [
                row[1] for row in outcome_data
            ]
        },
        x="Outcome",
        y="Patients"
    )

except Exception as error:

    st.error(
        f"Unable to load outcome data: {error}"
    )


# ---------------------------------------------------------
# INSURANCE ANALYSIS
# ---------------------------------------------------------

st.markdown("## 🛡️ Insurance Claims Analysis")

try:

    insurance_data = run_query("""
        SELECT
            Insurance_Claimed,
            COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY Insurance_Claimed;
    """)

    total_insurance_records = sum(
        row[1] for row in insurance_data
    )

    claimed_count = 0

    for row in insurance_data:

        if str(row[0]).lower() == "yes":

            claimed_count = row[1]

    if total_insurance_records > 0:

        claim_rate = (
            claimed_count /
            total_insurance_records
        ) * 100

    else:

        claim_rate = 0

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🛡️ Insurance Claim Rate",
            f"{claim_rate:.2f}%"
        )

    with col2:

        st.metric(
            "📄 Patients with Claims",
            f"{claimed_count:,}"
        )

    st.bar_chart(
        data={
            "Insurance Status": [
                row[0] for row in insurance_data
            ],
            "Patients": [
                row[1] for row in insurance_data
            ]
        },
        x="Insurance Status",
        y="Patients"
    )

except Exception as error:

    st.error(
        f"Unable to load insurance data: {error}"
    )


# ---------------------------------------------------------
# TREATMENT COST ANALYSIS
# ---------------------------------------------------------

st.markdown("## 💰 Treatment Cost Analysis")

try:

    cost_data = run_query("""
        SELECT
            `Condition`,
            ROUND(AVG(Total_Cost), 2) AS average_cost
        FROM patient_records
        GROUP BY `Condition`
        ORDER BY average_cost DESC;
    """)

    st.bar_chart(
        data={
            "Condition": [
                row[0] for row in cost_data
            ],
            "Average Cost": [
                float(row[1]) for row in cost_data
            ]
        },
        x="Condition",
        y="Average Cost"
    )

except Exception as error:

    st.error(
        f"Unable to load treatment cost data: {error}"
    )


# ---------------------------------------------------------
# AI ANALYTICS AGENT
# ---------------------------------------------------------

st.divider()

st.markdown("## 🤖 Ask the Healthcare Analytics Agent")

st.markdown(
    """
    Ask questions about the healthcare dataset using
    natural language.
    """
)

question = st.text_input(
    "Your question",
    placeholder="Example: Which condition is most common?"
)


if st.button("🔍 Analyze"):

    if question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Analyzing healthcare data..."
        ):

            answer = run_agent(question)

        st.success(
            "Analysis complete!"
        )

        st.markdown("### 🤖 Agent Response")

        st.info(answer)


# ---------------------------------------------------------
# EXAMPLE QUESTIONS
# ---------------------------------------------------------

st.markdown("### 💡 Try asking")

example_questions = [
    "How many patients are in the dataset?",
    "What is the average age of patients?",
    "Which condition is most common?",
    "What is the readmission rate?",
    "Show me the details of patient 101",
    "What is the highest treatment cost?"
]

for example in example_questions:

    st.markdown(
        f"• `{example}`"
    )


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("🏥 Optum Care Intelligence")

st.sidebar.markdown(
    """
    ### Analytics Capabilities

    👥 Patient statistics

    🎂 Age analysis

    🏥 Condition analysis

    📍 State analysis

    🔄 Readmission analysis

    🛏️ Length of stay

    🛡️ Insurance analysis

    📈 Patient outcomes

    💰 Treatment cost

    ⭐ Satisfaction analysis
    """
)

st.sidebar.divider()

st.sidebar.markdown(
    """
    ### 🔐 Security

    The agent validates generated SQL
    before executing it against the database.

    Only analytical SELECT queries are
    permitted.
    """
)

st.sidebar.divider()

st.sidebar.caption(
    "Optum Care Intelligence — Healthcare Analytics Project"
)

st.sidebar.caption(
    "Built with Python • MySQL • Streamlit • AI Agent Architecture"
)


# ---------------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------------

st.divider()

st.caption(
    "⚠️ This project is designed for healthcare data analytics "
    "and educational purposes. Analytical flags and insights "
    "are not medical diagnoses or clinical recommendations."
)