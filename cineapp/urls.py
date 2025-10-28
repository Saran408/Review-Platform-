from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'cineapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.category_list, {'category': 'Movie'}, name='movies'),
    path('series/', views.category_list, {'category': 'Series'}, name='series'),
    path('books/', views.category_list, {'category': 'Book'}, name='books'),

    path('item/add/', views.add_item, name='add_item'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('item/<int:pk>/delete/', views.delete_item, name='delete_item'),

    path('item/<int:pk>/review/add/', views.add_review, name='add_review'),
    path('review/<int:pk>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:pk>/delete/', views.delete_review, name='delete_review'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('profile/<str:username>/', views.user_profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('item/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorite/<int:item_id>/', views.toggle_favorite, name='toggle_favorite'),
    # path('item/<int:pk>/toggle_watchlist/', views.toggle_watchlist, name='toggle_watchlist'),
    # path('my-watchlist/', views.my_watchlist, name='my_watchlist'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/<int:pk>/toggle_watchlist/', views.toggle_watchlist, name='toggle_watchlist'),
    path('review/<int:review_pk>/reply/', views.add_reply, name='add_reply'),
    # path('reply/<int:pk>/delete/', views.delete_reply, name='delete_reply'),
    path('reply/<int:pk>/delete/', views.delete_reply, name='delete_reply'),
    
]
