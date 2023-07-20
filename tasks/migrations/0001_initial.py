# Generated by Django 4.2.1 on 2023-07-20 11:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authuser', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('created', models.DateField(auto_created=True, default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('driver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_id', to='authuser.driver')),
                ('order_id', models.ManyToManyField(related_name='orders', to='orders.order')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
