class ViewBiblioteca:
    
    
    def mostrar_menu(self):
        opcion = int(input('''
                           
    Menú Principal
    1. Registrar libro
    2. Mostrar libros
    3. Buscar libro por código
    4. Buscar libros por categoría
    5. Actualizar libro
    6. Eliminar libro
    7. Salir
                           
    Input: '''))
        

        return opcion

    #=-=--==--=-==-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    def pedir_datos(self): #codigo, titulo, autor, categoria)
        codigo = input('Ingrese el codigo del libro a registrar: ')
        titulo = input('Ingrese el titulo del libro a registrar: ')
        autor = input('Ingrese el autor del libro a registrar: ')
        categoria = input('Ingrese la cAtegoria del libro a registrar: ')

        return codigo,titulo,autor,categoria
    
    #3
    def pedir_codigo(self):
        return input('Ingrese el codigo del libro a registrar: ')
        
    #4
    def pedir_categoria(self):
        return input('Ingrese la cAtegoria del libro a registrar: ')

    #=-=--==--=-==-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
    
    #=-=--==--=-==-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    