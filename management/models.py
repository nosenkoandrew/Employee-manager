import mptt
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


mptt.register(Category, order_insertion_by=['name'])


class Employee(MPTTModel):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    position = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    salary = models.IntegerField(default="0", blank=True, null=True)
    created_time = models.DateTimeField(null=True, auto_now_add=True, auto_now=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.position}"


mptt.register(Employee, order_insertion_by=['first_name'])
