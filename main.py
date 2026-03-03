import mean_var_std

# Prueba para forzar el error de longitud
try:
    print(mean_var_std.calculate([1, 2, 3, 4, 5, 6, 7]))
except ValueError as e:
    print(e)