from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Q, DateField
from django.db.models.functions import Trunc
from django.views.generic import TemplateView, ListView

from .models import Category, Expense


class StatsView(TemplateView):
    template_name = "expenses/stats.html"
    extra_context = {
        'title': "Statistics",
    }

    def get_context_data(self, **kwargs):
        general = (
            Expense.objects
                .annotate(
                    trunc_date=Trunc('date', 'month', output_field=DateField())
                )
                .values('trunc_date')
                .annotate(
                    sum_expenses=Sum('amount', filter=Q(income=False)),
                    sum_incomes=Sum('amount', filter=Q(income=True)),
                )
                .order_by()
        )
        category = (
            Category.objects
                .annotate(
                    trunc_date=Trunc('expense__date', 'month',
                                     output_field=DateField())
                )
                .values('trunc_date', 'name')
                .filter(trunc_date__isnull=False)
                .annotate(
                    sum_expenses=Sum('expense__amount',
                                     filter=Q(expense__income=False)),
                    sum_incomes=Sum('expense__amount',
                                    filter=Q(expense__income=True)),
                )
                .order_by('name', 'trunc_date')
        )
        expense_months = (
            Expense.objects
                .annotate(
                    trunc_date=Trunc('date', 'month', output_field=DateField())
                )
                .values('trunc_date')
                .distinct()
                .order_by()
        )
        results = dict(
            general_results=general,
            category_results=category,
            expense_months=expense_months,
        )
        return super().get_context_data(**results)


class ExpenseList(ListView):
    queryset = Expense.objects.select_related('category')
    template_name = "expenses/expenses.html"
    extra_context = {
        'title': "List of expenses",
    }


class CategoryList(ListView):
    model = Category
    template_name = "expenses/category_list.html"
    extra_context = {
        'title': "Categories",
    }
