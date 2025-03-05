def serialize_document(document):
    document["_id"] = str(document["_id"])
    return document