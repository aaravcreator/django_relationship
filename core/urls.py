from django.urls import path
from .views import *
urlpatterns = [
    path('profile/<int:userid>',profile),
    path('view_profile/<str:username>',view_profile),
    path('view_post/',view_post),
    path('view_post/<int:id>/',view_post_detail,name="post_detail"),
    path('post/',post_view)
]
