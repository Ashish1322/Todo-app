from django.db import models

# Status Choices
status_choices = ( 
    ("1","Done"),
    ("2","Pending"),
) 
  
# Create your models here.
class Tasks(models.Model):
    sno = models.AutoField(primary_key=True)
    data = models.TextField(default="")
    status = models.CharField(max_length=20,choices=status_choices,default="2")
    user = models.CharField(default="",max_length=50)
    def __str__(self):
        return self.data[0:10]
    