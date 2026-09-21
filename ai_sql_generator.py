import re


def generate_ai_sql(question):

    question = question.lower().strip()

    # ==========================================
    # PATIENT PROFILE
    # ==========================================

    patient_match = re.search(
        r"(?:patient|patient id|patient number)\s*(?:id\s*)?(\d+)",
        question
    )

    if patient_match:
        patient_id = patient_match.group(1)

        return f"""
        SELECT
            Patient_ID,
            Age,
            Gender,
            `Condition`,
            Medication,
            Admission_Date,
            Discharge_Date,
            Patient_State,
            Year_of_Admission,
            Length_of_Stay,
            Readmission,
            Outcome,
            Satisfaction,
            Insurance_Claimed,
            Total_Cost
        FROM patient_records
        WHERE Patient_ID = {patient_id};
        """

    # ==========================================
    # AGE + READMISSION
    # ==========================================

    if (
        (
            "older than 65" in question
            or "over 65" in question
            or "above 65" in question
            or "age above 65" in question
            or "elderly" in question
        )
        and "readmitted" in question
    ):
        return """
        SELECT COUNT(*) AS patient_count
        FROM patient_records
        WHERE Age > 65
          AND LOWER(Readmission) = 'yes';
        """

    # ==========================================
    # AVERAGE AGE + AVERAGE COST
    # ==========================================

    if (
        "average age" in question
        and (
            "average cost" in question
            or "average treatment cost" in question
        )
    ):
        return """
        SELECT
            ROUND(AVG(Age), 2) AS average_age,
            ROUND(AVG(Total_Cost), 2) AS average_cost
        FROM patient_records;
        """

    # ==========================================
    # PATIENT COUNT + READMISSION RATE
    # ==========================================

    if (
        (
            "how many patients" in question
            or "total patients" in question
            or "number of patients" in question
        )
        and (
            "readmission rate" in question
            or "rate of readmission" in question
        )
    ):
        return """
        SELECT
            COUNT(*) AS total_patients,
            ROUND(
                SUM(
                    CASE
                        WHEN LOWER(Readmission) = 'yes' THEN 1
                        ELSE 0
                    END
                ) * 100.0 / COUNT(*),
                2
            ) AS readmission_rate
        FROM patient_records;
        """

    # ==========================================
    # STATE ANALYSIS
    # ==========================================

    if (
        "which state" in question
        or "state has" in question
        or "state with the most" in question
        or "state with the highest" in question
        or "patients by state" in question
        or "state analysis" in question
    ):
        return """
        SELECT Patient_State, COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY Patient_State
        ORDER BY patient_count DESC;
        """

    # ==========================================
    # HIGH PRIORITY ANALYTICAL FLAG
    # ==========================================

    if (
        "high risk" in question
        or "high-risk" in question
        or "high priority" in question
        or "high-priority" in question
        or "high flag" in question
    ):
        return """
        SELECT COUNT(*) AS patient_count
        FROM patient_records
        WHERE
            (Age >= 65)
            + (LOWER(Readmission) = 'yes')
            + (Length_of_Stay >= 10) >= 2;
        """

    # ==========================================
    # MODERATE PRIORITY ANALYTICAL FLAG
    # ==========================================

    if (
        "moderate risk" in question
        or "moderate-risk" in question
        or "moderate priority" in question
        or "moderate-priority" in question
        or "moderate flag" in question
    ):
        return """
        SELECT COUNT(*) AS patient_count
        FROM patient_records
        WHERE
            (Age >= 65)
            + (LOWER(Readmission) = 'yes')
            + (Length_of_Stay >= 10) = 1;
        """

    # ==========================================
    # NUMBER OF READMITTED PATIENTS
    # ==========================================

    if (
        "how many patients were readmitted" in question
        or "how many patients are readmitted" in question
        or "number of readmitted patients" in question
        or "count of readmitted patients" in question
    ):
        return """
        SELECT COUNT(*) AS readmitted_patients
        FROM patient_records
        WHERE LOWER(Readmission) = 'yes';
        """

    # ==========================================
    # READMISSION RATE
    # ==========================================

    if (
        "readmission rate" in question
        or "rate of readmission" in question
        or "percentage of readmission" in question
        or "percent of patients were readmitted" in question
    ):
        return """
        SELECT
            ROUND(
                SUM(
                    CASE
                        WHEN LOWER(Readmission) = 'yes' THEN 1
                        ELSE 0
                    END
                ) * 100.0 / COUNT(*),
                2
            ) AS readmission_rate
        FROM patient_records;
        """

    # ==========================================
    # TOTAL PATIENTS
    # ==========================================

    if (
        "how many patients" in question
        or "total patients" in question
        or "number of patients" in question
        or "how many people" in question
        or "total people" in question
        or "patient count" in question
        or "how many records" in question
        or "total number of patients" in question
        or "number of people" in question
    ):
        return """
        SELECT COUNT(*) AS total_patients
        FROM patient_records;
        """

    # ==========================================
    # AVERAGE AGE
    # ==========================================

    if (
        "average age" in question
        or "mean age" in question
        or "how old" in question
        or "average patient age" in question
    ):
        return """
        SELECT ROUND(AVG(Age), 2) AS average_age
        FROM patient_records;
        """

    # ==========================================
    # AVERAGE TREATMENT COST
    # ==========================================

    if (
        "average cost" in question
        or "average treatment cost" in question
        or "mean treatment cost" in question
        or "typical treatment cost" in question
    ):
        return """
        SELECT ROUND(AVG(Total_Cost), 2) AS average_cost
        FROM patient_records;
        """

    # ==========================================
    # HIGHEST TREATMENT COST
    # ==========================================

    if (
        "highest cost" in question
        or "maximum cost" in question
        or "most expensive" in question
        or "highest treatment cost" in question
        or "most costly" in question
    ):
        return """
        SELECT Patient_ID, Total_Cost
        FROM patient_records
        ORDER BY Total_Cost DESC
        LIMIT 1;
        """

    # ==========================================
    # HIGHEST AVERAGE COST BY CONDITION
    # ==========================================

    if (
        "highest average cost by condition" in question
        or "condition with highest average cost" in question
        or "most expensive condition on average" in question
    ):
        return """
        SELECT
            `Condition`,
            ROUND(AVG(Total_Cost), 2) AS average_cost
        FROM patient_records
        GROUP BY `Condition`
        ORDER BY average_cost DESC
        LIMIT 1;
        """

    # ==========================================
    # MOST COMMON CONDITION
    # ==========================================

    if (
        "most common condition" in question
        or "most common disease" in question
        or "most common illness" in question
        or "most frequent condition" in question
        or "most frequent disease" in question
        or "most frequently" in question
        or "which condition occurs most" in question
        or "which illness occurs most" in question
    ):
        return """
        SELECT `Condition`, COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY `Condition`
        ORDER BY patient_count DESC
        LIMIT 1;
        """

    # ==========================================
    # LONGEST AVERAGE STAY BY CONDITION
    # ==========================================

    if (
        "longest average hospital stay" in question
        or "condition has the longest average stay" in question
        or "longest average stay by condition" in question
        or "condition with the longest stay" in question
    ):
        return """
        SELECT
            `Condition`,
            ROUND(AVG(Length_of_Stay), 2) AS average_stay
        FROM patient_records
        GROUP BY `Condition`
        ORDER BY average_stay DESC
        LIMIT 1;
        """

    # ==========================================
    # GENDER
    # ==========================================

    if (
        "gender" in question
        or "male and female" in question
        or "men and women" in question
        or "which gender" in question
    ):
        return """
        SELECT Gender, COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY Gender
        ORDER BY patient_count DESC;
        """

    # ==========================================
    # READMISSION ANALYSIS
    # ==========================================

    if (
        "readmission" in question
        or "readmitted" in question
    ):
        return """
        SELECT Readmission, COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY Readmission;
        """

    # ==========================================
    # INSURANCE
    # ==========================================

    if (
        "insurance" in question
        or "insurance claim" in question
        or "insurance claims" in question
        or "claimed by insurance" in question
    ):
        return """
        SELECT Insurance_Claimed, COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY Insurance_Claimed;
        """

    # ==========================================
    # LENGTH OF STAY
    # ==========================================

    if (
        "length of stay" in question
        or "average stay" in question
        or "hospital stay" in question
        or "how long do patients stay" in question
    ):
        return """
        SELECT ROUND(AVG(Length_of_Stay), 2) AS average_stay
        FROM patient_records;
        """

    # ==========================================
    # PATIENT OUTCOMES
    # ==========================================

    if (
        "outcome" in question
        or "patient outcomes" in question
        or "patient result" in question
        or "treatment outcome" in question
    ):
        return """
        SELECT Outcome, COUNT(*) AS patient_count
        FROM patient_records
        GROUP BY Outcome
        ORDER BY patient_count DESC;
        """

    # ==========================================
    # SATISFACTION
    # ==========================================

    if (
        "satisfaction" in question
        or "satisfaction score" in question
        or "patient satisfaction" in question
    ):
        return """
        SELECT ROUND(AVG(Satisfaction), 2) AS average_satisfaction
        FROM patient_records;
        """

    # ==========================================
    # UNKNOWN QUESTION
    # ==========================================

    return None