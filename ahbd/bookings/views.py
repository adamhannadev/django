from django.shortcuts import render
from datetime import datetime
from bookings.models import Lesson

def calendar(request):
    # Render the weekly calendar view
    times = []
    for t in range(6,21):
        formatted_time = datetime.strptime(f"{t}:00","%H:%M")
        times.append(formatted_time.strftime("%I:%M %p"))
    def return_formatted_time(lesson):
        return lesson.lesson_date.strftime("%I:%M %p")
    lessons = Lesson.objects.all()
    lesson_times = map(return_formatted_time, lessons)
    return render(
        request,
        "bookings/week.html",
        {
            "times": times,
            "lessons": list(lesson_times),
            "week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        }
    )
