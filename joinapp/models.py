from django.db import models



class Author(models.Model):
    name = models.CharField(max_length=30)


class Course(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='course')

