from django.forms import ModelForm
from .models import Quote
from django.contrib.auth.models import User

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['title','quoted_by', 'image', 'type', 'description']

    def clean_quoted_by(self):
        quoted_by = self.cleaned_data['quoted_by']
        return quoted_by or 'anonymous'
        