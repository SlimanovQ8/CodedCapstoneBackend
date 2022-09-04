# Generated by Django 4.1 on 2022-09-01 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tbr3at', '0002_alter_annoucement_charity_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tbr3at.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Like New', 'Like New'), ('Used', 'Used')], max_length=15, null=True),
        ),
    ]