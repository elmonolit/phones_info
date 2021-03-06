# Generated by Django 3.1.4 on 2021-01-10 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200, verbose_name='Бренд')),
                ('brand_logo', models.ImageField(upload_to='brand_logos', verbose_name='Логотип')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Phone_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_model', models.CharField(max_length=200, verbose_name='Модель')),
                ('phone_image', models.ImageField(upload_to='phones', verbose_name='Фото телефона')),
                ('phone_specs', models.TextField(verbose_name='Спецификации')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('phone_brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='showcase.brand', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
        migrations.AddField(
            model_name='brand',
            name='models_list',
            field=models.ManyToManyField(blank=True, to='showcase.Phone_model', verbose_name='Список моделей'),
        ),
    ]
