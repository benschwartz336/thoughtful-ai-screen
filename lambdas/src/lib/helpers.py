def sort_package(width, height, length, mass):
    """
    Sort a package into the correct stack.

    Rules:
    - Bulky if: volume >= 1,000,000 cm³ or any dimension >= 150 cm
    - Heavy if: mass >= 20 kg

    Stacks:
    - REJECTED: if the package is both bulky and heavy
    - SPECIAL: if the package is either bulky or heavy (but not both)
    - STANDARD: otherwise
    """
    volume = width * height * length
    is_bulky = (
        (volume >= 1000000) or (width >= 150) or (height >= 150) or (length >= 150)
    )
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
