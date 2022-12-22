Tax_Rate=0.2
Standard_Deduction=10000
Dependent_Deduction=3000
Gross_income=float(input("enter gross income"))
Dependents=int(input("enter no of dependents"))
Taxable_Income=Gross_income-Standard_Deduction-(Dependent_Deduction*Dependents)

if Taxable_Income<0:
    print("no tax payable")
else:
    print("taxable income is:",Taxable_Income*Tax_Rate)

