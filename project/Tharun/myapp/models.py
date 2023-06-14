from django.db import models
from django.utils.text import slugify

# Create your models here.
# class coursemanager(models.Manager):
#     def sort_desc_price(a):
#         return a.order_by('-cprice').all()

class Itvedant(models.Model):
    slug=models.SlugField(blank=True,null=True)
    cname=models.CharField(max_length=50)
    cdur=models.IntegerField()
    cprice=models.FloatField()
    #c_manager=models.Manager()
def save(self,*args,**kwargs):
    if self.slug is None:
        self.slug=slugify(self.name)
    super().save(*args,**kwargs)   


class User(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
         return str(self.name)  

class Profile(models.Model):

    user=models.OneToOneField(
       User,
        on_delete=models.PROTECT,
        primary_key=True
    ) 

    language=models.CharField(max_length=50)
    email=models.EmailField(max_length=70,blank=True,unique=True)

    def __str__(self):
        return str(self.email)

class Author(models.Model):
    name=models.CharField(max_length=50, blank=False,unique=True)

    def __str__(self):
        return str(self.name)

class Book(models.Model):
    author=models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        blank=False
    )  

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title            

   