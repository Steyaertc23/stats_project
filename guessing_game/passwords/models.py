from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.

class GGUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

class GGPassword(models.Model):
    user = models.ForeignKey(GGUser, on_delete=models.CASCADE, blank=True)
    pw = models.TextField(validators=[MinLengthValidator(4, "the field must be 4 characters")], max_length=4)

    def __str__(self) -> str:
        return f'{self.pw}'
    
class PasswordGuess(models.Model):
    guess = models.TextField(validators=[MinLengthValidator(4, "the field must be 4 characters")], max_length=4, blank=True)
    password = models.OneToOneField(GGPassword, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.guess}'