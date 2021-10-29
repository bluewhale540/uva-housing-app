from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions
from django import forms

from listings.models import Listing, Review


class ReviewForm(forms.Form):
    review = forms.CharField(widget=forms.Textarea)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('review', rows="5", css_class='input-xlarge'),
        FormActions(
            Submit('submit', 'Submit', css_class="btn-primary"),
            Submit('cancel', 'Cancel', css_class="btn-secondary", formnovalidate='formnovalidate'),
        )
    )

'''
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = []

    def __init__(self, *args, **kwargs):
        listing = kwargs.pop('listing')
        print(listing)
        super(ReviewForm, self).__init__(*args, *kwargs)
        self.title = "listing"
        self.fields['Reviews'] = forms.ModelChoiceField(widget=forms.RadioSelect,
                                                        queryset=Review.objects.filter(listing=listing))
        self.helper = FormHelper(self)
'''
