from django import template
register = template.Library()
@register.filter(name='remove_special')
def remove_char(value,arg):
    print("Arg :",arg)
    print("Value :",value)
    for character in arg:
      print("Character :",character)
      value = value.replace(character,"")
    return value
    
    
    
