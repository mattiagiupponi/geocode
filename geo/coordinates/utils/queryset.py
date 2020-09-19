from datetime import datetime

from coordinates.models import RequestHistory


def from_coordinates_qs_to_list(queryset):
    return [item.to_tuple() for item in queryset]


def save_request_history(url, x, y, points, action):
    save_history = RequestHistory(
        request=url, timestamp=datetime.utcnow(), x_axes=x, y_axes=y, points=points, operation=action
    )
    save_history.save()
    return save_history
