from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Workout(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  type = models.CharField(max_length=100)
  distance = models.DecimalField(max_digits=5, decimal_places=1)
  time = models.DurationField(max_length=100)

  # currently support 10 exercises to be input per lift!
  exercise_1 = models.CharField(max_length=100, default='')
  exercise_1_weight = models.IntegerField()
  exercise_1_sets = models.IntegerField()
  exercise_1_reps = models.IntegerField()

  exercise_2 = models.CharField(max_length=100, default='')
  exercise_2_weight = models.IntegerField()
  exercise_2_sets = models.IntegerField()
  exercise_2_reps = models.IntegerField()

  exercise_3 = models.CharField(max_length=100, default='')
  exercise_3_weight = models.IntegerField()
  exercise_3_sets = models.IntegerField()
  exercise_3_reps = models.IntegerField()

  exercise_4 = models.CharField(max_length=100, default='')
  exercise_4_weight = models.IntegerField()
  exercise_4_sets = models.IntegerField()
  exercise_4_reps = models.IntegerField()

  exercise_5 = models.CharField(max_length=100, default='')
  exercise_5_weight = models.IntegerField()
  exercise_5_sets = models.IntegerField()
  exercise_5_reps = models.IntegerField()

  exercise_6 = models.CharField(max_length=100, default='')
  exercise_6_weight = models.IntegerField()
  exercise_6_sets = models.IntegerField()
  exercise_6_reps = models.IntegerField()

  exercise_7 = models.CharField(max_length=100, default='')
  exercise_7_weight = models.IntegerField()
  exercise_7_sets = models.IntegerField()
  exercise_7_reps = models.IntegerField()

  exercise_8 = models.CharField(max_length=100, default='')
  exercise_8_weight = models.IntegerField()
  exercise_8_sets = models.IntegerField()
  exercise_8_reps = models.IntegerField()

  exercise_9 = models.CharField(max_length=100, default='')
  exercise_9_weight = models.IntegerField()
  exercise_9_sets = models.IntegerField()
  exercise_9_reps = models.IntegerField()

  exercise_10 = models.CharField(max_length=100, default='')
  exercise_10_weight = models.IntegerField()
  exercise_10_sets = models.IntegerField()
  exercise_10reps = models.IntegerField()

  caption = models.CharField(max_length=280)
  feeling = models.CharField(max_length=100)

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
