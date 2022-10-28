from django import forms

class TechSurveyForm(forms.Form):
    CHOICES = [(0, ''), (1, ''), (2, ''), (3, '')]

    que_1 = forms.ChoiceField(
        label='Pertanyaan 1',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_2 = forms.ChoiceField(
        label='Pertanyaan 2',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_3 = forms.ChoiceField(
        label='Pertanyaan 3',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_4 = forms.ChoiceField(
        label='Pertanyaan 4',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_5 = forms.ChoiceField(
        label='Pertanyaan 5',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))