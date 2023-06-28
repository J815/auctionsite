from django.db import models

# Create your models here.



class User(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class AuctionItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_photo = models.ImageField(upload_to='auction_items')
    minimum_bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    auction_end_datetime = models.DateTimeField()