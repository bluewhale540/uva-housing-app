from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions
from django import forms
from django.forms import ModelForm
from .models import Listing, Review

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


class ListingForm(ModelForm):
    """
    address = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(widget=forms.Textarea)
    is_house = forms.BooleanField()  # 0 = apt, 1 = house
    rating = forms.FloatField()  # average of ratings from reviews
    rent = forms.IntegerField()  # in $
    beds = forms.IntegerField(default=0)
    baths = forms.IntegerField(default=0)
    desc = forms.CharField(widget=forms.Textarea)  # description of listing
    link = forms.URLField(widget=forms.Textarea)
    lat = forms.DecimalField(default=0)
    lon = forms.DecimalField(default=0)
    """

    class Meta:
        model = Listing
        fields = ['address', 'name', 'is_house', 'aircon', 'furnished', 'has_pool', 'pets_allowed', 'has_gym',
                  'unit_laundry', 'shared_laundry', 'rating', 'rent', 'beds', 'baths', 'desc', 'link']

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('address', rows="1"),
        Field('name', rows="1"),
        Field('is_house', rows="1"),
        Field('aircon', rows="1"),
        Field('furnished', rows="1"),
        Field('has_pool', rows="1"),
        Field('pets_allowed', rows="1"),
        Field('has_gym', rows="1"),
        Field('unit_laundry', rows="1"),
        Field('shared_laundry', rows="1"),
        Field('rating', rows="1"),
        Field('rent', rows="1"),
        Field('beds', rows="1"),
        Field('baths', rows="1"),
        Field('desc', rows="5", css_class='input-xlarge'),
        Field('link', rows="1"),
        FormActions(
            Submit('submit', 'Submit', css_class="btn-primary"),
            Submit('cancel', 'Cancel', css_class="btn-secondary", formnovalidate='formnovalidate'),
        )
    )