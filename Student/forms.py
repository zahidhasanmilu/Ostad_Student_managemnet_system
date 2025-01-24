from django import forms
from Student.models import Students


class StudentForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password',

    )

    class Meta:
        model = Students
        fields = "__all__"

        labels = {
            'name': 'Full Name',
            'email': 'Email',
            'phone': 'Phone',
            'password': 'Password',
            'photo': 'Photo',
            'checked': 'Checked'
        }

        # help_texts = {
        #     'name': 'Enter your full name.',
        #     'email': 'Enter your valid email address.',
        #     'phone': 'Enter your phone number.',
        #     'photo': 'Upload a profile photo.',
        #     'checked': 'Check the box to agree.',
        # }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'photo': forms.ClearableFileInput(attrs={'placeholder': 'Upload your photo'}),
            'checked': forms.CheckboxInput(),
        }
