import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="bisag",
        password="pmis",
        database="pmis"
    )

def fetch_user_details(user_name):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Get basic user details and internship counts
    query = """
    SELECT 
        ud.name, 
        COUNT(DISTINCT ui.internship_id) AS total_internships,
        COUNT(DISTINCT id.company_name) AS total_companies,
        GROUP_CONCAT(DISTINCT id.company_name SEPARATOR ', ') AS company_list,
        GROUP_CONCAT(DISTINCT CASE WHEN ui.status = 'yes' THEN id.company_name END SEPARATOR ', ') AS selected,
        GROUP_CONCAT(DISTINCT CASE WHEN ui.status = 'no' THEN id.company_name END SEPARATOR ', ') AS rejected
    FROM pmis.user_details ud
    JOIN pmis.user_internship ui ON ud.user_name = ui.user_name
    JOIN pmis.internship_details id ON ui.internship_id = id.internship_id
    WHERE ud.user_name = %s
    GROUP BY ud.name
    """
    
    cursor.execute(query, (user_name,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return result