from django.db import models
from django.forms import ValidationError
import re

# Create your models here.
def only_int(value):
    if value.isdigit()==False:
        raise ValidationError('Serial Number contains characters')
def only_img(value):
    reg_result = re.match(".*\.jpg\Z", value) or re.match(".*\.jpeg\Z", value) or re.match(".*\.png\Z", value)
    if not reg_result:
        raise ValidationError('File is not an image')

class ShopItem(models.Model) :
    serial_number = models.CharField(max_length=12, validators=[only_int])
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=50, validators=[only_img])
