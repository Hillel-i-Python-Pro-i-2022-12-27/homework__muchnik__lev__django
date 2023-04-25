from typing import Final
from datetime import datetime


from django.contrib.sessions.backends.cached_db import SessionStore
from django.views.generic import TemplateView

KEY__COUNT_OF_VISITS: Final[str] = "count_of_visits"

KEY__PREVIOUS_TIME: [str] = "datetime_of_last_visit"


class SessionUserView(TemplateView):
    template_name = "sessions_example/index.html"

    def get_context_data(self, **kwargs):
        session: SessionStore = self.request.session
        count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)

        count_of_visits += 1
        date_real = str(datetime.now().strftime("%d.%m.%Y | %H:%M:%S"))
        datetime_of_last_visit = session.get(KEY__PREVIOUS_TIME, 0)

        session[KEY__PREVIOUS_TIME] = date_real

        session[KEY__COUNT_OF_VISITS] = count_of_visits

        context = super().get_context_data(**kwargs)
        context["title"] = "Session user"
        context["session_id"] = session.session_key
        context["count_of_visits"] = count_of_visits

        context["date_real"] = date_real
        context["datetime_of_last_visit"] = datetime_of_last_visit

        return context
