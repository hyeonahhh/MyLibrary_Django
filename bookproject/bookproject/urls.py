"""bookproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from bookapp import views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mybook/', views.mybook, name='mybook'),
    path('search/', views.search, name='search'),
    path('bookform/', views.bookform, name='bookform'),
    path('detail/<int:book_id>/', views.detail, name='detail'),
    path('bookdelete/<int:book_id>/', views.bookdelete, name='bookdelete'),
    path('bookedit/<int:book_id>/', views.bookedit, name='bookedit'),
    path('review/<int:book_id>/', views.review, name='review'),
    path('create_comment/<int:book_id>/', views.create_comment, name='create_comment'),
    path('reviewedit/<int:review_id>/', views.reviewedit, name='reviewedit'),
    path('reviewdelete/<int:review_id>/', views.reviewdelete, name='reviewdelete'),
    path('login/', account_views.login, name='login'),
    path('logout/', account_views.logout, name='logout'),
    path('signup/', account_views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

