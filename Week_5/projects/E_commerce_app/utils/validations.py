def validate_url(actual, expected):
    if expected in actual:
        print(f"'{expected}' is present in the url : '{actual}'")
        return True
    else:
        print(f"{expected} is not present in the url : '{actual}'")
        return False
    
def validate_text(actual, expected):
    if expected in actual:
        print(f"Text matched successfully!! \nActual : '{actual}'\nExpected : '{expected}'")
        return True
    else:
        print(f"Text is not matched!! \nActual : '{actual}'\nExpected : '{expected}'")
        return False