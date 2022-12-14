# Generated by Django 4.1.1 on 2022-10-02 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('translation', models.CharField(max_length=200)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('point', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
