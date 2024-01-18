# Generated by Django 4.2.3 on 2024-01-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Description', models.CharField(max_length=450)),
                ('Storagespace', models.IntegerField()),
                ('Imagename', models.CharField(max_length=100)),
            ],
        ),
    ]
