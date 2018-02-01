from django.conf.urls import url
from basic_app import views

app_name='basic_app'

urlpatterns=[
	url(r'^register/$',views.register,name='register'),
	url(r'^user_login/$', views.user_login,name='user_login'),
	url(r'^about/$', views.about,name='about'),
	url(r'^contact/$', views.contact,name='contact'),
	url(r'^(?P<pk>\d+)/$',views.CompanyDetailView.as_view(),name='detail'),
	url(r'^create/$', views.CompanyCreateView.as_view(),name='create'),
] 