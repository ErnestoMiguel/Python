from tkinter import *
from tkinter import messagebox
import sys
from db_file import create_db
from db_file import insert_data

def create_root(): #Creamos la raiz de nuestro GUI
    root = Tk()
    root.title("Registro de Candidatos")
    root.config(height=450, width=350)
    return root

#Crea widjet de tipo Frame
def create_frame(root): 
    my_frame = Frame(root, height=400, width=300, padx=10, pady=10, border=5)
    my_frame.pack(expand=True, fill="both")
    return my_frame

 #Creamos widjet de tipo Label
def create_label(my_frame, mtext, mrow, mcolumn, msticky):
    my_label = Label(my_frame, text=mtext)
    my_label.grid(row=mrow, column=mcolumn, sticky=msticky, padx=10, pady=10)
    return my_label

#Creamos widjet de tipo Box
def create_box(my_frame, mrow, mcolumn, msticky, show_char=None): 
    my_box = Entry(my_frame, show=show_char)
    my_box.grid(row=mrow, column=mcolumn, sticky=msticky, padx=10, pady=10)
    return my_box

 #creamos widget de tipo scrollbar
def create_scrollbar(my_frame, mrow, mcolumn, msticky,mcommand):
    scrollbar_1 = Scrollbar(my_frame, command=mcommand)
    scrollbar_1.grid(row=mrow, column=mcolumn, sticky=msticky)
    return scrollbar_1

#Creamos el widjet de tipo button
def create_button(my_frame, mtext, mcommand=None): 
    my_button = Button(my_frame, text=mtext ,command=mcommand)
    my_button.pack(fill="x")
    return my_button

#Crea widjets de tipo radio button
def create_radio_button(my_frame, mtext, mrow, mcolumn, msticky, rb_option, mvalue, mcommand):
    my_rbutton = Radiobutton(my_frame, text=mtext, variable=rb_option, value=mvalue, command=mcommand)
    my_rbutton.grid(row=mrow, column=mcolumn, sticky=msticky)
    return my_rbutton

 #Creamos el widjet de tipo Text
def create_text(my_frame, mrow, mcolumn, msticky): 
    my_text= Text(my_frame, width=16, height=5)
    my_text.grid(row=mrow, column=mcolumn, sticky=msticky, padx=10,pady=10)
    return my_text

def create_menu(root):
    menu_bar = Menu(root)
    return menu_bar

#Funcion para recibir el genero desde los RadioButton
def gender_reveal(rb_option):
    return "Masculino" if rb_option.get()==1 else "Femenino"

#Tomamos los datos introducidos por el usuario y lo almacenamos en la base de datos
def get_data():  
    try:
        nombre = box_1.get()
        edad = box_2.get()
        genero = gender_reveal(rb_option)
        dir = box_3.get()
        tel = box_4.get()
        acerca = text_1.get("1.0", END)
        insert_data(nombre, edad, genero, dir, tel, acerca)
        messagebox.showinfo("Informacion", "Enviado exitosamente, ¡Gracias!")
    except Exception:
        messagebox.showerror("Error", "Ups, ha ocurrido un Error")
    clear_all()

#Funcion para limpiar todos los datos y empezar denuevo
def clear_all():
    box_1.delete(0, END)
    box_2.delete(0, END)
    box_3.delete(0, END)
    box_4.delete(0, END)
    text_1.delete("1.0", END)

def main():
    global box_1, box_2, box_3, box_4, text_1

    create_db() #creamos la base de datos y la tabla si no existen
    root = create_root()  #Instancia de la raiz
    my_frame = create_frame(root)  #Instancia del Frame

    global rb_option
    rb_option = IntVar()

    #Instancia del metodo de creacion del menu
    menu_bar = create_menu(my_frame)
    root.config(menu=menu_bar)
    menu_bar.config(cursor="hand2")

    menu_archivo = Menu(menu_bar, tearoff=0)
    menu_archivo.add_command(label="Administrar", underline=1)
    menu_archivo.add_command(label="Nuevo", underline=0, command=lambda:clear_all())
    menu_archivo.add_command(label="Salir", command=sys.exit, underline=0)

    menu_bar.add_cascade(label="Archivo", underline=0, menu=menu_archivo)

    #Instancas de las Etiquetas
    label_1 = create_label(my_frame, "Nombre:", 0, 0, "e")
    label_2 = create_label(my_frame, "Edad:", 1, 0, "e")
    label_3 = create_label(my_frame, "Direccion:", 2, 0, "e")
    label_4 = create_label(my_frame, "Telefono:", 3, 0, "e")  
    label_5 = create_label(my_frame, "Acerca de ti:", 6, 0, "e")
    label_6 = create_label(my_frame, "Genero", 4, 0, "e") 

    #Instancias de los boxes
    box_1 = create_box(my_frame, 0, 1,"e")
    box_2 = create_box(my_frame, 1, 1,"e")
    box_3 = create_box(my_frame, 2, 1,"e")
    box_4 = create_box(my_frame, 3, 1,"e")

    #Instancio el cuadro de texto
    text_1 = create_text(my_frame, 6, 1, "e")

    #creamos el scrollbar
    scrollbar_1 = create_scrollbar(my_frame, 6, 2, "nsew" ,text_1.yview)
    text_1.config(yscrollcommand=scrollbar_1.set)

    #Instanciamos los RadioButton
    radiobutton_1 = create_radio_button(my_frame, "Masculino", 4, 1, "e",rb_option , 1, lambda:rb_option.get())
    radiobutton_2 = create_radio_button(my_frame, "Femenino", 5, 1, "e",rb_option, 2, lambda:rb_option.get())
    #Instancias de los botones
    #Los Botones los instancie en el root pq esteticamente me gusta mas y no afecta mi funcionamiento general
    button_1 = create_button(root, "Enviar", mcommand=get_data)
    button_2 = create_button(root, "Cancelar", mcommand=sys.exit)


    root.mainloop()

if __name__=="__main__":
    main()
