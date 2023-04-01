from collections.abc import Callable
from .models import RequestLog


class RequestsMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        path = request.build_absolute_uri()
        session_id = request.session.session_key
        user_id = request.user.id
        requests_log = RequestLog.objects
        if requests_log.filter(
            path=path,
            session_id=session_id,
            user_id=user_id,
        ).exists():
            result = requests_log.get(
                path=path,
                session_id=session_id,
                user_id=user_id,
            )
            result.counter += 1
            result.save()
        else:
            requests_log.create(
                path=path,
                session_id=session_id,
                user_id=user_id,
                counter=1,
            )
        return response
