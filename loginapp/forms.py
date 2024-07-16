from django import forms
from .models import PoornimaEventDetail

class EventDetailsForm(forms.ModelForm):
    class Meta:
        model = PoornimaEventDetail
        fields = ['salutaion','fname','lname','designation','corresponding_email','contact','university_college_name','university_college_address','university_college_city']