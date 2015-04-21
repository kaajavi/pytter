from django import template


from main.models import UserProfile
from django.contrib.auth.models import User
register = template.Library()


#Deprecated
@register.simple_tag
def url_avatar(idx_user=None):
    
    profile = User.objects.get(pk=idx_user).userprofile
    
    return profile.avatar