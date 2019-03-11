import csv
import json
from flask import Flask, request, render_template
app = Flask(__name__)


def get_data():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = -1
        data = []
        for row in csv_reader:
            data.append(row)
        print(data)
        return data

@app.route('/')
def main():
    return render_template(
                           "index.html",
                           data=data,
                           size=len(data))

if __name__ == '__main__':
    data = get_data()
    app.secret_key = 'some_data'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
