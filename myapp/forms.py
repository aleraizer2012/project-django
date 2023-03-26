from django import forms
from .models import DocNumber

class DocNumberForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.fields['subject'].label = 'Assunto'
        self.fields['recipient'].label = 'Destinatário'
        self.fields['departmentrecipient'].label = 'Departamento do destinatário'

    class Meta:
        model = DocNumber
        fields = ['subject', 'recipient', 'departmentrecipient']