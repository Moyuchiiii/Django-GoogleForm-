from django.forms import ModelForm
from .models import Page


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ["title", "q1","q2","q3","q4","q5","q6","q7", "q8", "q9", "q10"]