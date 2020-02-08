from django.db.models import Sum, Q
from django.db.models.functions import ExtractYear, ExtractMonth
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, Expense


class StatsView(TemplateView):
    template_name = "expenses/stats.html"
    extra_context = {
        'title': "Stats",
    }

    def get_context_data(self, **kwargs):
        q = Expense.objects \
            .annotate(year=ExtractYear('date'), month=ExtractMonth('date')) \
            .values('year', 'month') \
            .annotate(
                sum_expenses=Sum('amount', filter=Q(income=False)),
                sum_incomes=Sum('amount', filter=Q(income=True)),
            ) \
            .order_by()
        return super().get_context_data(**dict(results=q))


class ExpenseList(ListView):
    model = Expense
    template_name = "expenses/expense_list.html"
    extra_context = {
        'title': "Expenses",
    }


class CategoryList(ListView):
    model = Category
    template_name = "expenses/category_list.html"
    extra_context = {
        'title': "Categories",
    }
