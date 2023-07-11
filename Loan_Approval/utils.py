#utility file
import json
import pickle
import numpy as np
import pandas as  pd


with open('ft_cols.json', 'r') as I:
    ftrs = json.load(I) ['features']

with open('Loan_apprvl_prjt.pickle','rb')as I:
    logistic_model = pickle.load(I)


def get_data_colmns():
    return {'Features' : ftrs}
 

def predict_loan_status(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):
   # with open('Loan_apprvl_prjt', 'rb') as file:
       # logistic_model = pickle.load(file)

    input_val = np.zeros(len(logistic_model.coef_[0]))

    # Set the values for the encoded categorical columns
    input_val[0] = Gender
    input_val[1] = Married
    input_val[2] = Dependents
    input_val[3] = Education
    input_val[4] = Self_Employed

    # Set the values for the numerical columns
    input_val[5] = ApplicantIncome
    input_val[6] = CoapplicantIncome
    input_val[7] = LoanAmount
    input_val[8] = Loan_Amount_Term
    input_val[9] = Credit_History
    input_val[10] = Property_Area

    # Make the prediction
    prediction = logistic_model.predict([input_val])

    # Return the predicted loan status
    return prediction[0]
#predicted_status = predict_loan_status(1,1,3,0,0,136,174,111,9,0,1)
#predicted_status
#print("Predicted Loan Status:", predicted_status)
