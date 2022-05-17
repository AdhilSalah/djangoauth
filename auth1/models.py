
from django.db import models

# Create your models here.

class User_data(models.Model):

    username =  models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    # def authenticateadhil(x,y):  
        
    #     if User_data.objects.filter(name=x): 
            
    #         q = User_data.objects.get(name=x)
    #         if y == q.password:
    #             return True
    #         else:
    #             return False

    #     return False



