import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="optum_healthcare"
    )


def run_query(query):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


if __name__ == "__main__":

    query = """
    SELECT COUNT(*)
    FROM patient_records
    """

    result = run_query(query)

    print("Total patient records:", result[0][0])