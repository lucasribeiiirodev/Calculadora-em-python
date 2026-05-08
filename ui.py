import tkinter as tk
import cores
from logica import calcular

def iniciar_app():
    janela = tk.Tk()
    janela.geometry("400x600")
    janela.title("CAUCULADORA PYTHON")
    janela.configure(bg=cores.BG)
    display = tk.Entry(janela,
                state="readonly",
                readonlybackground=cores.DISPLAY_BG,
                bd=0,
                relief="flat",
                font= ("arial", 60),
                justify="right",
                insertbackground="white",
                fg="white")
    
    def atualizar_display(valor):
        display.config(state="normal")
        display.delete(0, tk.END)
        display.insert(0, valor)
        display.config(state="readonly")
    
    atualizar_display("0")
    display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)
    #DISPLAY
    
    def clique(valor):
        atual = display.get()
        pos_resultado = [False]
        if atual == "0" and valor in ["/","*","-","+"]:
            return 

        if atual[-1] in ["-","+","/","*"] and valor in ["-","+","/","*"]:
            return
        
        if atual == "0" and valor == ".":           
            return 
        
        trecho_atual = atual.split("/")[-1].split("*")[-1].split("+")[-1].split("-")[-1]
        
        if "." in trecho_atual and valor == ".":
            return
        
        if valor == "CE":
            atualizar_display("0") 
        elif valor == "=":
            atualizar_display(calcular(atual))
            pos_resultado[0] = True
        else:
            if atual == "0" or pos_resultado[0]:
                atualizar_display(valor)
                pos_resultado[0] = False
            else:
                display.config(state="normal")
                display.insert(tk.END, valor)
                display.config(state="readonly")
    
    botoes=[
        ["7","8","9","/"],
        ["4","5","6","*"],
        ["1","2","3","-"],
        ["0",".","=","+"],
        ["CE","","",""]]
    
    for linha, lista in enumerate(botoes):
        for coluna, valor in enumerate(lista):
            
            if valor in ["/","*","-","+"]: 
                bg= cores.BTN_OP
            elif valor == "CE":
                bg= cores.BTN_C
            elif valor == "=":
                bg= "gray"
            elif valor == "":
                continue
            else:
                bg=cores.BTN_NUM
            
            
            btn = tk.Button(
                janela,
                command=lambda v=valor: clique(v),
                text=valor,
                bg=bg,
                fg=cores.BTN_TXT,
                font=("Arial", 18, "bold"),
                bd=0,
                activebackground=bg,
                activeforeground="white",
                cursor="hand2")
            
            btn.grid(
                row=linha + 1,
                column=coluna,
                padx=4,
                pady=4,
                sticky="nsew",
                ipadx=10,
                ipady=18
            )
            
    for i in range(4):
                janela.grid_columnconfigure(i, weight=1)   # 4 colunas iguais

    for i in range(6):
                janela.grid_rowconfigure(i, weight=1)
          
    janela.mainloop()
