# Generated by Django 3.2.9 on 2021-12-26 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_navbar_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='menu_slug',
            field=models.SlugField(default=None, max_length=200),
        ),
    ]
