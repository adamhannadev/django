from django.shortcuts import render
from datetime import datetime

def calendar(request):
    # Render the weekly calendar view
    times = []
    for t in range(6,21):
        formatted_time = datetime.strptime(f"{t}:00","%H:%M")
        times.append(formatted_time.strftime("%I:%M %p"))

    return render(
        request,
        "bookings/week.html",
        {
            "times": times,
            "week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        }
    )
