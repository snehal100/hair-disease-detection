from django.shortcuts import render

from django.http import HttpResponse

def userhome(request):
    return HttpResponse("Welcome to the Accounts app!")  # Replace with your logic
