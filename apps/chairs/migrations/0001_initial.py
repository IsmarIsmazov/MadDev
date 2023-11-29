# Generated by Django 4.2.7 on 2023-11-20 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('height', models.IntegerField(default=0, verbose_name='Высота')),
                ('depth', models.IntegerField(default=0, verbose_name='Глубина')),
                ('in_stock', models.BooleanField()),
                ('pickup', models.BooleanField()),
                ('delivery', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairs.category', verbose_name='Категория')),
                ('material', models.ManyToManyField(to='chairs.material', verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Стул',
                'verbose_name_plural': 'Стулья',
            },
        ),
    ]