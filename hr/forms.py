from django.forms import ModelForm
from hr.models import Department


class AddDeptForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
