from django import forms

class PostCommentForm(forms.Form):
    comment = forms.CharField(
        label='Comment',
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'id': 'comment',
                'placeholder': 'What do you think...',
                'rows': '4'
            }
        )
    )