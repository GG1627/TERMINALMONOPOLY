special_characters_allowed = ["'", "~", "!", "@", "#", "$", "%", "&", "*", "/", "\\", "<", ">"]

def validate_name(name):
    # less that 10 character
    if len(name) >= 10:
        return False

    # certain characters allowed
    for char in name:
        if not (char.isalnum() or char.isspace() or char in special_characters_allowed):
            return False

    return True