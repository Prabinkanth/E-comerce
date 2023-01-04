from django.urls import path
from . import views
app_name='home'

urlpatterns = [
    path('',views.index,name='welcome'),
    path('home/',views.home,name='home'),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout')
]