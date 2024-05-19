from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),  # reemplaza esto con el nombre de tu última migración
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='is_active',
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_active',
            field=models.SmallIntegerField(default=0, choices=[(0, 'EN PROCESO'), (1, 'PROCESADA'), (2, 'CONFIRMADA'), (3, 'CANCELADA'), (4, 'REPROGRAMADA'), (5, 'FINALIZADA')]),
        ),
    ]
