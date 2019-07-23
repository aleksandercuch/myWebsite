from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('froala_editor/', include('froala_editor.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]
