# Generated by Django 3.2.8 on 2021-10-12 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=225)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Children', to='Shope.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product/uploads/%Y/%m/%d/')),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=125)),
                ('size', models.FloatField()),
                ('seller', models.CharField(max_length=225)),
                ('in_line', models.IntegerField()),
                ('lines', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shope.category')),
            ],
        ),
    ]
