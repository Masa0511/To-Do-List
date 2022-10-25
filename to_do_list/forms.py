from django import forms

from .models import(
    To_do,
)

class To_doForm(forms.ModelForm):
    class Meta:
        model = To_do
        fields = (
            'deadline',
            'task',
        )
        widgets = {
            'deadline': forms.NumberInput(attrs={
                "type": "date",
            })
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'