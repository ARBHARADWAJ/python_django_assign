# ingest_data.py
import pandas as pd
from reditapp.models import Customer, Loan

customer_data = pd.read_excel("customer_data.xlsx")
loan_data = pd.read_excel("loan_data.xlsx")

for index, row in customer_data.iterrows():
    Customer.objects.create(
        first_name=row['first_name'],
        last_name=row['last_name'],
        phone_number=row['phone_number'],
        monthly_salary=row['monthly_salary'],
        approved_limit=row['approved_limit'],
        current_debt=row['current_debt']
    )

for index, row in loan_data.iterrows():
    Loan.objects.create(
        customer_id=row['customer_id'],
        loan_amount=row['loan_amount'],
        tenure=row['tenure'],
        interest_rate=row['interest_rate'],
        monthly_repayment=row['monthly_repayment'],
        emis_paid_on_time=row['emis_paid_on_time'],
        start_date=row['start_date'],
        end_date=row['end_date']
    )
