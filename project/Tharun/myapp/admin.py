from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Itvedant
from .models import User,Profile
from .models import Author,Book

admin.site.register(Itvedant)
admin.site.site_title="Itvedant"
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Book)