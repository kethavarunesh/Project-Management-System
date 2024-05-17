from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
      path('admin/', admin.site.urls),
      path('',views.home,name='home'),
      path('index/',views.index,name='index'),
      path('index/reports/', views.reports, name='reports'),
       path('project/<str:project_name>/', views.project_details, name='project_details'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)