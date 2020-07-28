# Generated by Django 2.2.13 on 2020-07-28 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=256)),
                ('todos_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField(default=0, verbose_name='Значение приритета')),
                ('todos_count', models.PositiveIntegerField(default=0, verbose_name='Количество задач')),
            ],
            options={
                'verbose_name': 'Приоритеты',
                'verbose_name_plural': 'Приоритеты',
            },
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='описание')),
                ('is_completed', models.BooleanField(default=False, verbose_name='выполнено')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(choices=[(1, 'Высокий приоритет'), (2, 'Средний приоритет'), (3, 'Низкий приоритет')], default=2, verbose_name='Приоритет')),
                ('category', models.ManyToManyField(blank=True, to='tasks.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Задачи',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
