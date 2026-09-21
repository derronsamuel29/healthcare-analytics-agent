def validate_sql(query):

    query = query.strip().lower()

    blocked_commands = [
        "insert ",
        "update ",
        "delete ",
        "drop ",
        "alter ",
        "truncate ",
        "create ",
        "replace ",
        "grant ",
        "revoke "
    ]

    # Only SELECT queries are allowed
    if not query.startswith("select"):
        return False, "Only SELECT queries are allowed."

    # Check for dangerous commands
    for command in blocked_commands:

        if command in query:
            return False, f"Blocked SQL command detected: {command.strip()}"

    return True, "SQL query is safe."


# Test the validator
if __name__ == "__main__":

    test_queries = [
        "SELECT COUNT(*) FROM patient_records;",
        "SELECT AVG(Age) FROM patient_records;",
        "DELETE FROM patient_records;",
        "DROP TABLE patient_records;"
    ]

    for query in test_queries:

        safe, message = validate_sql(query)

        print("\nQuery:", query)
        print("Safe:", safe)
        print("Message:", message)