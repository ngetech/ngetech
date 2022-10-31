from django import forms

class PostTechForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=160,
        widget=forms.TextInput(
            attrs={
                'id': 'post-tech-title',
                'placeholder': 'Add a title here...'
            }
        )
    )
    description = forms.CharField(
        label='Description',
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'id': 'post-tech-description',
                'placeholder': 'Tell us what are those...',
                'rows': '18'
            }
        )
    )