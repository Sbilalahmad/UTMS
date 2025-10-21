from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class CrispyAuthenticationForm(AuthenticationForm):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Login'))
class CrispyPasswordChangeForm(PasswordChangeForm):
    def init(self, *args, **kwargs):        
        super().init(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Change Password'))
