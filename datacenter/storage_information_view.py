from datetime import timezone, datetime

from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.visit_duration_functions import format_duration, get_duration
from datacenter.models import Visit


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(get_duration(visit))
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)





