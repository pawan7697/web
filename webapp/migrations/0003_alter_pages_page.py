# Generated by Django 3.2.9 on 2021-12-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='page',
            field=models.TextField(),
        ),
    ]