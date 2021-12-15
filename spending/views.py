import datetime

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

from spending.models import Spending


def index(request):
    amount = Spending.objects.aggregate(Sum('amount')).get('amount__sum')
    print(not amount)
    if not amount:
        amount = 666
    data = {
        'amount': amount
    }

    return render(request, "spelling/main.html", context=data)


def spending(request, cost):
    date = datetime.datetime.now()
    spending = Spending(amount=cost, payer='Leo', date=date, description='тестовый плаьтёж')
    spending.save()
    return HttpResponse("Платёж принят!")