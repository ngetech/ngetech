from django import forms

class DiscussionForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50, widget=forms.TextInput(attrs={
        "id": "title-field",
        "placeholder": "Thread title"
    }))
    content = forms.CharField(label="Content", max_length=500, widget=forms.Textarea(attrs={
        "rows": "5",
        "id": "content-field",
        "placeholder": "Enter your message here"
    }))

class ReplyForm(forms.Form):
    content = forms.CharField(label="Content", max_length=500, widget=forms.Textarea(attrs={
        "rows": "5",
        "id": "content-field",
        "placeholder": "Enter your message here"
    }))
