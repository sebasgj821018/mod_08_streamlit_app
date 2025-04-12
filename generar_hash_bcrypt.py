import bcrypt

# Contraseña original
password = "admin"

# Hashear
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Mostrar el hash
print(hashed.decode())