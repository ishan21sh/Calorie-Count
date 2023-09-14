from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'index.html')


def cals(request):
    return render(request,'calorieCalc.html')


def exercise(request):
    return render(request,'exercise.html')


def ingredient(request):
    return render(request,'ingredientParser.html')


def recepies(request):

    return render(request,'recipes.html')

def addfoods(request):
    return render(request,'addFood.html')