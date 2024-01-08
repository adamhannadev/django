from django.shortcuts import render
from progress.models import Figure


def list(request):
    context = {}
    context["figures"] = Figure.objects.all()
    return render(request, "progress/list.html", context)
