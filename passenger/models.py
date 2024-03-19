from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

pass_user= get_user_model()
class PassRegister(models.Model):
    pass_user= models.OneToOneField(pass_user,
                               related_name="passenger",
                               on_delete=models.CASCADE)
    fullname=models.CharField(max_length=30)
    dateOfBirth=models.DateField()
    phoneNumber=models.CharField(max_length=50)


    def __str__(self) -> str:
        return f"{self.pass_user.username}"


