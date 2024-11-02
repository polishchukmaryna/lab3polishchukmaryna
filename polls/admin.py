from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Author, Book, Purchases, Reader, Shop, Feedback

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Purchases)
admin.site.register(Reader)
admin.site.register(Shop)
admin.site.register(Feedback)
#  admin.site.register(AuthorBook)
