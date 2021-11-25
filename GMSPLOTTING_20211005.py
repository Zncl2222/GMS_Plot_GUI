import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import PIL.Image
import PIL.ImageTk
from matplotlib.font_manager import FontProperties
from pylab import *
import threading


class GUI_thread():
    
    def thread(func,*args):
        t=threading.Thread(target=func,args=args)
        t.setDaemon(True)
        t.start()


class GMS_Plot:
    
    def ReadData(self,filepath):
        a=os.listdir(filepath)
        Z = pd.read_table(filepath+'\\'+a[0],header=None,encoding='UTF16',sep='\s+')
        Z = np.zeros((len(a),np.shape(Z)[0],2))
        for i in range(len(a)):
            Y=pd.read_table(filepath+'\\'+a[i],header=None,encoding='UTF16',sep='\s+')
            Z[i,:]=Y.iloc[:,2:4]
        return Z
    
    def ReadData2(self,filepath):
        a=os.listdir(filepath)
        Z = pd.read_table(filepath+'\\'+a[0],header=None,encoding='UTF16')
        Z = np.zeros((len(a),np.shape(Z)[0],2))

        for i in range(len(a)):
            Y=pd.read_table(filepath+'\\'+a[i],header=None,encoding='UTF16')
            Y[2]=Y[2].apply(lambda x: np.NaN if str(x).isspace() else x)
            Y[3]=Y[3].apply(lambda x: np.NaN if str(x).isspace() else x)
            Z[i,:]=Y.iloc[:,2:4]
        return Z

    def Subplot4(self,Z,savdir,ratio):

        for i in range(len(Z[0][:,0])):
            if abs(Z[0][i,0]-Z[0][i-1,0])>=20:
                SL=i
            if np.isnan(Z[0][i,0])==True:
                SL2=i
                break

        fig, axes = plt.subplots(4,4, sharex=True, sharey=True,figsize=(15,8))
        print(axes.flatten())
        x1=range(SL)
        x2=range(SL,SL2)
        x_max1=Z[0][SL2-1][0]
        count=0
        for i, ax in enumerate(axes.flatten()):
            ax.plot(Z[count][x1,0], Z[count][x1,1],linewidth=2,color='k')
            ax.plot(Z[count][x2,0], Z[count][x2,1],linewidth=2,color='r',linestyle='--')
            ax.set_ylim([0, 1])
            if self.cc==False:
                ax.set_xlim([0, x_max1*ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count+=1
        plt.tight_layout()
        plt.savefig(savdir,dpi=800)

    def Subplot3(self,Z,savdir,ratio):

        for i in range(len(Z[0][:,0])):
            if abs(Z[0][i,0]-Z[0][i-1,0])>=20:
                SL=i
            if np.isnan(Z[0][i,0])==True:
                SL2=i
                break

        fig, axes = plt.subplots(3,3, sharex=True, sharey=True,figsize=(15,8))
        print(axes.flatten())
        x1=range(SL)
        x2=range(SL,SL2)
        x_max1=Z[0][SL2-1][0]
        count=0
        for i, ax in enumerate(axes.flatten()):
            ax.plot(Z[count][x1,0], Z[count][x1,1],linewidth=2,color='k')
            ax.plot(Z[count][x2,0], Z[count][x2,1],linewidth=2,color='r',linestyle='--')
            ax.set_ylim([0, 1])
            if self.cc==False:
                ax.set_xlim([0, x_max1*ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count+=1
        plt.tight_layout()
        plt.savefig(savdir,dpi=800)


    def Subplot2(self,Z,savdir,ratio):

        for i in range(len(Z[0][:,0])):
            if abs(Z[0][i,0]-Z[0][i-1,0])>=20:
                SL=i
            if np.isnan(Z[0][i,0])==True:
                SL2=i
                break
        
        fig, axes = plt.subplots(2,2, sharex=True, sharey=True,figsize=(15,8))

        #print(axes.flatten())
        x1=range(SL)
        x2=range(SL,SL2)
        x_max1=Z[0][SL2-1][0]
        count=0

        for i, ax in enumerate(axes.flatten()):
            ax.plot(Z[count][x1,0]*ratio, Z[count][x1,1],linewidth=2,color='k')
            ax.plot(Z[count][x2,0]*ratio, Z[count][x2,1],linewidth=2,color='r',linestyle='--')
            ax.set_ylim([0, 1])
            #ax.set_title('ab')
            if self.cc==False:
                ax.set_xlim([0, x_max1*ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count+=1   


        plt.tight_layout()
        
        plt.savefig(savdir,dpi=500)
        
        if __name__=='__main__':
            plt.show(block=False)

    def button_event(self,):


        filepath=myentry.get()
        filename=myentry2.get()
        figdir=myentry3.get()
        
        a=os.listdir(filepath)
        
        self.cc=check.get()

        ratio=float(myentry4.get())



        if os.path.isdir(figdir):
            print("Create the path")
        else:
            os.mkdir(figdir)


        Data=Case1.ReadData(filepath)

        #print(Data[0][:,0])


        figdir=figdir+"\\"+filename

        if len(a)==4:
            Case1.Subplot2(Data,figdir,ratio)
        elif len(a)==9:
            Case1.Subplot3(Data,figdir,ratio)
        elif len(a)==16:
            Case1.Subplot4(Data,figdir,ratio)
            
    def button_event2(self):

        filepath=myentry_semi.get()
        filename=myentry2_semi.get()
        figdir=myentry3_semi.get()
        
        a=os.listdir(filepath)
        
        self.cc=check_semi.get()

        ratio=float(myentry4_semi.get())

        if os.path.isdir(figdir):
            print("Create the path")
        else:
            os.mkdir(figdir)


        Data=Case1.ReadData2(filepath)

        #print(Data)


        figdir=figdir+"\\"+filename
        
        Case1.semi_plot(Data,figdir,ratio)
       
    def semi_plot(self,Z,savdir,ratio):

        for i in range(len(Z[0][:,0])):
            if np.isnan(Z[0][i,0])==True and np.isnan(Z[0][i-1,0])==False:
                SL=i
            if np.isnan(Z[0][i,0])==True and np.isnan(Z[0][i+1,0])==False:
                SL2=i
                break
        x1=range(SL)
        x2=range(SL2,len(Z[0][:]))

        for i in range(len(Z)):
            plt.figure(num=123+i,figsize=(9,7))
            plt.plot(Z[i][x1,0]*ratio, Z[i][x1,1],linewidth=2,color='k',label="Model")
            plt.plot(Z[i][x2,0]*ratio, Z[i][x2,1],linewidth=2,color='r',linestyle='--',label="Theory")
            plt.xticks(fontsize=18);plt.yticks(fontsize=18)
            plt.legend()
            plt.ylabel("Semi-variance",fontsize=24)
            plt.xlabel("Lag distance",fontsize=24)
            plt.ticklabel_format(style='sci',axis='x',scilimits=(0,0),useMathText=True,useOffset=False)
            plt.rc('font', size=17)
            plt.grid(alpha=0.25)
            plt.tight_layout()
            plt.savefig(savdir,dpi=500)
            if __name__=='__main__':
                plt.show(block=False)
        
        

if __name__=='__main__':
    root = tk.Tk()
    root.title('莊信宏GMS畫圖懶人包')
    root.geometry('700x720')

    tab_main=ttk.Notebook()
    tab_main.place(relx=0,rely=0,relwidth=1,relheight=1)

    tab1=ttk.Frame(tab_main)
    tab1.place(x=0,y=30)
    tab_main.add(tab1,text='Markov Chain')
    
    tab2=ttk.Frame(tab_main)
    tab2.place(x=10,y=30)
    tab_main.add(tab2,text="Semi-Variance")

    #------------------------------------Options for Spatial Plotting---------------------------------


    im = PIL.Image.open("C:\JianYu\THM project\GUITEST\X\X.png")
    photo = PIL.ImageTk.PhotoImage(im)
    label = tk.Label(tab1, image=photo,compound=tk.CENTER)
    label.image = photo  
    label.grid(row=7,column=1,pady=20)


    Case1=GMS_Plot()

    title=tk.Label(tab1,text="莊信宏GMS畫圖懶人包",bg='blue', fg='white',font='18')
    title.grid(row=0,column=1)

    label1=tk.Label(tab1,text='Path for DataReading')
    label1.grid(row=1,column=0)

    label2=tk.Label(tab1,text='File name')
    label2.grid(row=2,column=0)

    label3=tk.Label(tab1,text='Path for figure saving')
    label3.grid(row=3,column=0)

    label4=tk.Label(tab1,text="X axis Magnification")
    label4.grid(row=4,column=0)

    check=tk.BooleanVar()
    check.set(False)

    checkbox=ttk.Checkbutton(tab1,text="Constrain X axis",var=check)
    checkbox.grid(row=5,column=0,padx=5,ipadx=5)

    myentry = tk.Entry(tab1)
    myentry.insert(0,(r"C:\Users\3002shinning\Downloads\2X2\2X2"))
    myentry.grid(row=1,column=1,pady=5,ipadx=100)

    myentry2 = tk.Entry(tab1)
    myentry2.insert(0,("GMS_Plot1"))
    myentry2.grid(row=2,column=1,pady=5,ipadx=100)


    myentry3=tk.Entry(tab1)
    myentry3.insert(0,'C:\JianYu\THM project\GUITEST\X')
    myentry3.grid(row=3,column=1,pady=5,ipadx=100)

    myentry4=tk.Entry(tab1)
    myentry4.insert(0,'1')
    myentry4.grid(row=4,column=1,pady=5,ipadx=10)


    mybutton = tk.Button(tab1, text='Run', command=lambda:GUI_thread.thread(Case1.button_event))
    mybutton.grid(row=5,column=1)

    #-----------------------------Semi-Vairnace---------------------------------------
    
    title_semi=tk.Label(tab2,text="莊信宏GMS畫圖懶人包",bg='blue', fg='white',font='18')
    title_semi.grid(row=0,column=1)

    label1_semi=tk.Label(tab2,text='Path for DataReading')
    label1_semi.grid(row=1,column=0)

    label2_semi=tk.Label(tab2,text='File name')
    label2_semi.grid(row=2,column=0)

    label3_semi=tk.Label(tab2,text='Path for figure saving')
    label3_semi.grid(row=3,column=0)

    label4_semi=tk.Label(tab2,text="X axis Magnification")
    label4_semi.grid(row=4,column=0)

    check_semi=tk.BooleanVar()
    check_semi.set(False)

    checkbox_semi=ttk.Checkbutton(tab2,text="Constrain X axis",var=check)
    checkbox_semi.grid(row=5,column=0,padx=5,ipadx=5)

    myentry_semi = tk.Entry(tab2)
    myentry_semi.insert(0,(r"C:\Users\3002shinning\Downloads\semivarigram\semivarigram"))
    myentry_semi.grid(row=1,column=1,pady=5,ipadx=100)

    myentry2_semi = tk.Entry(tab2)
    myentry2_semi.insert(0,("GMS_Plot1"))
    myentry2_semi.grid(row=2,column=1,pady=5,ipadx=100)


    myentry3_semi=tk.Entry(tab2)
    myentry3_semi.insert(0,'C:\JianYu\THM project\GUITEST\X')
    myentry3_semi.grid(row=3,column=1,pady=5,ipadx=100)

    myentry4_semi=tk.Entry(tab2)
    myentry4_semi.insert(0,'1')
    myentry4_semi.grid(row=4,column=1,pady=5,ipadx=10)

    mybutton_semi = tk.Button(tab2, text='Run', command=Case1.button_event2)
    mybutton_semi.grid(row=5,column=1)

    root.mainloop()

