from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Itvedant
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import signupform
  # Create your views here.

# def index(request):
#      content={}
#      content['l']=[10,20,30,40,50]
#      content['t']=(1,2,3,4,5,'IT-vedant')
#      content['s']={1,2,3,4,5}
#      content['d']={'a':'Tharun','b':'Vikas','c':'Clinton'}
#      return render(request,'index.html',content)
    #  return HttpResponse('<h1>Welcome to django class!</h1>')
  #   form='''
  #   <html>
  #   <head>
  #   <title>My form</title>
  #   </head>
  #   <body>
  #   <form method="">
  #   <table>
  #   <tr>
  #   <td>heading</td>
  #   <td><input type="text" name="bhead"></td>
  #   </tr>
  #   <tr>
  #   <td>category</td>
  #   <td><input type="text" name="bcate"></td>
  #   </tr>
  #   <tr>
  #  <td> <input type="submit" name="bcate"></td>
  #  </tr>
  #  </table>
  #  </form>
  #  </body>
  #  </html>'''
  #   return HttpResponse(form)

# def home(request):
#      return HttpResponse('<h1>Hello world!</h1>')   
# class Home(View):
#   def get(self,request):
#     return HttpResponse('<h1>todays days is good</h1>')
# def Home(request):
#   x=20
#   content='value of x is :{}'.format(x)
#   return HttpResponse(content)

# def user(request,user):
#   content='<h1.Hello:{}</h1>'.format(user)
#   return HttpResponse(content)

# def delete(request,x1,x2):
#   x=int(x1)+int(x2)
#   content="add of x {} and {} is :{}".format(x1,x2,x)
#   return HttpResponse(content) 

# def contact(request):
#   return render(request,'contact.html')

# def placement(request):
#   return render(request,'placement.html')      

# def my_view(request):
#     product=[
#       {
      
#       'name':'pet food',
#       'description':'Delicious and nutricios food',
#       'price':10
#     },
#     {
      
#       'name':'pet toy',
#       'description':'fun and interactive toy for pets',
#       'price':50
#     }
#     ]
#     return render(request,'main.html',{'products':product})

# def my_views(request):
#     products=[
#         {
#             'id':1,
#             'name':'pet food',
#             'description':'delicious and nutrious pet food',
#             'price':10
#         },
#         {
#             'id':2,
#             'name':'tommy',
#             'description':'its is looking good',
#             'price':40
#         }
#     ]
#     return render(request,'main.html',{'products':products})
# def product_details(request,product_id):
#   products=[
#     {
#       'id':1,
#       'name':'pet food',
#       'description':'delicious and nutrious pet food',
#       'price':10
#     },
#     {
#       'id':2,
#       'name':'tommy',
#       'description':'its is looking good',  
#       'price':40
#     }
#     ]
#   product=next((p for p in products if p['id']==product_id),None)
#   if product is None:
#     return render(request,'product_not_found.html')
#   return render(request,'product_details.html',{'product':product})  
import datetime
# def index(request):
#   content={}
#   content['name']='Itvedant'
#   return render(request,'index.html',content)
def index(request):
  content={}
  now=datetime.datetime.now()
  content['name']='Itvedant_class'
  content['cdt']=now
  return render(request,'index.html',content)
def tharun(request):
  return render(request,'myapp/index.html')
def getform(request):
  return render(request,'form.html')  
def formsubmit(request):
  mn=request.POST['mn']
  fd=request.POST['feedback']
  content={'m':mn,'f':fd}
  return render(request,'contact.html',content)

def course(request):
  return render(request,'create_course.html')

def create_course(request):
  if request.method=='POST':
    x=request.POST['cname']
    y=request.POST['cdur']
    z=request.POST['cprice']
    c1=Itvedant.objects.create(cname=x,cdur=y,cprice=z)
    c1.save()
    # return HttpResponse('record inserted successfully')
    return redirect('/')

def get_course(request):
  content={}
  content['data']=Itvedant.objects.order_by('cprice')
  return render(request,'dashboard.html',content)

def delete(request,rid):
  x=Itvedant.objects.get(id=rid)
  x.delete()
  return redirect('/')

def edit(request,rid):
  if request.method=="POST":
      x=request.POST['cname']
      y=request.POST['cdur']
      z=request.POST['cprice']
      c=Itvedant.objects.filter(id=rid)
      c.update(cname=x,cdur=y,cprice=z)
      return redirect('/')
  else:
      content={}
      content['data']=Itvedant.objects.get(id=rid)  
      return render(request,'edit_course.html',content)

def set_cookie(request):
  res=render(request,"setcookie.html")
  res.set_cookie('name','BTHCV') 
  return res   

def get_cookie(request):
  v=request.COOKIES.get('name','Guest')
  return render(request,'getcookie.html',{'value':v})

def del_cookie(request):
  res=render(request,'delcookie.html')
  res.delete_cookie('name')  
  return res
def set_session(request):
  request.session['name']='bumblle beee'
  return render(request,"setsession.html")

def get_session(request):
  v=request.session['name']
  return render(request,'getsession.html',{'value':v})

def del_session(request):
  if 'name' in request.session:del request.session['name']
  return render(request,'delsession.html')    

def register(request):
  if request.method=='POST':
    fn=signupform(request.POST)
    print(fn)
    if fn.is_valid():
      # uname=fn.cleaned_data['username']
      # upass=fn.cleaned_data['password1']
      # u1=User.objects.create(username=uname,password=upass)
      # u1.save()
      
      fn.save()
  else:
    fn=signupform()
  return render(request,'signup.html',{'form':fn})

def user_login(request):
  if request.method=='POST':
    fn=AuthenticationForm(request=request,data=request.POST)
    if fn.is_valid():
      uname=fn.cleaned_data['username']
      upass=fn.cleaned_data['password']
      u=authenticate(username=uname,password=upass)
      print(u)
      if u is not None:
        login(request,u)
        # return HttpResponse('profile page')
        return redirect('/profile')

  else:
    fn=AuthenticationForm()
  return render(request,'login.html',{'form':fn}) 

def user_profile(request):
  return render(request,'profile.html' )  

def user_logout(request):
  logout(request)
  return redirect('/login')  

# def search_results(request):
#   query=request.GET.get('query','')
#   return render(request,'search.html',{'query':query})  
 
#  for seaching in database
def search_results(request):
    query = request.GET.get('query', '')
    # Perform the database search based on the query
    courses = Itvedant.objects.filter(cname__icontains=query)
    
    return render(request, 'search_results.html',{'query': query, 'courses': courses})




    
