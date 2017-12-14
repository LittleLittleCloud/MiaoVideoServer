from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include

urlpatterns = [
    path(r'',views.video_directory,{'document_root':settings.MEDIA_ROOT}),    
    re_path(r'^(?P<path>.*)/(?P<file_name>.*)$',views.video_or_directory,{'document_root':settings.MEDIA_ROOT}),
]