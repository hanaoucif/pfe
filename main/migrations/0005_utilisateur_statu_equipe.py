# Generated by Django 5.0.3 on 2024-03-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_utilisateur_email_utilisateur_nom_utilisateur_prenom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='STATU_equipe',
            field=models.BooleanField(default=True),
        ),
    ]
