from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_("Name"),
        help_text=_("Unique name of a category"),
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-details', kwargs={'pk': self.pk})


class Expense(models.Model):
    description = models.CharField(
        max_length=200,
        verbose_name=_("Description"),
        help_text=_("Short description of the expense"),
    )
    shop = models.CharField(
        max_length=200,
        verbose_name=_("Shop"),
        help_text=_("Shop name"),
    )
    date = models.DateField(
        # instead of auto_now_add=True, which is non-overriddable
        default=now,
        verbose_name=_("Date"),
        help_text=_("Purchase / income date"),
    )
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT,
        verbose_name=_("Category"),
        help_text=_(""),
    )
    amount = models.DecimalField(
        max_digits=12, decimal_places=2,
        verbose_name=_("Amount"),
        help_text=_("Purchase / income amount"),
    )
    income = models.BooleanField(
        null=False, default=False, blank=True,
        verbose_name=_("Is this income?"),
        help_text=_("If not income, then it's an expense"),
    )

    class Meta:
        ordering = ["date", "description"]

    def __str__(self):
        return f"{self.description} {self.shop} {self.date}"
