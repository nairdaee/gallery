from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        Location.objects.filter().delete()

    @classmethod
    def get_location(cls):
        location_found = cls.objects.all()
        return location_found

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        Category.objects.filter().delete()


class Photos(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank= True)
    owner = models.ForeignKey(User, default= None)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
      return self.title

    def snippet(self):
        return self.body[:30] + '...'

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def all_photos(cls):
        photos = cls.objects.all()
        return photos
    @classmethod
    def search_by_category(cls,search_term):
        searched_photos = cls.objects.filter(category__category__icontains=search_term)
        return searched_photos

    @classmethod
    def filter_by_location(cls,location_filter):
        located_photos = Photos.objects.filter(location__id=location_filter)
        return located_photos

    @classmethod
    def get_photo_by_id(cls, id):
        photos = Photos.objects.get(id=id)
        return photos

