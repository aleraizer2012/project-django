from django.urls import include, path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('',
        views.HomeView.as_view(),
        name='home'),
    path('requestdocnumber/<doctype>',
        views.RequestDocNumber.as_view(),
        name='requestdocnumber'),
]