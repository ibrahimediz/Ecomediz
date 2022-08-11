from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    @staticmethod
    def get_all_categories():
        return Category.objects.all() # ORM: Object Relational Mapping

    def __str__(self):
        return self.name

