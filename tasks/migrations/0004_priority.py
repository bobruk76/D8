# Generated by Django 2.2.13 on 2020-07-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200724_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField(default=0)),
                ('todos_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
