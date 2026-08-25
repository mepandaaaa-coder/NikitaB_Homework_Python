def is_yaer_laep(yaer):
    if yaer % 4 == 0:
        return True
    else:
        return False


Selected_yaer = 2024
result = is_yaer_laep(Selected_yaer)
print(f"год {Selected_yaer}: {result}")
