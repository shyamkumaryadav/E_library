from django import forms
from .models import Member, City, State, Test

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		exclude = ['status']
		labels = {
            'name': 'Writer',
        }
		widgets = {
            'name': forms.TextInput(attrs={'id':'member_id_name','class':'id_name_member test'}),
        }
		error_messages = {
            'name': {
                'max_length': "This writer's name is too long.",
			},
		}


class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = '__all__'
		