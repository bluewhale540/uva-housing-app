from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions
from django import forms
from .models import Review

from listings.models import Listing, Review

RATINGS = [tuple([x, x]) for x in range(1, 6)]


class ReviewForm(forms.Form):
    rating = forms.CharField(widget=forms.Select(choices=RATINGS))
    review = forms.CharField(widget=forms.Textarea)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('rating', rows="1"),
        Field('review', rows="5", css_class='input-xlarge'),
        FormActions(
            Submit('submit', 'Submit', css_class="btn-primary"),
            Submit('cancel', 'Cancel', css_class="btn-secondary", formnovalidate='formnovalidate'),
        )
    )

