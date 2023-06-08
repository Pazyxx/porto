from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/") # <> macht das ganze Dynamisch
def my_home():
      return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
      return render_template(page_name)

def write_to_csv(data):
      if request.method == 'POST':
            data = request.form.to_dict()
            with open('database.csv', mode='a', newline='', encoding='utf-8') as database2:
                  csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                  csv_writer.writerow([data['email'],data['subject'], data['message']])
            return redirect('submit_form.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
      if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('submit_form.html')
      else:
            return 'something went wrong. Try again!'
      
