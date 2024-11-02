# Create your models here.
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    pseudonym = models.CharField(max_length=20, blank=True, null=True)
    name_field = models.CharField(db_column='name_', max_length=20, blank=True, null=True)  # Field renamed because it ended with '_'.
    surname = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    book = models.ManyToManyField('Book', related_name='authors')

    class Meta:
        managed = True
        db_table = 'author'

    def __str__(self):
        if self.pseudonym:
            return self.pseudonym
        elif self.name_field and self.surname:
            return f"{self.name_field} {self.surname}"
        elif self.name_field:
            return self.name_field
        elif self.surname:
            return self.surname
        return "Unknown Author"


# class AuthorBook(models.Model):
#     author = models.OneToOneField(Author, on_delete=models.CASCADE)  # The composite primary key (author_id, book_id) found, that is not supported. The first column is selected.
#     book = models.ForeignKey('Book', on_delete=models.CASCADE)
#
#     class Meta:
#         managed = False
#         db_table = 'author_book'
#         unique_together = (('author', 'book'),)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name_field = models.CharField(db_column='name_', max_length=50)  # Field renamed because it ended with '_'.
    price_uah = models.IntegerField(db_column='price_UAH')  # Field name made lowercase.
    pages = models.IntegerField()
    genre = models.CharField(db_column='genre', max_length=50)

    class Meta:
        managed = True
        db_table = 'book'

    def __str__(self):
        return self.name_field


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey('Purchases', on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)
    rating = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'feedback'

    def __str__(self):
        return f"Feedback number {self.feedback_id} on book '{self.purchase.book}' by reader {self.purchase.reader}"


class Purchases(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    reader = models.ForeignKey('Reader', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, blank=True, null=True)
    purchase_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'purchases'

    def __str__(self):
        return f"Purchase number {self.purchase_id} by {self.reader} - {self.book} on {self.purchase_date}"


class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    name_field = models.CharField(db_column='name_', max_length=20)  # Field renamed because it ended with '_'.
    surname = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'reader'

    def __str__(self):
        return f"{self.name_field} {self.surname}"


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    town = models.CharField(max_length=20)
    adress = models.CharField(unique=True, max_length=30)
    hotline = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shop'

    def __str__(self):
        return self.adress