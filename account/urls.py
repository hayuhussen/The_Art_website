from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
app_name = 'Account'

urlpatterns = [
    path('', index, name='index'),
    path('index2', index2, name='index2'),  
    path('index3', index3, name='index3'),  
    path('index4', index4, name='index4'),  
    path('index5', index5, name='index5'),  
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('collection/', collection, name='collection'),
    path('single_collection/', collection_single, name='single_collection'),
    path('blog/', homeblog, name='blog'),
    path('creator/', creator, name='creator'),
    path('contact/', contact, name='contact'),
    path('dashboard', dashboard, name='dashboard'),
    path('userlist', userlist, name='userlist'),
    path('adminblog', adminblog, name='adminblog'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)