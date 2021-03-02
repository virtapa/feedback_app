from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

"""class FeedbackTopic(models.Model):
    TOPIC_CHOICES = (
        (1,"Ruoka"), 
        (2,"Palvelu"), 
        (3,"Muu"), 
)
    topic = models.IntegerField(choices=TOPIC_CHOICES, null=True)
    #def __init__(self):
        #return str(self.topic)"""
    
class Feedback(models.Model):
    TOPIC_CHOICES = (
        (1,"Ruoka"), 
        (2,"Palvelu"), 
        (3,"Muu"), 
)  

    GRADE_CHOICES = (
        (1,"1"),
        (1,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
)
    user = models.ForeignKey(User,
        on_delete=models.CASCADE, null=True,
    )
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    topic = models.IntegerField(choices=TOPIC_CHOICES, default='1')
    grade = models.IntegerField(choices=GRADE_CHOICES, default='1')
    good = models.TextField()
    bad = models.TextField()
    ideas = models.TextField()
    date = models.DateTimeField('date sent', auto_now_add=True)
    def __str__(self):
        return str(self.date)