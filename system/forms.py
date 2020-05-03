from django import forms
from .models import Member, City, State, Test

class MemberForm(forms.ModelForm):
	state = forms.ModelChoiceField(queryset=State.objects.all(), empty_label="select State")
	state.widget.attrs.update({'onchange': 'myFunction()'})
	city = forms.ModelChoiceField(queryset=City.objects.filter(),empty_label="select City")
	class Meta:
		model = Member
		fields = '__all__'


class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = '__all__'