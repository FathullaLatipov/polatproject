# Generated by Django 4.2.11 on 2024-04-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyixa', '0003_alter_zapchast_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='maxsulot',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]