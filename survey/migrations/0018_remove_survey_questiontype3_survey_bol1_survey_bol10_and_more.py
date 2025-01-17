# Generated by Django 4.0.4 on 2022-07-16 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0017_survey_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='questiontype3',
        ),
        migrations.AddField(
            model_name='survey',
            name='bol1',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='bol10',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='bol2',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='bol3',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='bol4',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='bol5',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='bol6',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='bol7',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='bol8',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='bol9',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer1',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer10',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer2',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer3',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer4',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer5',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer6',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer7',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer8',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='answer9',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol1',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol10',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol2',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol3',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol4',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol5',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol6',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol7',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol8',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyanswers',
            name='bol9',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
