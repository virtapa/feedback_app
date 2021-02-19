from django.db import models

# Create your models here.



class Feedback(models.Model):
    CHOICES = ( 
    (1,"Ruoka"), 
    (2,"Palvelu"), 
    (3,"Muu"), 
)
    topic = models.IntegerField(choices=CHOICES, default='1')
    grade = models.IntegerField()
    good = models.TextField()
    bad = models.TextField()
    ideas = models.TextField()
    date = models.DateTimeField('date sent', auto_now_add=True)
    def __str__(self):
        return str(self.date)
                                
