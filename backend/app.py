from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Database connection
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=35.243.252.245;DATABASE=myappdb;UID=sqlserver;PWD=Haj@1600')
cursor = conn.cursor()

@app.route('/api/submit', methods=['POST'])
def submit():
    # Get form-data values
    value1 = request.form.get('value1')
    value2 = request.form.get('value2')

    # Insert into the database
    cursor.execute("INSERT INTO Data (value1, value2) VALUES (?, ?)", value1, value2)
    conn.commit()

    return jsonify({"message": "Data submitted successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

