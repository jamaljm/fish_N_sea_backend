from django.db import models

# Create your models here.


class customer(models.Model):
    name = models.TextField(blank=False)
    email = models.EmailField(blank=True,null=True)
    location= models.TextField(blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)
    password2 = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name  





class retailers(models.Model):
    name = models.TextField(blank=False)
    email = models.EmailField(blank=True,null=True)
    location= models.TextField(blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)
    password2 = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name


class fishermen(models.Model):
    name = models.TextField(blank=False)
    email = models.EmailField(blank=True,null=True)
    location= models.TextField(blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)
    password2 = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name



class fish1(models.Model):
    retailers = models.ForeignKey(retailers,on_delete=models.CASCADE,null=True,blank=True)
    fishermen = models.ForeignKey(fishermen,on_delete=models.CASCADE,null=True,blank=True)
    name = models.TextField(blank=False)
    price = models.IntegerField(blank=False)
    description = models.TextField(blank=True,null=True)
    image = models.TextField(default="/images/f4.jpg")

    
    def __str__(self):
        return self.name


class fish2(models.Model):
    user = models.ForeignKey(fishermen,on_delete=models.CASCADE)
    name = models.TextField(blank=False)
    price = models.IntegerField(blank=False)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name


class fishcount(models.Model):
    name = models.TextField(blank=False)
    rating = models.IntegerField(blank=False)
    
    
    def __str__(self):
        return self.name