import os
from flask import Flask, request, render_template, url_for
from db import create_connection, create_table, insert_request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        enrollee_id = request.form['enrollee_id']
        insurance_plan = request.form['insurance_plan']
        diagnosis = request.form['diagnosis']
        drugs = request.form['drugs']
        investigations = request.form['investigations']
        procedures = request.form['procedures']
        room_and_board = request.form['room_and_board']
        
        conn = create_connection()
        if conn:
            create_table(conn)
            request_data = (enrollee_id, insurance_plan, diagnosis, drugs, investigations, procedures, room_and_board)
            insert_request(conn, request_data)
            conn.close()
        
        # Process the request
        # ...
        # Render the result page
        return render_template('result.html', enrollee_id=enrollee_id, insurance_plan=insurance_plan, diagnosis=diagnosis, drugs=drugs, investigations=investigations, procedures=procedures, room_and_board=room_and_board)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)