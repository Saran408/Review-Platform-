# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models import Avg

# # Create your models here.



# class Item(models.Model):
#     CATEGORY_CHOICES = [
#         ('Movie', 'Movie'),
#         ('Series', 'Series'),
#         ('Book', 'Book'),
#     ]
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
#     poster = models.ImageField(upload_to='posters/', blank=True, null=True)
#     release_year = models.IntegerField(blank=True, null=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def average_rating(self):
#         agg = self.reviews.aggregate(avg=Avg('rating'))
#         return round(agg['avg'] or 0, 1)

#     def reviews_count(self):
#         return self.reviews.count()

#     def __str__(self):
#         return f"{self.title} ({self.category})"


# class Review(models.Model):
#     RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
#     item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
#     comment = models.TextField()
#     rating = models.IntegerField(choices=RATING_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"{self.user.username} - {self.item.title} ({self.rating})"


# class ContactMessage(models.Model):
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     subject = models.CharField(max_length=120)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"From {self.name}: {self.subject}"




from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from multiselectfield import MultiSelectField


# class Item(models.Model):
#     CATEGORY_CHOICES = [
#         ('Movie', 'Movie'),
#         ('Series', 'Series'),
#         ('Book', 'Book'),
#     ]

#     GENRE_CHOICES = [
#         ('Crime', 'Crime'),
#         ('Thriller', 'Thriller'),
#         ('Love', 'Love'),
#         ('Action', 'Action'),
#         ('Comedy', 'Comedy'),
#         ('Drama', 'Drama'),
#         ('Horror', 'Horror'),
#         ('Sci-Fi', 'Sci-Fi'),
#         ('Fantasy', 'Fantasy'),
#     ]

#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
#     poster = models.ImageField(upload_to='posters/', blank=True, null=True)
#     release_year = models.IntegerField(blank=True, null=True)
#     streaming_link = models.URLField(blank=True, null=True)  # Optional streaming link
#     genres = MultiSelectField(choices=GENRE_CHOICES, blank=True)  # Dropdown multiple select
#     youtube_link = models.URLField(blank=True, null=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
#     created_at = models.DateTimeField(auto_now_add=True)

#     # Optional: maximum allowed dimensions
#     MAX_WIDTH = 1000
#     MAX_HEIGHT = 700

#     def save(self, *args, **kwargs):
#         if self.poster:
#             try:
#                 img = Image.open(self.poster)
#                 img_format = img.format  # Keep original format (JPEG, PNG, etc.)

#                 # Resize if image exceeds max dimensions, maintaining aspect ratio
#                 if img.width > self.MAX_WIDTH or img.height > self.MAX_HEIGHT:
#                     img.thumbnail((self.MAX_WIDTH, self.MAX_HEIGHT), Image.Resampling.LANCZOS)

#                     # Save resized image back to the ImageField
#                     img_io = BytesIO()
#                     if img_format == 'PNG':
#                         img.save(img_io, format='PNG', quality=95)
#                     else:
#                         img = img.convert("RGB")  # Ensure JPEG format is RGB
#                         img.save(img_io, format='JPEG', quality=90)

#                     # Replace the original image
#                     self.poster.save(self.poster.name, ContentFile(img_io.getvalue()), save=False)

#             except Exception as e:
#                 raise ValidationError(f"Invalid image file. {str(e)}")

#         super().save(*args, **kwargs)

#     def average_rating(self):
#         agg = self.reviews.aggregate(avg=Avg('rating'))
#         return round(agg['avg'] or 0, 1)

#     def reviews_count(self):
#         return self.reviews.count()

#     def __str__(self):
#         return f"{self.title} ({self.category})"


class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Movie', 'Movie'),
        ('Series', 'Series'),
        ('Book', 'Book'),
    ]

    GENRE_CHOICES = [
        ('Crime', 'Crime'),
        ('Thriller', 'Thriller'),
        ('Love', 'Love'),
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Fantasy', 'Fantasy'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    streaming_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True, help_text="Add YouTube link (full URL)")
    genres = MultiSelectField(choices=GENRE_CHOICES, blank=True)
    theatrical_experience = models.CharField(max_length=200, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)

    MAX_WIDTH = 1000
    MAX_HEIGHT = 700

    def save(self, *args, **kwargs):
        if self.poster:
            try:
                img = Image.open(self.poster)
                img_format = img.format
                if img.width > self.MAX_WIDTH or img.height > self.MAX_HEIGHT:
                    img.thumbnail((self.MAX_WIDTH, self.MAX_HEIGHT), Image.Resampling.LANCZOS)
                    img_io = BytesIO()
                    if img_format == 'PNG':
                        img.save(img_io, format='PNG', quality=95)
                    else:
                        img = img.convert("RGB")
                        img.save(img_io, format='JPEG', quality=90)
                    self.poster.save(self.poster.name, ContentFile(img_io.getvalue()), save=False)
            except Exception as e:
                raise ValidationError(f"Invalid image file. {str(e)}")
        super().save(*args, **kwargs)

    def average_rating(self):
        agg = self.reviews.aggregate(avg=Avg('rating'))
        return round(agg['avg'] or 0, 1)

    def reviews_count(self):
        return self.reviews.count()

    def __str__(self):
        return f"{self.title} ({self.category})"


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.item.title} ({self.rating})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.name}: {self.subject}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')

    def __str__(self):
        return f"{self.user.username} ❤️ {self.item.title}"
    

class Watchlist(models.Model):
    STATUS_CHOICES = [
        ('watching', 'Watching'),
        ('watched', 'Watched')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='watching')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')
        
        
class ReviewReply(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.username} on {self.review.id}"
