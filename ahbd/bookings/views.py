from django.shortcuts import render

def calendar(request):
    # Render the weekly calendar view
    return render(
        request,
        "bookings/week.html",
        {
            "foo": "bar",
        }
    )
