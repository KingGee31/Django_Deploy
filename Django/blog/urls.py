from django.urls import path

# this indicates that i'll be using class base view
from django.contrib.auth import views as auth_views
# this helps to get my path url path
from django.urls import path, re_path
# it allows access only to your site defined settings file, which overwrites django default settings
from django.conf import settings
# here i am indicating that i'll be importing views from my app "blog"
from blog import views


# app_name = 'blog'

# here i am mapping url's with the views " Connecting views with URL' "
urlpatterns = [
        path('',views.PostListView.as_view(),name='post_list'),
        path('about',views.AboutView.as_view(),name = 'about'),
        path('post/(<int:pk>/)',views.PostDetailView.as_view(),name='post_detail'),
        path('post/new',views.CreatePostView.as_view(),name='post_new'),
        path('post/(<int:pk>/)/edit/',views.PostUpdateView.as_view(),name='post_edit'),
        path('post/(<int:pk>/)/remove/',views.PostDeleteView.as_view(),name='post_remove'),
        path('draft',views.DraftListView.as_view(),name='post_draft_list'),

        # path('post/(?P<pk>/)/comment/',views.add_comment_to_post,name='add_comment_to_post'),
        path('post/new/comment/<int:pk>/',views.add_comment_to_post,name='add_comment_to_post'),
        path('comment/(<int:pk>/)/approved/',views.comment_approved,name='comment_approve'),
        path('comment/(<int:pk>/)/remove/',views.comment_remove,name='comment_remove'),
        path('post/(<int:pk>/)/publish/',views.post_publish,name='post_publish'),





]
