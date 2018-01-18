
from django.conf.urls import url
from django.contrib import admin

from bookmark import views as bk_views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', bk_views.index, name='index'),
    url(r'^bookmark$', bk_views.bookmark, name='bookmark'),
    url(r'^login$', bk_views.login, name='login'),
    url(r'^logout$', bk_views.logout, name='logout'),
    url(r'^logout_process', bk_views.logout_process, name='logout_process'),
    url(r'^login_check$', bk_views.login_check, name='login_check'),
    url(r'^user_registration$', bk_views.user_registration, name='user_registration'),
    url(r'^product$', bk_views.product, name='product')
]
