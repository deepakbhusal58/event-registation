from django.db import models

class PoornimaEventDetail(models.Model):
    salutaion= models.CharField(max_length=5)
    fname= models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    designation=models.CharField(max_length=20)
    corresponding_email=models.EmailField(max_length=250)
    contact=models.CharField(max_length=15,null=True,default=None)
    university_college_name=models.CharField(max_length=50)
    university_college_address=models.CharField(max_length=50)
    university_college_city=models.CharField(max_length=50)

    def __str__(self):
        return self.fname + " "+self.lname