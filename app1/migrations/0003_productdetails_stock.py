# Generated by Django 5.0.1 on 2024-01-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_productdetails_imagename_productbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='Stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
