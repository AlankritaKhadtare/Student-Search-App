from django.db import models

# Create your models here.

class Student(models.Model):
    First_Year='FE'
    Second_Year='SE'
    Year_In_College_Choices = (
        (First_Year,'First Year'),
        (Second_Year,'Second Year')
    )
    st_roll = models.IntegerField(null=True, blank=True, unique=True)
    st_name = models.CharField(max_length=100, null=True, blank=True)
    st_class = models.CharField(max_length=10, choices=Year_In_College_Choices, default=First_Year)
    st_age = models.IntegerField(null=True, blank=True)
    st_address = models.TextField(null=True, blank=True)
    st_mail = models.EmailField(null=True, blank=True)

    class Meta:
        ordering = ('st_roll',)
    
    def __str__(self):
        return str(self.st_roll)+') '+ self.st_name