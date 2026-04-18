def validate(sector: str):
    if not sector.isalpha():
        raise ValueError("Invalid sector")
    return sector.lower()