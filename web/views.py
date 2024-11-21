from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User , Token ,Expense ,Income
from datetime import datetime

# Create your views here.


@csrf_exempt
def submit_income(request):
    """user submits aa income"""
    #TODO; validate date. user might be fake. token might fake. amount might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user = this_user , amount = request.POST['amount'] ,
    text = request.POST['text'], date = date)
    # print("I'M SUBMIT EXpense")
    print(request.POST)

    return JsonResponse({
        'status' : 'ok'
    }, encoder = JSONEncoder)



@csrf_exempt
def submit_expense(request):
    """user submits aa expense"""
    #TODO; validate date. user might be fake. token might fake. amount might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user = this_user , amount = request.POST['amount'] ,
    text = request.POST['text'], date = date)
    # print("I'M SUBMIT EXpense")
    print(request.POST)

    return JsonResponse({
        'status' : 'ok'
    }, encoder = JSONEncoder)
