# Generated by Django 4.2.6 on 2023-11-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_fotografia_publicada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('MAMÍFERO', 'Mamífero'), ('AVE', 'Ave'), ('RÉPTIL', 'Réptil'), ('INSETO/ARACNÍDEO', 'Inseto/Aracnídeo'), ('ANFÍBIO', 'Anfíbio'), ('PEIXES', 'Peixes'), ('CRUSTÁCEO', 'Crustáceo'), ('OUTROS', 'Outros')], default='', max_length=100),
        ),
    ]