from datetime import datetime

def variant_dict(doc):
    return {

        "variant_id": str(doc.get("_id")),
        "day": doc.get("day"),
        "name": doc.get("name"),
        "description": doc.get("description"),
        "price": doc.get("price"),
        "available": doc.get("available"),
        "reserved": doc.get("reserved"),
        "created_at": doc.get("created_at"),
        "updated_at": doc.get("updated_at")

    }


def reservation_dict(doc):
    return {

        "reservation_id": str(doc.get("_id")),
        "variant_id": str(doc.get("variant_id")),
        "user_id": str(doc.get("user_id")),
        "quantity": doc.get("qty") or doc.get("quantity"),
        "status": doc.get("status"),
        "client_token": doc.get("client_token"),
        "expires_at": doc.get("exttl sweeps ky hota h" \
        "pires_at"),
        "created_at": doc.get("created_at"),
        "updated_at": doc.get("updated_at")

    }


def audit_dict(actor,action, before, after,route,created_at=None):
    return {

        "actor": actor,
        "action": action,
        "before": before,
        "after": after,
        "route": route,
        "created_at": created_at or datetime.utcnow()

    }