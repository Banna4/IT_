from django.urls import path
from basic_app import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'basic_app'


urlpatterns = [
    path(r'register/',views.register,name='register'),
    path(r'user_login/',views.user_login,name='user_login'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)