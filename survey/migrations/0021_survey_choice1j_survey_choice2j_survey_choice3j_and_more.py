# Generated by Django 4.0.4 on 2022-07-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0020_rename_choice1j_survey_bol1a_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='choice1j',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2j',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3j',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4j',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
