# Generated by Django 4.1.7 on 2023-04-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='remark',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]