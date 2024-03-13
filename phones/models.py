from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='image/', verbose_name="Изображение", default='default.png')
    release_date = models.DateField(default=timezone.now)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(name, default=name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

