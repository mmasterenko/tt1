from django.conf.urls import include, url
from django.contrib import admin

from app import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^$', views.index, name='index'),
]
