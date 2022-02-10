from flask import Flask, render_template, url_for, request, redirect
import csv


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        name = data["name"]
        phone = data["phone"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,phone,message])



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    if request.method == "POST":
        # try:
            # global data
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        # except:
        #     return 'did not save to database'
    else:
        return "something went wrong. Try agian!"