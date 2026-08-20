def eat_ghost(power_pillet_active, touching_ghost):
    return power_pillet_active and touching_ghost

def score(touching_power_pillet, touching_dot):
    return touching_power_pillet or touching_dot

def lose(power_pillet_active, touching_ghost):
    return power_pillet_active and not touching_ghost

def win(has_eaten_all_dots, power_pillet_active, touching_ghost, ):
    return has_eaten_all_dots and not lose(power_pillet_active, touching_ghost)