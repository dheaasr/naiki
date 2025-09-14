from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
    ]

    RATING_CHOICES = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    thumbnail = models.URLField(default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgLNLbFmOl-wuybKGc6IrdKYGPxe62xr-wYA&s")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='men')
    comment = models.TextField() #implementasinya nanti aja
    rating = models.IntegerField(choices=RATING_CHOICES, default=5) #nanti
    is_featured = models.BooleanField()
    likes = models.IntegerField(default=0)

    # increment = models.IntegerField(default=0)
    # rate_store = models.IntegerField(default=0)
    # rate_result = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def increment_likes(self):
        self.likes += 1
        self.save()


    # def avg_rating(self): TODO perlu ditinjau lebih lanjut buat handle biar 1 user cuma punya 1 rating
    #     self.rate_store += self.rating
    #     self.increment+=1
    #     self.rate_result = self.rate_store / self.increment
    #     self.save()


    #TODO bikin method buat average rating lalu dikembalikan ke self.rating = ini avg nya tambahin var index++. methodnya di sini
    #TODO bikin add.html, show.html, rating.html. gimana caranya bikin form rating? = tambahin method di forms.py buat rating trs bikin html sendiri
    #price, category, rating, is_featured