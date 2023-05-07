from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Dashboard, TreePoint


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ['name', 'description']


class PointForm(forms.ModelForm):

    class Meta:
        model = TreePoint
        fields = ['name', 'parent_id']

    def __init__(self, dashboard_id=None, **kwargs):
        super(PointForm, self).__init__(**kwargs)
        if dashboard_id:
            self.fields['parent_id'] = forms.ModelChoiceField(
                queryset=TreePoint.objects.filter(dashboard_id=dashboard_id), required=False
            )




