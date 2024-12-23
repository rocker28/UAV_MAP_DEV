from django import forms
from .models import service_req



class service_form(forms.ModelForm):
    class Meta:
        model = service_req
        fields = ['name',  'email_id', 'country_code', 'mobile_no', 'service_type', 'service_info']
