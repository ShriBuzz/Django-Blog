from django.urls import path
from blog.views import home_view, PostList, PostDetail


app_name = 'blog'


urlpatterns = [
    path('', home_view, name='home'),
    path('blog', PostList.as_view(), name='post_list'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]