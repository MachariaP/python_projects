# musiclibrary/urls.py
from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('song.urls')),  # include the song app's URLs

]

urlpatterns += staticfiles_urlpatterns()