# Generated by Django 3.2.4 on 2021-06-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='name',
            field=models.CharField(default='Munchme', max_length=500),
            preserve_default=False,
        ),
    ]
