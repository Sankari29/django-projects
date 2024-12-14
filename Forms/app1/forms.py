from django import forms
from app1.models import Reg

'''
class Reg_forms(forms.Form):
    First_Name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter firstname'}),required=True)
    Last_Name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter lastname'}),required=True)
    Age=forms.IntegerField(widget=forms.NumberInput())
    optns=[['male','MALE'],['female','FEMALE'],['others','OTHERS']]
    Gender=forms.CharField(widget=forms.RadioSelect(choices=optns))
'''

class Reg_forms(forms.ModelForm):
    class Meta:
        model = Reg
        #fields='__all__'
        fields=['fname','lname','age','gender']