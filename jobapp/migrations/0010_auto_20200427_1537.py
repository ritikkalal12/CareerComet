from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0009_auto_20200427_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_description',
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(),
        ),
    ]
