from django import forms
from .models import Emp
class EmployeeFrom(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ('fullName', 'empCode', 'mobile', 'position')
        labels = {
            'fullName': 'Full name',
            'empCode': 'EMP. Code',
        }


    def __init__(self, *args, **kwargs):
        super(EmployeeFrom, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Tanlov"
        self.fields['empCode'].request = False