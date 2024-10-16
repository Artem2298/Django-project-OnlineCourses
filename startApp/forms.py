from django import forms
from .models import Customer, Course, Category
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomerCreationForm(UserCreationForm):
    is_instructor = forms.BooleanField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'is_instructor')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            customer = Customer(user=user, is_instructor=self.cleaned_data['is_instructor'])
            customer.save()
        return user

class CustomerLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        
class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
