from django import forms
from django.contrib.auth import (
    get_user_model, password_validation,
)
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


class CustomUserCreationForm(forms.ModelForm):
    """
    Based off of django.contrib.auth.forms.UserCreationForm.
    Could not extend class due to Meta using hard coded User class
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    first_name = forms.CharField(label=_("FirstName"), max_length=254, required=False)
    last_name = forms.CharField(label=_("LastName"), max_length=254, required=False)
    email = forms.EmailField(label=_("Email"), max_length=254, required=False)


    # Uses User model from get_user_model()
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)
        try:
            email = self.cleaned_data.get('email')
            User.objects.get(email=email)
            self.add_error('email', "%s already in use by another account"%email)
        except ObjectDoesNotExist:
            pass

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
