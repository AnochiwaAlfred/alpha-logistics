# Generated by Django 4.2.1 on 2023-07-20 11:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('created', models.DateField(auto_created=True, default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
            options={
                'verbose_name': 'Sub Category',
                'verbose_name_plural': 'Sub Categories',
            },
        ),
    ]
