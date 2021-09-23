from flask import Flask
from flask import render_template, request
from datetime import *


app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    return render_template('index.html')


@app.route('/date', methods=['POST'])
def date():
    birthDate = request.form["date"]
    year = datetime.utcnow().year
    ageInMonths = (int(year) - int(birthDate)) * 12
    birthDate = int(birthDate)
    if birthDate > 1:
        if birthDate % 2 == 1 or birthDate == 2:
            prime = "PRIME number"
        else:
            prime = "COMPOSITE number"
    elif birthDate > 0:
        prime = "your age is neither prime nor composite"
    else:
        prime = "You do not appear to exist"
    return render_template('convertPrime.html', formData=birthDate, birthDate=ageInMonths, prime=prime)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
