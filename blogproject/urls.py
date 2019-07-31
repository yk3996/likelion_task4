from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    path('blog/new/', blogapp.views.new, name='new'),
    path('blog/create', blogapp.views.create, name='create'),
    path('portfolio/', blogapp.views.portfolio, name='portfolio'),
    path('', blogapp.views.index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)