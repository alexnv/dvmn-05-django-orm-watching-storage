from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    # Программируем здесь
    this_passcard_visits = []
    if passcard:
        visits = Visit.objects.filter(passcard=passcard)
        for visit in visits:
            this_passcard_visits.append({
                'entered_at': localtime(visit.entered_at),
                'duration': get_duration(visit),
                'is_strange': is_visit_long(visit)
            })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


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
        seconds = duration.total_seconds()
        if seconds >= (minutes * 60):
            return True

    return False
