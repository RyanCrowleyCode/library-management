from django.db import models
from .library import Library

class Book(models.Model):

    title = models.CharField(max_length=50)
    ISBN_number = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = IntegerField
    location = models.ForeignKey(Library, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("book")
        verbose_name_plural = ("books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})