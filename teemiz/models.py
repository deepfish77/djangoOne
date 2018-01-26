from django.db import models

# Create your models here.


class members(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100 , blank=True, default='')
    email = models.EmailField()
    proffession = models.CharField(max_length=100 , blank=True, default='')
    
    
    def abv(self):
        print ("abc")
        
        
class teams(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    team_name = models.CharField(max_length=100 , blank=True, default='')
    team_goal =  models.CharField(max_length=100 , blank=True, default='')
    