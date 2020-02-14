# Generated by Django 3.0.3 on 2020-02-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=128)),
                ('author', models.CharField(blank=True, default='', max_length=20)),
                ('pw', models.CharField(blank=True, default='', max_length=12)),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]