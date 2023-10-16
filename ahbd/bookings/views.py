from django.shortcuts import render
from datetime import datetime, timedelta
from bookings.models import Lesson

def calendar(request):
    # Render the weekly calendar view
    # Create a list of formatted times for each day
    
    def first_day_of_week(date):
        # Return the first day of the week of the date passed in
        return date + datetime.timedelta(days = -date.weekday())

    def build_calendar_blocks():
        pass

    return render(
        request,
        "bookings/week.html",
        {
            
        }
    )
