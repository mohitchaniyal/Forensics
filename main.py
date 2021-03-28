from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import winreg
from codecs import decode
import sys
from tkinter import filedialog
import webbrowser
class Forensics(object) :
    def __init__(self,window):
       
        self.window=window

        self.imgg=Image.open("IMG/new.png")
        self.imgre=self.imgg.resize((195,50),Image.ANTIALIAS)
        self.logo=ImageTk.PhotoImage(self.imgre)

        # save_ico=Image.open('IMG/filesave.png')
        # save_ico_re=imgg.resize((20,30),Image.ANTIALIAS)
        # self.save_ico=ImageTk.PhotoImage(save_ico_re)
        
        
        self.mainframe=Frame(self.window)
        self.mainframe.pack()

        self.manubar=Menu(self.window)
        self.window.config(menu=self.manubar)
        self.file=Menu(self.manubar,tearoff=0)
        self.About=Menu(self.manubar,tearoff=0)
        self.manubar.add_cascade(label='File',menu=self.file)
        self.file.add_command(label='New',command=main)
        
        self.file.add_command(label='Save',command=self.save_file)
       
        self.file.add_command(label='Exit',command=sys.exit)
        self.manubar.add_cascade(label='About',menu=self.About)

        self.About.add_command(label='Follow Us On Facebook',command=self.open_facebook)
        self.About.add_command(label='Follow Us On Instagram',command=self.open_instagram)
        self.About.add_command(label='Follow Us On Github',command=self.open_github)
        self.About.add_command(label='Subscribe To Our Youtube Channel',command=self.open_youtube)

        self.bottom_frame=Frame(self.mainframe,height='20',bg='#292929',pady=1,padx=1)
        self.bottom_frame.pack(side=BOTTOM,fill=X)
        self.bottom_frame_label=Label(self.bottom_frame,text='All Rights Are Reserved To Mohit Kumar Chaniyal  |  Nitesh Kumar |  Harsh Thapliyal  |  Paurash Yadav ***   ',fg='White',bg='#292929')
        self.bottom_frame_label.pack(side=RIGHT)

        self.left_frame=Frame(self.mainframe,height='700',width='200',bg='#393939',borderwidth=2,relief=GROOVE,padx=10)
        self.left_frame.pack(side=LEFT,fill=Y)
        
        
        self.right_frame=Frame(self.mainframe,height='700',width='1000',bg='#393939',borderwidth=2,relief=GROOVE,pady=1,padx=1)
        self.right_frame.pack(side=RIGHT,fill=Y)

        

        self.tabs=ttk.Notebook(self.right_frame,width='900',height='700')
        
        self.tabs.pack(side=TOP)
        self.tab1=ttk.Frame(self.tabs)
        self.tabs.add(self.tab1,text='Introduction')
        self.intro_label=Text(self.tab1,width='800',height='700')
        
        self.intro_label.pack()
        self.intro_label.insert(END,'''Welcome To Forensics\n> This tool is based on digital forensics and Digital forensics is a branch of forensic science encompassing the recovery and investigation of material foundin digital devices, often in relation to computer crime.By using this tool we can perform windows forensics in a begginer level .
\n>This tool is build using python 3 and the modules used in this tool are ->\n 1.Tkinter for GUI \n 2.Winreg for communicating with Windows Registry 
 3.PIL for image resizing  
 4.Decode for decoding the regbinary data to readable format.''')

        try:
            self.lable=Label(self.left_frame,image=self.logo,bg='#393939')
            self.lable.pack(side=TOP)
        except :
            pass

        self.lframe=LabelFrame(self.left_frame,text='Tools',height='650',width='200',bg="#393939",fg='white',padx=5,pady=5)
        self.lframe.pack()

        self.recent_D_B=Button(self.lframe,text="Recent Doc",height=3,width=25,bg='#292929',fg='white',command=self.recent_doc)
        self.recent_D_B.pack()
        
        self.p_ran=Button(self.lframe,text="Previusly Run",height=3,width=25,bg='#292929',fg='white',command=self.p_run_app)
        self.p_ran.pack()

        self.Run_search=Button(self.lframe,text="Run Searches",height=3,width=25,bg='#292929',fg='white',command=self.run_searches)
        self.Run_search.pack()
        
    def recent_doc(self) :
        self.recent_doc_list=[]
        net=r"Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs"
        with winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER) as access_registry :
            with winreg.OpenKey(access_registry,net,0,winreg.KEY_ALL_ACCESS) as access_key :
                num_of_values = winreg.QueryInfoKey(access_key)[1]
                self.recent_doc_list.append('Recent Doc\n\n')
                for i in range(1,num_of_values):
                    try :
                        name,value,type = winreg.EnumValue(access_key,i)
                        a=value[::2][:value[::2].find(b'\x00')].decode()
                        
                        self.recent_doc_list.append(a+'\n')
                    except :
                        continue
                self.recent_doc_list.append('\n')
                self.recent_doc_tab()
    def recent_doc_tab(self):
        self.rtab=ttk.Frame(self.tabs)
        self.tabs.add(self.rtab,text='Recently Open Doc')
        self.r_d_textbox=Text(self.rtab,width='800',height='700',wrap=WORD)
        self.r_d_textbox.pack()
        
        for i in self.recent_doc_list:
            self.r_d_textbox.insert(END,i)


    def p_run_app(self):
        self.p_run_app_list=[]
        def enum_key(hive, subkey):
            with winreg.OpenKey(hive, subkey, 0, winreg.KEY_ALL_ACCESS) as key:
                num_of_values = winreg.QueryInfoKey(key)[1]
                self.p_run_app_list.append('Priviosly Run Application\n\n')
                for i in range(num_of_values):
                    values=winreg.EnumValue(key, i)
                    if values[0] == "MRUList":
                        continue
                    val=str(values[1])
                    
                    self.p_run_app_list.append(val+'\n')
                self.p_run_app_list.append('\n')
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkcu_hive:
            enum_key(hkcu_hive, r"SOFTWARE\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache")
        self.p_run_app_tab()
    
    def p_run_app_tab(self):
        self.p_run_tab=ttk.Frame(self.tabs)
        self.tabs.add(self.p_run_tab,text='Priviously Run App')
        self.p_r_textbox=Text(self.p_run_tab,width='800',height='700',wrap=WORD)
        self.p_r_textbox.pack()
        for i in self.p_run_app_list:
            self.p_r_textbox.insert(END,i)
    
    def run_searches(self):
        self.run_searches=[]
        def enum_key(hive, subkey):
            with winreg.OpenKey(hive, subkey, 0, winreg.KEY_ALL_ACCESS) as key:
                num_of_values = winreg.QueryInfoKey(key)[1]
                self.run_searches.append('Run searches \n\n')
                for i in range(num_of_values):
                    values=winreg.EnumValue(key, i)
                    if values[0] == "MRUList":
                        continue
                    val=str(values[1])
                    
                    self.run_searches.append(val+'\n')
                self.run_searches.append('\n')
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkcu_hive:
            enum_key(hkcu_hive, r"Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU")
        self.run_searches_tab()

    def run_searches_tab(self):
        self.run_searches_tab=ttk.Frame(self.tabs)
        self.tabs.add(self.run_searches_tab,text='Run Searches')
        self.run_searches_textbox=Text(self.run_searches_tab,width='800',height='700',wrap=WORD)
        self.run_searches_textbox.pack()
        for i in self.run_searches:
            self.run_searches_textbox.insert(END,i)
    def save_file(self):
        file=filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if file== None:
            return
        try :
            self.recent_doc_data=self.r_d_textbox.get(1.0, 'end-1c')
            file.write(self.recent_doc_data)
        except:
            pass
        try :
            self.p_run_data=self.p_r_textbox.get(1.0, 'end-1c')
            file.write(self.p_run_data)
        except:
            pass
        try :
            self.run_searches_data=self.run_searches_textbox.get(1.0, 'end-1c')
            file.write(self.run_searches_data)
        except:
            pass
    def open_youtube(self):
        webbrowser.open('https://www.youtube.com/pythohacker')

    def open_facebook(self):
        webbrowser.open('https://www.facebook.com/pythohacker')

    def open_instagram(self):
        webbrowser.open('https://www.instagram.com/pythohacker')

    def open_github(self):
        webbrowser.open('https://github.com/mohitchaniyal')
def main():
    root=Tk()
    root.title('Forensics')
    root.geometry('1132x770+100+50')
    root.iconbitmap('IMG/Turbo.ico')
    # root.maxsize(1080,720)
    app=Forensics(root)
    root.mainloop()
if __name__=="__main__":
    main()