# Generated by Django 5.0.6 on 2024-05-09 10:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0004_gguser_alter_ggpassword_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordguess',
            name='guess',
            field=models.TextField(blank=True, max_length=4, validators=[django.core.validators.MinLengthValidator(4, 'the field must be 4 characters')]),
        ),
    ]
