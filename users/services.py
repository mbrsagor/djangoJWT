def note_validate_service(attrs):
    if "title" in attrs and len(attrs.get("title")) < 1:
        return "Title field is required"
    else:
        pass
