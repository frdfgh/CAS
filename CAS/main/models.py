from django.db import models


# Create your models here.

# class Category(models.Model):
#     Title = models.CharField(max_length=50)
#     slug = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.Title


class User(models.Model):
    StudentID = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    # photo = models.ImageField(upload_to="images")
    # excerpt = models.TextField()
    # content = models.TextField()
    # date = models.DateTimeField()
    # file = models.FileField(upload_to="files")
    # helpFile = models.FileField(upload_to="help_files")
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.StudentID
