from django import forms
from app.models import *

class TopicForm(forms.Form):
    topicname=forms.CharField(max_length=50)



def check_for_a(subvalue):
    if subvalue[0].lower() == 'a':
        raise forms.ValidationError('Entered value is a')
    
def check_len(subvalue):
    if len(subvalue)<5:
        raise forms.ValidationError('min length is 5')
    
def check_url(subvalue):
    if subvalue.startswith('http://'):
        raise forms.ValidationError('incorrect url')



class WebpageForm(forms.Form):
    topicname=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100,validators=[check_for_a,check_len])
    url=forms.URLField(validators=[check_url])
    email=forms.EmailField()

class AccessForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    author=forms.CharField(max_length=50)
    date=forms.DateField()


class TopicModelForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
    


class WebpageModelForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'

class AccessModelForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'
    