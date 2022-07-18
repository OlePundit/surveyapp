from django.forms import ModelForm
from .models import Survey

class Businesses(ModelForm):
    class Meta:
        model =Survey
        fields = '__all__'