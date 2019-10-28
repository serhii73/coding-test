# Write your code here


def get_temperature_closest_to_zero(temperatures):
    if not temperatures or 0 in temperatures:
        return 0

    min_value = min(temperatures, key=abs)
    min_abs_value = abs(min_value)

    if min_abs_value in temperatures:
        return min_abs_value
    else:
        return min_value

    return None