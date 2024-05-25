
from django.contrib import admin
from django.urls import path,include
# from . import views
from practice_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('food/', views.food),
    path('practice_app/', include('practice_app.urls'))
]
