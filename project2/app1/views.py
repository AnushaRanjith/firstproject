from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def good_mng(request):
    return Response("GOOD MORNING")