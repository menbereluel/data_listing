# from django.db import models
# class Category(models.Model):
#     name=models.CharField(max_length=28)

# class Tag(models.Model):
#     name=models.CharField(max_length=28)
# class Product(models.Model):
#     name=models.CharField(max_length=50)
#     stock=models.IntegerField()
#     price=models.DecimalField(decimal_places=2,max_digits=6)
#     description=models.TextField()
#     category=models.ForeignKey(Category,null=True, on_delete=models.PROTECT)
#     tags=models.ManyToManyField(Tag, blank=True)

# def __str__(self):
#     return self.name


from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Subscription(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"Name: {self.name}, price: {self.price}"
