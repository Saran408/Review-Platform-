# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Item, Review
# from .forms import ItemForm, ReviewForm, ContactForm, SignUpForm
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.db.models import Avg
# from django.contrib.auth import login
# from django.core.paginator import Paginator

# def home(request):
#     top = Item.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')[:8]
#     recent = Item.objects.order_by('-created_at')[:8]
#     return render(request, 'cineapp/home.html', {'top': top, 'recent': recent})

# def category_list(request, category):
#     items = Item.objects.filter(category=category).order_by('-created_at')
#     paginator = Paginator(items, 12)
#     page = request.GET.get('page')
#     items_page = paginator.get_page(page)
#     return render(request, 'cineapp/item_list.html', {'items': items_page, 'category': category})

# def item_detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     review_form = ReviewForm()
#     return render(request, 'cineapp/item_detail.html', {'item': item, 'review_form': review_form})

# @login_required
# def add_item(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             it = form.save(commit=False)
#             it.created_by = request.user
#             it.save()
#             messages.success(request, 'Item created.')
#             return redirect('cineapp:item_detail', pk=it.pk)
#     else:
#         form = ItemForm()
#     return render(request, 'cineapp/item_form.html', {'form': form})

# @login_required
# def edit_item(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.user != item.created_by:
#         messages.error(request, "You can only edit items you created.")
#         return redirect('cineapp:item_detail', pk=pk)
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Item updated.')
#             return redirect('cineapp:item_detail', pk=pk)
#     else:
#         form = ItemForm(instance=item)
#     return render(request, 'cineapp/item_form.html', {'form': form, 'item': item})

# @login_required
# def delete_item(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.user != item.created_by:
#         messages.error(request, "You can only delete items you created.")
#         return redirect('cineapp:item_detail', pk=pk)
#     if request.method == 'POST':
#         item.delete()
#         messages.success(request, 'Item deleted.')
#         return redirect('cineapp:home')
#     return render(request, 'cineapp/item_confirm_delete.html', {'item': item})

# @login_required
# def add_review(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # prevent user from posting multiple reviews for same item (optional)
#             existing = Review.objects.filter(item=item, user=request.user)
#             if existing.exists():
#                 messages.error(request, "You have already reviewed this item. Edit your review instead.")
#                 return redirect('cineapp:item_detail', pk=pk)
#             rv = form.save(commit=False)
#             rv.item = item
#             rv.user = request.user
#             rv.save()
#             messages.success(request, 'Review added.')
#             return redirect('cineapp:item_detail', pk=pk)
#     return redirect('cineapp:item_detail', pk=pk)

# @login_required
# def edit_review(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.user != review.user:
#         messages.error(request, "You can only edit your own reviews.")
#         return redirect('cineapp:item_detail', pk=review.item.pk)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, instance=review)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Review updated.')
#             return redirect('cineapp:item_detail', pk=review.item.pk)
#     else:
#         form = ReviewForm(instance=review)
#     return render(request, 'cineapp/review_form.html', {'form': form, 'review': review})

# @login_required
# def delete_review(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.user != review.user:
#         messages.error(request, "You can only delete your own reviews.")
#         return redirect('cineapp:item_detail', pk=review.item.pk)
#     if request.method == 'POST':
#         item_pk = review.item.pk
#         review.delete()
#         messages.success(request, 'Review deleted.')
#         return redirect('cineapp:item_detail', pk=item_pk)
#     return render(request, 'cineapp/review_confirm_delete.html', {'review': review})

# def about(request):
#     return render(request, 'cineapp/about.html')

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Message sent.')
#             return redirect('cineapp:contact')
#     else:
#         form = ContactForm()
#     return render(request, 'cineapp/contact.html', {'form': form})

# def user_profile(request, username):
#     from django.contrib.auth.models import User
#     user = get_object_or_404(User, username=username)
#     items = user.items.all()
#     reviews = user.reviews.all()
#     return render(request, 'cineapp/profile.html', {'profile_user': user, 'items': items, 'reviews': reviews})

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Registration successful.')
#             return redirect('cineapp:home')
#     else:
#         form = SignUpForm()
#     return render(request, 'cineapp/signup.html', {'form': form})


# from django.contrib.auth import logout
# from django.shortcuts import redirect

# def logout_view(request):
#     logout(request)
#     return redirect('cineapp:home')  # or redirect('/')


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, f"Welcome, {user.username}!")
#             return redirect('cineapp:home')
#         else:
#             messages.error(request, "Invalid username or password")

#     return render(request, 'cineapp/login.html')



# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Item, Review
# from .forms import ItemForm, ReviewForm, ContactForm, SignUpForm
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.db.models import Avg
# from django.contrib.auth import login, logout, authenticate
# from django.core.paginator import Paginator

# def home(request):
#     top = Item.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')[:8]
#     recent = Item.objects.order_by('-created_at')[:8]
#     return render(request, 'cineapp/home.html', {'top': top, 'recent': recent})

# def category_list(request, category):
#     items = Item.objects.filter(category=category).order_by('-created_at')
#     paginator = Paginator(items, 12)
#     page = request.GET.get('page')
#     items_page = paginator.get_page(page)
#     return render(request, 'cineapp/item_list.html', {'items': items_page, 'category': category})

# def item_detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     review_form = ReviewForm()
#     return render(request, 'cineapp/item_detail.html', {'item': item, 'review_form': review_form})

# @login_required
# def add_item(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             it = form.save(commit=False)
#             it.created_by = request.user
#             it.save()
#             form.save_m2m()  # Important: saves the MultiSelectField (genres)
#             messages.success(request, 'Item created.')
#             return redirect('cineapp:item_detail', pk=it.pk)
#     else:
#         form = ItemForm()
#     return render(request, 'cineapp/item_form.html', {'form': form})

# @login_required
# def edit_item(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.user != item.created_by:
#         messages.error(request, "You can only edit items you created.")
#         return redirect('cineapp:item_detail', pk=pk)
    
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             form.save()
#             form.save_m2m()  # Important: update genres
#             messages.success(request, 'Item updated.')
#             return redirect('cineapp:item_detail', pk=pk)
#     else:
#         form = ItemForm(instance=item)
    
#     return render(request, 'cineapp/item_form.html', {'form': form, 'item': item})

# @login_required
# def delete_item(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.user != item.created_by:
#         messages.error(request, "You can only delete items you created.")
#         return redirect('cineapp:item_detail', pk=pk)
    
#     if request.method == 'POST':
#         item.delete()
#         messages.success(request, 'Item deleted.')
#         return redirect('cineapp:home')
    
#     return render(request, 'cineapp/item_confirm_delete.html', {'item': item})

# @login_required
# def add_review(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             existing = Review.objects.filter(item=item, user=request.user)
#             if existing.exists():
#                 messages.error(request, "You have already reviewed this item. Edit your review instead.")
#                 return redirect('cineapp:item_detail', pk=pk)
#             rv = form.save(commit=False)
#             rv.item = item
#             rv.user = request.user
#             rv.save()
#             messages.success(request, 'Review added.')
#             return redirect('cineapp:item_detail', pk=pk)
#     return redirect('cineapp:item_detail', pk=pk)

# @login_required
# def edit_review(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.user != review.user:
#         messages.error(request, "You can only edit your own reviews.")
#         return redirect('cineapp:item_detail', pk=review.item.pk)
    
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, instance=review)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Review updated.')
#             return redirect('cineapp:item_detail', pk=review.item.pk)
#     else:
#         form = ReviewForm(instance=review)
    
#     return render(request, 'cineapp/review_form.html', {'form': form, 'review': review})

# @login_required
# def delete_review(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.user != review.user:
#         messages.error(request, "You can only delete your own reviews.")
#         return redirect('cineapp:item_detail', pk=review.item.pk)
    
#     if request.method == 'POST':
#         item_pk = review.item.pk
#         review.delete()
#         messages.success(request, 'Review deleted.')
#         return redirect('cineapp:item_detail', pk=item_pk)
    
#     return render(request, 'cineapp/review_confirm_delete.html', {'review': review})

# def about(request):
#     return render(request, 'cineapp/about.html')

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Message sent.')
#             return redirect('cineapp:contact')
#     else:
#         form = ContactForm()
#     return render(request, 'cineapp/contact.html', {'form': form})

# def user_profile(request, username):
#     from django.contrib.auth.models import User
#     user = get_object_or_404(User, username=username)
#     items = user.items.all()
#     reviews = user.reviews.all()
#     return render(request, 'cineapp/profile.html', {'profile_user': user, 'items': items, 'reviews': reviews})

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Registration successful.')
#             return redirect('cineapp:home')
#     else:
#         form = SignUpForm()
#     return render(request, 'cineapp/signup.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('cineapp:home')

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, f"Welcome, {user.username}!")
#             return redirect('cineapp:home')
#         else:
#             messages.error(request, "Invalid username or password")

#     return render(request, 'cineapp/login.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Review
from .forms import ItemForm, ReviewForm, ContactForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from .models import Item

# def home(request):
#     top = Item.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')[:8]
#     recent = Item.objects.order_by('-created_at')[:8]
#     return render(request, 'cineapp/home.html', {'top': top, 'recent': recent})


# def home(request):
#     genre_filter = request.GET.get('genre')  # Get selected genre
#     category_filter = request.GET.get('category')  # optional

#     items = Item.objects.all().order_by('-created_at')

#     if genre_filter:
#         items = items.filter(genres__contains=genre_filter)  # MultiSelectField contains

#     if category_filter:
#         items = items.filter(category=category_filter)

#     top = items.order_by('-reviews__rating')[:8]  # Example for top rated
#     recent = items.order_by('-created_at')[:8]

#     context = {
#         'items': items,
#         'top': top,
#         'recent': recent,
#         'genres': [choice[0] for choice in Item.GENRE_CHOICES],
#         'categories': [choice[0] for choice in Item.CATEGORY_CHOICES],
#         'selected_genre': genre_filter,
#         'selected_category': category_filter,
#     }
#     return render(request, 'cineapp/home.html', context)


def home(request):
    genre = request.GET.get('genre', '')
    category = request.GET.get('category', '')

    items = Item.objects.all()

    if genre:
        items = items.filter(genres__contains=[genre])  # MultiSelectField filter
    if category:
        items = items.filter(category=category)

    # Top rated items (avoid duplicates)
    top = items.annotate(avg_rating=Avg('reviews__rating')) \
               .order_by('-avg_rating') \
               .distinct()[:8]  # show top 8

    # Recent additions (avoid duplicates)
    recent = items.order_by('-created_at').distinct()[:8]

    # For dropdowns
    genres = [g[0] for g in Item.GENRE_CHOICES]
    categories = [c[0] for c in Item.CATEGORY_CHOICES]

    context = {
        'top': top,
        'recent': recent,
        'genres': genres,
        'categories': categories,
        'selected_genre': genre,
        'selected_category': category,
    }
    return render(request, 'cineapp/home.html', context)

def category_list(request, category):
    items = Item.objects.filter(category=category).order_by('-created_at')
    paginator = Paginator(items, 12)
    page = request.GET.get('page')
    items_page = paginator.get_page(page)
    return render(request, 'cineapp/item_list.html', {'items': items_page, 'category': category})

# def item_detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     review_form = ReviewForm()
#     return render(request, 'cineapp/item_detail.html', {'item': item, 'review_form': review_form})


from urllib.parse import urlparse, parse_qs

# def item_detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     review_form = ReviewForm()

#     video_id = None
#     if item.streaming_link:
#         if "youtu.be" in item.streaming_link:
#             # short link format
#             video_id = item.streaming_link.split('/')[-1]
#         elif "youtube.com" in item.streaming_link:
#             # normal youtube link
#             query = urlparse(item.streaming_link).query
#             params = parse_qs(query)
#             video_id = params.get('v', [None])[0]

#     context = {
#         'item': item,
#         'review_form': review_form,
#         'video_id': video_id,
#     }
#     return render(request, 'cineapp/item_detail.html', context)

# def item_detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     review_form = ReviewForm()

#     # 🎬 Extract YouTube video ID
#     video_id = None
#     if item.youtube_link:
#         if "youtu.be" in item.youtube_link:
#             video_id = item.youtube_link.split('/')[-1]
#         elif "youtube.com" in item.youtube_link:
#             query = urlparse(item.youtube_link).query
#             params = parse_qs(query)
#             video_id = params.get('v', [None])[0]

#     # ❤️ Check if the current user has favorited this item
#     is_favorited = False
#     if request.user.is_authenticated:
#         is_favorited = Favorite.objects.filter(user=request.user, item=item).exists()

#     context = {
#         'item': item,
#         'review_form': review_form,
#         'video_id': video_id,
#         'is_favorited': is_favorited,
#     }

#     return render(request, 'cineapp/item_detail.html', context)

# def item_detail(request, pk):
#     # Get the item or 404
#     item = get_object_or_404(Item, pk=pk)
    
#     # Review form
#     review_form = ReviewForm()

#     # 🎬 Extract YouTube video ID
#     video_id = None
#     if item.youtube_link:
#         if "youtu.be" in item.youtube_link:
#             video_id = item.youtube_link.split('/')[-1]
#         elif "youtube.com" in item.youtube_link:
#             query = urlparse(item.youtube_link).query
#             params = parse_qs(query)
#             video_id = params.get('v', [None])[0]

#     # ❤️ Check if the current user has favorited this item
#     is_favorited = False
#     if request.user.is_authenticated:
#         is_favorited = Favorite.objects.filter(user=request.user, item=item).exists()

#     # 🔄 Similar items (same category, exclude current)
#     similar_items = Item.objects.filter(category=item.category).exclude(pk=item.pk)[:4]

#     context = {
#         'item': item,
#         'review_form': review_form,
#         'video_id': video_id,
#         'is_favorited': is_favorited,
#         'similar_items': similar_items,
#     }

#     return render(request, 'cineapp/item_detail.html', context)

# @login_required
# def item_detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     review_form = ReviewForm()

#     # YouTube Video ID
#     video_id = None
#     if item.youtube_link:
#         if "youtu.be" in item.youtube_link:
#             video_id = item.youtube_link.split('/')[-1]
#         elif "youtube.com" in item.youtube_link:
#             query = urlparse(item.youtube_link).query
#             params = parse_qs(query)
#             video_id = params.get('v', [None])[0]

#     # Favorite
#     is_favorited = False
#     if request.user.is_authenticated:
#         is_favorited = Favorite.objects.filter(user=request.user, item=item).exists()
#         # Watchlist items for template
#         watchlist_items = Watchlist.objects.filter(user=request.user).values_list('item_id', flat=True)
#     else:
#         watchlist_items = []
        
    

#     context = {
#         'item': item,
#         'review_form': review_form,
#         'video_id': video_id,
#         'is_favorited': is_favorited,
#         'watchlist_items': watchlist_items,  # <-- pass list of item IDs
#     }

#     return render(request, 'cineapp/item_detail.html', context)



# from django.db.models import Q
# from urllib.parse import urlparse, parse_qs

# @login_required
# def item_detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     review_form = ReviewForm()

#     # Extract YouTube video ID
#     video_id = None
#     if item.youtube_link:
#         if "youtu.be" in item.youtube_link:
#             video_id = item.youtube_link.split('/')[-1]
#         elif "youtube.com" in item.youtube_link:
#             query = urlparse(item.youtube_link).query
#             params = parse_qs(query)
#             video_id = params.get('v', [None])[0]

#     # Favorite and Watchlist
#     is_favorited = False
#     if request.user.is_authenticated:
#         is_favorited = Favorite.objects.filter(user=request.user, item=item).exists()
#         watchlist_items = Watchlist.objects.filter(user=request.user).values_list('item_id', flat=True)
#     else:
#         watchlist_items = []

#     # ✅ Similar items (same category and sharing any genre text)
#     similar_items = Item.objects.filter(category=item.category).exclude(id=item.id)

#     # Refine similarity by checking overlapping genres manually
#     if item.genres:
#         # Convert genre list (MultiSelectField gives list)
#         item_genres = set(item.genres)
#         similar_items = [s for s in similar_items if set(s.genres).intersection(item_genres)]
#         # Limit to 4 items
#         similar_items = similar_items[:4]
#     else:
#         similar_items = similar_items[:4]

#     context = {
#         'item': item,
#         'review_form': review_form,
#         'video_id': video_id,
#         'is_favorited': is_favorited,
#         'watchlist_items': watchlist_items,
#         'similar_items': similar_items,
#     }

#     return render(request, 'cineapp/item_detail.html', context)



@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    review_form = ReviewForm()

    # -------------------------------
    # Extract YouTube video ID
    # -------------------------------
    video_id = None
    if item.youtube_link:
        if "youtu.be" in item.youtube_link:
            video_id = item.youtube_link.split('/')[-1]
        elif "youtube.com" in item.youtube_link:
            query = urlparse(item.youtube_link).query
            params = parse_qs(query)
            video_id = params.get('v', [None])[0]

    # -------------------------------
    # Favorite & Watchlist
    # -------------------------------
    is_favorited = Favorite.objects.filter(user=request.user, item=item).exists()
    watchlist_items = Watchlist.objects.filter(user=request.user).values_list('item_id', flat=True)

    # -------------------------------
    # Similar Items (same category & overlapping genres)
    # -------------------------------
    similar_items_qs = Item.objects.filter(category=item.category).exclude(id=item.id)
    similar_items = []

    if item.genres:
        item_genres_set = set(item.genres)
        for s in similar_items_qs:
            if set(s.genres).intersection(item_genres_set):
                similar_items.append(s)
                if len(similar_items) >= 4:  # Limit to 4 items
                    break
    else:
        similar_items = list(similar_items_qs[:4])

    # -------------------------------
    # Context
    # -------------------------------
    context = {
        'item': item,
        'review_form': review_form,
        'video_id': video_id,
        'is_favorited': is_favorited,
        'watchlist_items': watchlist_items,
        'similar_items': similar_items,
    }

    return render(request, 'cineapp/item_detail.html', context)





def category_items(request, category_name):
    # Start with all items in this category
    items = Item.objects.filter(category=category_name)

    # Get filters from GET request
    query = request.GET.get('q', '').strip()
    genre_filter = request.GET.get('genre', '').strip()

    # Filter by search query
    if query:
        items = items.filter(title__icontains=query)

    # Filter by genre
    if genre_filter:
        # MultiSelectField → filter manually in Python
        items = [i for i in items if i.genres and genre_filter in i.genres]

    # Get all genres for the dropdown
    all_genres = set()
    for i in Item.objects.filter(category=category_name):
        if i.genres:
            all_genres.update(i.genres)
    
    context = {
        'items': items,
        'category_name': category_name,
        'all_genres': sorted(all_genres),
    }
    return render(request, 'cineapp/item_list.html', context)









@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            it = form.save(commit=False)
            it.created_by = request.user
            it.save()
            form.save_m2m()  # Important: saves the MultiSelectField (genres)
            messages.success(request, 'Item created.')
            return redirect('cineapp:item_detail', pk=it.pk)
    else:
        form = ItemForm()
    return render(request, 'cineapp/item_form.html', {'form': form})

@login_required
# def edit_item(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.user != item.created_by:
#         messages.error(request, "You can only edit items you created.")
#         return redirect('cineapp:item_detail', pk=pk)
    
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             form.save()
#             form.save_m2m()  # Important: update genres
#             messages.success(request, 'Item updated.')
#             return redirect('cineapp:item_detail', pk=pk)
#     else:
#         form = ItemForm(instance=item)
    
#     return render(request, 'cineapp/item_form.html', {'form': form, 'item': item})

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item_instance = form.save(commit=False)  # save instance but not m2m yet
            item_instance.save()                     # save the instance
            form.save_m2m()                          # now save MultiSelectField/ManyToMany
            messages.success(request, "Item updated successfully!")
            return redirect('cineapp:home')
    else:
        form = ItemForm(instance=item)

    return render(request, 'cineapp/item_form.html', {'form': form, 'item': item})


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.user != item.created_by:
        messages.error(request, "You can only delete items you created.")
        return redirect('cineapp:item_detail', pk=pk)
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted.')
        return redirect('cineapp:home')
    
    return render(request, 'cineapp/item_confirm_delete.html', {'item': item})

@login_required
def add_review(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            existing = Review.objects.filter(item=item, user=request.user)
            if existing.exists():
                messages.error(request, "You have already reviewed this item. Edit your review instead.")
                return redirect('cineapp:item_detail', pk=pk)
            rv = form.save(commit=False)
            rv.item = item
            rv.user = request.user
            rv.save()
            messages.success(request, 'Review added.')
            return redirect('cineapp:item_detail', pk=pk)
    return redirect('cineapp:item_detail', pk=pk)

@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user != review.user:
        messages.error(request, "You can only edit your own reviews.")
        return redirect('cineapp:item_detail', pk=review.item.pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated.')
            return redirect('cineapp:item_detail', pk=review.item.pk)
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'cineapp/review_form.html', {'form': form, 'review': review})

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user != review.user:
        messages.error(request, "You can only delete your own reviews.")
        return redirect('cineapp:item_detail', pk=review.item.pk)
    
    if request.method == 'POST':
        item_pk = review.item.pk
        review.delete()
        messages.success(request, 'Review deleted.')
        return redirect('cineapp:item_detail', pk=item_pk)
    
    return render(request, 'cineapp/review_confirm_delete.html', {'review': review})

def about(request):
    return render(request, 'cineapp/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent.')
            return redirect('cineapp:contact')
    else:
        form = ContactForm()
    return render(request, 'cineapp/contact.html', {'form': form})

# def user_profile(request, username):
#     from django.contrib.auth.models import User
#     user = get_object_or_404(User, username=username)
#     items = user.items.all()
#     reviews = user.reviews.all()
#     return render(request, 'cineapp/profile.html', {'profile_user': user, 'items': items, 'reviews': reviews})

from django.contrib.auth.models import User
def user_profile(request, username):
    # Get the user whose profile is being viewed
    user = get_object_or_404(User, username=username)
    
    # User's own items and reviews
    items = user.items.all()  # Assuming Item has a 'created_by' ForeignKey to User
    reviews = user.reviews.all()  # Assuming Review has a 'user' ForeignKey
    
    # User's favorite items
    favorites = Favorite.objects.filter(user=user).select_related('item')
    
    # User's watchlist items
    watchlist_items = Watchlist.objects.filter(user=user).select_related('item')
    
    # Calculate watchlist progress
    total_watchlist = watchlist_items.count()
    watched_count = watchlist_items.filter(status='watched').count()
    watchlist_progress = int((watched_count / total_watchlist) * 100) if total_watchlist > 0 else 0
    
    context = {
        'profile_user': user,
        'items': items,
        'reviews': reviews,
        'favorites': favorites,
        'watchlist_items': watchlist_items,
        'watchlist_progress': watchlist_progress,
    }
    
    return render(request, 'cineapp/profile.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('cineapp:home')
    else:
        form = SignUpForm()
    return render(request, 'cineapp/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('cineapp:home')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('cineapp:home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'cineapp/login.html')


from .models import Item, Favorite

@login_required
def toggle_favorite(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, item=item)
    
    if not created:
        favorite.delete()  # remove favorite
    return redirect('cineapp:item_detail', pk=item.id)



from .models import Watchlist
@login_required
def toggle_watchlist(request, pk):
    item = get_object_or_404(Item, pk=pk)
    obj, created = Watchlist.objects.get_or_create(user=request.user, item=item)

    if not created:
        obj.delete()  # remove from watchlist if already exists

    return redirect('cineapp:item_detail', pk=item.pk)


from .models import Review, ReviewReply
from .forms import ReviewReplyForm

@login_required
def add_reply(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'POST':
        form = ReviewReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.review = review
            reply.save()
    return redirect('cineapp:item_detail', pk=review.item.pk)


@login_required
def delete_reply(request, pk):
    reply = get_object_or_404(ReviewReply, pk=pk)
    
    if request.user != reply.user:
        messages.error(request, "You are not allowed to delete this reply.")
        return redirect('cineapp:item_detail', pk=reply.review.item.pk)
    
    item_pk = reply.review.item.pk
    reply.delete()
    messages.success(request, "Reply deleted successfully.")
    return redirect('cineapp:item_detail', pk=item_pk)

# from .models import Reply
# @login_required
# def delete_reply(request, pk):
#     reply = get_object_or_404(Reply, pk=pk)
#     if request.user == reply.user:
#         review_item_id = reply.review.id  # to redirect to the item's detail page
#         reply.delete()
#         return redirect('cineapp:item_detail', pk=review_item_id)
#     else:
#         return redirect('cineapp:item_detail', pk=reply.review.id)
    



def category_items(request, category_name):
    # Start with all items in this category
    items_qs = Item.objects.filter(category=category_name)

    # Get search query and genre filter from GET request
    query = request.GET.get('q', '').strip()
    genre_filter = request.GET.get('genre', '').strip()

    # Filter by search query
    if query:
        items_qs = items_qs.filter(title__icontains=query)

    # Filter by genre (MultiSelectField)
    if genre_filter:
        items_qs = [i for i in items_qs if i.genres and genre_filter in i.genres]

    # Collect all genres for dropdown
    all_genres = set()
    for i in Item.objects.filter(category=category_name):
        if i.genres:
            all_genres.update(i.genres)

    context = {
        'items': items_qs,
        'category_name': category_name,
        'all_genres': sorted(all_genres),
        'selected_genre': genre_filter,
        'search_query': query,
    }
    return render(request, 'cineapp/item_list.html', context)