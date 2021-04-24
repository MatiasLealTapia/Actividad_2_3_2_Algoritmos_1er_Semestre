#Valor de cada producto
agua=600
azucar=1200
aceite=1500
arroz=1250
fideos=790
bebida=1780
chocolate=2500
pan_molde=1340

total_pagar=0
descuento=1.00
vuelto=0

print("\n           --- Bienvenido a tu Supermercado Favorito ---           ")

#Preguntar si es cliente preferencial y poner descuento
c_pref=(input("\n¿Usted es Cliente preferencial?(si/no) "))
if c_pref.lower()=="si":
    descuento=0.80
    print("Se le aplicara un descuento del 20% a su compra final.\n")
elif c_pref.lower()=="no":
    descuento=1.00
    print("No se le aplicara descuento a su compra final.\n")

#Agua
resp_ag=input("¿Quiere llevar agua?(si/no): ")
if resp_ag.lower()=="si":
    #Darle valor a la agua que lleva
    num_agua=int(input("¿Cuantas botellas de agua quiere llevar? "))
    valor_agua=agua*num_agua
    total_pagar+=valor_agua

#Azucar
resp_az=input("¿Quiere llevar azucar?(si/no): ")
if resp_az.lower()=="si":
    #Darle valor a la azucar que lleva
    num_azucar=int(input("¿Cuanta azucar quiere llevar? "))
    valor_azucar=azucar*num_azucar
    total_pagar+=valor_azucar

#Aceite
resp_ac=input("¿Quiere llevar aceite?(si/no): ")
if resp_ac.lower()=="si":
    #Darle valor al aceite que lleva
    num_aceite=int(input("¿Cuanto aceite quiere llevar? "))
    valor_aceite=aceite*num_aceite
    total_pagar+=valor_aceite

#Arroz
resp_ar=input("¿Quiere llevar arroz?(si/no): ")
if resp_ar.lower()=="si":
    #Darle valor al arroz que lleva
    num_arroz=int(input("¿Cuanto arroz quiere llevar? "))
    valor_arroz=arroz*num_arroz
    total_pagar+=valor_arroz

#Fideos
resp_fi=input("¿Quiere llevar fideos?(si/no): ")
if resp_fi.lower()=="si":
    #Darle valor a los fideos que lleva
    num_fideos=int(input("¿Cuantos fideos quiere llevar? "))
    valor_fideos=fideos*num_fideos
    total_pagar+=valor_fideos

#Bebida
resp_be=input("¿Quiere llevar bebida?(si/no): ")
if resp_be.lower()=="si":
    #Darle valor a las bebidas que lleva
    num_bebida=int(input("¿Cuantas botellas de bebida quiere llevar? "))
    valor_bebida=bebida*num_bebida
    total_pagar+=valor_bebida

#Chocolates
resp_ch=input("¿Quiere llevar chocolate?(si/no): ")
if resp_ch.lower()=="si":
    #Darle valor a los chocolates que lleva
    num_chocolate=int(input("¿Cuanto chocolate quiere llevar? "))
    valor_chocolate=chocolate*num_chocolate
    total_pagar+=valor_chocolate

#Pan molde
resp_pm=input("¿Quiere llevar pan de molde?(si/no): ")
if resp_pm.lower()=="si":
    #Darle valor a el pan molde que lleva
    num_pan_molde=int(input("¿Cuanto pan molde quiere llevar? "))
    valor_pan_molde=pan_molde*num_pan_molde
    total_pagar+=valor_pan_molde

#Total
total_sin_desc=int(total_pagar)
total_pagar*=descuento
total_pagar=int(total_pagar)
print(f"\nEl total de su boleta es de: ${total_pagar}")
pago=int(input("¿Con cuanto dinero pagará?: $"))
if pago>=total_pagar: #Boleta
    vuelto=pago-total_pagar
    print("\n|     --- Supermercado Favorito --- |\n")
    if resp_ag.lower()=="si":
        print(f"|    Agua:       {num_agua}             ${valor_agua} |")
    if resp_az.lower()=="si":
        print(f"|    Azucar:     {num_azucar}            ${valor_azucar} |")
    if resp_ac.lower()=="si":
        print(f"|    Aceite:     {num_aceite}            ${valor_aceite} |")
    if resp_ar.lower()=="si":
        print(f"|    Arroz:      {num_arroz}            ${valor_arroz} |")
    if resp_fi.lower()=="si":
        print(f"|    Fideos:     {num_fideos}             ${valor_fideos} |")
    if resp_be.lower()=="si":
        print(f"|    Bebida:     {num_bebida}            ${valor_bebida} |")
    if resp_ch.lower()=="si":
        print(f"|    Chocolate:  {num_chocolate}            ${valor_chocolate} |")
    if resp_pm.lower()=="si":
        print(f"|    Pan Molde:  {num_pan_molde}            ${valor_pan_molde} |")
    print(f"\n|    Total:                  ${total_sin_desc} |")
    if c_pref.lower()=="si":
        print("|                              -20% |")
    print(f"|                             ----- |\n|                             ${total_pagar} |\n|                            -${pago} |")
    print(f"|    Vuelto:                   ${vuelto} |")
    print("\n|     --- Supermercado Favorito --- |\n")







    print("\nGracias por comprar, vuelva pronto!")
else:
    print("Dinero insuficiente, Guardias!”.")

