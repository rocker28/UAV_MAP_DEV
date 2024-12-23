from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class service_req(models.Model):
    COUNTRY_CODES = [
        ('+93', 'Afghanistan'),('+355', 'Albania'),('+213', 'Algeria'),('+1', 'American Samoa'),('+376', 'Andorra'),('+244', 'Angola'),
        ('+1', 'Anguilla'),('+54', 'Argentina'),('+374', 'Armenia'),('+297', 'Aruba'),('+61', 'Australia'),('+43', 'Austria'),('+994', 'Azerbaijan'),
        ('+1', 'Bahamas'),('+973', 'Bahrain'),('+880', 'Bangladesh'),('+1', 'Barbados'),('+375', 'Belarus'),('+32', 'Belgium'),('+501', 'Belize'),
        ('+229', 'Benin'),('+1', 'Bermuda'),('+975', 'Bhutan'),('+591', 'Bolivia'),('+387', 'Bosnia and Herzegovina'),('+267', 'Botswana'),
        ('+55', 'Brazil'),('+1', 'British Virgin Islands'),('+673', 'Brunei'),('+359', 'Bulgaria'),('+226', 'Burkina Faso'),('+257', 'Burundi'),
        ('+855', 'Cambodia'),('+237', 'Cameroon'),('+1', 'Canada'),('+238', 'Cape Verde'),('+599', 'Caribbean Netherlands'),('+1', 'Cayman Islands'),
        ('+236', 'Central African Republic'),('+235', 'Chad'),('+56', 'Chile'),('+86', 'China'),('+61', 'Christmas Island'),('+61', 'Cocos (Keeling) Islands'),
        ('+57', 'Colombia'),('+269', 'Comoros'),('+242', 'Congo (Brazzaville)'),('+243', 'Congo (Kinshasa)'),('+682', 'Cook Islands'),('+506', 'Costa Rica'),
        ('+385', 'Croatia'),('+53', 'Cuba'),('+599', 'Curaçao'),('+357', 'Cyprus'),('+420', 'Czech Republic'),('+45', 'Denmark'),('+253', 'Djibouti'),
        ('+1', 'Dominica'),('+1', 'Dominican Republic'),('+593', 'Ecuador'),('+20', 'Egypt'),('+503', 'El Salvador'),('+240', 'Equatorial Guinea'),
        ('+291', 'Eritrea'),('+372', 'Estonia'),('+251', 'Ethiopia'),('+500', 'Falkland Islands'),('+298', 'Faroe Islands'),('+679', 'Fiji'),
        ('+358', 'Finland'),('+33', 'France'),('+594', 'French Guiana'),('+689', 'French Polynesia'),('+262', 'French Southern'),('+241', 'Gabon'),
        ('+220', 'Gambia'),('+995', 'Georgia'),('+49', 'Germany'),('+233', 'Ghana'),('+350', 'Gibraltar'),('+30', 'Greece'),('+299', 'Greenland'),
        ('+1', 'Grenada'),('+590', 'Guadeloupe'),('+1', 'Guam'),('+502', 'Guatemala'),('+224', 'Guinea'),('+245', 'Guinea-Bissau'),('+592', 'Guyana'),
        ('+509', 'Haiti'),('+504', 'Honduras'),('+852', 'Hong Kong'),('+36', 'Hungary'),('+354', 'Iceland'),('+91', 'India'),('+62', 'Indonesia'),
        ('+98', 'Iran'),('+964', 'Iraq'),('+353', 'Ireland'),('+972', 'Israel'),('+39', 'Italy'),('+225', 'Ivory Coast'),('+1', 'Jamaica'),]

    Service_choice = [
        ('UAV-DRONE', 'UAV DRONE'),
        ('MAPPING_SERVICES', 'Mapping Services'),
        ('IMAGING_SERVICES', 'Imaging Services'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=75)
    email_id = models.EmailField(max_length=95)
    country_code = models.CharField(max_length=25,choices=COUNTRY_CODES)
    mobile_no = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(999999999999)])
    service_type = models.CharField(max_length=55, choices=Service_choice)
    service_info = models.TextField()
