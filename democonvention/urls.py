"""democonvention URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from registration import views as registration_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),

    # Registration
    path('register/', registration_views.Register.as_view(), name='convention_registration'),
    path('register/site/', registration_views.RegisterSimple.as_view(), name='convention_onsite_reg'),
    path('upgrade/', registration_views.Upgrade.as_view(), name='convention_upgrade'),
    re_path(r'^upgrade/(?P<external_id>[0-9A-Za-z]*)$', registration_views.Upgrade.as_view(), name='convention_upgrade'),
    path('confirm/<external_id>', registration_views.confirm, name='convention_confirm'),
    path('confirm/<external_id>/change', registration_views.confirm_change, name='convention_confirm_change'),
    path('confirm/<external_id>/change/<confirmation>', registration_views.confirm_change, name='convention_confirm_change'),
    path('confirm/<external_id>/claim', registration_views.confirm_claim, name='convention_confirm_claim'),
    path('register/avatar/upload', registration_views.handle_avatar_upload, name='avatar_upload'),
    path('register/avatar/<avatar_type>/<avatar_id>/<int:maxwidth>x<int:maxheight>', registration_views.avatar_thumbnail, name='avatar_thumbnail'),
    path('register/qr/<int:badge_number>', registration_views.registration_qrcode, name='badge_qrcode'),
    path('register/staff_badge/<int:registration_id>', registration_views.staff_badge_image, name='staff_badge_image'),
    re_path(r'^register/check_in/(?:(?P<registration_id>[0-9]+))?(?:/(?P<mode>[a-z]+))?$', registration_views.check_in, name='convention_check_in'),
    re_path(r'^register/badge_puller/(?:(?P<registration_id>[0-9]+))?$', registration_views.badge_puller, name='convention_badge_puller'),
]
