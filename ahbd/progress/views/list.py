from django.shortcuts import render
from progress.models import Figure


def list(request):
    context = {}
    context["figures"] = Figure.objects.all()
    return render(request, "progress/list.html", context)

def show(request, id):
    figure = Figure.objects.filter(id=id).first()
    return render(request, "progress/show.html", {"figure": figure})