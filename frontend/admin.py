from django.contrib import admin
from .models import Partner, Product, Skill, TeamMember

# Register your models here.
admin.site.register(Product)
admin.site.register(Skill)
admin.site.register(TeamMember)
admin.site.register(Partner)