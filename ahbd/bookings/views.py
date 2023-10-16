from django.shortcuts import render
from datetime import datetime, timedelta
import pandas as pd
from bookings.models import Lesson

def calendar(request):
    # Render the weekly calendar view
    # Create a list of formatted times for each day
    times = []
    for t in range(6,21):
        formatted_time = datetime.strptime(f"{t}:00","%H:%M")
        times.append(formatted_time.strftime("%I:%M %p"))

    lessons = Lesson.objects.all()
    lesson_times = map(return_formatted_time, lessons)
    formatted_dates = map(return_formatted_time, datelist)
    
    def build_calendar_blocks(lessons, formatted_dates):
        blocks = {}
        blocks['Monday': {
            lessons[::1]
        }]
        return blocks

    return render(
        request,
        "bookings/week.html",
        {
            "days": datelist,
            "lessons": lessons,
            "times": times,
            "lesson_times": list(lesson_times),
            "week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        }
    )
