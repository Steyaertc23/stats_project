from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.

class GuessPasswordModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pw = models.TextField(validators=[MinLengthValidator(4, "the field must be 4 characters")], max_length=4)

    def __str__(self) -> str:
        return f'{self.pw}'
    
class PasswordGuess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    guess = models.TextField(validators=[MinLengthValidator(4, "the field must be 4 characters")], max_length=4, default="0000")

    def __str__(self) -> str:
        return f'{self.guess}'