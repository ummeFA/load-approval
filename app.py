import gradio as gr
import pandas as pd
import joblib
def predic_loan(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):
        input_data=pd.DataFrame({"Gender":[Gender], 
                                  "Married":[Married], 
                                  "Dependents":[Dependents], 
                                  "Education":[Education], 
                                  "Self_Employed":[Self_Employed], 
                                  "ApplicantIncome":[ApplicantIncome], 
                                  "CoapplicantIncome":[CoapplicantIncome], 
                                  "LoanAmount":[LoanAmount],
                                  "Loan_Amount_Term":[Loan_Amount_Term], 
                                  "Credit_History":[Credit_History], 
                                  "Property_Area":[Property_Area]
 
                                  })

        input_data["Gender"]=input_data["Gender"].map({"Male":1, "Female":0})
        input_data["Married"]=input_data["Married"].map({"Yes":1, "No":0})
        input_data["Dependents"]=input_data["Dependents"].map({"0":0, "1":1, "2":2, "3+":3})
        input_data["Education"]=input_data["Education"].map({"Graduate":1, "Not Graduate":0})
        input_data["Self_Employed"]=input_data["Self_Employed"].map({"Yes":1, "No":0})
        input_data["Property_Area"]=input_data["Property_Area"].map({"Urban":2, "Semiurban":1, "Rural":0})

        prediction=best_model.predict(input_data)[0]

        return "Approved" if prediction==1 else "Rejected"

app=gr.Interface(
      fn=predic_loan,
      inputs=[
          gr.Dropdown(["Male", "Female"], label="Gender"),
          gr.Dropdown(["Yes", "No"], label="Married"),
          gr.Dropdown(["0", "1", "2", "3+"], label="Dependents"),
          gr.Dropdown(["Graduate", "Not Graduate"], label="Education"),
          gr.Dropdown(["Yes", "No"], label="Self_Employed"),
          gr.Number(label="ApplicantIncome"),
          gr.Number(label="CoapplicantIncome"),
          gr.Number(label="LoanAmount"),
          gr.Number(label="Loan_Amount_Term"),
          gr.Dropdown([1, 0], label="Credit_History"),
          gr.Dropdown(["Urban", "Semiurban", "Rural"], label="Property_Area")
      ],

          outputs="text",
      title="Loan approval prediction system"
  )

app.launch(share=True)