from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import PostListView, PostUpdateView, PostDetailView, PostCreateView, PostDeleteView, UserInfoListView, UserInfoDetailView, UserInfoUpdateView


app_name = 'webapp'


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('users', UserInfoListView.as_view(), name='user_list'),
    path('users/<int:pk>', UserInfoDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/update', UserInfoUpdateView.as_view(), name='user_update')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)