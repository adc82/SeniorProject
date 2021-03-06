from django.conf.urls import url

import views

urlpatterns = [
    url(r'^createaccount/$', views.CreateAccountView.as_view(),
        name='create_account'),
    url(r'^dashboard/$', views.DashboardView.as_view(),
        name='dashboard'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^linktoecho/$', views.LinkEchoToUserView.as_view(),
        name='link_echo_to_user'),

    url(r'^itworkd/$', views.ItWorkedView.as_view(), name='it_worked'),
]
