# -*- coding: utf-8 -*-


#Empezaremos a ejecutar algunos algoritmos
#Cristian David Moreno
#Variable: referencias a posiciones de memoria de un dato o valor
Edad=18;
print(Edad);
print("Edad: ", Edad);
Nombre= "Jonias";
print(Nombre);
print("Nombre: ", Nombre);
alto=False;
print("Edad: ", Edad, "Nombre: ", Nombre, "Alto?", alto);
alto=True;
print("Edad: ", Edad, "Nombre: ", Nombre, "Alto?", alto);
estatura=1.67;
print("Edad: ", Edad, "Nombre: ", Nombre, "Alto?", alto, "Estatura: ", estatura);

#Operaciones aritmeticas
numero_1 = 3;
numero_2 = 4;
suma= numero_1 + numero_2;
resta= numero_1-numero_2;
negacion = -numero_1;
multiplicacion= numero_1 * numero_2;
exponente = numero_1**numero_2;
division = numero_1/numero_2;
division_entera = numero_1//numero_2;
modulo = numero_1%numero_2;


print("Numero 1: ", numero_1, "Numero 2: ", numero_2, "Suma: ", suma, "Resta: ", resta, "Negación: ", negacion, "Multiplicación: ", multiplicacion, "Exponente n1^n2:", exponente, " División: ", division, "División entera:", division_entera, "Módulo: ", modulo);

#Variables binarias y operadores
a = int(input("Ingrese un numero 1: "));
b = int(input("Ingrese un numero 2: "));
c = a + b;
d = a - b;
e = a % b;
print("Suma: ", c, "Resta: ", d, "Módulo: ", e);
if(c>d):
    print("Es mayor la suma que la resta");
else:
    print("Es menor la suma que la resta");
 
#Ingreso de valores

nombre_1 = input("Ingrese su nombre a continuación: ");
    
print("Su nombre es: ", nombre_1);


edad_i = int (input("Ingrese su edad a continuación: "));


print("Su edad es: ", edad_i);

edade = int (input("Ingrese su edad a continuación: "));
if(edade>18):
    print("Usted es mayor de edad");
else:
    print("Usted es menor de edad");
       
#Operadores mod div
numero1 = 28;
numero2 = 8;
modulo = 28 % 8;
print("Modulo:", modulo);
div = numero1 // numero2;
print("Div:", div);

#Condicionales con ingresos

numero = int(input ("Ingrese un numero: "));
if(numero % 2 ==0):
    print("el numero es par")
else:
    print("el numero es impar")
    

#Ciclo mientras

i = 1;
s = 0;
while(i < 10):
    s = s+i;
    print("S: ", s, "i:", i);
    i= i+1;
    
cantidad = int(input("Ingrese el número de estudiantes del grupo: "));
j = 1;
sumas = 0;
promedio = 0;
while(j < cantidad):
    an = int(input("Ingrese edad del estudiante: "));
    sumas = sumas + an;
    j = j + 1;
    
prom = sumas / cantidad;
print("El promedio de edad del grupo es: ", prom);

tamano = int(input("Ingrese el tamaño del grupo: "));
mayores = 0;
edad_mayor = 0;
k=1;
while(k <= tamano):
    edad_1 = int(input("Ingrese la edad del estudiante: "));
    if(edad_1 >= 18):
        mayores = mayores + 1;
    if (edad_1 > edad_mayor):
        edad_mayor=edad_1;
k= k +1;            
print("La cantidad de mayores es:", mayores);
print("La edad del mayor es:", edad_mayor);


#Ciclo para

for l in range(10):
    print (l);

for m in range(1,10):
    print (l);

for n in range(1,10,2):
    print (l);


#arreglos en python
edz = [23, 17, 45, 46, 32, 16];
for o in range (len(edz)):
    print(edz[o]);
    print("posición 0: ", edz[0]);
    print("posición 4: ", edz[4]);

temperaturas = [12,13,14,11,10,19,14,16,17,18];
print(temperaturas[-1]);
print(temperaturas[-2]);
for p in range (len(temperaturas)):
     print(temperaturas[p]);
 
     
edu = [12,15,16,17,18,19,20,21,14];
es = int(input("Ingrese la edad: "));
for r in range (len(edu)):
    if(es == edu[r]):
        print("Se encontro esa edad en el arreglo");
        print("En la posición", r);
        
#Matrices en python

Ma = ([12,13,45], [45,42,16], [78,16,17]);
for s in range(len(Ma)):
    for t in range(len(Ma)):
        print (Ma[s][t], end = "  ");
        print ("  ");

Mat = ([13,14,15], [16,17,18], [19,20,21]);
for u in range(3):
    for v in range(3):
        Mat[u][v]= u+v;
        print (Mat);
        
        
#Funciones en python

def funcion (a,b,c):
    return (a+b+c)
suma_3 = funcion(13, 15, 30);
print("La suma es igial a ", suma_3);


def primate (w):
    for x in range(2,int(w/2)):
        if(x % w == 0):
            return False;
        return True;
    print(primate(14));
    
Arr=[13,21,24,27,31,33,32];
for x in Arr:
    if (primate(x)):
      print  ("el numero", x ," es primo");
        
    
Arreglito =[21,25,26,27,28,29];
def promedito(Arreglito):
    sumita=0;
    for y in Arreglito:
        sumita = sumita + y;
    return sumita/len(Arreglito);
print("Promedio:", promedito(Arreglito));

Arregla = [65, 47, 46, 49, 19, 78, 13, 20];
def mayor_arregla(z):
    mayora=z[0];
    for aa in range(len(z)):
        if(mayora<z[aa]):
            mayora=z[aa]
            return mayora;
print("El mayor del arreglo es:", mayor_arregla(Arregla));

    
            
    
       
        

        
    







    

    

