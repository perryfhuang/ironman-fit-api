from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Workout(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  type = models.CharField(max_length=100)
  distance = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
  # time = models.PositiveIntegerField(blank=True, null=True)
  time_hours = models.PositiveIntegerField(blank=True, null=True)
  time_minutes = models.PositiveIntegerField(blank=True, null=True)
  time_seconds = models.PositiveIntegerField(blank=True, null=True)

  # currently support 10 exercises to be input per lift!
  exercise_1 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_1_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_1_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_1_reps = models.PositiveIntegerField(blank=True, null=True)

  exercise_2 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_2_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_2_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_2_reps = models.PositiveIntegerField(blank=True, null=True)

  exercise_3 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_3_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_3_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_3_reps = models.PositiveIntegerField(blank=True, null=True)

  exercise_4 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_4_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_4_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_4_reps = models.PositiveIntegerField(blank=True, null=True)

  exercise_5 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_5_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_5_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_5_reps = models.PositiveIntegerField(blank=True, null=True)

  exercise_6 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_6_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_6_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_6_reps = models.PositiveIntegerField(blank=True, null=True)

  exercise_7 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_7_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_7_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_7_reps = models.PositiveIntegerField(blank=True, null=True)

  exercise_8 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_8_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_8_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_8_reps = models.PositiveIntegerField(blank=True, null=True)

  exercise_9 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_9_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_9_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_9_reps = models.PositiveIntegerField(blank=True, null=True)

  exercise_10 = models.CharField(max_length=100, default='', blank=True, null=True)
  exercise_10_weight = models.PositiveIntegerField(blank=True, null=True)
  exercise_10_sets = models.PositiveIntegerField(blank=True, null=True)
  exercise_10_reps = models.PositiveIntegerField(blank=True, null=True)

  caption = models.CharField(max_length=280, blank=True, null=True)
  feeling = models.CharField(max_length=100, blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"Workout type: '{self.type}' for time: {self.time} and distance {self.distance}."

  def as_dict(self):
    """Returns dictionary version of Workout models"""
    return {
        'id': self.id,
        'type': self.type,
        'distance': self.distance,
        'time': self.time,
        'caption': self.caption,
        'feeling': self.feeling,
        'created_at': self.created_at,
        'updated_at': self.updated_at
    }
