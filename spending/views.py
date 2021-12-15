import datetime

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

from spending.forms import SpendingForm
from spending.models import Spending


def index(request):
    if request.method == "POST":
        payer = request.POST.get("payer")
        amount = request.POST.get("amount")
        date = request.POST.get("date")
        description = request.POST.get("description")
        if not date:
            date = datetime.datetime.now()
        spending = Spending(amount=amount, payer=payer, date=date, description=description)
        spending.save()
        return HttpResponse("Платёж принят!")
    else:
        amount = Spending.objects.aggregate(Sum('amount')).get('amount__sum')
        data = {
            'amount': amount,
            'form': SpendingForm()
        }
        return render(request, "spelling/main.html", context=data)


def spending(request, cost):
    date = datetime.datetime.now()
    spending = Spending(amount=cost, payer='Leo', date=date, description='тестовый плаьтёж')
    spending.save()
    return HttpResponse("Платёж принят!")