from django import forms
from .models import Item, Review, ContactMessage,Favorite,Watchlist,ReviewReply
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from multiselectfield import MultiSelectFormField

# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = [
#             'title',
#             'description',
#             'category',
#             'poster',
#             'release_year',
#             'streaming_link',   # ✅ Add this
#             'genres', 
#             'youtube_link',# ✅ Add this
#         ]
#         widgets = {
#             'description': forms.Textarea(attrs={'rows':4}),
#             'genres': forms.CheckboxSelectMultiple()
#         }


class ReviewReplyForm(forms.ModelForm):
    class Meta:
        model = ReviewReply
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Reply...', 'class': 'form-control form-control-sm'})
        }

class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = []

class ItemForm(forms.ModelForm):
    genres = MultiSelectFormField(
        choices=Item.GENRE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Item
        fields = [
            'title',
            'description',
            'category',
            'poster',
            'release_year',
            'streaming_link',      # ✅ Streaming link
            'youtube_link',        # ✅ YouTube link
            'theatrical_experience', # ✅ Theatrical experience
            'genres', 
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows':3}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows':4}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
