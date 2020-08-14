from django.contrib import admin
from django.urls import path
from mysite.views import HomeView
from django.conf.urls import include

from mysite.views import HomeView, UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('accounts/', include('Django.contrib.auth.urls')),
    path('accounts/signup/', UserCreateView.as_view(), name='signup'),
    path('accounts/signup/done/', UserCreateDoneTV.as_view(), name='signup_done'),

    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('recipe/', include('recipe.urls')),
    path('hotplace/', include('hotplace.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
