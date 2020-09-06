# Login de usuario-admin
names_and_passwords = {'admin': '1234', 'Tech1': '1000', 'Tech2': '2000', 'Tech3': '3000', 'Tech4': '4000'}

while True:  # desbloquear
    user_name = input('Bienvenido a  los registros de Lifestore  \
    \nIngrese su nombre y presione Enter (username) \n')
    password = input('Ingrese contraseña (1234) y presione Enter\n')
    if user_name in names_and_passwords.keys() and password == names_and_passwords.get(user_name):
        print('Bienvenido', user_name)
        break
    else:
        print('Nombre o contraseña incorrectos, intente de nuevo', '\n' * 7)

#### 100 productos más vendidos
from listas import lifestore_sales, lifestore_products, lifestore_searches


class color:
    azul = '\033[94m'
    normalc = '\033[0m'


# contador de repeticiones en multilistas, con index relacionado
a = lifestore_sales[:]
elementos_usados = []
salida = []
for i in range(len(a)):
    element_in_question = a[i][1]
    count = 0
    if element_in_question not in elementos_usados:  # ya contaste los unos, los tachas
        for element in range(len(a)):
            if element_in_question == a[element][1]:
                count += 1

            for i in range(len(lifestore_products)):
                if element_in_question == lifestore_products[i][0]:
                    nombre = lifestore_products[i][1]
        salida.append(['No. Items vendidos', count, 'idproducto', element_in_question, 'nombre', nombre])
    elementos_usados.append(element_in_question)
b = salida
# ordenador de elementos top de mayor a menor en multilist
for i in range(len(b)):
    for j in range(len(b) - 1):
        if b[j][1] < b[j + 1][1]:  # menor o mayor orden
            temp = b[j]
            b[j] = b[j + 1]
            b[j + 1] = temp

cuantosproductossevendieron = len(b)
print(
    color.azul + 20 * ' ' + 'Top ' + str(cuantosproductossevendieron) + ' productos vendidos' + color.normalc)  # center
for i in b:
    print(i, '\n')

# 100 productos con mayores busquedas

# contador de repeticiones en multilistas, con index relacionado
a = lifestore_searches[:]
elementos_usados = []
salida = []
for i in range(len(a)):
    element_in_question = a[i][1]
    count = 0
    if element_in_question not in elementos_usados:  # ya contaste los unos, los tachas
        for element in range(len(a)):
            if element_in_question == a[element][1]:
                count += 1

            for i in range(len(lifestore_products)):
                if element_in_question == lifestore_products[i][0]:
                    nombre = lifestore_products[i][1]
        salida.append(['No. busquedas', count, 'idproducto', element_in_question, 'nombre', nombre])
    elementos_usados.append(element_in_question)
b = salida
for i in range(len(b)):
    for j in range(len(b) - 1):
        if b[j][1] < b[j + 1][1]:  # menor o mayor orden
            temp = b[j]
            b[j] = b[j + 1]
            b[j + 1] = temp
cuantosproductossebuscaron = len(b)
print(color.azul + 20 * ' ' + 'Top ' + str(cuantosproductossebuscaron) + ' productos buscados' + color.normalc)
for i in b:
    print(i, '\n')




# [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
# cuenta cada cuanto de que cosa y ordena de mayor a menor desde 0 hasta 49

# ORDENADOR DE CATEGORIA, PRODUCTOS MENOS VENDIDOS LISTO
from listas import lifestore_products, lifestore_sales


#
class color:
    azul = '\033[94m'
    normalc = '\033[0m'
    verde = '\033[92m'


a = lifestore_products
categorias = []
categoria_inicial = []
# lista de todas las categorias
for i in range(len(a)):  # por cada producto
    categoria_i = a[i][3]  # categoria == a categ. product
    if categoria_i not in categoria_inicial:
        categorias.append(categoria_i)  # crea una categoria
        categoria_inicial.append(categoria_i)  # RECONOCE que categorias se repiten
# lista de productos por categoria
elementos_por_categorias = categorias[:]

ids_pro_numero = []
for k in range(len(categorias)):  # por cada categoria
    elem = categorias[k]  # borrar esto
    elem = []  # aqui se elimina, guardalo antes, variable temporal index
    for i in range(len(a)):  # por cada producto
        if categorias[k] == a[i][3]:
            elem.append(a[i])  # anade el producto completo a elem, lista simple
    elementos_por_categorias[k] = elem
    print('categ: ', elementos_por_categorias[k][0][3], 'cantidad: ',
          len(elementos_por_categorias[k]))  # es la longitud de cada seccion listal

    ids = []
    # funciona y es para obtener lista de ids
    for e in elementos_por_categorias[k]:
        ids.append(e[0])
    ids_pro_numero.append(ids)
# print(ids_pro_numero) #salida de ids producto
# hasta aca funciona bien
ids_producto_por_categori = ids_pro_numero  # contar repeticiones de una lista de ids categorizada
for i in range(len(ids_producto_por_categori)):  # por cada categoria #entra el ids producto
    ids_producto_por_categoria = ids_producto_por_categori[i]
    a = lifestore_sales[:]  # accede a ventas
    elementos_usados = []
    salida = []
    for ids in ids_producto_por_categoria:  # para cada id producto
        count = 0
        nombre = ''
        if ids not in elementos_usados:  # en el caso de que existan duplicados indeseados
            for element in range(len(a)):  # para cada venta en ventas
                if ids == a[element][1]:  # si el elemento coincide se suma,
                    count += 1
            for g in range(len(lifestore_products)):
                if ids == lifestore_products[g][0]:
                    nombre = lifestore_products[g][1]
                    break  # para no seguir buscando el nombre para el ids
            salida.append(['No. Items vendidos', count, 'idproducto',
                           ids, 'nombre', nombre[0:19]])
        elementos_usados.append(ids)  # al final de la condicion, debes agregar
    b = salida
    # ordenador de elementos top de mayor a menor en multilist
    for i in range(len(b)):
        for j in range(len(b) - 1):
            if b[j][1] > b[j + 1][1]:  # menor o mayor orden
                temp = b[j]
                b[j] = b[j + 1]
                b[j + 1] = temp
    cuantosproductossevendieron = len(b)
    print("\n", 20 * ' ' + color.verde + 'Top ' + str(
        cuantosproductossevendieron) + ' productos menos vendidos por categoria' + color.normalc)  # center
    for q in b:
        print(q, '\n')

######### menos buscados por categoria, eliminar partes repetitivas
# ORDENADOR DE CATEGORIA, PRODUCTOS MENOS BUSCADOS
from listas import lifestore_products, lifestore_searches


#
class color:
    azul = '\033[94m'
    normalc = '\033[0m'
    verde = '\033[92m'
    amari = '\033[93m'


a = lifestore_products
categorias = []
categoria_inicial = []
# lista de todas las categorias
for i in range(len(a)):  # por cada producto
    categoria_i = a[i][3]  # categoria == a categ. product
    if categoria_i not in categoria_inicial:
        categorias.append(categoria_i)  # crea una categoria
        categoria_inicial.append(categoria_i)  # RECONOCE que categorias se repiten
# lista de productos por categoria
elementos_por_categorias = categorias[:]

ids_pro_numero = []
for k in range(len(categorias)):  # por cada categoria
    elem = categorias[k]  # borrar esto
    elem = []  # aqui se elimina, guardalo antes, variable temporal index
    for i in range(len(a)):  # por cada producto
        if categorias[k] == a[i][3]:
            elem.append(a[i])  # anade el producto completo a elem, lista simple
    elementos_por_categorias[k] = elem
    # print('categ: ', elementos_por_categorias[k][0][3], 'cantidad: ',
    #       len(elementos_por_categorias[k]))  # es la longitud de cada seccion listal

    ids = []
    # funciona y es para obtener lista de ids
    for e in elementos_por_categorias[k]:
        ids.append(e[0])
    ids_pro_numero.append(ids)
# print(ids_pro_numero) #salida de ids producto
# hasta aca funciona bien
ids_producto_por_categori = ids_pro_numero  # contar repeticiones de una lista de ids categorizada

for i in range(len(ids_producto_por_categori)):  # por cada categoria #entra el ids producto
    ids_producto_por_categoria = ids_producto_por_categori[i]
    a = lifestore_searches[:]  # accede a ventas
    elementos_usados = []
    salida = []
    for ids in ids_producto_por_categoria:  # para cada id producto
        count = 0
        nombre = ''
        if ids not in elementos_usados:  # en el caso de que existan duplicados indeseados
            for element in range(len(a)):  # para cada venta en ventas
                if ids == a[element][1]:  # si el elemento coincide se suma,
                    count += 1
            for g in range(len(lifestore_products)):
                if ids == lifestore_products[g][0]:
                    nombre = lifestore_products[g][1]
                    break  # para no seguir buscando el nombre para el ids
            salida.append(['No. Items buscados', count, 'idproducto',
                           ids, 'nombre', nombre[0:19]])
        elementos_usados.append(ids)  # al final de la condicion, debes agregar
    b = salida
    # ordenador de elementos top de mayor a menor en multilist
    for i in range(len(b)):
        for j in range(len(b) - 1):
            if b[j][1] > b[j + 1][1]:  # menor
                temp = b[j]
                b[j] = b[j + 1]
                b[j + 1] = temp
    cuantosproductossevendieron = len(b)
    print('\n', 20 * ' ' + color.amari + 'Top ' + str(
        cuantosproductossevendieron) + ' productos menos buscados por categoria' + color.normalc)  # center
    for q in b:
        print(q, '\n')


# top y anti top 20  scores productocada producto #######

# identificador de idproducto,
# parte del id producto y ve sacando promedios de cada lista
results = []
from listas import lifestore_products, lifestore_sales

b = lifestore_products
a = lifestore_sales
# TOMA B Y A
for id in b:
    # print(id[0]) #cada id  count if
    Z = 0
    N = 0
    refunds = 0
    for sale in a:  # por cada venta
        if id[0] == sale[1]:
            # print(sale)
            Z += sale[2]
            N += 1
            if 1 == sale[4]:
                refunds += 1
    # print(refunds,'ef')
    # print('new')
    # print(Z, N)
    if N != 0:
        # z = x / y
        prom_score = Z / N
    else:
        prom_score = -1
    # print("{0:.2f}".format(prom_score))
    results.append([id[0], id[1][0:27], 'Rate', round(prom_score, 2), 'Refund', refunds])
#
# for i in results:
#     print(i[3])
#     print(i,'\n')


# ordenador de elementos top de mayor a menor en multilist
for i in range(len(results)):
    for j in range(len(results) - 1):
        if results[j][3] < results[j + 1][3]:  # mayor
            temp = results[j]
            results[j] = results[j + 1]
            results[j + 1] = temp
# cuantosproductossevendieron = len(results)
cuantosproductossevendieron = 20
print('\n', 20 * ' ' + 'Top ' + str(
    cuantosproductossevendieron) + ' productos ordenados por score más alta')  # center
for q in results[0:20]:
    print(q, '\n')

# ordenar de menor a mayor considerando refunds
for i in range(len(results)):
    for j in range(len(results) - 1):
        if results[j][3] > results[j + 1][3]:  # mayor
            temp = results[j]
            results[j] = results[j + 1]
            results[j + 1] = temp
c = 0
for i in results:
    if i[3] == -1:
        c += 1
        # print('change')
        # print(c)
    # print(i[3])

cuantosproductossevendieron = 20
print('\n', 20 * ' ' + 'Antitop ' + str(
    cuantosproductossevendieron) + ' productos ordenados por score más baja')  # center
for q in results[c:c + 20]:
    print(q, '\n')
def sort(Numlist, pos_ord):  # ordena en un solo orden menor>  y mayor >
    for i in range(len(Numlist)):
        for j in range(i + 1, len(Numlist)):
            if Numlist[i][pos_ord] > Numlist[j][pos_ord]:
                temp = Numlist[i]
                Numlist[i] = Numlist[j]
                Numlist[j] = temp
    for i in Numlist:
        print(i[0],'*',i[1])  # el asterisco es solo para pasarlo a excel y es un ejemplo para entender
        #que estoy haciendo

#ejemplo de mi función creada
Numlist = [[5, 0], [3, 4], [6, 0], [4, 2]]
# Numlist= [1,3,24,6,7]
pos_ord = 1
mayor = '>'
sort(Numlist, pos_ord)


#MESES THING , crea los días por mes de cada año al usar división fraccionaria o restos en python
bisiesto=True
dias_mes=[]
for x in range(1,13):
    num_days= 28 + (x+x//8)%2 + (2%x) + 2*(1//x)
    if x==2 and bisiesto == True:
        num_days+=1
    dias_mes.append(num_days)
# print(dias_mes)
#MESES thing


from listas import lifestore_sales
for i in range(len(lifestore_sales)):
    for j in range(i + 1, len(lifestore_sales)):
        if int(lifestore_sales[i][3][3:5]) < int(lifestore_sales[j][3][3:5]):
            temp = lifestore_sales[i]
            lifestore_sales[i] = lifestore_sales[j]
            lifestore_sales[j] = temp
nor=[]

for i in lifestore_sales:
    print(i)

from listas import lifestore_products
nor = []
newlis = []
for i in range(len(lifestore_sales)):

    if int(lifestore_sales[i - 1][3][3:5]) != int(lifestore_sales[i][3][3:5]):
        if i != 0:
            # print(newlis)
            nor.append([newlis, lifestore_sales[i - 1][3][3:5]])  #
            # nor.append( lifestore_sales[i][3])
            # print('1')
        newlis = []
        newlis.append(int(lifestore_sales[i][1]))
    else:
        newlis.append(int(lifestore_sales[i][1]))
    if i == (len(lifestore_sales) - 1):
        # print(newlis)
        nor.append([newlis, lifestore_sales[i][3][3:5]])  #
        # print('2')
# print(nor)
puros_ids_de_venta_por_mes = []

for i in nor:
    # print(i[0])
    puros_ids_de_venta_por_mes.append(i[0])
# print(puros_ids_de_venta_por_mes)
# busca el item y ve sumando los ingresos por el mes
# PRIMERO mapear el a
# luego mapear el lifestore
count = 0
a = puros_ids_de_venta_por_mes
# print(range(len(a)))
total=0
num_ventas=0
listf=[]
tempx=[]
#usar los ids de producto para sacar ventas
for i in range(len(a)):
    print('\n')
    for k in range(len(a[i])):
        element_in_question = a[i][k]
        # print(element_in_question)

        for id in range(len(lifestore_products)):
            if element_in_question == lifestore_products[id][0]:
                count += lifestore_products[id][2]
                num_ventas+=1
                # print('Id',element_in_question,'Total $',count, 'Pre. Ind. $', lifestore_products[id][2])
                break
    total = total + count
    print('No. ventas ', num_ventas)
    print('las ventas del mes',nor[i][1],'fueron de $',count) # se reutiliza nor, que tiene la misma
    tempx.append([nor[i][1],count])
    #print(temp,'bnsajfdsbhfsdhkjf')
    listf.append(tempx)
    count=0
    print('Venta promedio mensual es ',round(num_ventas/dias_mes[int(nor[i][1])-1],4))
    print( nor[i][1], round(num_ventas/dias_mes[int(nor[i][1])-1],4))
    num_ventas=0
    # tempx=[]
print('\nIngresos anuales $',total)
print('La venta promedio anual corresponde a ',round(len(lifestore_sales)/(366-31),4)) #-31 dias de dic.
# ya que no hubo ventas ese mes
# print(tempx,'tempx')


# print('\n',listf)
print('\n Meses con mayores ventas $$$')
sort(tempx,1)
# for i in o:
#     print (i)
# print(nor)