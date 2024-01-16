from django.http import HttpResponseRedirect
from django.shortcuts import render

from progress.forms.new_figure_form import NewFigureForm

def new_figure(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NewFigureForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewFigureForm()

    return render(request, "progress/new.html", {"form": form})