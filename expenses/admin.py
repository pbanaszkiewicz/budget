from django.contrib import admin

from .models import Category, Expense


class CategoryAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ["name"]


class ExpenseAdmin(admin.ModelAdmin):
    date_hierarchy = "date"
    list_display = [
        "description",
        "shop",
        "date",
        "category",
        "amount",
        "income",
    ]
    list_filter = [
        "shop",
        "date",
        "category",
        "income",
    ]
    list_select_related = True
    autocomplete_fields = ["category"]
    search_fields = [
        "description",
        "shop",
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Expense, ExpenseAdmin)
