from django.db import models
from datetime import datetime


# Create your models here.
class Survey(models.Model):
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    location = models.CharField(max_length=10000)
    image = models.ImageField (upload_to='images/')
    created_at = models.DateTimeField(default=datetime.now)
    question1 = models.CharField(max_length=10000)
    questiontype1 = models.CharField(max_length=100)
    choice1a = models.CharField(max_length=5000, blank = True)
    choice2a = models.CharField(max_length=5000, blank = True)
    choice3a = models.CharField(max_length=5000, blank = True)
    choice4a = models.CharField(max_length=5000, blank = True)
    question2 = models.CharField(max_length=10000)
    questiontype2 = models.CharField(max_length=100)
    choice1b = models.CharField(max_length=5000, blank = True)
    choice2b = models.CharField(max_length=5000, blank = True)
    choice3b = models.CharField(max_length=5000, blank = True)
    choice4b = models.CharField(max_length=5000, blank = True)
    question3 = models.CharField(max_length=10000)
    questiontype3 = models.CharField(max_length=100)
    choice1c = models.CharField(max_length=5000, blank = True)
    choice2c = models.CharField(max_length=5000, blank = True)
    choice3c = models.CharField(max_length=5000, blank = True)
    choice4c = models.CharField(max_length=5000, blank = True)
    question4 = models.CharField(max_length=10000)
    questiontype4 = models.CharField(max_length=100)
    choice1d = models.CharField(max_length=5000, blank = True)
    choice2d = models.CharField(max_length=5000, blank = True)
    choice3d = models.CharField(max_length=5000, blank = True)
    choice4d = models.CharField(max_length=5000, blank = True)
    question5 = models.CharField(max_length=10000)
    questiontype5 = models.CharField(max_length=100)
    choice1e = models.CharField(max_length=5000, blank = True)
    choice2e = models.CharField(max_length=5000, blank = True)
    choice3e = models.CharField(max_length=5000, blank = True)
    choice4e = models.CharField(max_length=5000, blank = True)
    question6 = models.CharField(max_length=10000, blank = True)
    questiontype6 = models.CharField(max_length=100, blank = True)
    choice1f = models.CharField(max_length=5000, blank = True)
    choice2f = models.CharField(max_length=5000, blank = True)
    choice3f = models.CharField(max_length=5000, blank = True)
    choice4f = models.CharField(max_length=5000, blank = True)
    question7 = models.CharField(max_length=10000, blank = True)
    questiontype7 = models.CharField(max_length=100, blank = True)
    choice1g = models.CharField(max_length=5000, blank = True)
    choice2g = models.CharField(max_length=5000, blank = True)
    choice3g = models.CharField(max_length=5000, blank = True)
    choice4g = models.CharField(max_length=5000, blank = True)
    question8 = models.CharField(max_length=10000, blank = True)
    questiontype8 = models.CharField(max_length=100, blank = True)
    choice1h = models.CharField(max_length=5000, blank = True)
    choice2h = models.CharField(max_length=5000, blank = True)
    choice3h = models.CharField(max_length=5000, blank = True)
    choice4h = models.CharField(max_length=5000, blank = True)
    question9 = models.CharField(max_length=10000, blank = True)
    questiontype9 = models.CharField(max_length=100, blank = True)
    choice1i = models.CharField(max_length=5000, blank = True)
    choice2i = models.CharField(max_length=5000, blank = True)
    choice3i = models.CharField(max_length=5000, blank = True)
    choice4i = models.CharField(max_length=5000, blank = True)
    question10 = models.CharField(max_length=10000, blank = True)
    questiontype10 = models.CharField(max_length=100, blank = True)
    choice1j = models.CharField(max_length=5000, blank = True)
    choice2j = models.CharField(max_length=5000, blank = True)
    choice3j = models.CharField(max_length=5000, blank = True)
    choice4j = models.CharField(max_length=5000, blank = True)

    bol1a = models.CharField(max_length=5000, blank = True)
    bol2a = models.CharField(max_length=5000, blank = True)
    bol3a = models.CharField(max_length=5000, blank = True)
    bol4a = models.CharField(max_length=5000, blank = True)
    bol1b = models.CharField(max_length=5000, blank = True)
    bol2b = models.CharField(max_length=5000, blank = True)
    bol3b = models.CharField(max_length=5000, blank = True)
    bol4b = models.CharField(max_length=5000, blank = True)
    bol1c = models.CharField(max_length=5000, blank = True)
    bol2c = models.CharField(max_length=5000, blank = True)
    bol3c = models.CharField(max_length=5000, blank = True)
    bol4c = models.CharField(max_length=5000, blank = True)
    bol1d = models.CharField(max_length=5000, blank = True)
    bol2d = models.CharField(max_length=5000, blank = True)
    bol3d = models.CharField(max_length=5000, blank = True)
    bol4d = models.CharField(max_length=5000, blank = True)
    bol1e = models.CharField(max_length=5000, blank = True)
    bol2e = models.CharField(max_length=5000, blank = True)
    bol3e = models.CharField(max_length=5000, blank = True)
    bol4e = models.CharField(max_length=5000, blank = True)
    bol1f = models.CharField(max_length=5000, blank = True)
    bol2f = models.CharField(max_length=5000, blank = True)
    bol3f = models.CharField(max_length=5000, blank = True)
    bol4f = models.CharField(max_length=5000, blank = True)
    bol1g = models.CharField(max_length=5000, blank = True)
    bol2g = models.CharField(max_length=5000, blank = True)
    bol3g = models.CharField(max_length=5000, blank = True)
    bol4g = models.CharField(max_length=5000, blank = True)
    bol1h = models.CharField(max_length=5000, blank = True)
    bol2h = models.CharField(max_length=5000, blank = True)
    bol3h = models.CharField(max_length=5000, blank = True)
    bol4h = models.CharField(max_length=5000, blank = True)
    bol1i = models.CharField(max_length=5000, blank = True)
    bol2i = models.CharField(max_length=5000, blank = True)
    bol3i = models.CharField(max_length=5000, blank = True)
    bol4i = models.CharField(max_length=5000, blank = True)
    bol1j = models.CharField(max_length=5000, blank = True)
    bol2j = models.CharField(max_length=5000, blank = True)
    bol3j = models.CharField(max_length=5000, blank = True)
    bol4j = models.CharField(max_length=5000, blank = True)

class Surveyanswers(models.Model):
    question1 = models.CharField(max_length=10000, blank = True)
    choice1a = models.CharField(max_length=5000, blank = True)
    choice2a = models.CharField(max_length=5000, blank = True)
    choice3a = models.CharField(max_length=5000, blank = True)
    choice4a = models.CharField(max_length=5000, blank = True)
    question2 = models.CharField(max_length=10000, blank = True)
    choice1b = models.CharField(max_length=5000, blank = True)
    choice2b = models.CharField(max_length=5000, blank = True)
    choice3b = models.CharField(max_length=5000, blank = True)
    choice4b = models.CharField(max_length=5000, blank = True)
    question3 = models.CharField(max_length=10000, blank = True)
    choice1c = models.CharField(max_length=5000, blank = True)
    choice2c = models.CharField(max_length=5000, blank = True)
    choice3c = models.CharField(max_length=5000, blank = True)
    choice4c = models.CharField(max_length=5000, blank = True)
    question4 = models.CharField(max_length=10000, blank = True)
    choice1d = models.CharField(max_length=5000, blank = True)
    choice2d = models.CharField(max_length=5000, blank = True)
    choice3d = models.CharField(max_length=5000, blank = True)
    choice4d = models.CharField(max_length=5000, blank = True)
    question5 = models.CharField(max_length=10000, blank = True)
    choice1e = models.CharField(max_length=5000, blank = True)
    choice2e = models.CharField(max_length=5000, blank = True)
    choice3e = models.CharField(max_length=5000, blank = True)
    choice4e = models.CharField(max_length=5000, blank = True)
    question6 = models.CharField(max_length=10000, blank = True)
    choice1f = models.CharField(max_length=5000, blank = True)
    choice2f = models.CharField(max_length=5000, blank = True)
    choice3f = models.CharField(max_length=5000, blank = True)
    choice4f = models.CharField(max_length=5000, blank = True)
    question7 = models.CharField(max_length=10000, blank = True)
    choice1g = models.CharField(max_length=5000, blank = True)
    choice2g = models.CharField(max_length=5000, blank = True)
    choice3g = models.CharField(max_length=5000, blank = True)
    choice4g = models.CharField(max_length=5000, blank = True)
    question8 = models.CharField(max_length=10000, blank = True)
    choice1h = models.CharField(max_length=5000, blank = True)
    choice2h = models.CharField(max_length=5000, blank = True)
    choice3h = models.CharField(max_length=5000, blank = True)
    choice4h = models.CharField(max_length=5000, blank = True)
    question9 = models.CharField(max_length=10000, blank = True)
    choice1i = models.CharField(max_length=5000, blank = True)
    choice2i = models.CharField(max_length=5000, blank = True)
    choice3i = models.CharField(max_length=5000, blank = True)
    choice4i = models.CharField(max_length=5000, blank = True)
    question10 = models.CharField(max_length=10000, blank = True)
    choice1j = models.CharField(max_length=5000, blank = True)
    choice2j = models.CharField(max_length=5000, blank = True)
    choice3j = models.CharField(max_length=5000, blank = True)
    choice4j = models.CharField(max_length=5000, blank = True)
    bol1 = models.BooleanField(blank = True)
    bol2 = models.BooleanField(blank = True)
    bol3 = models.BooleanField(blank = True)
    bol4 = models.BooleanField(blank = True)
    bol5 = models.BooleanField(blank = True)
    bol6 = models.BooleanField(blank = True)
    bol7 = models.BooleanField(blank = True)
    bol8 = models.BooleanField(blank = True)
    bol9 = models.BooleanField(blank = True)
    bol10 = models.BooleanField(blank = True)
    answer1 = models.CharField(max_length=5000, blank =True)
    answer2 = models.CharField(max_length=5000, blank =True)
    answer3 = models.CharField(max_length=5000, blank =True)
    answer4 = models.CharField(max_length=5000, blank =True)
    answer5 = models.CharField(max_length=5000, blank =True)
    answer6 = models.CharField(max_length=5000, blank =True)
    answer7 = models.CharField(max_length=5000, blank =True)
    answer8 = models.CharField(max_length=5000, blank =True)
    answer9 = models.CharField(max_length=5000, blank =True)
    answer10 = models.CharField(max_length=5000, blank =True)
    