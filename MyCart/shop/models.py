from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.IntegerField(max_length=200)
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pud_date=models.DateField()
    image=models.ImageField(upload_to='images')#image=models.ImageField(upload_to='shop/images',default="")
    #location=models.ForeignKey(location, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Location(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'



class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Destination:
    id:int
    name:str
    img:str
    desc:str
    price:int

