# Generated by Django 4.0.4 on 2022-09-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyimages',
            name='color',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='studyimages',
            name='highlight',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
