# Generated by Django 2.0.5 on 2018-08-23 17:15

from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[news.validators.validate_file_extension]),
        ),
    ]
