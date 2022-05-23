import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
from tkinter import font,colorchooser,messagebox,filedialog
win=tk.Tk()
win.title("file222")
win.wm_iconbitmap(r"C:\Users\Admin\Desktop\text editor 2\icon (1).ico")
menubar=tk.Menu(win)
open_icon=tk.PhotoImage(r"C:\Users\Admin\Desktop\text editor 2\icons2\save_as.png")
save_as_icon=tk.PhotoImage(r"C:\Users\Admin\Desktop\text editor 2\icons2\save_as.png")
exit_icon=tk.PhotoImage(r"C:\Users\Admin\Desktop\text editor 2\icons2\red.png")
new_icon=tk.PhotoImage(file=r"C:\Users\Admin\Desktop\text editor 2\icons2\new.png")
# open(r'C:\\Users\\Admin\\Desktop\\text editor 2')
# save_icon=tk.PhotoImage(r"C:\Users\Admin\Desktop\text editor 2\icons2\save.png")
file_menu=tk.Menu(menubar,tearoff=0)
url=""
text_changed=""
def new(event=None):
    global url
    url=""
    text_editer.delete(1.0,tk.END)
    
file_menu.add_command(label="New",accelerator="Ctrl+N",command=new)
def save_op(event=None):
    global url
    try:
        if url:
            content=str(text_editer.get(1.0,tk.END))
            with open (url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url= filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
            content2=text_editer.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

file_menu.add_command(label="Save",accelerator="Ctrl+S",command=save_op)
def exi(event=None):
    global url
    text_changed=text_editer.get(1.0,tk.END)
    try:
        if text_changed:
            mbox= messagebox.askyesnocancel('Warning','Do you want to save the file?')
            if mbox is True:
                if url:
                    content=str(text_editer.get(1.0,tk.END))
                    with open (url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                else:
                    content2=str(text_editer.get(1.0,tk.END))
                    url= filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
                    content2=text_editer.get(1.0,tk.END)
                    url.write(content2)
                    url.close()
            elif mbox is False:
                    win.destroy()
                
        else:
            win.destroy()
    except:
        return
            
file_menu.add_command(label="Exit",accelerator="Ctrl+Q",command=exi)
def save_as(event=None):
    global url
    try:
           content=text_editer.get(1.0,tk.END)
           url= filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
           url.write(content)
           url.close()
    except:
        return


file_menu.add_command(label="Save_as",accelerator="Ctrl+Shift+S",command=save_as)
def open_file():
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title="select file",filetypes=(('Text File','*.txt'),("ALL files",'*.*')))
    try:
        with open(url,'r') as fr:
            text_editer.delete(1.0,tk.END)
            text_editer.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    win.title(os.path.basename(url))
file_menu.add_command(label="Open",accelerator="Ctrl+O",command=open_file)
#EDIT MENU
edit_menu=tk.Menu(menubar,tearoff=0)

def et():
    text_editer.event_generate("<Control z>")
def tt():
    text_editer.event_generate("<Control+shift+z>")
def er():
    text_editer.event_generate("<Control c>")
def sd():
     text_editer.event_generate("<Control v>")
def aw():
     text_editer.event_generate("<Control x>")  
edit_menu.add_command(label="Copy",accelerator="Ctrl+S",command=er)
edit_menu.add_command(label="Paste",accelerator="Ctrl+V",command=sd)
edit_menu.add_command(label="Cut",accelerator="Ctrl+X",command=aw)
edit_menu.add_command(label="Undo",accelerator="Ctrl+Z",command=et)
edit_menu.add_command(label="Redo",accelerator="Ctrl+Shift+Z",command=tt)


View_menu=tk.Menu(menubar,tearoff=0)
shoe_statusbar=tk.BooleanVar()
shoe_statusbar.set(True)

shoe_toolbar=tk.BooleanVar()
shoe_toolbar.set(True)

def hide_toolbar():
    global shoe_toolbar
    if shoe_toolbar:
        tool_bar.pack_forget()
        shoe_toolbar=False
    else:
        text_editer.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editer.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        shoe_toolbar=True
def hide_statusbar():
    global shoe_statusbar
    if shoe_statusbar:
        status_bar.pack_forget()
        shoe_statusbar=False
    else:
        text_editer.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editer.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        shoe_statusbar=True
View_menu.add_checkbutton(label="toolbar_icon",onvalue=True,offvalue=1,variable=shoe_toolbar,command=hide_toolbar)
View_menu.add_checkbutton(label="statusbar_icon",onvalue=1,offvalue=False,variable=shoe_statusbar,command=hide_statusbar)


colour_menu=tk.Menu(menubar,tearoff=0)
# colour_theme=tk.Menu(menubar,tearoff=0)
theme_choice=tk.StringVar()
colour_dict={
    'Light Default':("#000000","#ffffff"),
    'Light Plus':("#474747","#e0e0e0"),
    "Dark":("#c4c4c4","#2d2d2d"),
    "Red":("#2d2dd2","#ffe8e8"),
    'Night Blue':("#d2b774","#474747")
    }
def change_theme():
    choosen_theme=theme_choice.get()
    colour_tiple=colour_dict.get(choosen_theme)
    fg_colur,bg_coloue=colour_tiple[0],colour_tiple[1]
    text_editer.config(background=bg_coloue,fg=fg_colur)
    
    
counter=0
for i in colour_dict:
    colour_menu.add_radiobutton(label=i,variable=theme_choice,command=change_theme)
    counter+=1
    
#toolbar    
tool_bar=ttk.Label(win)    
tool_bar.pack(side=tk.TOP,fill=tk.X)
tool_tuple=tk.font.families()
# print(tk.font.families())
font_family=tk.StringVar()
font_bow=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
# font_bow.current(tool_tuple.index("Arial"))
font_bow["values"]=tool_tuple
font_bow.grid(row=0,column=0,padx=5)
#size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state="readonly")
font_size["values"]=tuple(range(2,30,2))
font_size.current(6)
font_size.grid(row=0,column=1,padx=5)
#bold botton

bold_icon=tk.PhotoImage(file=r"C:\Users\Admin\Desktop\text editor 2\icons2\bold.png")
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=3)
italic_icon=tk.PhotoImage(file=r"C:\Users\Admin\Desktop\text editor 2\icons2\italic.png")
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=4)
underline_icon=tk.PhotoImage(file=r"C:\Users\Admin\Desktop\text editor 2\icons2\underline.png")
underine=ttk.Button(tool_bar,image=underline_icon)
underine.grid(row=0,column=5)
align_left_icon=tk.PhotoImage(file=r"C:\Users\Admin\Desktop\text editor 2\icons2\align_left.png")
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

align_center_icon=tk.PhotoImage(file=r"C:\Users\Admin\Desktop\text editor 2\icons2\align_center.png")
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

align_right_icon=tk.PhotoImage(file=r"C:\Users\Admin\Desktop\text editor 2\icons2\align_right.png")
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

colorchooser_tk = tk.PhotoImage(file=r"C:\Users\Admin\Desktop\text editor 2\icons2\font_color.png")
colorchooser_tk_btn=ttk.Button(tool_bar,image=colorchooser_tk)
colorchooser_tk_btn.grid(row=0,column=9,padx=5)

text_editer=tk.Text(win)
text_editer.config(wrap="word",relief=tk.FLAT)
text_editer.pack()
scroll_bar=tk.Scrollbar(win)
text_editer.focus()
scroll_bar.pack(side=tk.RIGHT,fill=tk.BOTH)
text_editer.pack(fill=tk.BOTH,expand=True)
scroll_bar.configure(command=text_editer.yview)
text_editer.configure(yscrollcommand=scroll_bar)
currunt_font_family='Arial' 
currunt_font_size=12
def change_font(win):
    global currunt_font_family
    currunt_font_family=font_family.get()
    text_editer.configure(font=(currunt_font_family,currunt_font_size))
def change_size(win):
    global currunt_font_size
    currunt_font_size=size_var.get()
    text_editer.configure(font=(currunt_font_family,currunt_font_size)) 
font_bow.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)
#botton's funtionality
#bold botton
def fuctiion():
    

    
    def change_bold():
        
        text_property=tk.font.Font(font=text_editer['font'])
        if text_property.actual()['weight']=='normal':
            text_editer.configure(font=(currunt_font_family,currunt_font_size,"bold"))
            
        if text_property.actual()['weight']=='bold':
            text_editer.configure(font=(currunt_font_family,currunt_font_size,"normal"))
    bold_btn.configure(command=change_bold)
    #italic 
    def change_italic():
       
        text_property=tk.font.Font(font=text_editer['font'])
        if text_property.actual()['slant']=='roman':
            text_editer.configure(font=(currunt_font_family,currunt_font_size,"italic"))
        
        if text_property.actual()['slant']=='italic':
            text_editer.configure(font=(currunt_font_family,currunt_font_size,"normal"))
    italic_btn.configure(command=change_italic)
    #underline
    def change_underline():
        text_property=tk.font.Font(font=text_editer['font'])
        if text_property.actual()['underline']==1:
            text_editer.configure(font=(currunt_font_family,currunt_font_size,"normal"))   
        if text_property.actual()['underline']==0:
            text_editer.configure(font=(currunt_font_family,currunt_font_size,"underline"))
    underine.configure(command=change_underline)
fuctiion()
#alingment
def align_left():
    text_content=text_editer.get(1.0,'end')
    text_editer.tag_config('left',justify=tk.LEFT)
    text_editer.delete(1.0,'end')
    text_editer.insert(tk.INSERT,text_content,'left')
align_left_btn.configure(command=align_left)
def align_center():
    text_content=text_editer.get(1.0,'end')
    text_editer.tag_config('center',justify=tk.CENTER)
    text_editer.delete(1.0,'end')
    text_editer.insert(tk.INSERT,text_content,'center')
align_center_btn.configure(command=align_center)
def align_right():
    text_content=text_editer.get(1.0,'end')
    text_editer.tag_config('right',justify=tk.RIGHT)
    text_editer.delete(1.0,'end')
    text_editer.insert(tk.INSERT,text_content,'right')
align_right_btn.configure(command=align_right)

text_editer.configure(font=('Arial',12))

def change_font_color():
    var_p=tk.colorchooser.askcolor()
    text_editer.configure(fg=var_p[1]) 
colorchooser_tk_btn.configure(command = change_font_color)
#STATUS BAR
status_bar=ttk.Label(win,text="status bar")
status_bar.pack(side=tk.BOTTOM)
def change(Event=None):
    if text_editer.edit_modified():
        words=len(text_editer.get(1.0,"end-1c").split())
        char=len(text_editer.get(1.0,"end-1c").replace(" ",""))
        status_bar.configure(text=f"charcters:{char} : words={words}")
    text_editer.edit_modified(False)
text_editer.bind("<<Modified>>",change)

menubar.add_cascade(label="FILE",menu=file_menu)
menubar.add_cascade(label="EDIT",menu=edit_menu)
menubar.add_cascade(label="View",menu=View_menu)
menubar.add_cascade(label="Colour",menu=colour_menu)
win.configure(menu=menubar) 
win.bind("<Control-n>",new)
win.bind("<Control-o>",open_file)
# win.bind("<Control-s>",save_op)
# win.bind("<Control-v>",)
# win.bind("<Control-c>",open_file)
# win.configure(menu=tool_bar)
win.mainloop()
