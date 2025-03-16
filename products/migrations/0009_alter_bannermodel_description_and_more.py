# Generated by Django 5.1.6 on 2025-03-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_bannermodel_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannermodel',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banners/'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='name_en',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='name_ru',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='name_uz',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='name'),
        ),
    ]
