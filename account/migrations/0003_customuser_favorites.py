# Generated by Django 3.2.8 on 2021-10-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shope', '0001_initial'),
        ('account', '0002_auto_20211022_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorites',
            field=models.ManyToManyField(blank=True, null=True, to='Shope.Product'),
        ),
    ]