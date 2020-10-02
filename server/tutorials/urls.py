from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/user$', views.user),
    url(r'^api/user_connection$', views.user_connection),
    url(r'^api/user_transaction$', views.user_transaction),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
