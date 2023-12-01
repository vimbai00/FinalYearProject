from .models import Flock

def getPaddocks(request):
    paddocks = Flock.objects.all()
    return {'paddocks': paddocks}
