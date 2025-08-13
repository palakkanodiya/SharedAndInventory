from django.http import JsonResponse
from app.mongo import get_mongoo_client

def metrics_view(request):
    client = get_mongoo_client()
    reservations = client.invdb.reservations
    total = reservations.count_documents({})
    confirmed = reservations.count_documents({"status": "CONFIRMED"})
    backorders = reservations.count_documents({"status": "BACKORDER"})
    hold = reservations.count_documents({"status": "HOLD"})

    return JsonResponse({
        "total_reservations": total,
        "confirmed": confirmed,
        "backorders": backorders,
        "hold": hold
    })