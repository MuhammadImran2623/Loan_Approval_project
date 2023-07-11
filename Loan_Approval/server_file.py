from flask import Flask, request,jsonify
from flask_cors import CORS  # Import CORS module
from flask import render_template


import utils

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/web')
def web():
    return render_template('web.html')

@app.route('/get_columns')
def get_columns():
    response = utils.get_data_colmns()
    return response

@app.route('/loan_status', methods=['POST'])
def loan_status():
    # Retrieve form data from the request
    #data = request.get_json()
    Gender = request.form['Gdr']
    Married = request.form['Mrd']
    Dependents = request.form['dpnts']
    Education = request.form['Edc']
    Self_Employed = request.form['SE']
    ApplicantIncome = request.form['Apinc']
    CoapplicantIncome = request.form['Coapinc']
    LoanAmount = request.form['LAmnt']
    Loan_Amount_Term = request.form['LAT']
    Credit_History = request.form['CrHtry']
    Property_Area = request.form['PprAr']

    # Make the loan status prediction
    status = utils.predict_loan_status(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
                                       CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)[0]


    response = jsonify({"loan_status" : status })
    #response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
  app.run()
