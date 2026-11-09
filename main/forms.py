from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Person.objects.filter(name=name).exists():
            raise forms.ValidationError('Такое имя уже есть')
        return name
