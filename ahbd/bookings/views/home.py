from datetime import datetime
from django.shortcuts import render

def home(request):
    return render(
        request,
        "bookings/week.html",
        {
            'today': datetime.now().date,

        }
    )


