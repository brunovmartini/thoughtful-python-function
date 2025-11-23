def sort(width, height, length, mass) -> str:
    if not all(isinstance(i, (int, float)) for i in [width, height, length, mass]):
        raise ValueError("All inputs must be numeric.")

    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("Dimensions and mass must be greater than zero.")

    volume = width * height * length
    is_bulky = False

    if volume >= 1_000_000:
        is_bulky = True
    if width >= 150 or height >= 150 or length >= 150:
        is_bulky = True

    is_heavy = True if mass >= 20 else False

    if is_heavy and is_bulky:
        return "REJECTED"
    if is_heavy or is_bulky:
        return "SPECIAL"
    return "STANDARD"


print(sort(10, 10, 10, 10))