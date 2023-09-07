'''
Simula el funcionamiento de una máquina expendedora creando una operación que reciba dinero 
(array de monedas) y un número que indique la selección del producto.
- El programa retornará el nombre del producto y un array con el dinero de vuelta 
(con el menor número de monedas).
- Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un 
mensaje y retornar todas las monedas.
- Si no hay dinero de vuelta, el array se retornará vacío.
- Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
- Debemos controlar que las monedas enviadas estén dentro de las soportadas.
'''
def dispensadora(pago:list,producto:int):
    # lista de precio de productos. El producto es dado por la posicion
    # y el precio por el valor
    list_productos = [1200, 200, 125, 1555, 2200, 375, 80, 30, 150]

    # diccionario con el nombre de los productos
    name_productos = {
        0:'Iphone',
        1:'Memoria',
        2:'Cargador',
        3:'Diademas gaming',
        4:'Smart TV',
        5:'Smart Watch',
        6:'Cable USB',
        7:'Llavero',
        8:'Protector pantalla'
    }

    # lista de monedas soportadas
    monedas = [5, 10, 50, 100, 200]


    # validar monedas soportadas
    for i in pago:
        if i not in monedas:
            return 'alguna moneda no es soportada. Revisa el pago'
        
    # validar numero de producto
    if producto not in name_productos:
        return 'No Existe el producto'

    # validar que el pago sea suficiente para comprar el producto
    precio_prod = list_productos[n_producto]
    total_pago = sum(pago)
    
    if total_pago < precio_prod:
        return 'Pago insuficiente'
    
    else:
        # Calcular devuelta
        devuelta = total_pago - precio_prod
        list_devuelta = []
    
        if devuelta == 0:
            list_devuelta = list_devuelta + [0]
        else: 
            # recorre monedas de forma inversa
            for i in range(len(monedas)-1, -1, -1):
                
                if monedas[i] <= devuelta:
                    num_monedas = devuelta//monedas[i]
                    devuelta = devuelta % monedas[i]
            
                    if num_monedas == 1:
                        list_devuelta = list_devuelta + [monedas[i]]
                    else:
                        for n in range(num_monedas):
                            list_devuelta = list_devuelta + [monedas[i]]
                
                if devuelta == 0:
                    break
                
    return f'Nombre Del Producto: {name_productos[producto]}. \nDevuelta: {list_devuelta}'
                
###### Test
pago = [200,200,200,200,200,200,200,200]
n_producto = 3

print(dispensadora(pago, n_producto))
# --> Nombre Del Producto: Diademas gaming. 
#     Devuelta: [10, 10, 10, 10, 5]

n_producto = 1
print(dispensadora(pago, n_producto))
# --> Nombre Del Producto: Memoria. 
#     Devuelta: [200, 200, 200, 200, 200, 200, 200]

pago = [200,2]
n_producto = 1
print(dispensadora(pago, n_producto))
# --> alguna moneda no es soportada. Revisa el pago

pago = [200, 100]
n_producto = 20
print(dispensadora(pago, n_producto))
# --> No Existe el producto

pago = [100]
n_producto = 1
print(dispensadora(pago, n_producto))
# --> Pago insuficiente