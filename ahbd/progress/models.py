from django.db import models

'''The models needed to keep track of students progress will include models for dances, figures and technqiues.
    The Figures Model
    - figure_name = CharField
    - leader_description = TextField
    - follower_description = TextField
    - dance = Reference - Dance
    - level = Reference - Level
'''

class Level(models.Model):
    level_name = models.CharField(max_length=30)
    level_value = models.IntegerField()
    
class Dance(models.Model):
    dance_name = models.CharField(max_length=30)

class Figure(models.Model):
    figure_name = models.CharField(max_length=30)
    leader_description = models.TextField()
    follower_description = models.TextField()
    dance = models.ForeignKey(Dance, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)



