# Generated by Django 2.1.7 on 2020-12-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gr33kLibrary', '0020_article_article_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_link',
            field=models.TextField(default='', null=True),
        ),
    ]