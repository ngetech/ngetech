from django import forms

class TechSurveyForm(forms.Form):
    CHOICES = [(0, ''), (1, ''), (2, ''), (3, '')]

    que_1 = forms.ChoiceField(
        label='Saya mampu mencari dan mengakses informasi di media digital sesuai kebutuhan.',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_2 = forms.ChoiceField(
        label='Saya dapat dengan mudah menyaring informasi dan mampu mendeteksi berita bohong (hoax) di media sosial.',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_3 = forms.ChoiceField(
        label='Saya mampu menggunakan media digital sebagai wadah berinteraksi dan komunikasi.',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_4 = forms.ChoiceField(
        label='Saya seringkali mencari informasi mengenai G20, khususnya pada topik Transformasi Digital pada berbagai aspek kehidupan.',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_5 = forms.ChoiceField(
        label='Saya menyadari dan mendukung pentingnya Transformasi Digital di era perkembangan digital saat ini.',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_6 = forms.ChoiceField(
        label='Saya siap akan konsekuensi bahwa apa yang saya tulis di media sosial dapat diakses banyak orang dan dapat meninggalkan jejak digital.',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_7 = forms.ChoiceField(
        label='Saya terbiasa mengkaji ulang dan memeriksa kebenaran informasi yang saya temui di media digital.',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    que_8 = forms.ChoiceField(
        label='Saya memanfaatkan proses digitalisasi dalam kehidupan sehari-hari, contohnya dalam bertransaksi online, digital learning, dan lain-lain.',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))