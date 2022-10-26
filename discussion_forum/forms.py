from django import forms

class ForumForm(forms.Form):
    content = forms.CharField(label="Content", max_length=500, widget=forms.Textarea(attrs={
        "rows": "5",
        "id": "content-field",
        "placeholder": "Enter your message here"
    }))