from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView


app_name = 'blog'
urlpatterns = [
    path('all/', BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/<int:year>/<int:month>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<slug:slug>/edit/', BlogEditView.as_view(), name='blog_edit'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
