from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_auto_20200426_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(blank=True),
        ),
    ]
