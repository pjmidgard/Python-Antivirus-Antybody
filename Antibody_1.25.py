# author: Jurijus Pacalovas


from tkinter import *

from queue import Queue


from random import shuffle

class AntivirusAntibody(Frame):

    # initialises the application
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        
        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        self.pack(expand=True)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(self)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(self)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(self)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames
        self.open_card = Button(cards_frame)
        the_card = PhotoImage(file='cards/antibody.gif')
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        closed_deck = Button(cards_frame)
        closed_card = PhotoImage(file='cards/antibody.gif')
        closed_deck.config(image=closed_card)
        closed_deck.grid(row=0, column=1, padx=2, pady=2)
        closed_deck.photo = closed_card

        
        exit_button = Button(button_frame, text="Scan", command=self.AntivirusAntibody_exit)
        exit_button.grid(row=2, column=0, pady=13)


        



    # called by the exit_button Button
    # ends the GUI application
    def AntivirusAntibody_exit(self):
        
        import subprocess, os, time, binascii, glob
        
        
        for namez1 in glob.glob("*exe"):
                print(namez1)
                close_malware=0
                nemez='taskkill /F /IM '+namez1
                with open(namez1, "rb") as binary_file:
                                # Read the whole file at once
                                data = binary_file.read()
                                s=str(data)
                                lenf1=len(data)
                                sda=bin(int(binascii.hexlify(data),16))[2:]
                                lenf=len(sda)      
                                lenf1=len(data) 
                                xc=(lenf1*8)-lenf
                                z=0
                                if xc!=0:
                                        while z<xc:
                                                sda="0"+sda
                                                z=z+1
                                sdas=sda[0:256]
                                sdasb=int(sdas,2)
                with open("save.bin", "rb") as binary_file:
                        data1 = binary_file.read()
                        s=str(data1)
                        lenf1=len(data1)
                        sda=bin(int(binascii.hexlify(data1),16))[2:]
                        lenf=len(sda)      
                        lenf1=len(data1) 
                        xc=(lenf1*8)-lenf
                        z=0
                        if xc!=0:
                                while z<xc:
                                        sda="0"+sda
                                        z=z+1
                        lenf2=len(sda) 
                        ww1=0
                        ww2=0
                        while ww2<lenf2:
                                ww1=ww2
                                ww2=ww2+256
                                sdas1=sda[ww1:ww2]
                                sdasb1=int(sdas1,2)
                                if sdasb1==sdasb:
                                        close_malware=close_malware+1
                if close_malware>0:
                        print("Malware deleted")
                        CREATE_NO_WINDOW = 0x08000000
                        subprocess.call(nemez, creationflags=CREATE_NO_WINDOW)
                        os.remove(namez1)
                        close_malware=0
                else:
                        print("Malware has not founded")
                def destroy(plat):
                        if plat == 'win':
                                import _winreg
                                from _winreg import HKEY_CURRENT_USER as HKCU
                                run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
                                try:
                                        reg_key = _winreg.OpenKey(HKCU, run_key, 0, _winreg.KEY_ALL_ACCESS)
                                        _winreg.DeleteValue(reg_key, 'br')
                                        _winreg.CloseKey(reg_key)
                                except WindowsError:
                                        pass
                        elif plat == 'nix':
                                pass
                        elif plat == 'mac':
                                pass
                        os.remove(sys.argv[0])
                        sys.exit(0) 
        raise SystemExit

    


# object creation here:
root = Tk()
root.geometry("1324x1324")

root.title("Antibody")

app = AntivirusAntibody(root)

root.mainloop()


