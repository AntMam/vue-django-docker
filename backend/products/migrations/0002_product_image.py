# Generated by Django 3.1.3 on 2021-10-20 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
