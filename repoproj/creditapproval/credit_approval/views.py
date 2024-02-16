from django.shortcuts import render

# Create your views here.
# credit_approval/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Loan
from .serializers import CustomerSerializer, LoanSerializer

@api_view(['POST'])
def register_customer(request):
    # Implementation for /register endpoint
    pass

@api_view(['POST'])
def check_eligibility(request):
    # Implementation for /check-eligibility endpoint
    pass

@api_view(['POST'])
def create_loan(request):
    # Implementation for /create-loan endpoint
    pass

@api_view(['GET'])
def view_loan(request, loan_id):
    # Implementation for /view-loan/loan_id endpoint
    pass

@api_view(['GET'])
def view_loans_by_customer(request, customer_id):
    # Implementation for /view-loans/customer_id endpoint
    pass
