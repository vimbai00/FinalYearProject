from .models import Paddock

def getPaddocks(request):
    paddocks = Paddock.objects.all()
    return {'paddocks': paddocks}
