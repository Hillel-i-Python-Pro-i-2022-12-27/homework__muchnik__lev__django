from django.views.generic import ListView
from apps.middleware_counter.models import RequestLog


class LogsListView(ListView):
    model = RequestLog
    template_name = "middleware_counter/list.html"
    queryset = RequestLog.objects.all().order_by("-visit_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count_all_logs = RequestLog.objects.count()
        context["title"] = "List"
        context["count_all_logs"] = count_all_logs
        return context
