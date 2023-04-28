from django import forms
from myapp.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'username']
