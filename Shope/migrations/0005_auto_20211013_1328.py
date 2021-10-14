# Generated by Django 3.2.8 on 2021-10-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shope', '0004_auto_20211013_1307'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('orderId',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('orderId',)},
        ),
        migrations.AddField(
            model_name='image',
            name='orderId',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='orderId',
            field=models.IntegerField(null=True),
        ),
    ]
