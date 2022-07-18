# Generated by Django 4.0.4 on 2022-07-15 23:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_alter_survey_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, size=[250, 200], upload_to='images/'),
        ),
    ]
