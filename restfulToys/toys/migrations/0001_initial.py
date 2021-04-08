# Generated by Django 2.2.20 on 2021-04-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=150)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('category', models.CharField(default='', max_length=200)),
                ('release_date', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]