Preciosfruna = {
    "frunacola": 500,
    "frunacola": 300,
    "tabletones": 200,
    "cerealinflado": 450,
    "galleton": 150,
    "cassata": 500,
}
print("=== Productos disponibles ===")
for producto in Preciosfruna:
    print(f"- {producto}: ${Preciosfruna[producto]}")

milistadeproducto = []

def aparte(producto):
    if producto:
        milistadeproducto.append(producto)
        return True
    return False

while True:
    producto = input('Ingrese el producto o "ahi nomas pelao" para finalizar): ')
    
    if not producto:
        print("Error: No ingresó ningún producto")
        continue
    
    if producto == 'ahi noma pelao':
        break
    
    if producto.isdigit():
        print("Error: No se permiten números como producto")
        continue
    
    aparte(producto)

print("\n--- Factura de productos ---")
acumulador = 0

for producto in milistadeproducto:
    precio = Preciosfruna.get(producto.lower(), 0)
    print(f"Producto: {producto} - Precio: ${precio}")
    acumulador += precio

print(f"\nTotal a pagar: ${acumulador}")