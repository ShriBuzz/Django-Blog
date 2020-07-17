from django.urls import path
from blog.views import home_view, PostList, PostDetail, PostCreateView


app_name = 'blog'


urlpatterns = [
    path('', home_view, name='home'),
    path('blog', PostList.as_view(), name='post_list'),
    path('create', PostCreateView.as_view(), name='create'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
