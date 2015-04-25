from django import template


from main.models import UserProfile
from django.contrib.auth.models import User
from main.models import Pytt
register = template.Library()


#Deprecated
@register.simple_tag
def render_pytt(idx_pytt):
    
    profile = Pytt.objects.get(pk=idx_user).userprofile
    
    return profile.avatar