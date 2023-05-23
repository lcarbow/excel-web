from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['kunden_id']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefon_sekundär'].required = False
        self.fields['objekt'].required = False
        self.fields['anlage'].required = False
        self.fields['dach'].required = False
        self.fields['speicher'].required = False
        self.fields['jährlicher_stromverbrauch'].required = False
        self.fields['anfrage_über'].required = False
        for field_name, field in self.fields.items():
            if field.required:
                field.label = f'{field.label} *'

