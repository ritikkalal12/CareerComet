from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='catagory',
            new_name='category',
        ),
    ]
