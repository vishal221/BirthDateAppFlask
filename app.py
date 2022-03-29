from flask import Flask
from flask import render_template, request
from datetime import datetime


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/date', methods=['POST'])
def date():
    birthYear = request.form["year"]
    birthMonth = request.form["month"]
    birthDays = request.form["day"]
    currentYear = datetime.utcnow().year
    ageInMonths = (int(currentYear) - int(birthYear)) * 12
    currentMonth = datetime.utcnow().month
    currentMonth = int(currentMonth)
    birthMonth = int(birthMonth)
    birthDays = int(birthDays)
    currentDay = datetime.utcnow().day
    currentDay = int(currentDay)

    if currentMonth == 4 or 6 or 9 or 11:
        if birthDays - currentDay > 0 and birthDays - currentDay < 30:
            ageInMonths =- 1 + ageInMonths 
        else:
            ageInMonths = ageInMonths
    elif currentMonth == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if birthDays - currentDay > 0 and birthDays - currentDay < 31:
            ageInMonths =- 1 + ageInMonths
        else:
            ageInMonths = ageInMonths
    elif currentMonth == 2:
        if birthDays - currentDay > 0 and birthDays - currentDay < 28:
            ageInMonths =- 1 + ageInMonths
        else:
            ageInMonths = ageInMonths
    elif ((birthYear % 4 == 0) and (birthYear % 100 != 0)) or (birthYear % 400 == 0) and currentMonth == 2:
        if birthDays - currentDay > 0 and birthDays - currentDay < 29:
            ageInMonths =- 1 + ageInMonths
        else:
            ageInMonths = ageInMonths

    totalAgeMonths = (ageInMonths + currentMonth) - birthMonth

    if totalAgeMonths > 1:
        if totalAgeMonths % 2 == 1 or totalAgeMonths == 2:
            prime = "Yes, you are PRIME"
        else:
            prime = "No, you are COMPOSITE"
    elif totalAgeMonths > 0:
        prime = "your age is neither prime nor composite"
    else:
        prime = "You do not appear to exist"

    birthDate = str(birthDays) + '/' + str(birthMonth) + '/' + str(birthYear)

    return render_template('ConvertPrime.html', formData=birthDate, birthDate=totalAgeMonths, prime=prime)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# app is working but this is basic functionality
