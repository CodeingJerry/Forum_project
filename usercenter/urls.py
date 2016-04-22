from django.conf.urls import url
from usercenter.views import register,activate,uploadavatar
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^register$', register, name="usercenter_register"),
    url(r'^activate/(?P<code>\w+)$', activate, name="usercenter_activate"),
    url(r'^logout', logout_then_login, name="logout_then_login"),
    url(r'^uploadavatar$', uploadavatar, name="uploadavatar"),
]