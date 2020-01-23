from django.db.models import Sum, Q
from django.db.models.functions import ExtractYear, ExtractMonth
from django.views.generic import TemplateView

from .models import Category, Expense


class StatsView(TemplateView):
    template_name = "expenses/stats.html"

    def get_context_data(self, **kwargs):
        q = Expense.objects \
            .annotate(year=ExtractYear('date'), month=ExtractMonth('date')) \
            .values('year', 'month') \
            .annotate(
                sum_expenses=Sum('amount', filter=Q(income=False)),
                sum_incomes=Sum('amount', filter=Q(income=True)),
            ) \
            .order_by()
        return dict(results=q)
