# Generated by Django 5.0 on 2023-12-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('extracted_keyword', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=500)),
                ('decription', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
    ]
