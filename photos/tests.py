from django.test import TestCase
from .models import Location,Category,Photos

class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(location='Nairobi')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_location(self):
        self.nairobi.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.clout = Category(category='Goals')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.clout,Category))

    def test_save_method(self):
        self.clout.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)  

    def test_delete_category(self):
        self.clout.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class PhotosTestCase(TestCase):
    def setUp(self):
        self.buru = Location(location='Buru')
        self.buru.save_location()

        self.sports = Category(category='Sports')
        self.sports.save_category()

        self.new_photo = Photos(title='Any',body='Caption',location=self.buru,category=self.sports)
        self.new_photo.save_photo()

    def test_save_image(self):
        self.photo_test.save()
        photos = Photos.objects.all()
        self.assertTrue(len(photos)>0)

    def test_delete_photo(self):
        self.photo_test.save()
        self.photo_test.delete()
        photos  = Photos.objects.all()
        self.assertTrue(len(photos)==0)

    def test_get_photo_by_id(self):
        found_photo = self.photo_test.get_photo_by_id(self.photo_test.id)
        img = Photos.objects.filter(id=self.photo_test.id)
        self.assertTrue(found_photo,img)
