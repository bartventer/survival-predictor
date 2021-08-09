from django.shortcuts import redirect, render
from . import ml_predict
from .forms import TitanicForm

def home(request):
    form = TitanicForm()
    return render(request, 'index.html',{"form":form})

def result(request):
    form = TitanicForm(request.POST)
    if form.is_valid():
        form = form.cleaned_data
        pclass = int(form['pclass'])
        sex = int(form['sex'])
        age = int(form['age'])
        sibsp = int(form['sibsp'])
        parch = int(form['parch'])
        fare = int(form['fare'])
        embarked = int(form['embarked'])
        title = int(form['title'])
        prediction = ml_predict.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
        return render(request, 'result.html', {'prediction':prediction})
    return redirect('home')
    