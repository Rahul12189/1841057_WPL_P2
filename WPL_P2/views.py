from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello...This is Jayesh Wani From \'T3\' Batch and My PRN is 1841057")
