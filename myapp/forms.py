from django import forms
from .models import SubService
from .models import ContactMessage



class AppointmentForm(forms.Form):
    subservice = forms.ModelChoiceField(queryset=SubService.objects.all(), label='Select Subservice')
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    time = forms.TimeField(widget=forms.TextInput(attrs={'placeholder': 'HH:MM'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'question']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})