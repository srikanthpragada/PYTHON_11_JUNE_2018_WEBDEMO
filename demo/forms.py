import django.forms as forms


class AddCourseForm(forms.Form):
    id = forms.CharField(required=True, label="Course Id")
    title = forms.CharField(max_length=50, required=True)
    duration = forms.CharField(required=True, max_length=3)
    fee = forms.CharField(required=True, max_length=5)
    prereq = forms.CharField(required=False, max_length=50)
