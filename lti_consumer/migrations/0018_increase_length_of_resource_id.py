# Generated by Django 3.2.23 on 2023-12-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lti_consumer', '0017_lticonfiguration_lti_1p3_redirect_uris'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ltiagslineitem',
            name='resource_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]