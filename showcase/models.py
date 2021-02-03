from django.db import models
from pytils.translit import slugify
from django.urls import reverse_lazy

# class Product(models.Model):
#     type = models.

class Brand(models.Model):
    brand_name = models.CharField(max_length=200,verbose_name='Бренд')
    models_list = models.ManyToManyField('Phone_model',verbose_name='Список моделей', blank=True)
    brand_logo = models.ImageField(upload_to='brand_logos', verbose_name='Логотип')
    slug = models.SlugField(blank=True,unique=True)

    def __str__(self):
        return self.brand_name

    def save(self):
        self.slug = slugify(self.brand_name)
        super(Brand,self).save()

    def  get_absolute_url(self):
        return reverse_lazy('brand_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Phone_model(models.Model):
    phone_brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, verbose_name='Производитель')
    phone_model = models.CharField(max_length=200, verbose_name='Модель')
    phone_image = models.ImageField(upload_to='phones',verbose_name='Фото телефона')
    phone_specs = models.TextField(verbose_name='Спецификации')
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return str(self.phone_brand)+" "+ str(self.phone_model)

    def save(self):
        self.slug = slugify(str(self.phone_brand)+str(self.phone_model))
        super(Phone_model,self).save()
        brand = Brand.objects.filter(brand_name=str(self.phone_brand)).first()
        brand.models_list.add(self)
        brand.save()

    def  get_absolute_url(self):
        return reverse_lazy('phone_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
