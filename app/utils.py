from bson import ObjectId

def convert_object_id(document: dict) -> dict:
    """
    Converts MongoDB's `_id` field to `id`.
    Args:
        document (dict): The document fetched from MongoDB.
    Returns:
        dict: The document with `_id` replaced by `id`.
    """
    if "_id" in document:
        document["id"] = str(document["_id"])
        del document["_id"]
    return document
