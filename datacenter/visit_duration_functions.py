from datetime import datetime, timezone


def format_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'{int(hours)}ч {int(minutes)}мин'


def get_visit_duration_in_seconds(visit):
    if visit.leaved_at:
        delta = visit.leaved_at - visit.entered_at
    else:
        delta = datetime.now(timezone.utc) - visit.entered_at
    return delta.total_seconds()


def is_visit_long(visit, minutes=60):
    seconds = get_visit_duration_in_seconds(visit)

    return seconds >= (minutes * 60)
