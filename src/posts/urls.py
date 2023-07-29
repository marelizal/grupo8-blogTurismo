# posts/urls.py
from django.urls import path
from . import views
# app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('add', views.post_add, name='post_add'),
    path('<int:post_id>/editar/', views.post_update, name='update_post'),
    path('<int:post_id>/eliminar/', views.post_delete, name='delete_post'),
    path('post/<int:pk>/comment/', views.post_detail, name='add_comment'),
    path('me-gusta/', views.me_gustaView, name = 'me-gusta'),
    #path('<int:post_id>/me-gusta/', views.me_gustaView, name = 'me-gusta'),
    path('add-tag/', views.tag_add.as_view(), name='tag_add'),
    path('add-category/', views.category_add.as_view(), name='category_add'),
    path('mis-publicaciones/', views.postByAuthor, name='post_byAuthor'),
]
