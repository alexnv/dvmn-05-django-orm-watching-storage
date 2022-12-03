from datetime import datetime


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'{int(hours)}ч {int(minutes)}мин'


def get_duration(visit):
    delta = visit.leaved_at - visit.entered_at
    return delta


def is_visit_long(visit, minutes=60):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = datetime.now() - visit.entered_at
    seconds = duration.total_seconds()

    return seconds >= (minutes * 60)
