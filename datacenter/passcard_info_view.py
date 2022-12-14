from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.visit_duration_functions import is_visit_long, get_visit_duration_in_seconds, format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    # Программируем здесь
    this_passcard_visits = []

    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        this_passcard_visits.append({
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_visit_duration_in_seconds(visit)),
            'is_strange': is_visit_long(visit)
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)





