from ai_sql_generator import generate_ai_sql
from sql_validator import validate_sql
from database import run_query
from result_interpreter import interpret_result


def run_agent(question):

    print("\n" + "=" * 50)
    print("OPTUM CARE INTELLIGENCE AGENT")
    print("=" * 50)

    print("\nUser Question:")
    print(question)

    # --------------------------------------------------
    # STEP 1: Generate SQL
    # --------------------------------------------------

    sql = generate_ai_sql(question)

    if sql is None:

        return "I don't know how to answer that question yet."

    print("\nGenerated SQL:")
    print(sql)

    # --------------------------------------------------
    # STEP 2: Validate SQL
    # --------------------------------------------------

    safe, message = validate_sql(sql)

    print("\nSQL Security Check:")
    print(message)

    if not safe:

        return "The query was blocked for security reasons."

    # --------------------------------------------------
    # STEP 3: Execute SQL
    # --------------------------------------------------

    try:

        results = run_query(sql)

    except Exception as error:

        return f"Database error: {error}"

    print("\nDatabase Result:")
    print(results)

    # --------------------------------------------------
    # STEP 4: Interpret Result
    # --------------------------------------------------

    answer = interpret_result(question, results)

    return answer


# --------------------------------------------------
# TEST THE AGENT
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("       OPTUM CARE INTELLIGENCE")
    print("=" * 50)

    while True:

        question = input(
            "\nAsk a healthcare analytics question: "
        )

        if question.lower().strip() in ["exit", "quit"]:

            print("\nAgent stopped.")

            break

        answer = run_agent(question)

        print("\n🤖 Agent:")
        print(answer)