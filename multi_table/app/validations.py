from django.core.exceptions import ValidationError

def validate_price(value):
    if value<=0:
        raise ValidationError('Price must be positive')

def v_name(name):
    if len(name)<3:
        raise ValidationError('Name should have atleast 3 characters')
    
def v_phone(num):
    if len(num)!=10:
        raise ValidationError('Phone number must be 10 digits')
    
def v_desc(dec):
    if len(dec)<10:
        raise ValidationError('Description must be atleast 10 char')