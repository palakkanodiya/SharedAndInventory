from datetime import datetime

def variant_dict(doc):
    """
    Converts a MongoDB variant document to a dictionary format.
    """
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
    """
    Converts a MongoDB reservation document to a dictionary format.
    """
    return {
        "reservation_id": str(doc.get("_id")),
        "variant_id": str(doc.get("variant_id")),
        "user_id": str(doc.get("user_id")),
        "quantity": doc.get("qty") or doc.get("quantity"),
        "status": doc.get("status"),
        "client_token": doc.get("client_token"),
        "expires_at": doc.get("expires_at"),
        "created_at": doc.get("created_at"),
        "updated_at": doc.get("updated_at")
    }


def audit_dict(actor, action, before, after, route, ip_hash, created_at=None):
    """
    Creates a structured audit trail entry.
    """
    return {
        "actor": actor,
        "action": action,
        "before": before,
        "after": after,
        "route": route,
        "ip_hash": ip_hash,
        "created_at": created_at or datetime.utcnow()
    }