from django.shortcuts import render
from datetime import datetime, timedelta
from bookings.models import Lesson

def calendar(request):
    # Render the weekly calendar view
    # Find the first day of the current week
    # Get a list of all current lessons
    # Create a list of all time blocks for a given day including, time: time, duration: int, booked: boolean
    
    def first_day_of_week(date):
        # Return the first day of the week of the date passed in
        return date + datetime.timedelta(days = -date.weekday())

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
        # If that block falls outside the current list of lessons
        # Add it to the time_blocks dictionary

        def datetime_range(start, end, delta):
            current = start
            while current < end:
                yield current
                current += delta

        def hour_rounder(t):
            # Rounds to nearest hour by adding a timedelta hour if minute >= 30
            return t.replace(second=0, microsecond=0, minute=0, hour=t.hour)


        dts = [dt for dt in 
            datetime_range(hour_rounder(datetime.now()) - timedelta(hours=8), datetime.now() + timedelta(hours=5), 
            timedelta(minutes=15))]

        booked_times = []
        
        for l in lessons:
            for time in dts:
                if time > l.lesson_date and time < l.lesson_date + timedelta(minutes=l.duration):
                    booked_times.append(time)
            
        free_times = filter(lambda t: t not in booked_times, dts)

        return list(free_times)

        
    time_blocks = build_time_blocks(datetime.now())
    return render(
        request,
        "bookings/week.html",
        {
            'week': range(7),
            'today': datetime.now().date,
            'time_blocks': time_blocks
            # 'time_blocks': sorted(time_blocks, key=lambda x:x['start'])
        }
    )


# from django.shortcuts import render
# from datetime import datetime, timedelta, time
# from bookings.models import Lesson
# import pandas as pd

# def calendar(request):
#     # Render the weekly calendar view
#     # Find the first day of the current week
#     # Get a list of all current lessons
#     # Create a list of all time blocks for a given day including, time: time, duration: int, booked: boolean
#     lessons = Lesson.objects.filter(lesson_date__date=datetime.now())
#     def first_day_of_week(date):
#         # Return the first day of the week of the date passed in
#         return date + timedelta(days = -date.weekday())
#     this_monday = first_day_of_week(datetime.now())

#     def build_time_blocks(day):
#         # Get all the lessons that occur within the argument passed in as day
#         # For each lesson returned create a dictionary with keys 'start', and 'duration'
#         time_blocks = []
#         # for lesson in lessons:
#         #     time_blocks.append({
#         #                         'lesson_date': lesson.lesson_date, 
#         #                         'duration': lesson.duration, 
#         #                         'booked': 'booked',
#         #                         'student': lesson.student
#         #                         })
#         # For each 15 minute block of time between a range of hours
#         # If that block falls outside the current list of lessons
#         # Add it to the time_blocks dictionary

#         def datetime_range(start, end, delta):
#             current = start
#             while current < end:
#                 yield current
#                 current += delta

#         dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in 
#             datetime_range(datetime.now().replace(hour=6, minute=0), datetime.now() + timedelta(hours=5), 
#             timedelta(minutes=15))]

#         for time_block in dts:
#             time_blocks.append({'lesson_date': datetime.strptime(time_block, "%Y-%m-%d T%H:%M Z"), 'duration': 15, 'booked': ''})
#         return time_blocks
        
#     blocks = build_time_blocks(datetime.now())

#     def check_not_booked(time_block):
#         if time_block['lesson_date'] < l.lesson_date:
#             return True
    
#     for l in lessons:
#         time_blocks = filter(check_not_booked, blocks)

#     return render(
#         request,
#         "bookings/week.html",
#         {
#             'week': range(7),
#             'today': datetime.now().date,
#             'time_blocks': sorted(time_blocks, key=lambda x:x['lesson_date'])
           
#         }
#     )











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
