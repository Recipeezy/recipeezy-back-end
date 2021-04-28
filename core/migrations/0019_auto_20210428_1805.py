# Generated by Django 3.2 on 2021-04-28 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210428_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pantry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_pantry', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipehistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_recipehistory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='selectedrecipes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_recipes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_shoppinglist', to=settings.AUTH_USER_MODEL),
        ),
    ]
