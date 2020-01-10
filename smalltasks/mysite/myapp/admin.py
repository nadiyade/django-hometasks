from django.contrib import admin
from .models import Animal, Visitor, Ticket, Visit


class AnimalAdmin(admin.ModelAdmin):
    pass


class VisitorAdmin(admin.ModelAdmin):
    pass


class VisitsAdmin(admin.ModelAdmin):
    pass


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticketBought', 'ticketVisitor')


admin.site.register(Visitor)
admin.site.register(Animal)
admin.site.register(Visit)
admin.site.register(Ticket)


# Register your models here.
