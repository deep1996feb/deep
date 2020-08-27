from django import Forms
from Calc.models import CalcModel
class CalcForms(Formss.ModelForm):
	class Meta:
		model = CalcModel
		fields = "_all_"