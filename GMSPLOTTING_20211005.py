import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import PIL.Image
import PIL.ImageTk
from matplotlib.font_manager import FontProperties
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#from matplotlib.backend_bases import key_press_handler
#from matplotlib.figure import Figure
from pylab import *



class GMS_Plot:
    
    def ReadData(self,filepath):
        a=os.listdir(filepath)
        Z = pd.read_table(filepath+'\\'+a[0],header=None,encoding='UTF16',sep='\s+')
        Z = np.zeros((len(a),np.shape(Z)[0],2))
        for i in range(len(a)):
            Y=pd.read_table(filepath+'\\'+a[i],header=None,encoding='UTF16',sep='\s+')
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
            ax.plot(Z[count][x1,0]*ratio, Z[count][x1,1],linewidth=2,color='k')
            ax.plot(Z[count][x2,0]*ratio, Z[count][x2,1],linewidth=2,color='r',linestyle='--')
            ax.set_ylim([0, 1])
            if self.cc==True:
                ax.set_xlim([0, x_max1*ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count+=1
        plt.tight_layout()
        plt.savefig(savdir,dpi=300)
        plt.show()

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
            ax.plot(Z[count][x1,0]*ratio, Z[count][x1,1],linewidth=2,color='k')
            ax.plot(Z[count][x2,0]*ratio, Z[count][x2,1],linewidth=2,color='r',linestyle='--')
            ax.set_ylim([0, 1])
            if self.cc==True:
                ax.set_xlim([0, x_max1*ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count+=1
        plt.tight_layout()
        plt.savefig(savdir,dpi=300)
        plt.show()


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
            if self.cc==True:
                ax.set_xlim([0, x_max1*ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count+=1   


        plt.tight_layout()
        
        plt.savefig(savdir,dpi=300)
    
        plt.show()

    def button_event(self,):


        filepath=self.myentry.get()
        filename=self.myentry2.get()
        figdir=self.myentry3.get()
        
        a=os.listdir(filepath)
        
        self.cc=self.check.get()

        ratio=float(self.myentry4.get())



        if os.path.isdir(figdir):
            print("Create the path")
        else:
            os.mkdir(figdir)


        Data=self.ReadData(filepath)

        #print(Data[0][:,0])


        figdir=figdir+"\\"+filename

        if len(a)==4:
            self.Subplot2(Data,figdir,ratio)
        elif len(a)==9:
            self.Subplot3(Data,figdir,ratio)
        elif len(a)==16:
            self.Subplot4(Data,figdir,ratio)
        


    def tkgui(self):

        root = tk.Tk()
        root.title('莊信宏GMS畫圖懶人包')
        root.geometry('700x720')


        #------------------------------------Options for Spatial Plotting---------------------------------


        im = PIL.Image.open("zklmr\X.png")
        photo = PIL.ImageTk.PhotoImage(im)
        label = tk.Label(root, image=photo,compound=tk.CENTER)
        label.image = photo  
        label.grid(row=7,column=1,pady=20)


        #x=np.arange(0,3,0.01)
        #y=np.sin(2*np.pi*x)

        #a.plot(x,y)

        #canvas=FigureCanvasTkAgg(F,master=root)
        #canvas.draw()
        #canvas.get_tk_widget().grid(row=6,column=1,pady=50,ipady=50)

        #Case1=GMS_Plot()

        self.title=tk.Label(root,text="莊信宏GMS畫圖懶人包",bg='blue', fg='white',font='18')
        self.title.grid(row=0,column=1)

        self.label1=tk.Label(root,text='Path for DataReading')
        self.label1.grid(row=1,column=0)

        self.label2=tk.Label(root,text='File name')
        self.label2.grid(row=2,column=0)

        self.label3=tk.Label(root,text='Path for figure saving')
        self.label3.grid(row=3,column=0)

        self.label4=tk.Label(root,text="X axis Magnification")
        self.label4.grid(row=4,column=0)

        self.check=tk.BooleanVar()
        self.check.set(True)

        self.checkbox=ttk.Checkbutton(root,text="Constrain X axis",var=self.check)
        self.checkbox.grid(row=5,column=0,padx=5,ipadx=5)

        self.myentry = tk.Entry(root)
        self.myentry.insert(0,(r"C:\Users\3002shinning\Downloads\2X2\2X2"))
        self.myentry.grid(row=1,column=1,pady=5,ipadx=100)

        self.myentry2 = tk.Entry(root)
        self.myentry2.insert(0,("GMS_Plot1"))
        self.myentry2.grid(row=2,column=1,pady=5,ipadx=100)


        self.myentry3=tk.Entry(root)
        self.myentry3.insert(0,'C:\JianYu\THM project\GUITEST\X')
        self.myentry3.grid(row=3,column=1,pady=5,ipadx=100)

        self.myentry4=tk.Entry(root)
        self.myentry4.insert(0,'1')
        self.myentry4.grid(row=4,column=1,pady=5,ipadx=10)




        self.mybutton = tk.Button(root, text='Run', command=lambda:self.button_event())
        self.mybutton.grid(row=5,column=1)


        root.mainloop()




if __name__ == '__main__':
    #queue = Queue()
    c=GMS_Plot()
    c.tkgui()
    #p = Process(target=c.tkgui)
    #p.start()
    
    #queue.put(c.tkgui())
    
    # Wait for the worker to finish
    #queue.close()
    #queue.join_thread()
    #p.join()