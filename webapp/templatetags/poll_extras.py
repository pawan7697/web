from django import template
from ..models import category
from ..models import navbar

register = template.Library()
@register.inclusion_tag("webhtml/navbar.html")
def menu():
    
    all_entries=category.get_categorty()
    
   
    return {'links':all_entries}
