from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Workout(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  type = models.CharField(max_length=100)
  distance = models.DecimalField(max_digits=5, decimal_places=1)
  time = models.DurationField(max_length=100)
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
