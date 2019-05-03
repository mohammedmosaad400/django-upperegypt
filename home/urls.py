from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('news/',views.NewsListView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news2/<int:pk>', views.News2DetailView.as_view(), name='news2-detail'),
    path('signup',views.signup,name='signup'),
    path('condition',views.condition,name='condition'),
]