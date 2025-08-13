from celery import shared_task
from app.mongo import get_mongoo_client

@shared_task
def reconcile_backorders():
    client = get_mongoo_client()
    reservations = client.invdb.reservations
    variants = client.invdb.variants

    backorders = reservations.find({"status": "BACKORDER"})

    for reservation in backorders:
        variant = variants.find_one({"variant_id": reservation["variant_id"]})
        if variant and variant.get("available", 0) >= reservation["qty"]:
            #update stock
            variants.update_one(
                {"variant_id": reservation["variant_id"]},
                {"$inc": {"available": -reservation["qty"], "reserved": reservation["qty"]}}
            )
            #uupdate reservation
            reservations.update_one(
                {"_id": reservation["_id"]},
                {"$set": {"status": "CONFIRMED"}}
            )