from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# create your models here.


class Proyek(models.Model):
    ITEM_CHOICES = [
        ('SQL', 'SQL'),
        ('Power BI', 'Power BI'),
        ('Tableau', 'Tableau'),
        ('Python Dash', 'Python Dash'),
        ('Python Django', 'Python Django'),
        ('Data Science', 'Data Sciance')
    ]
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=250)
    category = models.CharField(choices=ITEM_CHOICES, max_length=250)
    gambar = models.ImageField(upload_to='media', blank=True)
    gambar2 = models.ImageField(upload_to='media', blank=True)
    gambar3 = models.ImageField(upload_to='media', blank=True)
    gambar4 = models.ImageField(upload_to='media', blank=True)
    tanggal = models.DateField(default=timezone.now)
    client = models.CharField(max_length=55)
    output = models.URLField(default='a')
    detail = models.URLField(default='a')
    embed= models.TextField(blank=True, max_length=500)
    slug = models.SlugField(blank=True, editable=False)


    def __str__(self):
        return "{} - {}".format(self.nama, self.category)
    
    def save(self):
        self.slug = slugify(self.nama)
        super(Proyek, self).save()
            

