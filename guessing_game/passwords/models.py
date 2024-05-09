from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Create your models here.

class GGUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class GGPassword(models.Model):
    user = models.ForeignKey(GGUser, on_delete=models.CASCADE, blank=True)
    pw = models.TextField(validators=[MinLengthValidator(4, "the field must be 4 characters")], max_length=4)

    def __str__(self) -> str:
        return f'{self.password}'
    
class PasswordGuess(models.Model):
    guess = models.TextField(validators=[MinLengthValidator(4, "the field must be 4 characters")], max_length=4, blank=True)
    password = models.OneToOneField(GGPassword, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.guess}'