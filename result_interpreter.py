import re


def interpret_result(question, result):

    question = question.lower().strip()

    if result is None or len(result) == 0:
        return "No data was found."

    # ==========================================
    # PATIENT PROFILE
    # ==========================================

    patient_match = re.search(
        r"(?:patient|patient id|patient number)\s*(?:id\s*)?(\d+)",
        question
    )

    if patient_match and len(result[0]) >= 15:

        row = result[0]

        admission_date = str(row[5])

        if admission_date == "0000-00-00":
            admission_date = "Not available"

        return (
            f"Patient Profile — ID {row[0]}\n\n"
            f"• Age: {row[1]}\n"
            f"• Gender: {row[2]}\n"
            f"• Condition: {row[3]}\n"
            f"• Medication: {row[4]}\n"
            f"• Admission Date: {admission_date}\n"
            f"• Discharge Date: {row[6]}\n"
            f"• State: {row[7]}\n"
            f"• Year of Admission: {row[8]}\n"
            f"• Length of Stay: {row[9]} days\n"
            f"• Readmission: {row[10]}\n"
            f"• Outcome: {row[11]}\n"
            f"• Satisfaction: {row[12]}\n"
            f"• Insurance Claimed: {row[13]}\n"
            f"• Total Cost: ₹{row[14]:,.2f}"
        )

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

        return (
            f"There are {result[0][0]} patients "
            f"who are over 65 and were readmitted."
        )

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

        return (
            f"The average patient age is "
            f"{result[0][0]} years, "
            f"and the average treatment cost is "
            f"₹{result[0][1]:,.2f}."
        )

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

        return (
            f"There are {result[0][0]} patients in the healthcare dataset, "
            f"and the readmission rate is {result[0][1]:.2f}%."
        )

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

        if (
            "largest" in question
            or "most" in question
            or "highest" in question
        ):

            return (
                f"{result[0][0]} has the highest number "
                f"of patients, with {result[0][1]} patients."
            )

        answer = "Patients by state:\n"

        for row in result:
            answer += f"- {row[0]}: {row[1]} patients\n"

        return answer

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

        return (
            f"There are {result[0][0]} patients "
            f"with a high-priority analytical flag. "
            f"This flag is based on predefined dataset rules "
            f"and is not a medical diagnosis."
        )

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

        return (
            f"There are {result[0][0]} patients "
            f"with a moderate analytical flag. "
            f"This flag is based on predefined dataset rules "
            f"and is not a medical diagnosis."
        )

    # ==========================================
    # NUMBER OF READMITTED PATIENTS
    # ==========================================

    if (
        "how many patients were readmitted" in question
        or "how many patients are readmitted" in question
        or "number of readmitted patients" in question
        or "count of readmitted patients" in question
    ):

        return (
            f"There are {result[0][0]} readmitted patients "
            f"in the healthcare dataset."
        )

    # ==========================================
    # READMISSION RATE
    # ==========================================

    if (
        "readmission rate" in question
        or "rate of readmission" in question
        or "percentage of readmission" in question
        or "percent of patients were readmitted" in question
    ):

        return (
            f"The readmission rate is "
            f"{result[0][0]:.2f}%."
        )

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

        return (
            f"There are {result[0][0]} patients "
            f"in the healthcare dataset."
        )

    # ==========================================
    # AVERAGE AGE
    # ==========================================

    if (
        "average age" in question
        or "mean age" in question
        or "how old" in question
        or "average patient age" in question
    ):

        return (
            f"The average patient age is "
            f"{result[0][0]} years."
        )

    # ==========================================
    # AVERAGE TREATMENT COST
    # ==========================================

    if (
        "average cost" in question
        or "average treatment cost" in question
        or "mean treatment cost" in question
        or "typical treatment cost" in question
    ):

        return (
            f"The average treatment cost is "
            f"₹{result[0][0]:,.2f}."
        )

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

        return (
            f"The highest treatment cost is "
            f"₹{result[0][1]:,.2f}, "
            f"for Patient ID {result[0][0]}."
        )

    # ==========================================
    # HIGHEST AVERAGE COST BY CONDITION
    # ==========================================

    if (
        "highest average cost by condition" in question
        or "condition with highest average cost" in question
        or "most expensive condition on average" in question
    ):

        return (
            f"{result[0][0]} has the highest average treatment cost, "
            f"at ₹{result[0][1]:,.2f}."
        )

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

        return (
            f"The most common condition is "
            f"{result[0][0]}, "
            f"with {result[0][1]} patients."
        )

    # ==========================================
    # LONGEST AVERAGE STAY
    # ==========================================

    if (
        "longest average hospital stay" in question
        or "condition has the longest average stay" in question
        or "longest average stay by condition" in question
        or "condition with the longest stay" in question
    ):

        return (
            f"{result[0][0]} has the longest average hospital stay, "
            f"at {result[0][1]} days."
        )

    # ==========================================
    # GENDER
    # ==========================================

    if (
        "gender" in question
        or "male and female" in question
        or "men and women" in question
        or "which gender" in question
    ):

        answer = "Patients by gender:\n"

        for row in result:
            answer += f"- {row[0]}: {row[1]} patients\n"

        return answer

    # ==========================================
    # READMISSION ANALYSIS
    # ==========================================

    if (
        "readmission" in question
        or "readmitted" in question
    ):

        answer = "Readmission analysis:\n"

        for row in result:
            answer += f"- {row[0]}: {row[1]} patients\n"

        return answer

    # ==========================================
    # INSURANCE
    # ==========================================

    if (
        "insurance" in question
        or "insurance claim" in question
        or "insurance claims" in question
        or "claimed by insurance" in question
    ):

        answer = "Insurance claim analysis:\n"

        for row in result:
            answer += f"- {row[0]}: {row[1]} patients\n"

        return answer

    # ==========================================
    # LENGTH OF STAY
    # ==========================================

    if (
        "length of stay" in question
        or "average stay" in question
        or "hospital stay" in question
        or "how long do patients stay" in question
    ):

        return (
            f"The average hospital stay is "
            f"{result[0][0]} days."
        )

    # ==========================================
    # PATIENT OUTCOMES
    # ==========================================

    if (
        "outcome" in question
        or "patient outcomes" in question
        or "patient result" in question
        or "treatment outcome" in question
    ):

        answer = "Patient outcomes:\n"

        for row in result:
            answer += f"- {row[0]}: {row[1]} patients\n"

        return answer

    # ==========================================
    # SATISFACTION
    # ==========================================

    if (
        "satisfaction" in question
        or "satisfaction score" in question
        or "patient satisfaction" in question
    ):

        return (
            f"The average patient satisfaction score is "
            f"{result[0][0]}."
        )

    # ==========================================
    # UNKNOWN
    # ==========================================

    return f"The query returned {len(result)} result(s)."