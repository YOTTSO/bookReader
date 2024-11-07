import os
from django.db import models
from django.core.validators import RegexValidator

my_validator = RegexValidator(r"[a-zA-Z0-9]+\.(txt|pdf|fb2|doc)", "Your book must be in format = filename.file_format")


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    tags = models.CharField(max_length=250, blank=False)
    file = models.FileField(upload_to="./repository/")

    def save(self, *args, **kwargs):
        file_base, file_extension = os.path.splitext(self.file.name)
        self.file.name = f"{self.title}_{self.author}{file_extension}"
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

