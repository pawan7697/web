# Generated by Django 3.2.9 on 2021-12-26 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.category'),
        ),
    ]
