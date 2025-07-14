productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                           }
stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21], 
         '123FHD': [290890,32], 
         '342FHD': [444990,7],
         'GF75HD': [749990,2], 
         'UWU131HD': [349990,1], 
         'FS1230HD': [249990,0], 
                 }
 # Funciones
def menu():
    print('***MENU PRINCIPAL***')
    print('===========================')
    print('1.- Stock marca')
    print('2.- Busqueda por RAM y precio')
    print('3.- eliminar producto')
    print('4.- salir')
def buscar_ram_precio():
    while True:
        try:
            ram1=int(input('ingrese la ram minima:  '))
            break
        except:
            print('debe ser un numero entero')
    while True:
        try:
            ram2=int(input('ingrese la ram maxima:  '))
            break
        except:
            print('debe ser un numero entero')
    while True:
        try:
            precio=int(input('ingrese el precio:  '))
            break
        except:
            print('debe ser un numero entero')
    for c,v in productos.items():
        if ram1<=v[1]:
            if ram2>=v[1]:
                for clave,valor in stock.items():
                    if precio>=valor[0]:
                        print(valor)

def stock_marca():
    while True:
        nombre=input('Ingrese marca a consultar: ').capitalize()
        total=0
        for clave,valor in productos.items():
            if valor[0]==nombre:
                #print(valor)
                #total=0
                for c,v in stock.items():                
                    if c==clave:
                        total=total+v[1]
                print(total)     
                break 
                
        print('el modelo no existe')       
# NO reconoce el HP pero los demas si
def eliminar_producto():
    while True:
        nombre=input('Ingrese modelo a Eliminar: ')
        for clave,valor in productos.items():
            if clave==nombre:
                productos.pop(clave)
 #            del turistas[clave]  
            print('producto eliminado con exito.')
            return
        for clave,valor in stock.items():
            if clave==nombre:
                stock.pop(clave)
        print('producto eliminado con exito.')
        return
print('el modelo no existe')       
#programa principal
modelo='8475HD'
while True:
    menu()
    opc=input('ingrese una opcion:  ')
    if opc=='1':
            stock_marca()
    elif opc=='2':
            buscar_ram_precio()
    elif opc=='3':
            eliminar_producto()
    elif opc=='4':
        print('Gracias por preferirnos!!!!!!')
        break
    else:
        print('opcion incorrecta')
    