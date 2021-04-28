# Generated by Django 3.2 on 2021-04-27 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210427_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='pantry',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='shoppinglist',
        ),
        migrations.AddField(
            model_name='pantry',
            name='ingredients',
            field=models.ManyToManyField(blank=True, null=True, related_name='pantry_ingredients', to='core.Ingredient'),
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='ingredients',
            field=models.ManyToManyField(blank=True, null=True, related_name='shoppinglist_ingredients', to='core.Ingredient'),
        ),
    ]
