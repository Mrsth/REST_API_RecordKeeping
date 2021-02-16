from django.contrib import admin
from apis1.models import SalesTable, PurchaseTable, PurchaseRequisitionTable, Accept_Reject_Table

# Register your models here.
# admin.site.register(SalesTable)
#admin.site.register(PurchaseTable)
#admin.site.register(PurchaseRequisitionTable)

@admin.register(SalesTable)
class SalesTableAdmin(admin.ModelAdmin):
    list_display = ("salesItem", "salesAmount", "salesDate")

@admin.register(PurchaseTable)
class PurchaseTableAdmin(admin.ModelAdmin):
    list_display = ("purchaseItem", "purchaseAmount", "purchaseDate")

@admin.register(PurchaseRequisitionTable)
class PurchaseRequisitionTable(admin.ModelAdmin):
    list_display = ("purchaseItem", "purchaseAmount", "purchaseDate", "vendorName", "unitPrice", "phoneNo", "approve", "quantity")   

@admin.register(Accept_Reject_Table)
class Accept_Reject_Table_Admin(admin.ModelAdmin):
    list_display = ("value", "key")