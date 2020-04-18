from django import forms
from . import models

class Test(forms.ModelForm):

	class Meta:
		model = models.Test
		fields = ['state', 'city']
		