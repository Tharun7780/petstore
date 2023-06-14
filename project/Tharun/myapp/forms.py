from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class signupform(UserCreationForm):
    class meta:
        model=User
        fields=['username','first_name','last_name','email']