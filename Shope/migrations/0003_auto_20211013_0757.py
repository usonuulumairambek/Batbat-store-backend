# Generated by Django 3.2.8 on 2021-10-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shope', '0002_auto_20211012_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('orderId',)},
        ),
        migrations.AddField(
            model_name='category',
            name='orderId',
            field=models.IntegerField(null=True),
        ),
    ]
