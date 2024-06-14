from flask import Flask, request, render_template, redirect
import csv
import os

app = Flask(__name__)

data_dir = os.path.join(app.root_path, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

csv_file_path = os.path.join(data_dir, 'submissions.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'CGPA': request.form.get('CGPA'),
        'Courses_Completed': request.form.get('Courses_Completed'),
        'Preferred_Field': request.form.get('Preferred_Field'),
        'Learning_Style': request.form.get('Learning_Style'),
        'DSA_Marks': request.form.get('DSA_Marks'),
        'DBMS_Marks': request.form.get('DBMS_Marks'),
        'ML_Marks': request.form.get('ML_Marks'),
        'Microcontroller_Marks': request.form.get('Microcontroller_Marks')
    }

    try:
        os.remove(csv_file_path)
    except FileNotFoundError:
        pass  

    fieldnames = list(data.keys())
    try:
        with open(csv_file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  
            writer.writerow(data)
    except Exception as e:
        print(f"Error writing to CSV file: {e}")
        return redirect('/')

    # Redirect to the dashboard page
    return redirect('http://127.0.0.1:5500/FlexStart/dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)