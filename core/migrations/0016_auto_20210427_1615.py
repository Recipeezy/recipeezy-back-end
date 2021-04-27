# Generated by Django 3.2 on 2021-04-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210427_0307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='pantry',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='pantry',
            field=models.ManyToManyField(blank=True, null=True, related_name='pantry_ingredients', to='core.Pantry'),
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='shoppinglist',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='shoppinglist',
            field=models.ManyToManyField(blank=True, null=True, related_name='shoppinglist_ingredients', to='core.ShoppingList'),
        ),
    ]
