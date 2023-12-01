from .models import Field

def getField(request):
    field = Field.objects.all()
    return {'field': field}
