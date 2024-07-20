# Generated by Django 5.0.7 on 2024-07-20 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0002_studentprofile_bio_studentprofile_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='cgpa',
            field=models.FloatField(help_text='*required', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
