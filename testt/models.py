from django.db import models
from smart_selects.db_fields import GroupedForeignKey , ChainedForeignKey , ChainedManyToManyField
# Create your models here.

class Continent(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Country(models.Model):
    continent = models.ForeignKey(Continent , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Location(models.Model):
    continent = models.ForeignKey(Continent , on_delete=models.CASCADE)
    country = ChainedForeignKey(
        Country,
        chained_field="continent",
        chained_model_field="continent",
        show_all = False , 
        auto_choose=True ,
        default=None)

    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    def __str__(self):
        return str(self.country)


class Location2(models.Model):
    continent = models.ForeignKey(Continent , on_delete=models.CASCADE)
    country = GroupedForeignKey(Country,"continent")
    # area = ForeignKey(Area)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)

    def __str__(self):
        return str(self.country)




class Publication(models.Model):
    name = models.CharField(max_length=255)

class Writer(models.Model):
    name = models.CharField(max_length=255)
    publications = models.ManyToManyField('Publication', blank=True, null=True)

class Book(models.Model):
    publication = models.ForeignKey(Publication ,on_delete=models.CASCADE)
    writer = ChainedManyToManyField(
        Writer,
        horizontal=True,
        verbose_name='writer',
        chained_field="publication",
        chained_model_field="publications")
    name = models.CharField(max_length=255)