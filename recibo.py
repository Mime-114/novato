from datetime import date, datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab_qrcode import QRCodeImage
import time
class recibo:

    def __init__(self):
        self.nombrepre=str("Dies Menos")
        self.nit=str("NIT:812.666.862-4")
        self.telefono=str("Telefono:3172929023")
        self.correo=str("Correo:miguel_medinaib@fet.edu.co")
        self.direccion= str("Direccion:calle 73b 25-11")
        self.nombredu=str("Miguel Agel Medina Ibarra")
        #Contado y acumulador
        self.total = 0
        self.o=210#No tocar o si se modifica que sea +20
        self.r=220#No tocar o si se modifica que sea +20
        self.q=493#No tocar o si se modifica que sea +30
        self.g=270
        self.gr=255
        self.gu=360
        #Lista
        self.producto=["tomate","cebolla"]#SI TOCAR
        self.precios=["500","200"]#SI TOCAR
        self.productos=[]#NOOOO TOCAR
        self.c=canvas.Canvas("recibo2.pdf", pagesize=A4)
        self.w, self.h = A4
    def recibo_en_terminal(self):
        a=int(input("Ingrese la contraseña iniciar la factura "))
        if a==2426:
            print("=======================================================================================")
            print("                               ","Menu","                                      ")
            print("                               ",self.producto,"                                      ")
            print("=======================================================================================")
            print("                               ",self.nombredu,"                                      ")
            print("                               ",self.telefono,"                                            ")
            print("=======================================================================================")
            print("                              ", self.correo,"                                         ")
            print("                             ",self.nombrepre,"                                        ")
            print("                             ",self.direccion,"                                        ")
            print("                             ",self.nit,"                                              ")
            print("                             ",date.today(),"                               ")
            print("=======================================================================================")
            self.cajero=input("Ingrese el nombre del cajero ")
            #de aqui se modifico todo
            while True:
                self.resul_lis_pro=self.producto.index(input("Que producto deseas: "))
                self.lista_pro=self.producto[self.resul_lis_pro]
                self.lista_pro_1=str(self.lista_pro)
                self.cantidad = int(input("¿Cuanto va llevar?: "))
                self.lista_pre= self.precios[self.resul_lis_pro]
                self.precio =int(self.lista_pre)
                print("El precio por unidad es ",self.precio)
                self.subtotal=self.cantidad * self.precio
                self.total = self.total+self.subtotal
                self.productos.append(("       "+str(self.cantidad)+"        -       "+self.lista_pro_1+"         -       "+str(self.precio)+"        -      "+str(self.subtotal)+"     =     "))
                self.continuar = input("Presionar V para imprimir el recibo o enter para continuar agregando:")
                if self.continuar == "V":
                    print("Productos: ")
                    for p in self.productos:
                        self.o=self.o+30
                        print("       Unidades      -    Descripcion      -     Precio      -    subtotal     =     ")
                        print("=",p) 
                        self.produc=str(p)
                        print("Precio total: ", self.total)
                        self.tol=str(self.total)
                        self.c.drawString(150, self.h - self.r, " ="+self.produc)
                        self.o=self.o+5
                        self.r=self.r+20 #NO TOCAR
                        self.q=self.q-35
                        self.g=self.g+30
                        self.gr=self.gr+25
                        self.gu=self.gu+30

                    break
        else:
            print("Ingresaste mal la contraseña")
    def mostrar_en_pdf_1(self):
        self.i=500
        self.u=0
        self.tiempo=str(time.strftime("%X"))#este %X significa hora actual
        self.tiempo2=str(time.strftime("Fecha: %x"))#este %x significa fecha
        #no tocar
        self.c.drawString(150, self.h - 55, "===========================================")
        self.c.drawString(270, self.h - 70, " "+self.nombrepre )
        self.c.drawString(150, self.h - 85, "===========================================")
        self.c.drawString(150, self.h - 110, " -"+self.nit)
        self.c.drawString(318, self.h - 110, " -"+self.telefono)
        self.c.drawString(150, self.h - 130, " -"+self.correo)
        self.c.drawString(356, self.h - 130, " -"+self.tiempo2)
        self.c.drawString(150, self.h - 150, "===========================================")
        self.c.drawString(150, self.h - 165, " -"+self.cajero)
        self.c.drawString(318, self.h - 165, " -"+self.tiempo)
        self.c.drawString(150, self.h - 180, "===========================================")
        self.c.drawString(150, self.h - 200, " =Unidades====Descripcion====Precio====subtotal==")
        self.c.drawString(335, self.h - self.o, " =precio total "+self.tol)
        self.c.drawString(210, self.h - self.gr, "=Gracias por visitarnos que vuelvan pronto=")
        self.c.drawString(150, self.h - self.g, "===========================================")
        qr = QRCodeImage("https://github.com/Mime-114", size=30 * mm)
        qr.drawOn(self.c, 260, self.q)
        self.c.drawString(150, self.h - self.gu, "===========================================")
        self.c.save()
reci=recibo()
reci.recibo_en_terminal()
reci.mostrar_en_pdf_1()
