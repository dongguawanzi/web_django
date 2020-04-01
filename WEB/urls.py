"""WEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.views import static
from django.conf import settings

from django.contrib import admin
from django.conf.urls import url
from django.views.generic.base import RedirectView

if settings.APP_NAME == "login":
    from login import views
    from django.conf.urls import include
elif settings.APP_NAME == "application":
    from application import views


urlpatterns = [

    # 静态文件
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/img/favicon.ico')),

    # 后台管理
    url(r'^admin/', admin.site.urls),
]

if settings.APP_NAME == "login":
    urlpatterns += [  # login 模板
        url(r'^$', views.index),
        url(r'^index$', views.index),
        url(r'^it_01$', views.it_txt_001),
        url(r'^login$', views.login),
        url(r'^register$', views.register),
        url(r'^logout$', views.logout),
        url(r'^captcha', include('captcha.urls')),  # 验证模块captcha
    ]
elif settings.APP_NAME == "application":
    urlpatterns += [  # 应用系统
        url(r'^$', views.index),
        url(r'^index.html$', views.index),
        url(r'^login.html$', views.login),
        url(r'^logout.html$', views.logout),
        url(r'^#', views.login),
        # url(r'^profile.html$', views.profile),
    ]

# handler404 = views.page_not_found
# handler500 = views.page_error
