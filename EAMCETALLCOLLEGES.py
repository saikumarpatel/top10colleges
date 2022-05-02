from tkinter import ttk
from tkinter import *
import tkinter
import os
from tkinter.ttk import Combobox


import speech_recognition as sr
import pyttsx3
import pandas as pd
from PIL import Image, ImageTk
#import topdwon

def goto():
    import pandas as pd
    data=pd.read_csv("Eamcet analysis/ALL COLLEGES.csv")
    global rankbox,category,r,root4
    if r.get()==1:
        gender="BOYS"
    else:
        gender="GIRLS"
    count=0
    main_frame = Frame(root4)
    main_frame.pack(fill=BOTH, expand=1)

    # create a canvas
    my_canvas = Canvas(main_frame, bg=background)
    my_canvas.pack(side=LEFT, fill=BOTH)

    # add a scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    # create another frame inside the canvas
    second_frame = Frame(my_canvas)

    # add that new frame to a window in the canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
    for i,j,k,l,m,n,o in zip(data["INST CODE"],data["INSTITUTE NAME"],data["BRANCH"],data[f"{category.get()} {gender}"],data["PLACE"],data["TUITION FEE"],data["AFFILIATED"]):
        if k=="CSE":
            if type(l)==str:
                if int(l)<10000:
                    Label(second_frame,text=f'{i}  {j}  {k}  {l}  {m}  {n}  {o}',width=100,font=("BOLD",8)).grid(row=count,column=0)
                    count+=1

    my_canvas = Canvas(root4, bg=background)
    my_canvas.pack(side=LEFT, expand=1, fill=BOTH)
    my_scrollbar = ttk.Scrollbar(root4, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    print(count)

    root4.tkraise()


if __name__=="__main__":
    background="lightblue"
    root = Tk()
    root.title("EAMCET")
    w_width, w_height = 550, 700
    s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
    root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))  # center location of the screen
    root.configure(bg=background)
    # root.attributes('-toolwindow', True)
    root1 = Frame(root, bg=background)
    root2 = Frame(root, bg=background)
    root3 = Frame(root, bg=background)
    root4 = Frame(root, bg=background)
    root5 = Frame(root, bg=background)

    for f in (root1, root2, root3,root4,root5):
        f.grid(row=0, column=0,sticky="news")



    ###### ROOT1 #####
    Frame(root1,width=550,height=700,background=background).pack()
    G_img = Image.open("img.png")
    G_img = G_img.resize((500, 80))
    G_img = ImageTk.PhotoImage(G_img)
    Label(root1, image=G_img).place(x=10,y=10)
    l1 = Label(root1, text="Eamcet Rank",font=("BOLD",16)).place(x=50, y=120)
    rankbox=StringVar()
    rankbox = Entry(root1, width=13, font=("BOLD", 16), relief=FLAT)
    rankbox.place(x=250, y=120)
    l3 = Label(root1, text="Branch",font=("BOLD",16)).place(x=50, y=180)
    branchbox = Combobox(root1, font=("BOLD", 10))
    branchbox['values']=("", "CSE", "CSE_AIML", "CSE_DS", "CSE_CSBS", "MEC", "IT", "ECE", "EEE", "CIVIL")
    branchbox.current(0)
    branchbox.place(x=250, y=180)

    l21 = Label(root1, text="College", font=("BOLD", 16)).place(x=50, y=240)
    collegebox = Combobox(root1, font=("BOLD", 10))
    collegebox['values'] = ("","GRIET","CBIT","VASAVI","VARDHAMAN","VNR","CVR","MVSR","SREENIDHI")
    collegebox.current(0)
    collegebox.place(x=250, y=240)

    l21 = Label(root1, text="Category", font=("BOLD", 16)).place(x=50, y=300)
    category=Combobox(root1,font=("BOLD", 10))
    category['values']=("","OC","BC_A","BC_B","BC_C","BC_D","BC_E","SC","ST","EWS","PH")
    category.current(0)
    category.place(x=250,y=300)


    l5 = Label(root1, text="Gender",font=("BOLD",16)).place(x=50, y=360)
    r = IntVar()
    s = ttk.Style()
    s.configure('Wild.TRadiobutton', background=background, foreground="blue", font=('Arial Bold', 16),
                focuscolor=s.configure(".")["background"])
    genMale = ttk.Radiobutton(root1, text='Male', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
    genMale.place(x=250, y=360)
    genFemale = ttk.Radiobutton(root1, text='Female', value=2, variable=r, style='Wild.TRadiobutton',
                                takefocus=False)
    genFemale.place(x=350, y=360)

    Button(root1,text="Search",command=goto,font=("BOLD",16)).place(x=50,y=420)
    Button(root1,text="Clear",command=lambda:root.destroy(),font=("BOLD",16)).place(x=250,y=420)
    Button(root1, text="HOME", command= lambda :root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
    Button(root1, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
    Button(root1, text="INFO", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=150, y=650)


    #### ROOT 2   #college LOGO#####

    grietlogo = ImageTk.PhotoImage(Image.open("collegeImages/griet.png").resize((550, 200)))
    cbitlogo=ImageTk.PhotoImage(Image.open("collegeImages/cbit.png").resize((550, 200)))
    vasavilogo=ImageTk.PhotoImage(Image.open("collegeImages/vasavi.png").resize((550, 200)))
    mvsrlogo=ImageTk.PhotoImage(Image.open("collegeImages/mvsr.png").resize((550, 200)))
    sreenidhilogo=ImageTk.PhotoImage(Image.open("collegeImages/sreenidhi.png").resize((550, 200)))
    vardhamanlogo=ImageTk.PhotoImage(Image.open("collegeImages/vardhaman.png").resize((550, 200)))
    vnrlogo=ImageTk.PhotoImage(Image.open("collegeImages/vnr.png").resize((550, 200)))
    cvrlogo=ImageTk.PhotoImage(Image.open("collegeImages/cvr.png").resize((550, 200)))


    collegedict={"griet":grietlogo,"cbit":cbitlogo,"vasavi":vasavilogo,"mvsr":mvsrlogo,"vnr":vnrlogo,"sreenidhi":sreenidhilogo,"cvr":cvrlogo,
                 "vardhaman":vardhamanlogo}
    ##### ROOT 2####
    collegecode={"griet":"GRR","cbit":"CBIT","vasavi":"VASV","vnr":"VJEC","cvr":"CVRH","mvsr":"MVSR","vardhaman":"VMEG","sreenidhi":"SNIS"}
    collegebranches={"griet":"CSE,CSE_AIML,CSE_DS,CSE_CSBS,MEC,IT,ECE,EEE,CIVIL",
                     "cbit":"AID', 'CHE', 'CIC', 'CIV', 'CSE', 'CSM', 'ECE', 'EEE', 'INF', 'MEC",
                     "vasavi":"'CIV', 'CSE', 'CSM', 'ECE', 'EEE', 'INF', 'MEC'",
                     "vnr":"CSE,CSE_AIML,CSE_DS,CSE_CSBS,MEC,IT,ECE,EEE,CIVIL",
                     "cvr":"CSE,CSE_AIML,CSE_DS,MEC,IT,ECE,EEE,CIVIL",
                     "mvsr":"CSE,MEC,IT,ECE,EEE,CIVIL",
                    "vardhaman":"CSE,CSE_AIML,MEC,IT,ECE,EEE,CIVIL",
                     "sreenidhi":"CSE,CSE_AIML,CSE_DS,MEC,IT,ECE,EEE,CIVIL"}

    collegename={"griet":"GOKARAJU RANGARAJU INSTITUTE OF ENGERRNING AND TECHNOLOGY",
                 "cbit":"CHAITHNYA BARATHI INSTITUTE OF TECHONOLGY",
                 "vasavi":"VASAVI",
                 "vnr":"VNR",
                 "cvr":"CVR",
                 "mvsr":"MVSR",
                 "sreenidhi":"SREENIDHI",
                 "vardhaman":"VARDHAMAN"}
    collegeadress={}
    collegeurl={}
                   # "cbit":"CSE","CSE_AIML","CSE_DS","CSE_CSBS","MEC","IT","ECE","EEE","CIVIL"}
    def collegeframe(name):
        #root2image = Frame(master=root2, width=550, height=200, background="#d3d3d3").place(x=0, y=50)

        detailFrame2 = Frame(root2)
        detailFrame2.place(x=0,y=50)
        userFrame2 = Label(detailFrame2, image=collegedict[name],width=550, height=250, relief=FLAT)
        userFrame2.pack(padx=0, pady=10)
        collegedetails=Frame(root2,bg="white")
        collegedetails.place(x=0,y=320)
        Label(collegedetails,text="COLLEGE NAME ",width=20).grid(row=0,column=0)
        Label(collegedetails, text=collegename[name],width=60).grid(row=0, column=1)

        Label(collegedetails, text="COLLEGE CODE",width=20).grid(row=1, column=0)
        Label(collegedetails, text=name, width=60).grid(row=1, column=1)

        Label(collegedetails,text="AVILABLE BRANCHES",width=20).grid(row=2,column=0)
        Label(collegedetails,text=collegebranches[name],width=60).grid(row=2,column=1)

        Label(collegedetails, text="NAAC RANK",width=20).grid(row=3, column=0)
        Label(collegedetails, text="A++", width=60).grid(row=3, column=1)


        Label(collegedetails, text="COLLEGE ADDRESS",width=20).grid(row=4, column=0)
        Label(collegedetails, text="NIZAMPET,HYDERABAD", width=60).grid(row=4, column=1)

        Label(collegedetails, text="TUTION FEE",width=20).grid(row=5, column=0)
        Label(collegedetails, text="1,30,000", width=60).grid(row=5, column=1)

        Label(collegedetails, text="HOSTEL FECILITY",width=20).grid(row=6, column=0)
        Label(collegedetails, text="GIRLS", width=60).grid(row=6, column=1)

        Label(collegedetails, text="BUS FECILITY",width=20).grid(row=5, column=0)
        Label(collegedetails, text="YES", width=60).grid(row=5, column=1)

        Label(collegedetails, text="COLLEGE URL",width=20).grid(row=8, column=0)
        Button(collegedetails, text="griet.ac.in", width=60,foreground="blue").grid(row=8, column=1)



        #Label(collegedetails, text="1").grid(row=1, column=0)
        #Label(collegedetails, text=collegebranches[name], width=50).grid(row=2, column=1)



    colleges=["GRIET","CBIT","VASAVI","VARDHAMAN","VNR","CVR","MVSR","SREENIDHI"]
    #for j in range(8):
    x=tkinter.Frame(master=root2,relief=tkinter.RAISED,background="white",border=3)
    x.grid(row=0,column=0,pady=(10,10))
    Button(master=x,text="GRIET",command=lambda :collegeframe("griet"),font=("BOLD",10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=1)
    Button(master=x, text="CBIT", command=lambda :collegeframe("cbit"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=2)
    Button(master=x, text="VASAVI", command=lambda :collegeframe("vasavi"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=3)
    Button(master=x, text="VNR", command=lambda: collegeframe("vnr"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=4)
    Button(master=x, text="SREENIDHI", command=lambda: collegeframe("sreenidhi"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=5)
    Button(master=x, text="MVSR", command=lambda: collegeframe("mvsr"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=6)
    Button(master=x, text="CVR", command=lambda: collegeframe("cvr"), font=("BOLD", 10)).pack()
    x = tkinter.Frame(master=root2, relief=tkinter.RAISED, background="white", border=3)
    x.grid(row=0, column=7)
    Button(master=x, text="VARDHAMAN", command=lambda: collegeframe("vardhaman"), font=("BOLD", 10)).pack()
    """detailFrame2 = Frame(root2, bd=10, bg=background)
    detailFrame2.pack(fill=X)
    userFrame2 = Frame(detailFrame2, bd=10, width=300, height=250, relief=FLAT, bg=background)
    userFrame2.pack(padx=10, pady=10)"""






    Button(root2, text="HOME", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=5, y=650)
    Button(root2, text="COLLEGES", command=lambda: root2.tkraise(), font=("BOLD", 10)).place(x=60, y=650)
    Button(root2, text="INFO", command=lambda: root1.tkraise(), font=("BOLD", 10)).place(x=150, y=650)
    root1.tkraise()
    root1.mainloop()