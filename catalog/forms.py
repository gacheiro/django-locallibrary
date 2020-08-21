import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from catalog.models import BookInstance


class RenewBookForm(forms.ModelForm):

    class Meta:
        model = BookInstance
        fields = ["due_back"]

    due_back = forms.DateField(help_text="Enter a date between today and 4 weeks")

    def clean_due_back(self):
        data = self.cleaned_data["due_back"]
        # Checks if date is in the allowed range
        if data < datetime.date.today():
            raise ValidationError(_("Invalid date - date is in the past."))
        elif data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_("Invalid date - renewal more than "
                                    "4 weeks ahead"))
        return data
