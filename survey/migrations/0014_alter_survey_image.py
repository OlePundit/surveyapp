# Generated by Django 4.0.4 on 2022-07-15 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_alter_survey_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]