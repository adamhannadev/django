from django.shortcuts import render
from datetime import datetime, timedelta
from bookings.models import Lesson
import pandas as pd

def calendar(request):
    # Render the weekly calendar view
    # Find the first day of the current week
    # Get a list of all current lessons
    # Create a list of all time blocks for a given day including, time: time, duration: int, booked: boolean
    
    def first_day_of_week(date):
        # Return the first day of the week of the date passed in
        return date + timedelta(days = -date.weekday())
    this_monday = first_day_of_week(datetime.now())

    def build_time_blocks(day):
        # Get all the lessons that occur within the argument passed in as day
        lessons = Lesson.objects.filter(lesson_date__date=day)
        # For each lesson returned create a dictionary with keys 'start', and 'duration'
        time_blocks = []
        for lesson in lessons:
            time_blocks.append({'start': lesson.lesson_date,
                                'lesson_date': lesson.lesson_date, 
                                'duration': lesson.duration, 
                                'booked': 'booked',
                                'student': lesson.student
                                })
        # For each 15 minute block of time between a range of hours
        # If that block falls outside the current list of lessons
        # Add it to the time_blocks dictionary

        def datetime_range(start, end, delta):
            current = start
            while current < end:
                yield current
                current += delta

        dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in 
            datetime_range(pd.Timestamp.now().round('60min').to_pydatetime(), datetime.now() + timedelta(hours=5), 
            timedelta(minutes=15))]


        for hour in dts:
            if hour not in time_blocks:
                time_blocks.append({'start': datetime.strptime(hour, "%Y-%m-%d T%H:%M Z"), 'duration': 15, 'booked': ''})
        return time_blocks

        
    time_blocks = build_time_blocks(datetime.now())
    return render(
        request,
        "bookings/week.html",
        {
            'week': range(7),
            'today': datetime.now().date,
            'time_blocks': sorted(time_blocks, key=lambda x:x['start'])
           
        }
    )











# from django.shortcuts import render
# from datetime import datetime, timedelta
# from bookings.models import Lesson
# import pandas as pd

# def calendar(request):
#     # Render the weekly calendar view
#     # Find the first day of the current week
#     # Get a list of all current lessons
#     # Create a list of all time blocks for a given day including, time: time, duration: int, booked: boolean
    
#     def first_day_of_week(date):
#         # Return the first day of the week of the date passed in
#         return date + datetime.timedelta(days = -date.weekday())

#     def build_time_blocks(day):
#         # Get all the lessons that occur within the argument passed in as day
#         lessons = Lesson.objects.filter(lesson_date__date=day)
#         # For each lesson returned create a dictionary with keys 'start', and 'duration'
#         time_blocks = []
#         for lesson in lessons:
#             time_blocks.append({'start': lesson.lesson_date.hour,
#                                 'lesson_date': lesson.lesson_date, 
#                                 'duration': lesson.duration, 
#                                 'booked': 'booked',
#                                 'student': lesson.student
#                                 })
#         # For each 15 minute block of time between a range of hours
#         # If that block falls outside the current list of lessons
#         # Add it to the time_blocks dictionary

#         def datetime_range(start, end, delta):
#             current = start
#             while current < end:
#                 yield current
#                 current += delta

#         dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in 
#             datetime_range(pd.Timestamp.now().round('60min').to_pydatetime(), datetime.now() + timedelta(hours=5), 
#             timedelta(minutes=15))]


#         for hour in dts:
#             if hour not in time_blocks:
#                 time_blocks.append({'start': datetime.strptime(hour, "%Y-%m-%d T%H:%M Z"), 'duration': 15, 'booked': ''})
#         return time_blocks

        
#     time_blocks = build_time_blocks(datetime.now())
#     return render(
#         request,
#         "bookings/week.html",
#         {
#             'week': range(7),
#             'today': datetime.now().date,
#             #'time_blocks': sorted(time_blocks, key=lambda x:x['start'])
#              'time_blocks': time_blocks
#         }
#     )
