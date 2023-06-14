from django.urls import path
from. import views

urlpatterns = [
    path("index",views.index,name="index"),
    # path("home",views.Home,name="home"),
    # path('home/<user>',views.user,name='user'),
    # path('delete1/<rid>',views.delete,name='delete1'),
    # path("delete/<x1>/<x2>",views.delete,name="delete"),
    # path("contact",views.contact,name="contact"),
    # path("placement",views.placement,name="placement"),
    # path("product",views.my_view,name="product"),
    # path('',views.my_view,name="main"),
    # path('',views.my_views,name="main"),
    # path('products/<int:product_id>/',views.product_details,name="product_details"),
path('tharun',views.tharun,name='tharun'),
path('form',views.getform,name='form'),
path('formsubmit',views.formsubmit,name='formsubmit'),
path('course',views.course,name='course'),
path('create_course',views.create_course,name='create_course'),
path('',views.get_course,name="get_course"),
path('delete/<rid>',views.delete,name="delete"),
path('edit/<rid>',views.edit,name="edit"),
path('set_cookie',views.set_cookie,name='set_cookie'),
path('get_cookie',views.get_cookie,name='get_cookie'),
path('del_cookie',views.del_cookie,name='del_cookie'),
path('setsession',views.set_session,name='set_session'),
path('getsession',views.get_session,name='get_session'),
path('delsession',views.del_session,name='del_session'),
path('signup',views.register,name='user_register'),
path('login',views.user_login,name='user_login'),
path('profile',views.user_profile,name='user_profile'),
path('logout',views.user_logout,name='user_logout'),
path('search_results',views.search_results, name='search_results')
  
]
