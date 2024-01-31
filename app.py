from flask import Flask,render_template,redirect,url_for
import csv, db_operations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    #csv_to_db()
    db = db_operations.db_operations()
    fact = db.fetch_fact()
    return render_template('index.html', data = fact)

def csv_to_db():
    path = r'D:\Self_learning\practice_projects\output\facts.csv'
    data =[]
    with open(path,'r',encoding='utf-8') as path:
        #create reader object
        reader = csv.reader(path)
        for row in reader:
            data.append(row)
    db = db_operations.db_operations()
    db.insert_data(data)




if __name__ == '__main__':
    app.run(debug=True)