from django.shortcuts import render
from datetime import datetime, timedelta
from bookings.models import Lesson

def calendar(request):
    # Render the weekly calendar view
    # Find the first day of the current week
    # Get a list of all current lessons
    # Create a list of all time blocks for a each day including, time: time, duration: int, booked: boolean
    
    def first_day_of_week(date):
        # Return the first day of the week of the date passed in
        return date - timedelta(days=date.isoweekday() % 7)

    def build_time_blocks(day):
        # Get all the lessons that occur within the argument passed in as day
        lessons = Lesson.objects.filter(lesson_date__date=day)
        # For each lesson returned create a dictionary with keys 'start', and 'duration'
        time_blocks = []
        for lesson in lessons:
            time_blocks.append({
                                'lesson_date': lesson.lesson_date, 
                                'duration': lesson.duration, 
                                'booked': 'booked',
                                'student': lesson.student
                                })
            
        # For each 15 minute block of time between a range of hours
        # If that block falls outside the currently booked list of lessons
        # Add it to the time_blocks dictionary and return it

        def datetime_range(start, end, delta):
            current = start
            while current < end:
                yield current
                current += delta

        def hour_rounder(t):
            # Rounds to nearest hour by adding a timedelta hour if minute >= 30
            return t.replace(second=0, microsecond=0, minute=0, hour=t.hour)


        dts = [dt for dt in 
            datetime_range(hour_rounder(day) - timedelta(hours=8), day + timedelta(hours=5), 
            timedelta(minutes=15))]

        booked_times = []
        
        for l in lessons:
            for time in dts:
                if time >= l.lesson_date and time < l.lesson_date + timedelta(minutes=l.duration):
                    booked_times.append(time)
            
        free_times = list(filter(lambda t: t not in booked_times, dts))

        for time in free_times:
            time_blocks.append({'lesson_date': time, 'duration': 15, 'booked': ''})

        return  sorted(time_blocks, key=lambda x:x['lesson_date'])

    week_dates = [first_day_of_week(datetime.now()) + timedelta(days=x) for x in range(7)]
    week_days = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    this_week = []

    for num in range(7):
        this_week.append({
                          'day': week_days[num],
                          'week_date': week_dates[num],
                          'blocks': build_time_blocks(week_dates[num])
                          })
        

    time_blocks = build_time_blocks(datetime.now())
    return render(
        request,
        "bookings/week.html",
        {
            'today': datetime.now().date,
            'time_blocks': time_blocks,
            'day_numbers': range(7),
            'week': this_week
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
