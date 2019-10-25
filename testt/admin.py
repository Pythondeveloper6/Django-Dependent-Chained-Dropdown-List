from django.contrib import admin

# Register your models here.



from .models import Continent , Country , Location , Publication , Writer , Book , Location2




class LocationAdmin(admin.ModelAdmin):
    class Media:
        # js = (
        #     'smart-selects/admin/js/chainedfk.js',
        #     'smart-selects/admin/js/chainedm2m.js',
        # )
        pass


admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Location ,LocationAdmin)
# admin.site.register(Location2)
# admin.site.register(Publication)
# admin.site.register(Writer)
# admin.site.register(Book)