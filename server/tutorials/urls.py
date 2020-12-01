from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^api/user$', views.user),
    url(r'^api/user_connection$', views.user_connection),
    url(r'^api/user_transaction$', views.user_transaction),
]
