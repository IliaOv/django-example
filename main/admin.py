from django.contrib import admin
from .models import Message, Person

admin.site.register([Person, Message])
