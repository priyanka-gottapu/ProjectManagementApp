from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField()
    describe = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Tasks(models.Model):
    name = models.CharField(max_length=20)
    describe = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TaskList(models.Model):
    name = models.CharField(max_length=20)
    describe = models.CharField(max_length=20)

    def __str__(self):
        return self.name