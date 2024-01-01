from django.db import models

# Create your models here.
class subscription(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return'{} - {}'.format(self.name,self.email)



class contacts(models.Model):
    fname = models.CharField(max_length = 64)
    lname = models.CharField(max_length = 64)
    email = models.CharField(max_length = 64)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return'{}  -  {}'.format(self.timestamp,self.email)



class Corona(models.Model):
    global_table = models.CharField(max_length=99999)
    pakistan_table = models.CharField(max_length=99999)
    pak_stats = models.CharField(max_length=99999)
    global_stats = models.CharField(max_length=99999)


    class Meta:
        verbose_name_plural = 'Corona'