# Generated by Django 4.0.4 on 2022-07-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_survey_category_survey_description_survey_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='choice1',
            new_name='choice1a',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='choice2',
            new_name='choice2a',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='choice3',
            new_name='choice3a',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='question',
            new_name='question1',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='questiontype',
            new_name='questiontype1',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='choice4',
        ),
        migrations.AddField(
            model_name='survey',
            name='choice1b',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice1c',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice1d',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice1e',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice1f',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice1g',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice1h',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice1i',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice1j',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2b',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2c',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2d',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2e',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2f',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2g',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2h',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2i',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice2j',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3b',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3c',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3d',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3e',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3f',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3g',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3h',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3i',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice3j',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4a',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4b',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4c',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4d',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4e',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4f',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4g',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4h',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4i',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='choice4j',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='survey',
            name='question10',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='survey',
            name='question3',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='survey',
            name='question4',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='survey',
            name='question5',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='survey',
            name='question6',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='survey',
            name='question7',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='survey',
            name='question8',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='survey',
            name='question9',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='survey',
            name='questiontype10',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='questiontype2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='questiontype3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='questiontype4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='questiontype5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='questiontype6',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='questiontype7',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='questiontype8',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='questiontype9',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]