from django.contrib import admin
from .models import Item, Review, ContactMessage,Favorite,Watchlist,ReviewReply

# Register your models here.

# --- Customize Admin Panels for Better Usability ---

# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'created_by', 'average_rating', 'created_at')
#     list_filter = ('category','created_at')
#     search_fields = ('title', 'description', 'created_by__username')
#     ordering = ('-created_at',)
  

@admin.register(ReviewReply)
class ReviewReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'user', 'content', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('content', 'user__username', 'review__item__title')
    ordering = ('-created_at',)

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'item__title')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_by', 'average_rating', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'created_by__username')
    ordering = ('-created_at',)
    
    # Exclude non-editable fields from the form
    readonly_fields = ('created_at', 'average_rating')
    
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'item__title')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('item__title', 'user__username', 'comment')
    ordering = ('-created_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-created_at',)