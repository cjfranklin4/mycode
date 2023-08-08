from flask import Flask, render_template
import csv
app = Flask(__name__)

#CSV to list of dicitonaries
with open("emails.csv", "r") as emails:
    dict_reader = csv.reader(emails)
    email_list = list(dict_reader)
    print(email_list)

@app.route("/")
def index():
    return render_template("index.html", email_list = email_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)