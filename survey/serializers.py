from rest_framework import serializers
from .models import Survey

class StudentSerializer():
    class Meta:
        model = Survey
        fields = {
            'question', 'questiontype', 'choice1', 'choice2', 'choice3', 'choice4'
        }