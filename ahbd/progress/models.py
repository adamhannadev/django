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
    def __str__(self):
        return self.level_name
    
class Dance(models.Model):
    dance_name = models.CharField(max_length=30)
    def __str__(self):
        return self.dance_name

class Figure(models.Model):
    figure_name = models.CharField(max_length=30)
    element = models.CharField(max_length=30)
    leader_description = models.TextField()
    follower_description = models.TextField()
    dance = models.ForeignKey(Dance, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    def __str__(self):
        return self.figure_name



