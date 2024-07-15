import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("Database connection established")
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to the database:", error)
        return None

def create_table(conn):
    if conn:
        try:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS pa_requests
                         (enrollee_id TEXT, insurance_plan TEXT, diagnosis TEXT, drugs TEXT, investigations TEXT, procedures TEXT, room_and_board TEXT)''')
            conn.commit()
            print("Table created successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error creating table:", error)

def insert_request(conn, request_data):
    if conn:
        try:
            c = conn.cursor()
            c.execute("INSERT INTO pa_requests VALUES (%s, %s, %s, %s, %s, %s, %s)", request_data)
            conn.commit()
            print("Request inserted successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error inserting request:", error)