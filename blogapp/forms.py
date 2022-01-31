from django.forms import ModelForm

from blogapp.models import blogs

class blogForm(ModelForm):
    class Meta:
        model = blogs
        fields = '__all__'
