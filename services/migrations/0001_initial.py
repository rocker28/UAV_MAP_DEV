# Generated by Django 5.0 on 2024-08-20 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('email_id', models.EmailField(max_length=95)),
                ('country_code', models.CharField(choices=[('+93', 'Afghanistan'), ('+355', 'Albania'), ('+213', 'Algeria'), ('+1', 'American Samoa'), ('+376', 'Andorra'), ('+244', 'Angola'), ('+1', 'Anguilla'), ('+54', 'Argentina'), ('+374', 'Armenia'), ('+297', 'Aruba'), ('+61', 'Australia'), ('+43', 'Austria'), ('+994', 'Azerbaijan'), ('+1', 'Bahamas'), ('+973', 'Bahrain'), ('+880', 'Bangladesh'), ('+1', 'Barbados'), ('+375', 'Belarus'), ('+32', 'Belgium'), ('+501', 'Belize'), ('+229', 'Benin'), ('+1', 'Bermuda'), ('+975', 'Bhutan'), ('+591', 'Bolivia'), ('+387', 'Bosnia and Herzegovina'), ('+267', 'Botswana'), ('+55', 'Brazil'), ('+1', 'British Virgin Islands'), ('+673', 'Brunei'), ('+359', 'Bulgaria'), ('+226', 'Burkina Faso'), ('+257', 'Burundi'), ('+855', 'Cambodia'), ('+237', 'Cameroon'), ('+1', 'Canada'), ('+238', 'Cape Verde'), ('+599', 'Caribbean Netherlands'), ('+1', 'Cayman Islands'), ('+236', 'Central African Republic'), ('+235', 'Chad'), ('+56', 'Chile'), ('+86', 'China'), ('+61', 'Christmas Island'), ('+61', 'Cocos (Keeling) Islands'), ('+57', 'Colombia'), ('+269', 'Comoros'), ('+242', 'Congo (Brazzaville)'), ('+243', 'Congo (Kinshasa)'), ('+682', 'Cook Islands'), ('+506', 'Costa Rica'), ('+385', 'Croatia'), ('+53', 'Cuba'), ('+599', 'Curaçao'), ('+357', 'Cyprus'), ('+420', 'Czech Republic'), ('+45', 'Denmark'), ('+253', 'Djibouti'), ('+1', 'Dominica'), ('+1', 'Dominican Republic'), ('+593', 'Ecuador'), ('+20', 'Egypt'), ('+503', 'El Salvador'), ('+240', 'Equatorial Guinea'), ('+291', 'Eritrea'), ('+372', 'Estonia'), ('+251', 'Ethiopia'), ('+500', 'Falkland Islands'), ('+298', 'Faroe Islands'), ('+679', 'Fiji'), ('+358', 'Finland'), ('+33', 'France'), ('+594', 'French Guiana'), ('+689', 'French Polynesia'), ('+262', 'French Southern')], max_length=25)),
                ('mobile_no', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(999999999999)])),
                ('service_type', models.CharField(choices=[('UAV-DRONE', 'UAV DRONE'), ('MAPPING_SERVICES', 'Mapping Services'), ('IMAGING_SERVICES', 'Imaging Services'), ('OTHER', 'Other')], max_length=55)),
                ('service_info', models.TextField()),
            ],
        ),
    ]
