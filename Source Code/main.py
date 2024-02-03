#Boyd Gibson
#Graded Unit Developing Stage
#Fitness Application
#main.py



# main.py
import kivy



#-------------------------------------------------------------------------
#Importing all of the nessasery tools from the kivy dictionary
#-------------------------------------------------------------------------
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.carousel import Carousel
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.button import Button
from kivy.uix.video import Video
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.togglebutton import ToggleButton
import webbrowser
import sqlite3
import random
#-------------------------------------------------------------------------






#-------------------------------------------------------------------------
#This is all for making it easier to write to the database 
#-------------------------------------------------------------------------
global conn
conn = sqlite3.connect("Databse.db")
global cursor
cursor = conn.cursor()
un = ""
#-------------------------------------------------------------------------




























#====================================================================================================================
#this is where the email and password validation will be done for creating an account
#this will require the user to include a '@' and '.' in the email
#as well as preventing you from leaving the feilds empty
#====================================================================================================================


class CreateAccountWindow(Screen):


#Setting variables
    global namee
    namee = ObjectProperty(None)
    global email
    email = ObjectProperty(None)
    global password
    password = ObjectProperty(None)




#Declaring window properties
#this makes sure that the window size cant be changed by the user
#as well as not allowing the use to make the application full screen
    Config.set('graphics', 'fullscreen', '0')
    Config.set('graphics', 'resizable', '0')
    Config.set('graphics', 'width', '400')
    Config.set('graphics', 'height', '600')






#This is the verification process to make sure that the user has entered the right information and to make sure that the accound doesn't allredy exist
    def submit(self):


        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            #Make sure that the user hasn't left the feilds blank
            cursor.execute("SELECT * FROM UserIfo WHERE Email=?", [self.email.text])
            #Email verification
            if cursor.fetchone() == None:

                cursor.execute("SELECT * FROM UserIfo WHERE Username=?", [self.namee.text])
                #Username Verification
                if cursor.fetchone() == None:
                    
                    if self.password != "":

                        global un
                        un = self.namee.text
                        #usename namee
                        global em
                        em = self.email.text
                        #email
                        global ps
                        ps = self.password.text
                        #password
                        sm.current = "q1"
                    else:
                        invalidForm()
                        #input validation
                else: 
                    usedUsename()
                    #input validation

            else:
                usedEmail()
                #input validation
        else:
            invalidForm()
            #input validation    
#-------------------------------------------------------------------------------------------------------------------------------------------------------



    def login(self):
#Moves user to next screen
        self.reset()
        sm.current = "main"


    def reset(self):
#makes the feilds blank once they have created the account
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

#====================================================================================================================
#====================================================================================================================










































#====================================================================================================================
#this is where the validation will occur for teh user logging in 
#this will prevent the user form leaving the feilds empty
#ass well as checking that the email and password match and are in the database
#====================================================================================================================
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):

    #Verifing that the account exists and that the password matches it
        cursor.execute("SELECT * FROM UserIfo WHERE Email=? and Password=?", [self.email.text, self.password.text])
        global em
        em = self.email.text
        if cursor.fetchone() == None:
            invalidLogin()
        else:
            #make the feilds blank and send user to next page
            self.reset()
            sm.current = "home"
            


    def createBtn(self):
        #sends user to the create accound page
        self.reset()
        sm.current = "create"

    def reset(self):
        # makes the password feild blank
        self.password.text = ""
#====================================================================================================================
#====================================================================================================================

































#====================================================================================================================
#this is the first block of queations where the user will enter there firstname, lastname,  date of birth and select what gender they are
#this is validated so that the user must fill all feilds
#only once the validation process has been complete will the user move on to the lext screen
#====================================================================================================================

class Questions1(Screen):

    #Declaring variables
    fname = ""
    lname = ""
    global age
    age= 0
    ma = 0
    fem = 0




#--------------------------------------------------------------------------------------------
#This part of code changes the image of the button to make it look like it has been selected
#it also changes the value of the variable linked to it which is used later
    def male_on(self):
        self.ids.male.source = 'graphics/male2.png'
        self.ids.female.source = 'graphics/female1.png'

        self.ma = 1
        self.fem = 0
        


    def female_on(self):
        self.ids.female.source = 'graphics/female2.png'
        self.ids.male.source = 'graphics/male1.png'


        self.ma = 0
        self.fem = 1
#--------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------
#Next button
    def next_on(self):
        self.ids.next.source = 'graphics/next2.png'

    def next_off(self):
        self.ids.next.source = 'graphics/next.png'
#--------------------------------------------------------------------------------------------



#Verification to make sure that the user hasn't left the feilds blank 
    def check(self):


        if self.fname.text != "" and self.lname.text != "" and self.age.text != "" :
            if self.fname.text.count("0") >0 or self.fname.text.count("1") >0 or self.fname.text.count("2") >0 or self.fname.text.count("3") >0 or self.fname.text.count("4") >0 or self.fname.text.count("5") >0 or self.fname.text.count("6") >0 or self.fname.text.count("7") >0 or self.fname.text.count("8") >0 or self.fname.text.count("9") >0 or self.fname.text.count(".") > 0:
                #makes sure that the user doesnt enter numbers
                invalidSelection()
                #input validation
            elif self.lname.text.count("0") >0 or self.lname.text.count("1") >0 or self.lname.text.count("2") >0 or self.lname.text.count("3") >0 or self.lname.text.count("4") >0 or self.lname.text.count("5") >0 or self.lname.text.count("6") >0 or self.lname.text.count("7") >0 or self.lname.text.count("8") >0 or self.lname.text.count("9") >0 or self.lname.text.count(".") > 0:
                #makes sure that the user cant add numbers
                invalidSelection()
                #input validation
            elif int(self.age.text) > 100:
                #makes sure that the user enters appropriate age
                invalidSelection()
                #input validation
            elif int(self.age.text) < 14:
                #makes sure that the user anters an appropraite age
                invalidSelection()
                #input validation
            else:
                if self.ma == 0 and self.fem == 0 :
                    #making sure that the user clicked on of the buttons
                    invalidSelection()
                    #input validation
                
                else:
                    #this is for entering values into the database
                    global gn
                    global fn
                    fn = self.fname.text
                    #firstname
                    global ln
                    ln = self.lname.text
                    #lastname
                    global ag
                    ag = self.age.text
                    #age

                    if self.ma == 0:
                        
                        gn = "Female"
                        #gender
                    else:
                        
                        gn = "Male"
                        #gender

                    sm.current = "q2"
            
        else:
            invalidSelection()
            #input validation
#====================================================================================================================
#====================================================================================================================



































#====================================================================================================================
#this is the second block of questions where the user will select the button that corosponds closest to the question asked
#as the buttons are scelected the button will change color, visualy representing that the button has been clicked
#only once the validation process has been complete will the user move on to the lext screen
#====================================================================================================================

class Questions2(Screen):
#Decaring Variables
    beg = 0
    inter = 0
    advan = 0
    light = 0
    mod = 0
    high = 0
#=============================================================================================
    #NNext Button
    #changing the color of the button
    def next_on(self):
        self.ids.next.source = 'graphics/next2.png'

    def next_off(self):
        self.ids.next.source = 'graphics/next.png'

#=============================================================================================
    





#-------------------------------------------------------------------------------------------- 
#This part of code changes the image of the button to make it look like it has been selected
#it also changes the value of the variable linked to it which is used later
    def beginer_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process
        self.ids.beginer.source = 'graphics/beginer2.png'
        self.ids.intermediate.source = 'graphics/intermediate1.png'
        self.ids.advanced.source = 'graphics/advanced1.png'
        self.beg = 1
        self.inter = 0
        self.advan = 0


    def intermediate_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process
        self.ids.intermediate.source = 'graphics/intermediate2.png'
        self.ids.beginer.source = 'graphics/beginer1.png'
        self.ids.advanced.source = 'graphics/advanced1.png'

        self.beg = 0
        self.inter = 1
        self.advan = 0

    def advanced_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process
        self.ids.advanced.source = 'graphics/advanced2.png'
        self.ids.beginer.source = 'graphics/beginer1.png'
        self.ids.intermediate.source = 'graphics/intermediate1.png'

        self.beg = 0
        self.inter = 0
        self.advan = 1


#=============================================================================================

    def lightly_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process
        self.ids.lightly.source = 'graphics/lightly2.png'
        self.ids.moderatly.source = 'graphics/moderatly1.png'
        self.ids.highly.source = 'graphics/highly1.png'
        self.light = 1
        self.mod = 0
        self.high = 0

    def moderatly_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process
        self.ids.moderatly.source = 'graphics/moderatly2.png'
        self.ids.lightly.source = 'graphics/lightly1.png'
        self.ids.highly.source = 'graphics/highly1.png'
        self.light = 0
        self.mod = 1
        self.high = 0


    def highly_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process
        self.ids.highly.source = 'graphics/highly2.png'
        self.ids.lightly.source = 'graphics/lightly1.png'
        self.ids.moderatly.source = 'graphics/moderatly1.png'
        self.light = 0
        self.mod = 0
        self.high = 1





#-------------------------------------------------------------------------------------------- 




#Verification to make sure that the user has filled all feileds
    def button_check(self):
        if self.beg == 0 and self.inter == 0 and self.advan == 0:
            #making sure that the use clicked one of the buttons
            invalidSelection()
            #input validation
        elif self.light == 0 and self.mod == 0 and self.high == 0:
            #making sure thaat the user has clicked one of the buttons
            invalidSelection()
            #input validation
        else: 
            #this is uses the variables linked to the buttons to enter the information into the database
            if self.beg == 1:
                global lv
                lv = "Beginner"
                #level
            elif self.inter == 1:

                lv = "Intermediate"
                #level
            else:

                lv = "Advanced"
                #level
            
            if self.light == 1:

                global al
                al = "Lightly"
                #activity level
            elif self.mod == 1:


                al = "Moderatly"
                #activity level    
            
            else:


                al = "Highly"
                #activity level             
            
            sm.current = "q3"
            #changing screen

#====================================================================================================================
#====================================================================================================================














































#====================================================================================================================
#this is the thrid block of questions where the user will select the button that corosponds closest to the question asked
#as the buttons are scelected the button will change color, visualy representing that the button has been clicked
#only once the validation process has been complete will the user move on to the lext screen
#====================================================================================================================

class Questions3(Screen):
#Declaring variables
    gy = 0
    hom = 0
    n = 0
    so = 0
    on = 0
    mo = 0


#================================================================
#Next Button
    def next_on(self):
        self.ids.next.source = 'graphics/next2.png'
#changing the color of the button
    def next_off(self):
        self.ids.next.source = 'graphics/next.png'

#===============================================================



#-------------------------------------------------------------------------------------------- 
#This part of code changes the image of the button to make it look like it has been selected
#it also changes the value of the variable linked to it which is used later

    def gym_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.gym.source = 'graphics/gym2.png'
        self.ids.home.source = 'graphics/home1.png'
        self.gy = 1
        self.hom = 0

    def home_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.home.source = 'graphics/home2.png'
        self.ids.gym.source = 'graphics/gym1.png'
        self.gy = 0
        self.hom = 1

    def most_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.most.source = 'graphics/most2.png'
        self.ids.some.source = 'graphics/some1.png'
        self.ids.onlydb.source = 'graphics/onlydb1.png'
        self.ids.no.source = 'graphics/no1.png'
        self.no = 0
        self.so = 0
        self.on = 0
        self.mo = 1


    def some_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.some.source = 'graphics/some2.png'
        self.ids.most.source = 'graphics/most1.png'
        self.ids.onlydb.source = 'graphics/onlydb1.png'
        self.ids.no.source = 'graphics/no1.png'
        self.no = 0
        self.so = 1
        self.on = 0
        self.mo = 0

    def onlydb_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.onlydb.source = 'graphics/onlydb2.png'
        self.ids.no.source = 'graphics/no1.png'
        self.ids.most.source = 'graphics/most1.png'
        self.ids.some.source = 'graphics/some1.png'
        self.no = 0
        self.so = 0
        self.on = 1
        self.mo = 0

    def no_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.no.source = 'graphics/no2.png'
        self.ids.onlydb.source = 'graphics/onlydb1.png'
        self.ids.most.source = 'graphics/most1.png'
        self.ids.some.source = 'graphics/some1.png'
        self.n = 1
        self.so = 0
        self.on = 0
        self.mo = 0

#--------------------------------------------------------------------------------------------




#Verificcation to make sure that all feilds have been filled
    def button_check_two(self):
        if self.mo == 0 and self.on == 0 and self.so == 0 and self.n == 0:
            #maining sure that the user has clicked a button
            invalidSelection()
            #input validation
        elif self.gy == 0 and self.hom == 0:
            #making sure that the user has clicked a button
            invalidSelection()
            #input validation
        else:
            #this uses the variable linked to the buttons to enter the information into the database
            if self.mo == 1:

                global eq
                eq = "Most"
                #equiptment 

            elif self.on == 1:


                eq = "Only Dumbbells"
                #equiptment 

            elif self.so == 1:


                eq = "Some"
                #equiptment 

            else:


                eq = "No Equiptment"
                #equiptment 

            if self.gy == 1:

                global tl
                tl = "Gym"
                #training location

            else:


                tl = "Home"
                #training location         
            

            sm.current = "q4"
#changing the screen
#====================================================================================================================
#====================================================================================================================
























#====================================================================================================================
#this is the fourth block of questions where the user will select the button that corosponds closest to the question asked
#as the buttons are scelected the button will change color, visualy representing that the button has been clicked
#only once the validation process has been complete will the user move on to the lext screen
#====================================================================================================================
class Questions4(Screen):

#Declaring variables
    two = 0
    three = 0 
    four = 0
    five = 0
    six = 0
    ftc = 0
    cmc = 0
    lbsc = 0
    kgc = 0



#Next Button


    def next_on(self):
        self.ids.next.source = 'graphics/next2.png'
#changing the color of the button
    def next_off(self):
        self.ids.next.source = 'graphics/next.png'


#=============================================================================================

#-------------------------------------------------------------------------------------------- 
#This part of code changes the image of the button to make it look like it has been selected
#it also changes the value of the variable linked to it which is used later
    def twodays_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process
        self.ids.twodays.source = 'graphics/2days2.png'
        self.ids.threedays.source = 'graphics/3days1.png'
        self.ids.fourdays.source = 'graphics/4days1.png'
        self.ids.fivedays.source = 'graphics/5days1.png'
        self.ids.sixdays.source = 'graphics/6days1.png'  
        self.two = 1
        self.three = 0 
        self.four = 0
        self.five = 0
        self.six = 0

    def threedays_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.threedays.source = 'graphics/3days2.png'
        self.ids.twodays.source = 'graphics/2days1.png'
        self.ids.fourdays.source = 'graphics/4days1.png'
        self.ids.fivedays.source = 'graphics/5days1.png'
        self.ids.sixdays.source = 'graphics/6days1.png'
        self.two = 0
        self.three = 1 
        self.four = 0
        self.five = 0
        self.six = 0



    def fourdays_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.fourdays.source = 'graphics/4days2.png'
        self.ids.twodays.source = 'graphics/2days1.png'
        self.ids.threedays.source = 'graphics/3days1.png'
        self.ids.fivedays.source = 'graphics/5days1.png'
        self.ids.sixdays.source = 'graphics/6days1.png'
        self.two = 0
        self.three = 0 
        self.four = 1
        self.five = 0
        self.six = 0


    def fivedays_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.fivedays.source = 'graphics/5days2.png'
        self.ids.twodays.source = 'graphics/2days1.png'
        self.ids.threedays.source = 'graphics/3days1.png'
        self.ids.fourdays.source = 'graphics/4days1.png'
        self.ids.sixdays.source = 'graphics/6days1.png'
        self.two = 0
        self.three = 0 
        self.four = 0
        self.five = 1
        self.six = 0

    def sixdays_on(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.sixdays.source = 'graphics/6days2.png'
        self.ids.twodays.source = 'graphics/2days1.png'
        self.ids.threedays.source = 'graphics/3days1.png'
        self.ids.fourdays.source = 'graphics/4days1.png'
        self.ids.fivedays.source = 'graphics/5days1.png'
        self.two = 0
        self.three = 0 
        self.four = 0
        self.five = 0
        self.six = 1


    def ft (self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.ft.source = 'graphics/ft2.png'
        self.ids.cm.source = 'graphics/cm.png'

        self.cmc = 0
        self.ftc = 1



    def cm (self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.ft.source = 'graphics/ft.png'
        self.ids.cm.source = 'graphics/cm2.png'

        self.cmc = 1
        self.ftc = 0



    def kg (self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.kg.source = 'graphics/kg2.png'
        self.ids.lbs.source = 'graphics/lbs.png'

        self.kgc = 1
        self.lbsc = 0


    def lbs (self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.kg.source = 'graphics/kg.png'
        self.ids.lbs.source = 'graphics/lbs2.png'

        self.kgc = 0
        self.lbsc = 1

#-------------------------------------------------------------------------------------------- 


#Verification to make sure that the user has filled all feilds

    def button_check_three(self):

        if self.two == 0 and self.three == 0 and self.four == 0 and self.five == 0 and self.six == 0:
            #making sure that the user has clicked one of the buttons
            invalidSelection()
            #input validation

        elif self.heightof.text == "" and self.weightof.text == "":
            #malining sure that the user has entered something
            invalidSelection()
            #input validation
        elif self.kgc == 0 and self.lbsc == 0:
            #makining sure that hte user has clicked one of the buttons
            invalidSelection()
            #input validation
        elif self.cmc == 0 and self.ftc == 0:
            #makining sure that the user has clicked one of the buttons
            invalidSelection()
            #input validation
            
        else:
            #this uses the variables linked to the buttons to enter information into the database
            if self.two == 1:
                global dy
                dy = "2 Days"
                #days
            elif self.three == 1:

                dy = "3 Days"
                #days           
            elif self.four == 1:

                dy = "4 Days"
                #days            
            elif self.five == 1:

                dy = "5 Days"
                #days            
            else:

                dy = "6 Days"
                #days



            global he
            he = self.heightof.text
            #height

            if self.cmc == 1:
                global hm
                hm = "cm"
                #height metric
            else:

                hm = "ft"
                #height metric                                        

            if self.kgc == 1:
                global wm
                wm = "kg"
                #weight metric
            else:

                wm = "lbs"
                #weight metric

            global we
            we = self.weightof.text
            #weight 
                            
            
            sm.current = "q5"
#changes the screen


#====================================================================================================================
#====================================================================================================================




























#====================================================================================================================
#this is the fith block of questions where the user will select the button that corosponds closest to the question asked
#as the buttons are scelected the button will change color, visualy representing that the button has been clicked
#only once the validation process has been complete will the user move on to the lext screen
#====================================================================================================================

class Questions5(Screen):

#Declaring Variables
    cal = 0


    l1 = 0
    g1 = 0
    m1 = 0
    b1 = 0

    l2 = 0
    g2 = 0
    m2 = 0
    b2 = 0

    l3 = 0
    g3 = 0
    m3 = 0
    b3 = 0

    l4 = 0
    g4 = 0
    m4 = 0
    b4 = 0

    ftc = 0
    cmc = 0

    lbsc = 0
    kgc = 0

#=============================================================================================
#=============================================================================================
#Next  Button
    def next_on(self):
        self.ids.next.source = 'graphics/next2.png'
#changes the color of the button
    def next_off(self):
        self.ids.next.source = 'graphics/next.png'

#=============================================================================================
#=============================================================================================













#-------------------------------------------------------------------------------------------- 
#This part of code changes the image of the button to make it look like it has been selected
#it also changes the value of the variable linked to it which is used later

    def lose_one(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process
        self.ids.lose1.source = 'graphics/1p.png'
        self.ids.gain1.source = 'graphics/1.png'
        self.ids.maintain1.source = 'graphics/1.png'
        self.ids.build1.source = 'graphics/1.png'

        self.ids.lose2.source = 'graphics/2.png'
        self.ids.lose3.source = 'graphics/3.png'
        self.ids.lose4.source = 'graphics/4.png'

        self.l1 = 1
        self.l2 = 0
        self.l3 = 0
        self.l4 = 0

        self.g1 = 0
        self.m1 = 0
        self.b1 = 0

#=============================================================================================
#=============================================================================================

    def gain_one(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose1.source = 'graphics/1.png'
        self.ids.gain1.source = 'graphics/1p.png'
        self.ids.maintain1.source = 'graphics/1.png'
        self.ids.build1.source = 'graphics/1.png'

        self.ids.gain2.source = 'graphics/2.png'
        self.ids.gain3.source = 'graphics/3.png'
        self.ids.gain4.source = 'graphics/4.png'

        self.g1 = 1
        self.g2 = 0
        self.g3 = 0
        self.g4 = 0

        self.l1 = 0
        self.m1 = 0
        self.b1 = 0

#=============================================================================================
#=============================================================================================

    def maintain_one(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose1.source = 'graphics/1.png'
        self.ids.gain1.source = 'graphics/1.png'
        self.ids.maintain1.source = 'graphics/1p.png'
        self.ids.build1.source = 'graphics/1.png'


        self.ids.maintain2.source = 'graphics/2.png'
        self.ids.maintain3.source = 'graphics/3.png'
        self.ids.maintain4.source = 'graphics/4.png'

        self.m1 = 1
        self.m2 = 0
        self.m3 = 0
        self.m4 = 0

        self.l1 = 0
        self.g1 = 0
        self.b1 = 0

#=============================================================================================
#=============================================================================================

    def build_one(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose1.source = 'graphics/1.png'
        self.ids.gain1.source = 'graphics/1.png'
        self.ids.maintain1.source = 'graphics/1.png'
        self.ids.build1.source = 'graphics/1p.png'

        self.ids.build2.source = 'graphics/2.png'
        self.ids.build3.source = 'graphics/3.png'
        self.ids.build4.source = 'graphics/4.png'

        self.b1 = 1
        self.b2 = 0
        self.b3 = 0
        self.b4 = 0

        self.l1 = 0
        self.g1 = 0
        self.m1 = 0

#=============================================================================================
#=============================================================================================

    def lose_two(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose2.source = 'graphics/2p.png'
        self.ids.gain2.source = 'graphics/2.png'
        self.ids.maintain2.source = 'graphics/2.png'
        self.ids.build2.source = 'graphics/2.png'

        self.ids.lose1.source = 'graphics/1.png'
        self.ids.lose3.source = 'graphics/3.png'
        self.ids.lose4.source = 'graphics/4.png'

        self.l1 = 0
        self.l3 = 0
        self.l4 = 0

        self.l2 = 1
        self.g2 = 0
        self.m2 = 0
        self.b2 = 0

#=============================================================================================
#=============================================================================================

    def gain_two(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose2.source = 'graphics/2.png'
        self.ids.gain2.source = 'graphics/2p.png'
        self.ids.maintain2.source = 'graphics/2.png'
        self.ids.build2.source = 'graphics/2.png'

        self.ids.gain1.source = 'graphics/1.png'
        self.ids.gain3.source = 'graphics/3.png'
        self.ids.gain4.source = 'graphics/4.png'

        self.g1 = 0
        self.g3 = 0
        self.g4 = 0

        self.l2 = 0
        self.g2 = 1
        self.m2 = 0
        self.b2 = 0

#=============================================================================================
#=============================================================================================

    def maintain_two(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose2.source = 'graphics/2.png'
        self.ids.gain2.source = 'graphics/2.png'
        self.ids.maintain2.source = 'graphics/2p.png'
        self.ids.build2.source = 'graphics/2.png'

        self.ids.maintain1.source = 'graphics/1.png'
        self.ids.maintain3.source = 'graphics/3.png'
        self.ids.maintain4.source = 'graphics/4.png'

        self.m1 = 0
        self.m3 = 0
        self.m4 = 0

        self.l2 = 0
        self.g2 = 0
        self.m2 = 1
        self.b2 = 0

#=============================================================================================
#=============================================================================================

    def build_two(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose2.source = 'graphics/2.png'
        self.ids.gain2.source = 'graphics/2.png'
        self.ids.maintain2.source = 'graphics/2.png'
        self.ids.build2.source = 'graphics/2p.png'

        self.ids.build1.source = 'graphics/1.png'
        self.ids.build3.source = 'graphics/3.png'
        self.ids.build4.source = 'graphics/4.png'

        self.b1 = 0
        self.b3 = 0
        self.b4 = 0

        self.l2 = 0
        self.g2 = 0
        self.m2 = 0
        self.b2 = 1

#=============================================================================================
#=============================================================================================

    def lose_three(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose3.source = 'graphics/3p.png'
        self.ids.gain3.source = 'graphics/3.png'
        self.ids.maintain3.source = 'graphics/3.png'
        self.ids.build3.source = 'graphics/3.png'

        self.ids.lose1.source = 'graphics/1.png'
        self.ids.lose2.source = 'graphics/2.png'
        self.ids.lose4.source = 'graphics/4.png'

        self.b1 = 0
        self.b2 = 0
        self.b4 = 0

        self.l3 = 1
        self.g3 = 0
        self.m3 = 0
        self.b3 = 0

#============================================================================================= 
#=============================================================================================

    def gain_three(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose3.source = 'graphics/3.png'
        self.ids.gain3.source = 'graphics/3p.png'
        self.ids.maintain3.source = 'graphics/3.png'
        self.ids.build3.source = 'graphics/3.png'

        self.ids.gain1.source = 'graphics/1.png'
        self.ids.gain2.source = 'graphics/2.png'
        self.ids.gain4.source = 'graphics/4.png'

        self.g1 = 0
        self.g2 = 0
        self.g4 = 0

        self.l3 = 0
        self.g3 = 1
        self.m3 = 0
        self.b3 = 0

#=============================================================================================
#=============================================================================================

    def maintain_three(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose3.source = 'graphics/3.png'
        self.ids.gain3.source = 'graphics/3.png'
        self.ids.maintain3.source = 'graphics/3p.png'
        self.ids.build3.source = 'graphics/3.png'

        self.ids.maintain1.source = 'graphics/1.png'
        self.ids.maintain2.source = 'graphics/2.png'
        self.ids.maintain4.source = 'graphics/4.png'

        self.m1 = 0
        self.m2 = 0
        self.m4 = 0

        self.l3 = 0
        self.g3 = 0
        self.m3 = 1
        self.b3 = 0

#=============================================================================================
#=============================================================================================

    def build_three(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose3.source = 'graphics/3.png'
        self.ids.gain3.source = 'graphics/3.png'
        self.ids.maintain3.source = 'graphics/3.png'
        self.ids.build3.source = 'graphics/3p.png'

        self.ids.build1.source = 'graphics/1.png'
        self.ids.build2.source = 'graphics/2.png'
        self.ids.build4.source = 'graphics/4.png'

        self.b1 = 0
        self.b2 = 0
        self.b4 = 0

        self.l3 = 0
        self.g3 = 0
        self.m3 = 0
        self.b3 = 1

#=============================================================================================
#=============================================================================================

    def lose_four(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose4.source = 'graphics/4p.png'
        self.ids.gain4.source = 'graphics/4.png'
        self.ids.maintain4.source = 'graphics/4.png'
        self.ids.build4.source = 'graphics/4.png'

        self.ids.lose1.source = 'graphics/1.png'
        self.ids.lose2.source = 'graphics/2.png'
        self.ids.lose3.source = 'graphics/3.png'

        self.l1 = 0
        self.l2 = 0
        self.l3 = 0

        self.l4 = 1
        self.g4 = 0
        self.m4 = 0
        self.b4 = 0

#=============================================================================================
#=============================================================================================
        
    def gain_four(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose4.source = 'graphics/4.png'
        self.ids.gain4.source = 'graphics/4p.png'
        self.ids.maintain4.source = 'graphics/4.png'
        self.ids.build4.source = 'graphics/4.png'

        self.ids.gain1.source = 'graphics/1.png'
        self.ids.gain2.source = 'graphics/2.png'
        self.ids.gain3.source = 'graphics/3.png'

        self.g1 = 0
        self.g2 = 0
        self.g3 = 0

        self.l4 = 0
        self.g4 = 1
        self.m4 = 0
        self.b4 = 0

#=============================================================================================
#=============================================================================================

    def maintain_four(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose4.source = 'graphics/4.png'
        self.ids.gain4.source = 'graphics/4.png'
        self.ids.maintain4.source = 'graphics/4p.png'
        self.ids.build4.source = 'graphics/4.png'

        self.ids.maintain1.source = 'graphics/1.png'
        self.ids.maintain2.source = 'graphics/2.png'
        self.ids.maintain3.source = 'graphics/3.png'

        self.m1 = 0
        self.m2 = 0
        self.m3 = 0

        self.l4 = 0
        self.g4 = 0
        self.m4 = 1
        self.b4 = 0

#=============================================================================================
#=============================================================================================

    def build_four(self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.lose4.source = 'graphics/4.png'
        self.ids.gain4.source = 'graphics/4.png'
        self.ids.maintain4.source = 'graphics/4.png'
        self.ids.build4.source = 'graphics/4p.png'

        self.ids.build1.source = 'graphics/1.png'
        self.ids.build2.source = 'graphics/2.png'
        self.ids.build3.source = 'graphics/3.png'

        self.b1 = 0
        self.b2 = 0
        self.b3 = 0

        self.l4 = 0
        self.g4 = 0
        self.m4 = 0
        self.b4 = 1

#=============================================================================================
#=============================================================================================

    def ft (self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.ft.source = 'graphics/ft2.png'
        self.ids.cm.source = 'graphics/cm.png'

        self.cmc = 0
        self.ftc = 1



    def cm (self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.ft.source = 'graphics/ft.png'
        self.ids.cm.source = 'graphics/cm2.png'

        self.cmc = 1
        self.ftc = 0



    def kg (self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.kg.source = 'graphics/kg2.png'
        self.ids.lbs.source = 'graphics/lbs.png'

        self.kgc = 1
        self.lbsc = 0


    def lbs (self):
        #this changes the color of the buttons as they get clicked
        #when a button is clicked the value of the variable linked to the button changes to 1, 
        #changing the others to 0 in the process        
        self.ids.kg.source = 'graphics/kg.png'
        self.ids.lbs.source = 'graphics/lbs2.png'

        self.kgc = 0
        self.lbsc = 1


#-------------------------------------------------------------------------------------------- 














#=============================================================================================
#=============================================================================================
#=============================================================================================
#=============================================================================================


#This part of code includes verification to make sure that the user has filled all feilds
#this also includes the code to write to the database
#it also includes the pop uo that displays your daily recomended calorie intake 


    def check_two(self):



#Writing to Database
        global dbwrite
        def dbwrite():

            conn = sqlite3.connect("Databse.db")
            cursor = conn.cursor()

#writing the infomation to the database
            try:

                userdata = """INSERT INTO UserIfo 
                            (Username, firstName, lastName, Email, Password, Gender, Age, Level, activityLevel, trainingLocation, Equiptment, Days, loseWeight, maintainWeight, buildMuscle, gainWeight, Height, heightMetric, Weight, weightMetric, Calories)
                            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(un, fn, ln, em, ps, gn, ag, lv, al, tl, eq, dy, lw, bm, mw, gw, he, hm, we, wm, self.cal)


                cursor.execute(userdata)
                
                cursor.close()

            except:
                #If There is a problen with database
                print("Error while inserting data")


            conn.commit()
            conn.close()



       #Verification 
       #this block of if statenents is to make sure that the user has clicked one button from each of the options
        if self.l1 != 0 or self.l2 != 0 or self.l3 != 0 or self.l4 != 0:
            if self.g1 != 0 or self.g2 != 0 or self.g3 != 0 or self.g4 != 0:
                if self.m1 != 0 or self.m2 != 0 or self.m3 != 0 or self.m4 != 0:
                    if self.b1 != 0 or self.b2 != 0 or self.b3 != 0 or self.b4 != 0:
                                    
                                    
                                    if self.l1 == 1: 
                                        global lw
                                        lw = "1"
                                        #lose weight
                                    elif self.l2 == 1: 

                                        lw = "2"
                                        #lose weight
                                    elif self.l3 == 1: 

                                        lw = "3"
                                        #lose weight
                                    else: 

                                        lw = "4"
                                        #lose weight



                                    if self.b1 == 1: 
                                        global bm
                                        bm = "1"
                                        #build muscle
                                    elif self.b2 == 1: 

                                        bm = "2"
                                        #build muscle
                                    elif self.b3 == 1: 

                                        bm = "3"
                                        #build muscle
                                    else: 

                                        bm = "4"
                                        #build muscle

                                    if self.m1 == 1: 
                                        global mw
                                        mw = "1"
                                        #maintain weight
                                    elif self.m2 == 1: 

                                        mw = "2"
                                        #maintain weight
                                    elif self.m3 == 1: 

                                        mw = "3"
                                        #maintain weight
                                    else: 

                                        mw = "4"
                                        #maintain weight

                                    if self.g1 == 1: 
                                        global gw
                                        gw = "1"
                                        #gain weight
                                    elif self.g2 == 1: 

                                        gw = "2"
                                        #gain weight
                                    elif self.g3 == 1: 

                                        gw = "3"
                                        #gain weight
                                    else: 

                                        gw = "4"
                                        #gain weight






                                    global calorie
                                    def calorie(self):

                                        #Declaring variables
                                        global cal
                                        global kgWeight
                                        kgWeight = 0
                                        global cmHeight
                                        cmHeight = 0




#-------------------------------------------------------------------------------------------- 
#This part of code calculates your daily recomended calorie intake
 
                                        if wm == "lbs":
                                            kgWeight = kgWeight + (int(we) * 0.45359237)


                                            if hm == "ft":
                                                cmHeight = cmHeight + (int(he) * 30.48)

                                                if gn == "female":
                                                    
                                                    
                                                    femaleCal = 665 + (9.6 * kgWeight) + (1.8 * cmHeight) - (4.7 * age)
                                                    self.cal = round(femaleCal)
                                                    return self.cal
                                                else:
                                                    
                                                    maleCal = 66 + (13.7 * kgWeight) + (5 * cmHeight) - (6.8 * age)
                                                    self.cal = round(maleCal)
                                                    return self.cal                                            

                                            else:
                                                if gn == "female":
                                                    
                                                    
                                                    femaleCal = 665 + (9.6 * kgWeight) + (1.8 * int(float(he))) - (4.7 * age)
                                                    self.cal = round(femaleCal)
                                                    return self.cal
                                                else:
                                                    
                                                    maleCal = 66 + (13.7 * kgWeight) + (5 * int(float(he))) - (6.8 * age)
                                                    self.cal = round(maleCal)
                                                    return self.cal   


                                        elif hm == "ft":
                                            cmHeight = cmHeight + (int(float(he)) * 30.48)

                                            if gn == "female":
                                                
                                                
                                                femaleCal = 665 + (9.6 * int(float(we))) + (1.8 * cmHeight) - (4.7 * age)
                                                self.cal = round(femaleCal)
                                                return self.cal
                                            else:
                                                
                                                maleCal = 66 + (13.7 * int(float(we))) + (5 * cmHeight) - (6.8 * age)
                                                self.cal = round(maleCal)
                                                return self.cal

                                        else:
                                            if gn == "female":
                                                
        
                                                femaleCal = 665 + (9.6 * int(float(we))) + (1.8 * int(float(he))) - (4.7 * age)
                                                self.cal = round(femaleCal)
                                                return self.cal
                                            else:
                                                
                                                maleCal = 66 + (13.7 * int(float(we))) + (5 * int(float(he))) - (6.8 * int(float(age)))
                                                self.cal = round(maleCal)
                                                return self.cal
#-------------------------------------------------------------------------------------------- 
                                           

                                    
                                    calorie(self)
                                    dbwrite()          
                                    #Calling Database function to write to database  

                                    box = FloatLayout()

                                    box.add_widget(Label(pos_hint = {'x': 0.25, 'center_y': 0.8}, text=('Your recomended daily calorie\nintake is ' + str(self.cal) + " kcals. This has been\nestimated baised on the information\nthat you provided. You can track\nyour calories by using an app such\nas My Fitness Pal."), size_hint = (0.16, 0.1)))
                                    box.add_widget(Label(pos_hint = {'x': 0.22, 'center_y': 0.45}, text=(str(self.cal)), bold = True, size_hint = (1, 1), font_size='40sp'))
                                    box.add_widget(Label(pos_hint = {'x': 0.15, 'center_y': 0.05}, text=('Train Hard, Train Smart, Train Right'), bold = True, size_hint = (1, 1)))
                                    box.add_widget(Image(pos_hint = {'x': 0.4, 'center_y': 0.45}, source = 'graphics/circle.png', size_hint = (0.65, 0.65)))
                                    box.add_widget(Image(pos_hint = {'x': 0, 'center_y': 0.29}, source = 'graphics/logo.png', size_hint = (0.7, 0.7)))
                                    sm.current = "home"
                                    pop = Popup(title='Results',
                                    content=box,
                                    size_hint=(None, None), size=(400, 500),
                                    separator_color = (126/255, 28/255, 19/255, 1))

                                    pop.open() 
                                            
                        
                                    #This is the results popup that will happen when you user completes the questionair
                                    #this will include the recomended daily calorie intake and a recomended plan
                                    

#-------------------------------------------------------------------------------------------- 
#Validation
                    else:
                        invalidSelection()
                        #input validdation
                else:
                    invalidSelection()  
                    #input validation
            else:
                invalidSelection()  
                #input validation
        else:
            invalidSelection()
            #input validation
#-------------------------------------------------------------------------------------------- 


#====================================================================================================================
#====================================================================================================================





















#====================================================================================================================
#this is where the exersice tutorials will be
# they will be filtered down to muscle group and will provide demonstation videos and a few scentences on how the exercise should be carried out
#====================================================================================================================
class ExerciseTutorial(Screen):
    def profile(self):

        uProfile()


#====================================================================================================================
#====================================================================================================================



















#====================================================================================================================
#this is where the user will be able to view there progress
#for example there weight and mesurments as well as the weight that they ar lifting
#having a pb/pr section
#this could eventualy be moved into the profile section
#====================================================================================================================

class Progress(Screen):
    pass

#====================================================================================================================
#====================================================================================================================


















#====================================================================================================================
#Settings
#====================================================================================================================
# This is the setting window wich right now includes the log out feature and the privacy policy
class Settings(Screen):

    def profile(self):
        #calling the profile
        uProfile()

 
    def Privacy(self):
        pop = Popup(title='Privacy Policy',
                    content=Label(text='This Kivy app is a cross platform application.\nIt is a collection of exercise programs to be\nused at youre leisure.\n\nWhat Information Do We Collect?\n\nThis app only collects the user information that\nyou enter e.g. name, age, gender, weight etc.\n\n How Do We Use Your Information?\n\nThe information that you enter will only be\nused to determine what training plans are best\nsuited to yourself.\n\nWhat Information Do We Share?\n\nNo user information will be shared.', halign = 'center'),
                    size_hint=(None, None), size=(400, 400),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()   
        #privacy policy pop up


#====================================================================================================================
#====================================================================================================================















#====================================================================================================================
#Account Information
#====================================================================================================================
class Accountinfo(Screen):
    pass
#====================================================================================================================
#====================================================================================================================















#====================================================================================================================
#Training Plans
#this is where the featured training plan will be 
#====================================================================================================================

class TrainingPlans(Screen):

    def profile(self):
#calling user profile
        uProfile()
    
#====================================================================================================================
#==================================================================================================================== 



#====================================================================================================================
#Matts curent Training plan
# This is the current featured plan
#====================================================================================================================


    def mattplan(self):

        box = FloatLayout()
        
        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def monday(instance):
            # plan.clear_widgets()
            wipe()



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))

            
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Push  1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/inclinechestpress3.png', background_down='graphics/inclinechestpress2.png',size_hint = (0.7, 0.11), on_release = Chest.incline_chest_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/shoulderpress3.png', background_down='graphics/shoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.shoulder_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/triceppushdownbar3.png', background_down='graphics/triceppushdownbar2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_bar))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/lthcablefly3.png', background_down='graphics/lthcablefly2.png',size_hint = (0.7, 0.11), on_release = Chest.low_to_high_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/dips3.png', background_down='graphics/dips2.png',size_hint = (0.7, 0.11), on_release = Chest.dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='6-10             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/seatedlateralraise3.png', background_down='graphics/seatedlateralraise2.png',size_hint = (0.7, 0.11), on_release = Shoulder.seated_lateral_raise))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/singlearmtricepextention3.png', background_down='graphics/singlearmtricepextention2.png',size_hint = (0.7, 0.11), on_release = Tricep.single_arm_tricep_extention))







        def tuesday(instance):
            wipe()
            # plan.clear_widgets()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))            


            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Pull  1                    ', size_hint = (0.4, 0.2), bold = True))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/latpulldown3.png', background_down='graphics/latpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='10-15           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/hammercurl3.png', background_down='graphics/hammercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.hammer_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/vbarseatedrow3.png', background_down='graphics/vbarseatedrow2.png',size_hint = (0.7, 0.11), on_release = Back.vbar_seatedrow))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/inclinedumbbellcurl3.png', background_down='graphics/inclinedumbbellcurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.incline_dbcurl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 6-10              0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/pullthrough3.png', background_down='graphics/pullthrough2.png',size_hint = (0.7, 0.11), on_release = Back.pull_through))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/zottmancurl3.png', background_down='graphics/zottmancurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.zottman_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='10-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/cablefacepullrope3.png', background_down='graphics/cablefacepullrope2.png',size_hint = (0.7, 0.11), on_release = Shoulder.facepull_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='10-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
        

        def wednesday(instance):
            wipe()
            # plan.clear_widgets()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))            


            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Legs                      ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/highbarbacksquat3.png', background_down='graphics/highbarbacksquat2.png',size_hint = (0.7, 0.11), on_release = Quads.high_bar_back_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/seatedlegcurl3.png', background_down='graphics/seatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/singleseatedlegcurl3.png', background_down='graphics/singleseatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.single_seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 10-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/abductor3.png', background_down='graphics/abductor2.png',size_hint = (0.7, 0.11), on_release = Glutes.abductor))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            


        def thursday(instance):
            wipe()
            # plan.clear_widgets()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            
            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Push  2                    ', size_hint = (0.4, 0.2), bold = True))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/dbshoulderpress3.png', background_down='graphics/dbshoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_shoulder_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             2                 3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/flatchestpress3.png', background_down='graphics/flatchestpress2.png',size_hint = (0.7, 0.11), on_release = Chest.flat_chest_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12           1                 3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/seatedreversefly3.png', background_down='graphics/seatedreversefly2.png',size_hint = (0.7, 0.11), on_release = Shoulder.seated_reverse_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 12-15        0                 4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/inclinedbfly3.png', background_down='graphics/inclinedbfly2.png',size_hint = (0.7, 0.11), on_release = Chest.incline_db_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 8-12            0                 3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/ezbarskullcrusher3.png', background_down='graphics/ezbarskullcrusher2.png',size_hint = (0.7, 0.11), on_release = Tricep.ezbar_skullcrusher))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='6-10              0                3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/overheadpress3.png', background_down='graphics/overheadpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.overhead_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12              0                3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/triceppushdownrope3.png', background_down='graphics/triceppushdownrope2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='10-15            0                3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def friday(instance):
            wipe()
            # plan.clear_widgets()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))        



            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Pull  2                    ', size_hint = (0.4, 0.2), bold = True))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/vbarseatedrow3.png', background_down='graphics/vbarseatedrow2.png',size_hint = (0.7, 0.11), on_release = Back.vbar_seatedrow))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/dbpreachercurl3.png', background_down='graphics/dbpreachercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.db_preacher_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12           1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/reversegriplatpulldown3.png', background_down='graphics/reversegriplatpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.reverse_lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/ropehammercurl3.png', background_down='graphics/ropehammercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.rope_hammer_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 6-10           0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/pullthroughsb3.png', background_down='graphics/pullthroughsb2.png',size_hint = (0.7, 0.11), on_release = Back.pull_through_sb))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15          0              4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/wristcurl3.png', background_down='graphics/wristcurl2.png',size_hint = (0.7, 0.11), on_release = Forearm.wrist_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/dumbbellshrug3.png', background_down='graphics/dumbbellshrug2.png',size_hint = (0.7, 0.11), on_release = Trap.db_shrug))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
        box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
        box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
        box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
        box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))

#description of the training plan
        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='This is the current training plan that Matt is following.\n It is a variation of PPL, it includes two rest days.', size_hint = (0.2, 0.1), halign = 'center'))
        


        
        pop = Popup(title='Matts Plan',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#====================================================================================================================
#====================================================================================================================












































#====================================================================================================================
#This is the home plan section
#taining plans that have be constructed with the intention of them being able to be sompleted at home
#====================================================================================================================


class Homeplan(Screen):

    def profile(self):

        uProfile()

#====================================================================================================================
#This is the six day home plan training plan
#====================================================================================================================


    def sixdayhomeplan(self):

        box = FloatLayout()

        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def day1(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Day 4', size_hint = (0.16, 0.1), on_press = day4))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Day 5', size_hint = (0.16, 0.1), on_press = day5))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Day 6', size_hint = (0.16, 0.1), on_press = day6))



            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day 1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/homerow3.png', background_down='graphics/homerow2.png',size_hint = (0.7, 0.11), on_release = Back.home_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/floorpress3.png', background_down='graphics/floorpress2.png',size_hint = (0.7, 0.11), on_release = Chest.floor_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/bentoverfly3.png', background_down='graphics/bentoverfly2.png',size_hint = (0.7, 0.11), on_release = Back.bent_over_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 8-12          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/widepushup3.png', background_down='graphics/widepushup2.png',size_hint = (0.7, 0.11), on_release = Chest.wide_pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/renegaderow3.png', background_down='graphics/renegaderow2.png',size_hint = (0.7, 0.11), on_release = Back.renegade_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='10          0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def day2(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Day 4', size_hint = (0.16, 0.1), on_press = day4))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Day 5', size_hint = (0.16, 0.1), on_press = day5))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Day 6', size_hint = (0.16, 0.1), on_press = day6))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day 2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/armcircles3.png', background_down='graphics/armcircles2.png',size_hint = (0.7, 0.11), on_release = Shoulder.arm_circles))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='15             0               2', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/benchdips3.png', background_down='graphics/benchdips2.png',size_hint = (0.7, 0.11), on_release = Tricep.bench_dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/bicepcurl3.png', background_down='graphics/bicepcurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.bicep_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/abdominalcrunch3.png', background_down='graphics/abdominalcrunch2.png',size_hint = (0.7, 0.11), on_release = Abs.abdominal_crunch))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/standingdbpress3.png', background_down='graphics/standingdbpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.standing_db_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/hammercurl3.png', background_down='graphics/hammercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.hammer_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='6-10           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/plank3.png', background_down='graphics/plank2.png',size_hint = (0.7, 0.11), on_release = Abs.plank))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='60s           0               2', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def day3(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Day 4', size_hint = (0.16, 0.1), on_press = day4))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Day 5', size_hint = (0.16, 0.1), on_press = day5))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Day 6', size_hint = (0.16, 0.1), on_press = day6))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day 3                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/bodyweightsquat3.png', background_down='graphics/bodyweightsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.body_weight_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='10-15             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/romainiandeadlift3.png', background_down='graphics/romainiandeadlift2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.romanian_deadlift))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 10-15             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/lunges3.png', background_down='graphics/lunges2.png',size_hint = (0.7, 0.11), on_release = Quads.lunges))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 8-12          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/glutebridge3.png', background_down='graphics/glutebridge2.png',size_hint = (0.7, 0.11), on_release = Glutes.glute_bridge))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='6-10           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            # box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/cablefacepullrope3.png', background_down='graphics/cablefacepullrope2.png',size_hint = (0.7, 0.11), on_release = ))
            # box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='10-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def day4(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Day 4', size_hint = (0.16, 0.1), on_press = day4))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Day 5', size_hint = (0.16, 0.1), on_press = day5))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Day 6', size_hint = (0.16, 0.1), on_press = day6))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day 4                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/floorpress3.png', background_down='graphics/floorpress2.png',size_hint = (0.7, 0.11), on_release = Chest.floor_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/bentoverfly3.png', background_down='graphics/bentoverfly2.png',size_hint = (0.7, 0.11), on_release = Back.bent_over_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/widepushup3.png', background_down='graphics/widepushup2.png',size_hint = (0.7, 0.11), on_release = Chest.wide_pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/homerow3.png', background_down='graphics/homerow2.png',size_hint = (0.7, 0.11), on_release = Back.home_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 10-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='10           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/renegaderow3.png', background_down='graphics/renegaderow2.png',size_hint = (0.7, 0.11), on_release = Back.renegade_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='6-10           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            #box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/cablefacepullrope3.png', background_down='graphics/cablefacepullrope2.png',size_hint = (0.7, 0.11), on_release = facepull_rope))
            #box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='10-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def day5(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Day 4', size_hint = (0.16, 0.1), on_press = day4))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Day 5', size_hint = (0.16, 0.1), on_press = day5))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Day 6', size_hint = (0.16, 0.1), on_press = day6))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day 5                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/armcircles3.png', background_down='graphics/armcircles2.png',size_hint = (0.7, 0.11), on_release = Shoulder.arm_circles))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/hammercurl3.png', background_down='graphics/hammercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.hammer_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/standingdbpress3.png', background_down='graphics/standingdbpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.standing_db_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/abdominalcrunch3.png', background_down='graphics/abdominalcrunch2.png',size_hint = (0.7, 0.11), on_release = Abs.abdominal_crunch))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/benchdips3.png', background_down='graphics/benchdips2.png',size_hint = (0.7, 0.11), on_release = Tricep.bench_dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/bicepcurl3.png', background_down='graphics/bicepcurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.bicep_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/plank3.png', background_down='graphics/plank2.png',size_hint = (0.7, 0.11), on_release = Abs.plank))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='60s           0               2', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def day6(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Day 4', size_hint = (0.16, 0.1), on_press = day4))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Day 5', size_hint = (0.16, 0.1), on_press = day5))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Day 6', size_hint = (0.16, 0.1), on_press = day6))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day 6                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/romainiandeadlift3.png', background_down='graphics/romainiandeadlift2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.romanian_deadlift))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/lunges3.png', background_down='graphics/lunges2.png',size_hint = (0.7, 0.11), on_release = Quads.lunges))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/glutebridge3.png', background_down='graphics/glutebridge2.png',size_hint = (0.7, 0.11), on_release = Glutes.glute_bridge))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 10             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 8-12          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/bodyweightsquat3.png', background_down='graphics/bodyweightsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.body_weight_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='15              0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

        box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
        box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
        box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))
        box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Day 4', size_hint = (0.16, 0.1), on_press = day4))
        box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Day 5', size_hint = (0.16, 0.1), on_press = day5))
        box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Day 6', size_hint = (0.16, 0.1), on_press = day6))

        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='This is the 6 day home workout plan. This\nspans across the week giving you only one rest\nday. This plan is for those who are really active.', size_hint = (0.2, 0.1), halign = 'center'))

        
        pop = Popup(title='6 Day Home Workout',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    


#====================================================================================================================
#====================================================================================================================

































#====================================================================================================================
#This is the HITT home workout training plan
#====================================================================================================================


    def hiit(self):


        box = FloatLayout()

        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def five(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='5 Minute', size_hint = (0.225, 0.1), on_press = five))
            box.add_widget(Button(pos_hint = {'x': .25, 'center_y': 0.9}, text='10 Minute', size_hint = (0.225, 0.1), on_press = ten))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='15 Minute', size_hint = (0.225, 0.1), on_press = fifteen))
            box.add_widget(Button(pos_hint = {'x': .75, 'center_y': 0.9}, text='20 Minute', size_hint = (0.225, 0.1), on_press = twenty))

            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Active', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Rest', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='5 Minute                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/pulsingjumpsquat3.png', background_down='graphics/pulsingjumpsquat2.png',size_hint = (0.7, 0.11), on_release = Hiit.pulsing_jump_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='                 40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/frogjump3.png', background_down='graphics/frogjump2.png',size_hint = (0.7, 0.11), on_release = Hiit.frog_jump))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text='                  40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/highknees3.png', background_down='graphics/highknees2.png',size_hint = (0.7, 0.11), on_release = Hiit.high_knees))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text='                  40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/verticaljump3.png', background_down='graphics/verticaljump2.png',size_hint = (0.7, 0.11), on_release = Hiit.vertical_jump))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text='            40s              20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/plank3.png', background_down='graphics/plank2.png',size_hint = (0.7, 0.11), on_release = Abs.plank))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='                40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))




        def ten(instance):

            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='5 Minute', size_hint = (0.225, 0.1), on_press = five))
            box.add_widget(Button(pos_hint = {'x': .25, 'center_y': 0.9}, text='10 Minute', size_hint = (0.225, 0.1), on_press = ten))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='15 Minute', size_hint = (0.225, 0.1), on_press = fifteen))
            box.add_widget(Button(pos_hint = {'x': .75, 'center_y': 0.9}, text='20 Minute', size_hint = (0.225, 0.1), on_press = twenty))

            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Active', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Rest', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='10 Minute                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/mountainclimbers3.png', background_down='graphics/mountainclimbers2.png',size_hint = (0.7, 0.11), on_release = Hiit.mountain_climbers))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='                 40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/lungejump3.png', background_down='graphics/lungejump2.png',size_hint = (0.7, 0.11), on_release = Hiit.lunge_jumps))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text='                  40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/burpees3.png', background_down='graphics/burpees2.png',size_hint = (0.7, 0.11), on_release = Hiit.burpees))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text='                  40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/jumpingjacks3.png', background_down='graphics/jumpingjacks2.png',size_hint = (0.7, 0.11), on_release = Hiit.jumping_jacks))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text='            40s              20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/russiantwists3.png', background_down='graphics/russiantwists2.png',size_hint = (0.7, 0.11), on_release = Hiit.russian_twists))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='                40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .3, 'center_y': 0.22}, text='20 second rest then start the final round', size_hint = (0.4, 0.2), bold = True, halign = 'center'))




        def fifteen(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='5 Minute', size_hint = (0.225, 0.1), on_press = five))
            box.add_widget(Button(pos_hint = {'x': .25, 'center_y': 0.9}, text='10 Minute', size_hint = (0.225, 0.1), on_press = ten))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='15 Minute', size_hint = (0.225, 0.1), on_press = fifteen))
            box.add_widget(Button(pos_hint = {'x': .75, 'center_y': 0.9}, text='20 Minute', size_hint = (0.225, 0.1), on_press = twenty))

            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Active', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Rest', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='15 Minute                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/highknees3.png', background_down='graphics/highknees2.png',size_hint = (0.7, 0.11), on_release = Hiit.high_knees))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='                 40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text='                  40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/abcrunch3.png', background_down='graphics/abcrunch2.png',size_hint = (0.7, 0.11), on_release = Abs.ab_crunch))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text='                  40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/burpees3.png', background_down='graphics/burpees2.png',size_hint = (0.7, 0.11), on_release = Hiit.burpees))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text='            40s              20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/mountainclimbers3.png', background_down='graphics/mountainclimbers2.png',size_hint = (0.7, 0.11), on_release = Hiit.mountain_climbers))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='                40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .3, 'center_y': 0.22}, text='20 second rest then start the next round,\n there are 3 rounds in total', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def twenty(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='5 Minute', size_hint = (0.225, 0.1), on_press = five))
            box.add_widget(Button(pos_hint = {'x': .25, 'center_y': 0.9}, text='10 Minute', size_hint = (0.225, 0.1), on_press = ten))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='15 Minute', size_hint = (0.225, 0.1), on_press = fifteen))
            box.add_widget(Button(pos_hint = {'x': .75, 'center_y': 0.9}, text='20 Minute', size_hint = (0.225, 0.1), on_press = twenty))

            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Active', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Rest', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='20 Minute                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/burpees3.png', background_down='graphics/burpees2.png',size_hint = (0.7, 0.11), on_release = Hiit.burpees))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='                 40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/pulsingjumpsquat3.png', background_down='graphics/pulsingjumpsquat2.png',size_hint = (0.7, 0.11), on_release = Hiit.pulsing_jump_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text='                  40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/mountainclimbers3.png', background_down='graphics/mountainclimbers2.png',size_hint = (0.7, 0.11), on_release = Hiit.mountain_climbers))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text='                  40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/jumpingjacks3.png', background_down='graphics/jumpingjacks2.png',size_hint = (0.7, 0.11), on_release = Hiit.jumping_jacks))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text='            40s              20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/russiantwists3.png', background_down='graphics/russiantwists2.png',size_hint = (0.7, 0.11), on_release = Hiit.russian_twists))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='                40s               20s', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .3, 'center_y': 0.22}, text='20 second rest then start the next round,\n there are 4 rounds in total', size_hint = (0.4, 0.2), bold = True, halign = 'center'))




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   


        box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='5 Minute', size_hint = (0.225, 0.1), on_press = five))
        box.add_widget(Button(pos_hint = {'x': .25, 'center_y': 0.9}, text='10 Minute', size_hint = (0.225, 0.1), on_press = ten))
        box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='15 Minute', size_hint = (0.225, 0.1), on_press = fifteen))
        box.add_widget(Button(pos_hint = {'x': .75, 'center_y': 0.9}, text='20 Minute', size_hint = (0.225, 0.1), on_press = twenty))


        box.add_widget(Label(pos_hint = {'x': 0.42, 'center_y': 0.7}, text='Here are four different HIIT\n(High Intensity Interval Training), workouts\n for you to choose from.', size_hint = (0.2, 0.1), halign = 'center'))

        
        pop = Popup(title='HIIT',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

#====================================================================================================================
#====================================================================================================================
























#====================================================================================================================
#This is the home upper lower training plan
#====================================================================================================================


    def upperlower(self):

        box = FloatLayout()

        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def upper1(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Upper 1', size_hint = (0.2, 0.1), on_press = upper1))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Lower 1', size_hint = (0.2, 0.1), on_press = lower1))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Upper 2', size_hint = (0.2, 0.1), on_press = upper2))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Lower 2', size_hint = (0.2, 0.1), on_press = lower2))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Upper 1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/homerow3.png', background_down='graphics/homerow2.png',size_hint = (0.7, 0.11), on_release = Back.home_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/shouldertaps3.png', background_down='graphics/shouldertaps2.png',size_hint = (0.7, 0.11), on_release = Shoulder.shoulder_taps))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/widepushup3.png', background_down='graphics/widepushup2.png',size_hint = (0.7, 0.11), on_release = Chest.wide_pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 8          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/benchdips3.png', background_down='graphics/benchdips2.png',size_hint = (0.7, 0.11), on_release = Tricep.bench_dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/armcircles3.png', background_down='graphics/armcircles2.png',size_hint = (0.7, 0.11), on_release = Shoulder.arm_circles))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))



        def lower1(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Upper 1', size_hint = (0.2, 0.1), on_press = upper1))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Lower 1', size_hint = (0.2, 0.1), on_press = lower1))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Upper 2', size_hint = (0.2, 0.1), on_press = upper2))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Lower 2', size_hint = (0.2, 0.1), on_press = lower2))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Lower 1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/bodyweightsquat3.png', background_down='graphics/bodyweightsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.body_weight_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='10-15             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 15             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/lunges3.png', background_down='graphics/lunges2.png',size_hint = (0.7, 0.11), on_release = Quads.lunges))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/abdominalairbike3.png', background_down='graphics/abdominalairbike2.png',size_hint = (0.7, 0.11), on_release = Abs.abdominal_air_bike))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 60s          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/plank3.png', background_down='graphics/plank2.png',size_hint = (0.7, 0.11), on_release = Abs.plank))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='60s           0               2', size_hint = (0.4, 0.2), bold = True, halign = 'center'))




        def upper2(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Upper 1', size_hint = (0.2, 0.1), on_press = upper1))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Lower 1', size_hint = (0.2, 0.1), on_press = lower1))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Upper 2', size_hint = (0.2, 0.1), on_press = upper2))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Lower 2', size_hint = (0.2, 0.1), on_press = lower2))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Upper 2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/homerow3.png', background_down='graphics/homerow2.png',size_hint = (0.7, 0.11), on_release = Back.home_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/widepushup3.png', background_down='graphics/widepushup2.png',size_hint = (0.7, 0.11), on_release = Chest.wide_pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/armcircles3.png', background_down='graphics/armcircles2.png',size_hint = (0.7, 0.11), on_release = Shoulder.arm_circles ))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 12-15             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 10          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/benchdips3.png', background_down='graphics/benchdips2.png',size_hint = (0.7, 0.11), on_release = Tricep.bench_dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/shouldertaps3.png', background_down='graphics/shouldertaps2.png',size_hint = (0.7, 0.11), on_release = Shoulder.shoulder_taps))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def lower2(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Upper 1', size_hint = (0.2, 0.1), on_press = upper1))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Lower 1', size_hint = (0.2, 0.1), on_press = lower1))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Upper 2', size_hint = (0.2, 0.1), on_press = upper2))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Lower 2', size_hint = (0.2, 0.1), on_press = lower2))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Lower 2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/abdominalairbike3.png', background_down='graphics/abdominalairbike2.png',size_hint = (0.7, 0.11), on_release = Abs.abdominal_air_bike))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 60s             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/bodyweightsquat3.png', background_down='graphics/bodyweightsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.body_weight_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 10-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/lunges3.png', background_down='graphics/lunges2.png',size_hint = (0.7, 0.11), on_release = Quads.lunges))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/plank3.png', background_down='graphics/plank2.png',size_hint = (0.7, 0.11), on_release = Abs.plank))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='60s           0               2', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  

        box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Upper 1', size_hint = (0.2, 0.1), on_press = upper1))
        box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Lower 1', size_hint = (0.2, 0.1), on_press = lower1))
        box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Upper 2', size_hint = (0.2, 0.1), on_press = upper2))
        box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Lower 2', size_hint = (0.2, 0.1), on_press = lower2))


        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='An upper lower training split breaks the workouts\ninto two sessions, one for your upper body and one\nfor your lower body. This training plan is set\nout for four days of the week with three rest days\n however, feel free to tailor this to yourself.', size_hint = (0.2, 0.1), halign = 'center'))

        
        pop = Popup(title='Upper Lower Home',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 



#====================================================================================================================
#====================================================================================================================













#====================================================================================================================
#This is the Home Full body training plan
#====================================================================================================================

    def fullbody(self):
        box = FloatLayout()

        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def day1(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0.05, 'center_y': 0.9}, text='Day 1', size_hint = (0.3, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Day 2', size_hint = (0.3, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .65, 'center_y': 0.9}, text='Day 3', size_hint = (0.3, 0.1), on_press = day3))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day 1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/bodyweightsquat3.png', background_down='graphics/bodyweightsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.body_weight_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/lunges3.png', background_down='graphics/lunges2.png',size_hint = (0.7, 0.11), on_release = Quads.lunges))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/wallpushups3.png', background_down='graphics/wallpushups2.png',size_hint = (0.7, 0.11), on_release = Chest.wall_pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 10-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/benchdips3.png', background_down='graphics/benchdips2.png',size_hint = (0.7, 0.11), on_release = Tricep.bench_dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/plank3.png', background_down='graphics/plank2.png',size_hint = (0.7, 0.11), on_release = Abs.plank))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='60s           0               2', size_hint = (0.4, 0.2), bold = True, halign = 'center'))



        def day2(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0.05, 'center_y': 0.9}, text='Day 1', size_hint = (0.3, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Day 2', size_hint = (0.3, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .65, 'center_y': 0.9}, text='Day 3', size_hint = (0.3, 0.1), on_press = day3))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day 2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/benchdips3.png', background_down='graphics/benchdips2.png',size_hint = (0.7, 0.11), on_release = Tricep.bench_dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/lunges3.png', background_down='graphics/lunges2.png',size_hint = (0.7, 0.11), on_release = Quads.lunges))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 10-15             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/wallpushups3.png', background_down='graphics/wallpushups2.png',size_hint = (0.7, 0.11), on_release = Chest.wall_pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/bodyweightsquat3.png', background_down='graphics/bodyweightsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.body_weight_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/plank3.png', background_down='graphics/plank2.png',size_hint = (0.7, 0.11), on_release = Abs.plank))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='60s          0               2', size_hint = (0.4, 0.2), bold = True, halign = 'center'))



        def day3(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0.05, 'center_y': 0.9}, text='Day 1', size_hint = (0.3, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Day 2', size_hint = (0.3, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .65, 'center_y': 0.9}, text='Day 3', size_hint = (0.3, 0.1), on_press = day3))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day 3                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/plank3.png', background_down='graphics/plank2.png',size_hint = (0.7, 0.11), on_release = Abs.plank))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='60s             0               0', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/wallpushups3.png', background_down='graphics/wallpushups2.png',size_hint = (0.7, 0.11), on_release = Chest.wall_pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 10-15             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/lunges3.png', background_down='graphics/lunges2.png',size_hint = (0.7, 0.11), on_release = Quads.lunges))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 6-10          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/benchdips3.png', background_down='graphics/benchdips2.png',size_hint = (0.7, 0.11), on_release = Tricep.bench_dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/bodyweightsquat3.png', background_down='graphics/bodyweightsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.body_weight_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12          0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  

        box.add_widget(Button(pos_hint = {'x': 0.05, 'center_y': 0.9}, text='Day 1', size_hint = (0.3, 0.1), on_press = day1))
        box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Day 2', size_hint = (0.3, 0.1), on_press = day2))
        box.add_widget(Button(pos_hint = {'x': .65, 'center_y': 0.9}, text='Day 3', size_hint = (0.3, 0.1), on_press = day3))


        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='This is The Full Body Home Training Plan. Here are\n3 different full body sessions. You can either train\n3 or 6 days a week taking 4 or 1 rest day respectively\nthese plans are intended to be flexible.', size_hint = (0.2, 0.1), halign = 'center'))

        
        pop = Popup(title='Full Body Home',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          

#====================================================================================================================
#====================================================================================================================




























#====================================================================================================================
#This is whare the Gym training plans will be located
#
#====================================================================================================================
class Gymplan(Screen):

    def profile(self):
#calling the users proflie
        uProfile()

#====================================================================================================================
#this is the clasic 5 day training plan
#
#====================================================================================================================
    def clasic_five_day(self):

        box = FloatLayout()

        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def legs(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Chest', size_hint = (0.15, 0.1), on_press = chest))
            box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Back', size_hint = (0.15, 0.1), on_press = back))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Shoulders', size_hint = (0.2, 0.1), on_press = shoulders))
            box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Arms & Abs', size_hint = (0.3, 0.1), on_press = arms_abs))



            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Legs                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/highbarbacksquat3.png', background_down='graphics/highbarbacksquat2.png',size_hint = (0.7, 0.11), on_release = Quads.high_bar_back_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/seatedlegcurl3.png', background_down='graphics/seatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/singleseatedlegcurl3.png', background_down='graphics/singleseatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.single_seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 10-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/abductor3.png', background_down='graphics/abductor2.png',size_hint = (0.7, 0.11), on_release = Glutes.abductor))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))



        def chest(instanace):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Chest', size_hint = (0.15, 0.1), on_press = chest))
            box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Back', size_hint = (0.15, 0.1), on_press = back))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Shoulders', size_hint = (0.2, 0.1), on_press = shoulders))
            box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Arms & Abs', size_hint = (0.3, 0.1), on_press = arms_abs))



            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Chest                   ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/inclinechestpress3.png', background_down='graphics/inclinechestpress2.png',size_hint = (0.7, 0.11), on_release = Chest.incline_chest_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/declinedbfly3.png', background_down='graphics/declinedbfly2.png',size_hint = (0.7, 0.11), on_release = Chest.decline_db_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/dips3.png', background_down='graphics/dips2.png',size_hint = (0.7, 0.11), on_release = Chest.dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/floorpress3.png', background_down='graphics/floorpress2.png',size_hint = (0.7, 0.11), on_release = Chest.floor_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/lthcablefly3.png', background_down='graphics/lthcablefly2.png',size_hint = (0.7, 0.11), on_release = Chest.low_to_high_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))



        def back(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Chest', size_hint = (0.15, 0.1), on_press = chest))
            box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Back', size_hint = (0.15, 0.1), on_press = back))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Shoulders', size_hint = (0.2, 0.1), on_press = shoulders))
            box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Arms & Abs', size_hint = (0.3, 0.1), on_press = arms_abs))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Back                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/latpulldown3.png', background_down='graphics/latpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/bentoverdbrow3.png', background_down='graphics/bentoverdbrow2.png',size_hint = (0.7, 0.11), on_release = Back.bent_over_db_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/pullthrough3.png', background_down='graphics/pullthrough2.png',size_hint = (0.7, 0.11), on_release = Back.pull_through))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/vbarpulldown3.png', background_down='graphics/vbarpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.vbar_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/lowerbackextention3.png', background_down='graphics/lowerbackextention2.png',size_hint = (0.7, 0.11), on_release = Back.lower_back_extention))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/pullup3.png', background_down='graphics/pullup2.png',size_hint = (0.7, 0.11), on_release = Back.pull_up))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))



        def shoulders(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Chest', size_hint = (0.15, 0.1), on_press = chest))
            box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Back', size_hint = (0.15, 0.1), on_press = back))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Shoulders', size_hint = (0.2, 0.1), on_press = shoulders))
            box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Arms & Abs', size_hint = (0.3, 0.1), on_press = arms_abs))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Shoulders                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/dbshoulderpress3.png', background_down='graphics/dbshoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_shoulder_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/cablefacepullrope3.png', background_down='graphics/cablefacepullrope2.png',size_hint = (0.7, 0.11), on_release = Shoulder.facepull_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/seatedlateralraise3.png', background_down='graphics/seatedlateralraise2.png',size_hint = (0.7, 0.11), on_release = Shoulder.seated_lateral_raise))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/standingdbpress3.png', background_down='graphics/standingdbpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.standing_db_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/shouldertaps3.png', background_down='graphics/shouldertaps2.png',size_hint = (0.7, 0.11), on_release = Shoulder.shoulder_taps))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/cableuprightrow3.png', background_down='graphics/cableuprightrow2.png',size_hint = (0.7, 0.11), on_release = Shoulder.cable_upright_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
 


        def arms_abs(instance):

            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Chest', size_hint = (0.15, 0.1), on_press = chest))
            box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Back', size_hint = (0.15, 0.1), on_press = back))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Shoulders', size_hint = (0.2, 0.1), on_press = shoulders))
            box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Arms & Abs', size_hint = (0.3, 0.1), on_press = arms_abs))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='       Arms and Abs                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/ezbarskullcrusher3.png', background_down='graphics/ezbarskullcrusher2.png',size_hint = (0.7, 0.11), on_release = Tricep.ezbar_skullcrusher))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/dbpreachercurl3.png', background_down='graphics/dbpreachercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.db_preacher_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/triceppushdownrope3.png', background_down='graphics/triceppushdownrope2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/inclinedumbbellcurl3.png', background_down='graphics/inclinedumbbellcurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.incline_dbcurl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/hangingkneeraises3.png', background_down='graphics/hangingkneeraises2.png',size_hint = (0.7, 0.11), on_release = Abs.hanging_knee_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='Failure             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/wristcurl3.png', background_down='graphics/wristcurl2.png',size_hint = (0.7, 0.11), on_release = Forearm.wrist_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/abdominalcrunch3.png', background_down='graphics/abdominalcrunch2.png',size_hint = (0.7, 0.11), on_release = Abs.abdominal_crunch))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='6-10           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
        box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))
        box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Chest', size_hint = (0.15, 0.1), on_press = chest))
        box.add_widget(Button(pos_hint = {'x': .35, 'center_y': 0.9}, text='Back', size_hint = (0.15, 0.1), on_press = back))
        box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Shoulders', size_hint = (0.2, 0.1), on_press = shoulders))
        box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Arms & Abs', size_hint = (0.3, 0.1), on_press = arms_abs))


        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='This is The Classic 5 Day training plan. The 5 sessions\nare split into Legs, Chest, Shoulders, Arm & Abs and\nBack. This plan gives you 2 rest days, you can\ncomplete the sessions in whatever order is\nmost comfortable.', size_hint = (0.2, 0.1), halign = 'center'))

        
        pop = Popup(title='Classic 5 days',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  

#====================================================================================================================
#====================================================================================================================


































#====================================================================================================================
#this is the clasic 4 day training plan
#
#====================================================================================================================
    def clasic_four_day(self):

        box = FloatLayout()

        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def chest(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Chest', size_hint = (0.2, 0.1), on_press = chest))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Back', size_hint = (0.2, 0.1), on_press = back))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Shoulders & Arms', size_hint = (0.4, 0.1), on_press = shoulder_arms))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Chest                   ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/inclinechestpress3.png', background_down='graphics/inclinechestpress2.png',size_hint = (0.7, 0.11), on_release = Chest.incline_chest_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/declinedbfly3.png', background_down='graphics/declinedbfly2.png',size_hint = (0.7, 0.11), on_release = Chest.decline_db_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/dips3.png', background_down='graphics/dips2.png',size_hint = (0.7, 0.11), on_release = Chest.dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/floorpress3.png', background_down='graphics/floorpress2.png',size_hint = (0.7, 0.11), on_release = Chest.floor_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/lthcablefly3.png', background_down='graphics/lthcablefly2.png',size_hint = (0.7, 0.11), on_release = Chest.low_to_high_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def back(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Chest', size_hint = (0.2, 0.1), on_press = chest))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Back', size_hint = (0.2, 0.1), on_press = back))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Shoulders & Arms', size_hint = (0.4, 0.1), on_press = shoulder_arms))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Back                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/latpulldown3.png', background_down='graphics/latpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/bentoverdbrow3.png', background_down='graphics/bentoverdbrow2.png',size_hint = (0.7, 0.11), on_release = Back.bent_over_db_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/pullthrough3.png', background_down='graphics/pullthrough2.png',size_hint = (0.7, 0.11), on_release = Back.pull_through))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/vbarpulldown3.png', background_down='graphics/vbarpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.vbar_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/lowerbackextention3.png', background_down='graphics/lowerbackextention2.png',size_hint = (0.7, 0.11), on_release = Back.lower_back_extention))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/pullup3.png', background_down='graphics/pullup2.png',size_hint = (0.7, 0.11), on_release = Back.pull_up))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))



        def shoulder_arms(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Chest', size_hint = (0.2, 0.1), on_press = chest))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Back', size_hint = (0.2, 0.1), on_press = back))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Shoulders & Arms', size_hint = (0.4, 0.1), on_press = shoulder_arms))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='             Shoulders & Arms                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/dbshoulderpress3.png', background_down='graphics/dbshoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_shoulder_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/ezbarpreachercurl3.png', background_down='graphics/ezbarpreachercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.db_preacher_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/seatedlateralraise3.png', background_down='graphics/seatedlateralraise2.png',size_hint = (0.7, 0.11), on_release = Shoulder.seated_lateral_raise))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/inclinedumbbellcurl3.png', background_down='graphics/inclinedumbbellcurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.incline_dbcurl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/cablefacepullrope3.png', background_down='graphics/cablefacepullrope2.png',size_hint = (0.7, 0.11), on_release = Shoulder.facepull_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/zottmancurl3.png', background_down='graphics/zottmancurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.zottman_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/wristcurl3.png', background_down='graphics/wristcurl2.png',size_hint = (0.7, 0.11), on_release = Forearm.wrist_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='6-10           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
        
        def legs(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Chest', size_hint = (0.2, 0.1), on_press = chest))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Back', size_hint = (0.2, 0.1), on_press = back))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Shoulders & Arms', size_hint = (0.4, 0.1), on_press = shoulder_arms))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Legs                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/highbarbacksquat3.png', background_down='graphics/highbarbacksquat2.png',size_hint = (0.7, 0.11), on_release = Quads.high_bar_back_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/seatedlegcurl3.png', background_down='graphics/seatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/singleseatedlegcurl3.png', background_down='graphics/singleseatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.single_seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 10-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/abductor3.png', background_down='graphics/abductor2.png',size_hint = (0.7, 0.11), on_release = Glutes.abductor))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
  


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
        box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Chest', size_hint = (0.2, 0.1), on_press = chest))
        box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Back', size_hint = (0.2, 0.1), on_press = back))
        box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Shoulders & Arms', size_hint = (0.4, 0.1), on_press = shoulder_arms))
        box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Legs', size_hint = (0.2, 0.1), on_press = legs))


        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='This is the Classic 4 Day training plan. The sessions\nare grouped into Chest, Back, Shoulders & Arms\nand Legs. This training plan gives you 3 days rest.', size_hint = (0.2, 0.1), halign = 'center'))

        
        pop = Popup(title='Classic 4 Days',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  




#====================================================================================================================
#====================================================================================================================
































#====================================================================================================================
#Full body gym training plan
#
#====================================================================================================================
    def fullbody(self):

        box = FloatLayout()

        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def day1(instance):
            
                        
        # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day  1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/inclinechestpress3.png', background_down='graphics/inclinechestpress2.png',size_hint = (0.7, 0.11), on_release = Chest.incline_chest_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/triceppushdownbar3.png', background_down='graphics/triceppushdownbar2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_bar))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/dbshoulderpress3.png', background_down='graphics/dbshoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_shoulder_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/reversegriplatpulldown3.png', background_down='graphics/reversegriplatpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.reverse_lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/seatedlegextention3.png', background_down='graphics/seatedlegextention2.png',size_hint = (0.7, 0.11), on_release = Quads.seated_leg_extention))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/singleseatedlegcurl3.png', background_down='graphics/singleseatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.single_seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/hammercurl3.png', background_down='graphics/hammercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.hammer_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='6-10           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def day2(instance):
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day  2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/vbarpulldown3.png', background_down='graphics/vbarpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.vbar_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/straightbarcablecurl3.png', background_down='graphics/straightbarcablecurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.straight_bar_cable_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/flatdbfly3.png', background_down='graphics/flatdbfly2.png',size_hint = (0.7, 0.11), on_release = Chest.flat_db_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/overheadextentionrope3.png', background_down='graphics/overheadextentionrope2.png',size_hint = (0.7, 0.11), on_release = Tricep.overhead_extention_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/romainiandeadlift3.png', background_down='graphics/romainiandeadlift2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.romanian_deadlift))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             1               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/dumbbelllateralraise3.png', background_down='graphics/dumbbelllateralraise2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_lateral_raise))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='8-12           1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))



        def day3(instance):
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Day  3                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/dumbbellgobletsquat3.png', background_down='graphics/dumbbellgobletsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.db_goblet_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/seatedlegcurl3.png', background_down='graphics/seatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/lthcablefly3.png', background_down='graphics/lthcablefly2.png',size_hint = (0.7, 0.11), on_release = Chest.low_to_high_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/triceppushdownbar3.png', background_down='graphics/triceppushdownbar2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_bar))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          1              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/pullthrough3.png', background_down='graphics/pullthrough2.png',size_hint = (0.7, 0.11), on_release = Back.pull_through))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/cableuprightrow3.png', background_down='graphics/cableuprightrow2.png',size_hint = (0.7, 0.11), on_release = Shoulder.cable_upright_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/dbpreachercurl3.png', background_down='graphics/dbpreachercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.db_preacher_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
        box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Day 1', size_hint = (0.16, 0.1), on_press = day1))
        box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Day 2', size_hint = (0.16, 0.1), on_press = day2))
        box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Day 3', size_hint = (0.16, 0.1), on_press = day3))


        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='This is the Full Body gym training plan. Here are\nthree different full body sessions which you can\ndo throughout the week.', size_hint = (0.2, 0.1), halign = 'center'))

        
        pop = Popup(title='Full Body',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  



#====================================================================================================================
#====================================================================================================================


































#====================================================================================================================
# Push Pull Legs Training Plan
#
#====================================================================================================================
    def ppl(self):

        box = FloatLayout()

        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def push1(instance):
            
                        
        # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Push 1', size_hint = (0.16, 0.1), on_press = push1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Pull 1', size_hint = (0.16, 0.1), on_press = pull1))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Legs 1', size_hint = (0.16, 0.1), on_press = legs1))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Push 2', size_hint = (0.16, 0.1), on_press = push2))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Pull 2', size_hint = (0.16, 0.1), on_press = pull2))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Legs 2', size_hint = (0.16, 0.1), on_press = legs2))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Push  1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/benchpress3.png', background_down='graphics/benchpress2.png',size_hint = (0.7, 0.11), on_release = Chest.bench_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/triceppushdownrope3.png', background_down='graphics/triceppushdownrope2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/dbshoulderpress3.png', background_down='graphics/dbshoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_shoulder_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/htlcablefly3.png', background_down='graphics/htlcablefly2.png',size_hint = (0.7, 0.11), on_release = Chest.high_to_low_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/singledbskullcrusher3.png', background_down='graphics/singledbskullcrusher2.png',size_hint = (0.7, 0.11), on_release = Tricep.single_db_skullcrusher))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='6-10             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/dblateralraise3.png', background_down='graphics/dblateralraise2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_lateral_raise))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

        def pull1(instance):
                        
        # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Push 1', size_hint = (0.16, 0.1), on_press = push1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Pull 1', size_hint = (0.16, 0.1), on_press = pull1))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Legs 1', size_hint = (0.16, 0.1), on_press = legs1))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Push 2', size_hint = (0.16, 0.1), on_press = push2))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Pull 2', size_hint = (0.16, 0.1), on_press = pull2))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Legs 2', size_hint = (0.16, 0.1), on_press = legs2))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Pull  1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Pull  1                    ', size_hint = (0.4, 0.2), bold = True))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/vbarseatedrow3.png', background_down='graphics/vbarseatedrow2.png',size_hint = (0.7, 0.11), on_release = Back.vbar_seatedrow))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/hammercurl3.png', background_down='graphics/hammercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.hammer_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/reversegriplatpulldown3.png', background_down='graphics/reversegriplatpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.reverse_lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/inclinedumbbellcurl3.png', background_down='graphics/inclinedumbbellcurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.incline_dbcurl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 8-12              0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/pullthrough3.png', background_down='graphics/pullthrough2.png',size_hint = (0.7, 0.11), on_release = Back.pull_through))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='10-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/zottmancurl3.png', background_down='graphics/zottmancurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.zottman_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='10-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/cablefacepullrope3.png', background_down='graphics/cablefacepullrope2.png',size_hint = (0.7, 0.11), on_release = Shoulder.facepull_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='10-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            


        def legs1(instance):
                        
        # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Push 1', size_hint = (0.16, 0.1), on_press = push1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Pull 1', size_hint = (0.16, 0.1), on_press = pull1))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Legs 1', size_hint = (0.16, 0.1), on_press = legs1))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Push 2', size_hint = (0.16, 0.1), on_press = push2))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Pull 2', size_hint = (0.16, 0.1), on_press = pull2))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Legs 2', size_hint = (0.16, 0.1), on_press = legs2))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Legs  1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/highbarbacksquat3.png', background_down='graphics/highbarbacksquat2.png',size_hint = (0.7, 0.11), on_release = Quads.high_bar_back_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/seatedlegcurl3.png', background_down='graphics/seatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/singleseatedlegcurl3.png', background_down='graphics/singleseatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.single_seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 10-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/abductor3.png', background_down='graphics/abductor2.png',size_hint = (0.7, 0.11), on_release = Glutes.abductor))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

        def push2(instance):
                        
        # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Push 1', size_hint = (0.16, 0.1), on_press = push1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Pull 1', size_hint = (0.16, 0.1), on_press = pull1))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Legs 1', size_hint = (0.16, 0.1), on_press = legs1))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Push 2', size_hint = (0.16, 0.1), on_press = push2))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Pull 2', size_hint = (0.16, 0.1), on_press = pull2))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Legs 2', size_hint = (0.16, 0.1), on_press = legs2))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Push  2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7},  background_normal='graphics/dbshoulderpress3.png', background_down='graphics/dbshoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_shoulder_press)) 
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6},background_normal='graphics/inclinechestpress3.png', background_down='graphics/inclinechestpress2.png',size_hint = (0.7, 0.11), on_release = Chest.incline_chest_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/declinedbfly3.png', background_down='graphics/declinedbfly2.png',size_hint = (0.7, 0.11), on_release = Chest.decline_db_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/seatedlateralraise3.png', background_down='graphics/seatedlateralraise2.png',size_hint = (0.7, 0.11), on_release = Shoulder.seated_lateral_raise))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/vbartricepextention3.png', background_down='graphics/vbartricepextention2.png',size_hint = (0.7, 0.11), on_release = Tricep.vbar_tricep_extention))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='6-10             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/singlearmtricepextention3.png', background_down='graphics/singlearmtricepextention2.png',size_hint = (0.7, 0.11), on_release = Tricep.single_arm_tricep_extention))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

        def pull2(instance):
                        
        # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Push 1', size_hint = (0.16, 0.1), on_press = push1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Pull 1', size_hint = (0.16, 0.1), on_press = pull1))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Legs 1', size_hint = (0.16, 0.1), on_press = legs1))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Push 2', size_hint = (0.16, 0.1), on_press = push2))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Pull 2', size_hint = (0.16, 0.1), on_press = pull2))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Legs 2', size_hint = (0.16, 0.1), on_press = legs2))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Pull  2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/latpulldown3.png', background_down='graphics/latpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/ropehammercurl3.png', background_down='graphics/ropehammercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.rope_hammer_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/widebarseatedrow3.png', background_down='graphics/widebarseatedrow2.png',size_hint = (0.7, 0.11), on_release = Back.wide_bar_seated_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/dbpreachercurl3.png', background_down='graphics/dbpreachercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.db_preacher_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/pullthrough3.png', background_down='graphics/pullthrough2.png',size_hint = (0.7, 0.11), on_release = Back.pull_through))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/inclinedumbbellcurl3.png', background_down='graphics/inclinedumbbellcurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.incline_dbcurl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/cablefacepullrope3.png', background_down='graphics/cablefacepullrope2.png',size_hint = (0.7, 0.11), on_release = Shoulder.facepull_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

        def legs2(instance):
                        
        # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Push 1', size_hint = (0.16, 0.1), on_press = push1))
            box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Pull 1', size_hint = (0.16, 0.1), on_press = pull1))
            box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Legs 1', size_hint = (0.16, 0.1), on_press = legs1))
            box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Push 2', size_hint = (0.16, 0.1), on_press = push2))
            box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Pull 2', size_hint = (0.16, 0.1), on_press = pull2))
            box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Legs 2', size_hint = (0.16, 0.1), on_press = legs2))


            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Legs  2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/romainiandeadlift3.png', background_down='graphics/romainiandeadlift2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.romanian_deadlift))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/seatedlegextention3.png', background_down='graphics/seatedlegextention2.png',size_hint = (0.7, 0.11), on_release = Quads.seated_leg_extention))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/dumbbellhamstringcurl3.png', background_down='graphics/dumbbellhamstringcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/singlelegseatedextention3.png', background_down='graphics/singlelegseatedextention2.png',size_hint = (0.7, 0.11), on_release = Quads.single_leg_seated_extention))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/adductor3.png', background_down='graphics/adductor2.png',size_hint = (0.7, 0.11), on_release = Quads.adductor))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/abcrunch3.png', background_down='graphics/abcrunch2.png',size_hint = (0.7, 0.11), on_release = Abs.ab_crunch))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/hangingkneeraises3.png', background_down='graphics/hangingkneeraises2.png',size_hint = (0.7, 0.11), on_release = Abs.hanging_knee_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
        box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Push 1', size_hint = (0.16, 0.1), on_press = push1))
        box.add_widget(Button(pos_hint = {'x': .166, 'center_y': 0.9}, text='Pull 1', size_hint = (0.16, 0.1), on_press = pull1))
        box.add_widget(Button(pos_hint = {'x': .333, 'center_y': 0.9}, text='Legs 1', size_hint = (0.16, 0.1), on_press = legs1))
        box.add_widget(Button(pos_hint = {'x': .499, 'center_y': 0.9}, text='Push 2', size_hint = (0.16, 0.1), on_press = push2))
        box.add_widget(Button(pos_hint = {'x': .665, 'center_y': 0.9}, text='Pull 2', size_hint = (0.16, 0.1), on_press = pull2))
        box.add_widget(Button(pos_hint = {'x': .831, 'center_y': 0.9}, text='Legs 2', size_hint = (0.16, 0.1), on_press = legs2))

        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='This is the Push Pull Legs (PPL) Training plan. The\nsessions are split into 3 groups:\n \nPush - Chest, Shoulders, Triceps\nPull - Back, Biceps, Rear Delts \nLegs - Quads, Hamstring, Calves', size_hint = (0.2, 0.1), halign = 'center'))

        
        pop = Popup(title='Push Pull Legs',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  




#====================================================================================================================
#====================================================================================================================

































#====================================================================================================================
#Uppler Lower Gym Training Plan
#
#====================================================================================================================
    def upperlower(self):

        box = FloatLayout()

        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def monday(instance):
            
        # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0.1, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .3, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Upper  1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/benchpress3.png', background_down='graphics/benchpress2.png',size_hint = (0.7, 0.11), on_release = Chest.bench_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='8-12           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/bentoverdbrow3.png', background_down='graphics/bentoverdbrow2.png',size_hint = (0.7, 0.11), on_release = Back.bent_over_db_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 6-10             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/dbshoulderpress3.png', background_down='graphics/dbshoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_shoulder_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/latpulldown3.png', background_down='graphics/latpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/triceppushdownrope3.png', background_down='graphics/triceppushdownrope2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/dumbbelllateralraise3.png', background_down='graphics/dumbbelllateralraise2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_lateral_raise))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/pushups3.png', background_down='graphics/pushups2.png',size_hint = (0.7, 0.11), on_release = Chest.pushups))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


            
        def tuesday(instance):
           
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0.1, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .3, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Lower  1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/highbarbacksquat3.png', background_down='graphics/highbarbacksquat2.png',size_hint = (0.7, 0.11), on_release = Quads.high_bar_back_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/dumbbellstiffdeadlift3.png', background_down='graphics/dumbbellstiffdeadlift2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.db_stiff_deadlift))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 12-15             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/seatedlegextention3.png', background_down='graphics/seatedlegextention2.png',size_hint = (0.7, 0.11), on_release = Quads.seated_leg_extention))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/seatedlegcurl3.png', background_down='graphics/seatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/walkinglunges3.png', background_down='graphics/walkinglunges2.png',size_hint = (0.7, 0.11), on_release = Quads.walking_lunges))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/plank3.png', background_down='graphics/plank2.png',size_hint = (0.7, 0.11), on_release = Abs.plank))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='1 min           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def thursday(instance):
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0.1, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .3, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Upper  2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/inclinechestpress3.png', background_down='graphics/inclinechestpress2.png',size_hint = (0.7, 0.11), on_release = Chest.incline_chest_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/seatedrow3.png', background_down='graphics/seatedrow2.png',size_hint = (0.7, 0.11), on_release = Back.seated_row))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/lthcablefly3.png', background_down='graphics/lthcablefly2.png',size_hint = (0.7, 0.11), on_release = Chest.low_to_high_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 12-15             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/closegriplatpulldown3.png', background_down='graphics/closegriplatpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.close_lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 8-12          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/bicepcurl3.png', background_down='graphics/bicepcurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.bicep_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/triceppushdownbar3.png', background_down='graphics/triceppushdownbar2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_bar))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/pullup3.png', background_down='graphics/pullup2.png',size_hint = (0.7, 0.11), on_release = Back.pull_up))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

        def friday(instance):
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0.1, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .3, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))

            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Lower  2                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/landminesquat3.png', background_down='graphics/landminesquat2.png',size_hint = (0.7, 0.11), on_release = Quads.db_goblet_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/conventionaldeadlift3.png', background_down='graphics/conventionaldeadlift2.png',size_hint = (0.7, 0.11), on_release = Compound.conventional_deadlift))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/situp3.png', background_down='graphics/situp2.png',size_hint = (0.7, 0.11), on_release = Abs.sit_up))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 6-10            1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/seatedcalfraises3.png', background_down='graphics/seatedcalfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.seated_calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='8-12             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/lowerbackextention3.png', background_down='graphics/lowerbackextention2.png',size_hint = (0.7, 0.11), on_release = Back.lower_back_extention))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/hangingkneeraises3.png', background_down='graphics/hangingkneeraises2.png',size_hint = (0.7, 0.11), on_release = Abs.hanging_knee_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='Failure           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
   





#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
        box.add_widget(Button(pos_hint = {'x': 0.1, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
        box.add_widget(Button(pos_hint = {'x': .3, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
        box.add_widget(Button(pos_hint = {'x': .5, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
        box.add_widget(Button(pos_hint = {'x': .7, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))

        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='This is the upper lower gym training plan. The\nsessions are split into two groups, the upper and lower\nportion of your body. This training plan gives you\n3 rest days however you can easily alter that.', size_hint = (0.2, 0.1), halign = 'center'))

        
        pop = Popup(title='Upper Lower',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  



#====================================================================================================================
#====================================================================================================================































#====================================================================================================================
#Matts curent Training plan
#
#====================================================================================================================


    def mattplan(self):

        box = FloatLayout()
        
        def wipe():
            box.clear_widgets()
            #Wipe clears the screen so that the two sessions dont overlap

        def monday(instance):
            # plan.clear_widgets()
            wipe()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))

            
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Push  1                    ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/inclinechestpress3.png', background_down='graphics/inclinechestpress2.png',size_hint = (0.7, 0.11), on_release = Chest.incline_chest_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/shoulderpress3.png', background_down='graphics/shoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.shoulder_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/triceppushdownbar3.png', background_down='graphics/triceppushdownbar2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_bar))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/lthcablefly3.png', background_down='graphics/lthcablefly2.png',size_hint = (0.7, 0.11), on_release = Chest.low_to_high_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 12-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/dips3.png', background_down='graphics/dips2.png',size_hint = (0.7, 0.11), on_release = Chest.dips))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='6-10             0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/seatedlateralraise3.png', background_down='graphics/seatedlateralraise2.png',size_hint = (0.7, 0.11), on_release = Shoulder.seated_lateral_raise))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/singlearmtricepextention3.png', background_down='graphics/singlearmtricepextention2.png',size_hint = (0.7, 0.11), on_release = Tricep.single_arm_tricep_extention))

        def tuesday(instance):
            wipe()
            # plan.clear_widgets()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))            


            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Pull  1                    ', size_hint = (0.4, 0.2), bold = True))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/latpulldown3.png', background_down='graphics/latpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='10-15           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/hammercurl3.png', background_down='graphics/hammercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.hammer_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/vbarseatedrow3.png', background_down='graphics/vbarseatedrow2.png',size_hint = (0.7, 0.11), on_release = Back.vbar_seatedrow))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/inclinedumbbellcurl3.png', background_down='graphics/inclinedumbbellcurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.incline_dbcurl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 6-10              0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/pullthrough3.png', background_down='graphics/pullthrough2.png',size_hint = (0.7, 0.11), on_release = Back.pull_through))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/zottmancurl3.png', background_down='graphics/zottmancurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.zottman_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='10-15           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/cablefacepullrope3.png', background_down='graphics/cablefacepullrope2.png',size_hint = (0.7, 0.11), on_release = Shoulder.facepull_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='10-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
        

        def wednesday(instance):
            wipe()
            # plan.clear_widgets()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))            


            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Legs                      ', size_hint = (0.4, 0.2), bold = True))

            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/highbarbacksquat3.png', background_down='graphics/highbarbacksquat2.png',size_hint = (0.7, 0.11), on_release = Quads.high_bar_back_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/seatedlegcurl3.png', background_down='graphics/seatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12             1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/bulgariansplitsquat3.png', background_down='graphics/bulgariansplitsquat2.png',size_hint = (0.7, 0.11), on_release = Quads.bulgarian_split_squat))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12             0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/singleseatedlegcurl3.png', background_down='graphics/singleseatedlegcurl2.png',size_hint = (0.7, 0.11), on_release = Hamstrings.single_seated_leg_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 10-15          0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/calfraises3.png', background_down='graphics/calfraises2.png',size_hint = (0.7, 0.11), on_release = Calfs.calf_raises))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/abductor3.png', background_down='graphics/abductor2.png',size_hint = (0.7, 0.11), on_release = Glutes.abductor))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='12-15           0               4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            


        def thursday(instance):
            wipe()
            # plan.clear_widgets()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))

            
            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Push  2                    ', size_hint = (0.4, 0.2), bold = True))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/dbshoulderpress3.png', background_down='graphics/dbshoulderpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.db_shoulder_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10             2                 3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/flatchestpress3.png', background_down='graphics/flatchestpress2.png',size_hint = (0.7, 0.11), on_release = Chest.flat_chest_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12           1                 3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/seatedreversefly3.png', background_down='graphics/seatedreversefly2.png',size_hint = (0.7, 0.11), on_release = Shoulder.seated_reverse_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 12-15        0                 4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/inclinedbfly3.png', background_down='graphics/inclinedbfly2.png',size_hint = (0.7, 0.11), on_release = Chest.incline_db_fly))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 8-12            0                 3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/ezbarskullcrusher3.png', background_down='graphics/ezbarskullcrusher2.png',size_hint = (0.7, 0.11), on_release = Tricep.ezbar_skullcrusher))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='6-10              0                3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/overheadpress3.png', background_down='graphics/overheadpress2.png',size_hint = (0.7, 0.11), on_release = Shoulder.overhead_press))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12              0                3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/triceppushdownrope3.png', background_down='graphics/triceppushdownrope2.png',size_hint = (0.7, 0.11), on_release = Tricep.tricep_pushdown_rope))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='10-15            0                3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))


        def friday(instance):
            wipe()
            # plan.clear_widgets()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code adds widgets to the pop up,
#this is one of the taining plans , 
#this includes direct links to the popup in the exercise tutorial, 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
            box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
            box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
            box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
            box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))
            box.add_widget(Label(pos_hint = {'x': .32, 'center_y': 0.8}, text='Rep\n Range', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .5, 'center_y': 0.8}, text='Warm Up\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Label(pos_hint = {'x': .7, 'center_y': 0.8}, text='Working\n Sets', size_hint = (0.4, 0.2), bold = True, halign = 'center'))        



            box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.8}, text='Pull  2                    ', size_hint = (0.4, 0.2), bold = True))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.7}, background_normal='graphics/vbarseatedrow3.png', background_down='graphics/vbarseatedrow2.png',size_hint = (0.7, 0.11), on_release = Back.vbar_seatedrow))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.72}, text='6-10           2               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.6}, background_normal='graphics/dbpreachercurl3.png', background_down='graphics/dbpreachercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.db_preacher_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.62}, text=' 8-12           1               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.5}, background_normal='graphics/reversegriplatpulldown3.png', background_down='graphics/reversegriplatpulldown2.png',size_hint = (0.7, 0.11), on_release = Back.reverse_lat_pulldown))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.52}, text=' 8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.4}, background_normal='graphics/ropehammercurl3.png', background_down='graphics/ropehammercurl2.png',size_hint = (0.7, 0.11), on_release = Bicep.rope_hammer_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.42}, text=' 6-10           0              3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.3}, background_normal='graphics/pullthroughsb3.png', background_down='graphics/pullthroughsb2.png',size_hint = (0.7, 0.11), on_release = Back.pull_through_sb))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.32}, text='12-15          0              4', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.2}, background_normal='graphics/wristcurl3.png', background_down='graphics/wristcurl2.png',size_hint = (0.7, 0.11), on_release = Forearm.wrist_curl))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.22}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))
            box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.1}, background_normal='graphics/dumbbellshrug3.png', background_down='graphics/dumbbellshrug2.png',size_hint = (0.7, 0.11), on_release = Trap.db_shrug))
            box.add_widget(Label(pos_hint = {'x': .49, 'center_y': 0.12}, text='8-12           0               3', size_hint = (0.4, 0.2), bold = True, halign = 'center'))






#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part of code is the main function of the popup this call the other functions and displays the sessions to the user
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
        box.add_widget(Button(pos_hint = {'x': 0, 'center_y': 0.9}, text='Mon', size_hint = (0.2, 0.1), on_press = monday))
        box.add_widget(Button(pos_hint = {'x': .2, 'center_y': 0.9}, text='Tue', size_hint = (0.2, 0.1), on_press = tuesday))
        box.add_widget(Button(pos_hint = {'x': .4, 'center_y': 0.9}, text='Wed', size_hint = (0.2, 0.1), on_press = wednesday))
        box.add_widget(Button(pos_hint = {'x': .6, 'center_y': 0.9}, text='Thu', size_hint = (0.2, 0.1), on_press = thursday))
        box.add_widget(Button(pos_hint = {'x': .8, 'center_y': 0.9}, text='Fri', size_hint = (0.2, 0.1), on_press = friday))

        box.add_widget(Label(pos_hint = {'x': 0.4, 'center_y': 0.7}, text='This is the current training plan that Matt is following.\n It is a variation of PPL, it includes two rest days.', size_hint = (0.2, 0.1), halign = 'center'))
        


        
        pop = Popup(title='Matts Plan',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 




#====================================================================================================================
#====================================================================================================================


        
    
    


















#====================================================================================================================
#====================================================================================================================
#Here is Where the Individual Exercises will be stored
#
#====================================================================================================================

#====================================================================================================================
# Chest exercises
#====================================================================================================================
class Chest(Screen):

    def profile(self):
#calling user profile
        uProfile()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bench_press(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'To execute the bench press, first, lie on your back on\nthe bench and grip the bar slightly wider than shoulder\nwidth. From there press your feet firmly into the ground and\nmake sure that your hips are always on the bench.\nSlowly lift the bar off the rack and lower the bar to\nyour chest(just above your sternum) allowing your\nelbows to bend out to the side at 45 degrees.\nStop lowering when your elbows are just below the\nbench, press feet into the floor and push\nthe bar back up. Remember to always warm up\nto prevent injury and have a spotter when you can.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/BenchPress.mov', row_default_height = 0,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                      image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/BenchPress.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Bench Press',
                  content= box,          
                  size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def close_bench_press(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'To execute the close grip bench press first, lie on your\nback on the bench and grip the bar around shoulder\nwidth. From there press your feet firmly into the ground and\nmake sure that your hips are always on the bench.\nSlowly lift the bar off the rack and lower the bar to\nyour chest(just above your sternum) allowing your\nelbows to bend out to the side at 45 degrees.\nStop lowering when your elbows are just below the\nbench, press feet into the floor and push\nthe bar back up. Remember to always warm up\nto prevent injury and have a spotter when you can.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/CloseGripBenchPress.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                      image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/CloseGripBenchPress.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Close Grip Bench Press',
                  content= box,          
                  size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def incline_chest_press(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'For the machine incline chest press you first select\nthe handle that you feel most comfortable with,\nthen from there push up and slowly lower it\nback down. It is important for this exercise that you\ncontrol the weight throughout the whole movement.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/InclineChestPress.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                      image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/InclineChestPress.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Incline Chest Press',
                  content= box,          
                  size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def flat_chest_press(self):
        
        pop = Popup(title='flat chest press',
                  content=Label(text='Set bench so it is flat, from there\nlay back on the bench with arms straight\nand dumbbells above your chest. Then lower elbows\ndown either side of the chest, keeping\nforearms facing the sky. Make sure to pause\nat bottom before pushing dumbbells back up to\n the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def decline_chest_press(self):
        
        pop = Popup(title='decline chest press',
                  content=Label(text='Set bench so it is declined, from there\nlay back on the bench with arms straight\nand dumbbells above your chest. Then lower elbows\ndown either side of the chest, keeping\nforearms facing the sky. Make sure to pause\nat bottom before pushing dumbbells back up to\n the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def floor_press(self):
        
        pop = Popup(title='floor press',
                  content=Label(text='For the floor press first select a suitable\nweight, then from there sit on the floor,\nget the weights on your thighs then fall\nback and press up. For this it is\nimportant to control the weight both on the\nway down and up, keeping a steady pace.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def flat_db_fly(self):
        
        pop = Popup(title='flat dumbbell fly',
                  content=Label(text='Set bench so it is flat. From there\nlay back on the bench with arms straight\nand dumbbells above your chest. Then move dumbbells\napart in an arcing motion until elbows are\nlevel with the chest. Remember and pause at\nbottom before following the same arcing motion bringing\nthe dumbbells back together in the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def incline_db_fly(self):
        
        pop = Popup(title='Incline Dumbbell Fly',
                  content=Label(text='Set bench so it is inclined. From there\nlay back on the bench with arms straight\nand dumbbells above your chest. Then move dumbbells\napart in an arcing motion until elbows are\nlevel with the chest. Remember and pause at\nbottom before following the same arcing motion bringing\nthe dumbbells back together in the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def decline_db_fly(self):
        
        pop = Popup(title='Decline Dumbbell Fly',
                  content=Label(text='Set bench so it is declined. From there\nlay back on the bench with arms straight\nand dumbbells above your chest. Then move dumbbells\napart in an arcing motion until elbows are\nlevel with the chest. Remember and pause at\nbottom before following the same arcing motion bringing\nthe dumbbells back together in the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def low_to_high_fly(self):
        
        pop = Popup(title='low to high cable fly',
                  content=Label(text='Set cables to shin height. From there face\naway from cables and grip the handles. With\nan arcing motion press handles forward and bring\nthem together in front of the chest. Pause\nbefore following the same arcing motion lowering the\nhandles back to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def high_to_low_fly(self):
        
        pop = Popup(title= 'High To Low Cable Fly', 
                  content=Label(text='Set cables to shoulder height. From there face\naway from cables and grip the handles. With\nan arcing motion press handles forward and bring\nthem together in front of the chest. Pause\nbefore following the same arcing motion lowering the\nhandles back to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def mid_fly(self):
        
        pop = Popup(title='Mid Cable Fly',
                  content=Label(text='Set cables to waist height. From there face\naway from cables and grip the handles. With\nan arcing motion press handles forward and bring\nthem together in front of the chest. Pause\nbefore following the same arcing motion lowering the\nhandles back to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def wide_pushups(self):
        
        pop = Popup(title='Wide Pushups',
                  content=Label(text='Get down on all fours, placing your hands\n wider than your shoulders. Straighten\nyour arms and legs. Lower your body until\nyour chest nearly touches the floor. Pause, then\npush yourself back up.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def dips(self):
        
        pop = Popup(title='dips',
                  content=Label(text='Place hands firmly on the handles. From there\nstraighten arms fully, leaning forward slightly keeping\nforearms facing the sky. Keeping forearms facing the\nsky, bend at the elbow, lowering until reaching\na 90 degree angle in the elbow. Remember to\npause at the bottom before pushing against the\nhandles and straightening your arms.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def pushups(self):
        
        pop = Popup(title='push ups',
                  content=Label(text='Get down on all fours, placing your hands\nslightly wider than your shoulders. Straighten\nyour arms and legs. Lower your body until\nyour chest nearly touches the floor. Pause, then\npush yourself back up.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def knee_pushups(self):
        
        pop = Popup(title='knee push ups',
                  content=Label(text='Kneel on the floor. Extend arms and put\nhands shoulder width apart on the floor in\nfront of you. Tighten abs while you bend\narms, lowering your torso until chest grazes the\nfloor. Push torso back up by\nstraightening arms.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def wall_pushups(self):
        
        pop = Popup(title='wall push ups',
                  content=Label(text='When facing the wall stand just over one\narms length away, from there put your hands\non the wall around shoulder width apart. Slowly\nlower yourself towards the wall and push\nyourself back up, staning in control throughout\nthe movement.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#====================================================================================================================
#====================================================================================================================





























#====================================================================================================================
#Back
#====================================================================================================================

class Back(Screen):
    #lat pulldown, pull up, seated row, 


    def profile(self):
#calling user profile
        uProfile()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def lat_pulldown(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Set knee pad to sit just on knees.\nFrom there grab the bar with a shoulder\nwidth grip, Pull bar down to top of\nthe chest leaning back slightly. Remember to pause,\nthen slowly return bar up to starting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/LatPulldown.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/LatPulldown.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Lat Pulldown',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def pull_up(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Exhale while pulling yourself up so your chin\nis level with the bar. Pause at the\ntop. Lower yourself (inhaling as you go down)\nuntil your elbows are straight. Repeat the movement\n without touching the floor.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/PullUp.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/PullUp.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Pull Up',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def seated_row(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Sit on the pad with slight bend in\nknees and back straight making sure feet are\nplanted on the rests. From there take hold\nof the attatchment and pull in towards the\nbelly button, getting elbows as far behind the\nbody as possible. Keeping back straight, lower attatchment\nback to starting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/SeatedRow.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/SeatedRow.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Seated Row',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def lower_back_extention(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Your knees should be directly under your hips\nand your hands under your shoulders. Start with\na straight spine. Bend your spine upwards (flexion)\ntoward the ceiling, holding for 10 to 15\nseconds. Then relax and arch your lower back\nso your stomach moves toward the floor, holding\nfor 10 to 15 seconds.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/LowerBackExtention.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/LowerBackExtention.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Lower Back Extension',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def close_lat_pulldown(self):
        
        pop = Popup(title='close grip lat pulldown',
                  content=Label(text='Set knee pad to sit just on knees.\nFrom there grab the bar just in from a\nshoulder width grip, pull bar down to top of\nthe chest leaning back slightly. Remember to pause,\nthen slowly return bar up to starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def reverse_lat_pulldown(self):
        
        pop = Popup(title='reverse lat pulldown',
                  content=Label(text='Set knee pad to sit just on knees.\nFrom there grab the bar palms facing inwards with a\nshoulder width grip, Pull bar down to top of\nthe chest leaning back slightly. Remember to pause,\nthen slowly return bar up to starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def vbar_pulldown(self):
        
        pop = Popup(title='v-bar pulldown',
                  content=Label(text='Set knee pad to sit just on knees.\nFrom there grab the bar with a neutral\ngrip, Pull bar down to top of\nthe chest leaning back slightly. Remember to pause,\nthen slowly return bar up to starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def chin_up(self):
        
        pop = Popup(title='chin up',
                  content=Label(text='Your palms should be facing you and your\narms should be shoulder-width apart. Engage\nyour upper back and core. Continuing to hold\non to the bar, lift your chest up\ntowards it. Slowly lower yourself until you are\nback to your starting position', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#pullthrough rope
    def pull_through(self):
        
        pop = Popup(title='pull through (rope)',
                  content=Label(text='Set cable to highest setting. Grip attatchment and\npush hips back, letting chest drop and keeping\nthe back straight. Using an arcing motion, bring\nthe attatchment to your hips and elbows to\nyour sides, while pushing your hands away from\nyou. Hold at the bottom before following the\nsame arcing motion pushing your hands away from\nyou back to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def home_row(self):
        
        pop = Popup(title='Home Row',
                  content=Label(text='For this exercise i want you to get anything\nthat is a suitlable weight, if you\nhave weights you can use them but if\nnot you can fill a backpack with things\nand use that for example, but anything\nwill do.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def pull_through_sb(self):
        
        pop = Popup(title='pull through (straight bar)',
                  content=Label(text='Set cable to highest setting. Grip attatchment and\npush hips back, letting chest drop and keeping\nthe back straight. Using an arcing motion, bring\nthe attatchment to your hips and elbows to\nyour sides, while pushing your hands away from\nyou. Hold at the bottom before following the\nsame arcing motion pushing your hands away from\nyou back to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bent_over_db_row(self):
        
        pop = Popup(title='bent over dumbbell row',
                  content=Label(text='Set bench so it is flat. Place left\nhand on one end of the bench, left\nknee in the middle and your right foot\non the floor for balance. Allow your free\nright arm to hang in the open space\nwith a dumbbell in hand. Bending at the\nelbow, pull the dumbbell back towards the hips\nand behind the body. Hold then straighten your\narm, lowering it to the bottom again. Repeat\non the opposite side.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bent_over_barbell_row(self):
        
        pop = Popup(title='bent over barbell row',
                  content=Label(text='Stand in the starting position with your feet\nshoulder width apart. Squat down with your hips\nlower than your shoulders and your knees slightly\nbent, then grab the bar. Brace your torso\nand keep your back flat.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def vbar_seatedrow(self):
        
        pop = Popup(title='v-bar seatedrow',
                  content=Label(text='Sit on the pad with slight bend in\nknees and back straight making sure feet are\nplanted on the rests. From there take hold\nof the attatchment and pull in towards the\nbelly button, getting elbows as far behind the\nbody as possible. Keeping back straight, lower attatchment\nback to starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def wide_bar_seated_row(self):
        
        pop = Popup(title='wide bar seated row',
                  content=Label(text='Sit on the pad with slight bend in\nknees and back straight making sure feet are\nplanted on the rests. From there take hold\nof the attatchment and pull in towards the\nbelly button, getting elbows as far behind the\nbody as possible. Keeping back straight, lower attatchment\nback to starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def renegade_row(self):
        
        pop = Popup(title='renegade row',
                  content=Label(text='Place the dumbbells on the floor, positioned so\nthat when you set up in a plank\nposition. Inhale and shift your weight\nslightly to your left side so more of\nyour weight is supported by your left palm,\nSqueeze your right shoulder blade toward your spine and\ndraw the dumbbell held in your right hand toward\nyour chest, bending your elbow as you draw\nthe dumbbell toward you. Exhale as you lift\nthe dumbbell, then lower the dumbbell slowly\nto the floor.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bent_over_fly(self):
        
        pop = Popup(title='bent over fly',
                  content=Label(text='Hold dumbbells in each hand, stand with knees\nslightly bent. Exhale and lift both arms out\nto the side, maintaining a slight bend in\nthe elbows and squeezing your shoulder blades together.\nWith control, lower the dumbbells back toward the ground.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

#====================================================================================================================
#====================================================================================================================

















#====================================================================================================================
#Tricep
#====================================================================================================================
class Tricep(Screen):
    #tricep pushdowwn, rope tricep pushdown
    def profile(self):
#calling user profile
        uProfile()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def tricep_pushdown_bar(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Set cable to the highest setting. Take hold\nof the attatchment and step back until weight\ncomes off of the stack. Bring elbows tight into\nsides and keep them there for the whole exercise.\nPress attatchment down towards the ground, fully\nextending the arm. Pause, then while bending at the\nelbow return the attatchment to starting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/TricepPushdown.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/TricepPushdown.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Tricep Pushdown (Bar)',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def tricep_pushdown_rope(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Set cable to the highest setting. Take hold\nof the attatchment and step back until weight\ncomes off of the stack. Bring elbows tight into\nsides and keep them there for the whole exercise.\nPress attatchment down towards the ground, fully\nextending the arm. Pause, then while bending at the\nelbow return the attatchment to starting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/TricepPushdownRope.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/TricepPushdownRope.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Tricep Pushdown (Rope)',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def overhead_extention(self):
        
        pop = Popup(title='overhead extension',
                  content=Label(text='Stand with your feet staggered while holding a\ndumbbell directly overhead, with your palms facing each\nother and the weights touching. Without moving your\nupper arms, lower the weight behind your head.\n Then press up, returning to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ezbar_skullcrusher(self):
        
        pop = Popup(title='ezbar skullcrusher',
                  content=Label(text='Set bench so it is flat. Lay back\non the bench with arms straight and bar\nabove chest. Bending at the elbow, slowly drop\nthe bar back towards the top of your\nhead. Before hitting your head hold for a\nsecond then extend your arm fully back to\nstarting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def single_db_skullcrusher(self):
        
        pop = Popup(title='single dumbbell skullcrusher',
                  content=Label(text='Set bench so it is flat. Lay back\non the bench with arms straight and bar\nabove chest. Bending at the elbow, slowly drop\nthe bar back towards the top of your\nhead. Before hitting your head hold for a\nsecond then extend your arm fully back to\nstarting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def tricep_dip(self):
        
        pop = Popup(title='tricep dip',
                  content=Label(text='Place your hands behind you onto a chair,\nso that your fingers face forward. Extend your\nlegs and start bending your elbows. Lower your\nbody until your arms are at a 90-degree\nangle. Lift your body back up until your\narms are straight.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()







#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def overhead_extention_rope(self):
        
        pop = Popup(title='overhead extension rope',
                  content=Label(text='Inhale and lower the rope behind your head\nslowly as you bend your elbows and hold\nfor a second. Exhale and push the rope\nup by flexing your triceps and extending your\narms again, returning to the starting position', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def single_arm_tricep_extention(self):
        
        pop = Popup(title='single arm tricep extension',
                  content=Label(text='Set cable to the highest setting. Take hold\nof the attatchment and step back until weight\ncomes off of the stack. Bring elbow tight into\nside and keep it there for the whole exercise.\nPress attatchment down towards the ground, fully\nextending the arm. Pause, then while bending at the\nelbow return the attatchment to starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def vbar_tricep_extention(self):
        
        pop = Popup(title='v-bar tricep extension',
                  content=Label(text='Attatch a V-Bar to a high pulley and\ngrasp with an overhand grip. Stand tall with\nyour core braced, palms facing down,\nand a ninety degree angle at your elbows.\nKeep your upper arms stationary as you push\nthe bar down with an exhale. Push until\nyour elbows are fully extended and squeeze\nyour triceps.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bench_dips(self):
        
        pop = Popup(title='bench dips',
                  content=Label(text='Sit down on a bench, hands next to\nyour thighs. Walk your feet out and extend\nyour legs, lifting your bottom off the bench\nand holding there with extended arms. Hinging at\nthe elbow, lower your body down as far\nas you can go, or until your arms\nform a 90 degree angle.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

 

#====================================================================================================================
#====================================================================================================================





















#====================================================================================================================
#Bicep
#====================================================================================================================
class Bicep(Screen):
    #Bicep Curl, Hammer curl, Reversse curl, straight bar cable curl, zottman curl

    def profile(self):
#calling user profile
        uProfile()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bicep_curl(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'To do a biceps curl with a dumbbell,\nhold a dumbbell with your palm facing upward.\nSlowly curl the weight up by bending your\nelbow, keeping your elbow close to your body.\nThen slowly lower the weight to the starting\nposition. You will feel tension in the muscles\nin the front of your upper arm.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/BicepCurl.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/BicepCurl.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Bicep Curl',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def hammer_curl(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Bend at the elbow, lifting the lower arms\nto pull the weights toward the shoulders. Your\nupper arms are stationary and the wrists are\nin line with the forearms. Hold for one\nsecond at the top of the movement, then\nlower the weights to return to the\nstarting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/HammerCurl.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/HammerCurl.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Hammer Curl',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def straight_bar_cable_curl(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Set cable to lowest setting, Take attatchment in\nboth hands stepping back until weight comes off\nof stack. Keeping elbows tight to sides, bend\nat the elbow and bring the attachment up\nto your shoulders. Hold, then while keeping your\nelbows close to your sides, lower the weight\nback to starting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/StraightBarCableCurl.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/StraightBarCableCurl.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Straight Bar Cable Curl',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()









#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def zottman_curl(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Using a supinated grip, take a deep breath\nand curl the dumbbells towards your shoulders. Once\nthe biceps are fully shortened, rotate the forearms\nto a pronated position (palms down) and\nslowly lower the weight back to the\nstarting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/ZottmanCurl.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/ZottmanCurl.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Zottman Curl',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def incline_dbcurl(self):
        
        pop = Popup(title='incline dbcurl',
                  content=Label(text='Sit with your back flat against the bench,\nholding a dumbbell in each hand by your\nsides. Curl both dumbbells until your biceps fully\ncontract. Slowly lower the weights back to the\nstarting position and feel the stretch.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def rope_hammer_curl(self):
        
        pop = Popup(title='rope hammer curl',
                  content=Label(text='Set the rope to the lowest setting,\nbend at the elbow, lifting the lower arms\nto pull the rope toward the shoulders. Your\nupper arms are stationary and the wrists are\nin line with the forearms. Hold for one\nsecond at the top of the movement, then\nlower the rope to return to the\nstarting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()







#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def db_preacher_curl(self):
        
        pop = Popup(title='dumbbell preacher curl',
                  content=Label(text='Curl the dumbbell in towards your chin and\nupper chest in a single smooth arc. Hold\nfor a count of one while squeezing your\nbiceps. Lower the dumbbell by extending your arms\nback to the starting position. Repeat for the\ndesired number of repetitions then change to your\nother arm.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#====================================================================================================================
#====================================================================================================================
















#====================================================================================================================
#Shoulder
#====================================================================================================================
class Shoulder(Screen):

    def profile(self):
#calling user profile
        uProfile()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Shoulder press machine

    def shoulder_press(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Assume a seated position in the machine with\nthe handles set at roughly shoulder height. Grab\nthe handles with a pronated or neutral grip.\nInhale and press directly overhead. Slowly lower the\nhandles back to the starting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/ShoulderPress.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/ShoulderPress.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Shoulder Press',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()









#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def db_lateral_raise(self):
        
        pop = Popup(title='dumbbell lateral raise',
                  content=Label(text='Standing with a slight bend in your knees\nhold a dumbbell in each hand down by\nyour sides. Keeping a small bend in your\nelbows, raise the dumbbells out to your sides\nuntil your elbows are level with your shoulders.\nHold at the top before slowly lowering your\narms back to your sides.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def overhead_press(self):
        
        pop = Popup(title='overhead press',
                  content=Label(text='Standing with a slight bend in your knees,\ntake a slightly wider than shoulder width grip\non the barbell. Take the barbell off the\nrack and hold it just above your chest\nwith forearms facing the sky. Bring your head\nback slightly, press the bar above your head\nand push your head through the gap.\nHold before bringing your head back and lowering\nthe bar back to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()














#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def standing_db_press(self):
        
        pop = Popup(title='standing dumbbell press',
                  content=Label(text='Bend down with your knees to pick up\nthe dumbbells. Stand with your feet shoulder\nwidth apart and raise the dumbbells to shoulder\nheight. Once you have the correct stance, begin\npressing the dumbbells above your head until your\narms fully extend', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def facepull_rope(self):
        
        pop = Popup(title='facepull rope',
                  content=Label(text='Set the cable up to the highest setting.\nTake a hold of the attatchment and while\nkeeping your arms extended, step back until the\nweight comes off the stack. Drive your elbows\nback, pulling the attatchment towards your face keeping\nyour elbows as far apart as possible. Hold\nthen slowly return the attatchment to the\nstarting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def shoulder_taps(self):
        
        pop = Popup(title='shoulder taps',
                  content=Label(text='Get in a straight armplank position with shoulders stacked\nover wrists. Engage your core to stabilize your\nbody as you lift your right hand off\nthe ground and touch your left shoulder. Repeat \nyour left hand, making sure to keep\nyour hips stable.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def seated_lateral_raise(self):
        
        pop = Popup(title='seated lateral raise',
                  content=Label(text='Sit on a bench and hold a dumbbell in\neach hand by your side. Raise both dumbbells\nto your side until they are shoulder height. Lower\nunder control and repeat.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def seated_reverse_fly(self):
        
        pop = Popup(title='seated reverse fly',
                  content=Label(text='To do a reverse fly with dumbbells, sit with\nyour knees bent and hold a dumbbell in\neach hand. Lean forward, letting your arms hang\ndown next to your calves with your elbows\nslightly bent. Slowly raise the weights until your\nelbows are level with your shoulders.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

















#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def db_shoulder_press(self):
        
        pop = Popup(title='dumbbell shoulder press',
                  content=Label(text='Set bench so it is upright. With a\ndumbbell in each hand, bring them up to\nyour shoulders with your elbows forward at a\n45 degree angle and forearms facing the sky.\nPress the dumbbells up to the sky and\nabove head, fully extending your arms. Hold and\nslowly return the dumbbells to the starting position\nkeeping your forearms facing the sky.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def cable_upright_row(self):
        
        pop = Popup(title='cable upright row',
                  content=Label(text='Hold a cable bar with an overhand grip,\nresting on your thighs and shoulder width apart.\nFlex the elbows and pull the bar up\ntowards your chin, until the bar is in\nline with your collar bone. Lower the bar\nback down to your thighs and repeat.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





















#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def arm_circles(self):
        
        pop = Popup(title='arm circles',
                  content=Label(text='Stand with your feet shoulder-width apart\nand extend your arms parallel to the\nfloor. Circle your arms forward using small controlled\nmotions, gradually making the circles bigger until you\nfeel a stretch in your triceps. Reverse the\ndirection of the circles after about 10 seconds.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()

#====================================================================================================================
#====================================================================================================================


















#====================================================================================================================
#Trap
#====================================================================================================================
class Trap(Screen):
    def profile(self):
#calling user profile
        uProfile()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def db_shrug(self):
        
        pop = Popup(title='dumbbell shrug',
                  content=Label(text='Assume a standing position with the dumbbells on\nboth sides of your body. Hinge forward, inhale,\nand grab the dumbbells with a neutral grip.\nStand up tall and ensure your spine remains\nneutral. Contract the traps to elevate the shoulders', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()









#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def seated_db_shrug(self):
        
        pop = Popup(title='seated dumbbell shrug',
                  content=Label(text='Assume a steated position with the dumbbells on\nboth sides of your body. Hinge forward, inhale,\nand grab the dumbbells with a neutral grip.\nSit up tall and ensure your spine remains\nneutral. Contract the traps to elevate the shoulders.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def barbell_shrug(self):
        
        pop = Popup(title='barbell shrug',
                  content=Label(text='Stand tall, holding a bar in an overhand\ngrip with your hands just outside your\nthighs. Lift your shoulders straight up, hold for\none or two seconds in this elevated position,\nthen lower them back to the start.\nThroughout the exercise, make sure you keep your\nshoulders back and your spine and elbows straight.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#================================================================================================
#====================================================================================================================














#====================================================================================================================
#Forearm
#====================================================================================================================
class Forearm(Screen):

    def profile(self):
#calling user profile
        uProfile()









#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def wrist_curl(self):
        
        pop = Popup(title='wrist curl',
                  content=Label(text='Standing with a slight bend in your knees\nhold a dumbbell in each hand down by\nyour sides. Simultaneously while keeping your\narms straight curl the weight up using your wrists.\nHold at the top before slowly straightening your\nwrists out and lowering the weight.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def barbell_wrist_rollers(self):
        
        pop = Popup(title='barbell wrist rollers',
                  content=Label(text='With a wrist roller or a roller setup\non a barbell in a rack, rotate the\npipe or bar sleeve one direction until the\nweight reaches the top, then reverse to unroll\nit under control. Make sure you move the\nwrists through their complete range of \non each rotation.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#====================================================================================================================
#====================================================================================================================


















#====================================================================================================================
#Abs
#====================================================================================================================
class Abs(Screen):

    def profile(self):
#calling user profile
        uProfile()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Abdominal crunch machine

    def abdominal_crunch(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Sit with back against the pad. Set the\nchest pad so it rests against your chest.\nHook hands under the pad and squeeze your\ncore. Push forward following the path the pad\nwants to take. Hold at the bottom before\nslowly returning back up to the starting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/AbdominalCrunch.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/AbdominalCrunch.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Abdominal Crunch',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def plank(self):
        
        pop = Popup(title='plank',
                  content=Label(text='Lay on the ground face down. Place hands\neither side of your body flat on the\nground. Push up from the ground so just\nhands and toes are touching the ground. Maintain\na straight back while squeezing your core for\nas long as you can.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ab_crunch(self):
        
        pop = Popup(title='ab crunch',
                  content=Label(text='Keep your knees comfortably apart. Fold your arms\non your chest and tighten your abdominal muscles.\nRaise your head and shoulders off of the\nfloor. Hold for three deep breaths, then return\nto starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()







#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def sit_up(self):
        
        pop = Popup(title='sit up',
                  content=Label(text='Lie down on your back, with your feet\non the floor, knees bent. Place your\nhands on either side of your head\nin a comfortable position. Bend your hips and\nwaist to raise your body off the ground.\nLower your body back to the ground into\nthe starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def abdominal_air_bike(self):
        
        pop = Popup(title='abdominal air bike',
                  content=Label(text='Lay supine in a relaxed position with your\narms behind your head and legs straight. Exhale\nas you raise one knee towards your face\nwhile driving the opposite elbow to the knee.\nOnce your abs are fully contracted, slowly lower\nyourself back to the starting position and repeat\non the opposite side.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def hanging_knee_raises(self):
        
        pop = Popup(title='hanging knee raises',
                  content=Label(text='Start by hanging on a pull-up bar. Keep\nyour body straight and use an overhand grip.\nEngage your core as you raise knees toward\nchest. Stop when thighs are parallel to the\nfloor. Lower your legs slowly, returning to the\nstarting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()









#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def laying_floor_knee_tuck(self):
        
        pop = Popup(title='laying floor knee tuck',
                  content=Label(text='Raise the knees toward your forehead while contracting\nyour abdominals and exhaling. Once your abs are\nfully contracted and your knees are slightly\nabove parallel, slowly lower your legs back\nto the starting position. Complete for the assigned\nnumber of repetitions.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#====================================================================================================================
#====================================================================================================================























#====================================================================================================================
#Quads
#====================================================================================================================
class Quads(Screen):


    def profile(self):
#calling user profile
        uProfile()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bulgarian_split_squat(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Stand facing away from the bench, holding a\nbarbell across your upper back. Have one leg\nresting on the bench behind you, laces down.\nSquat with your standing leg until the knee\nof your trailing leg almost touches the floor.\nPush up through your front foot to return\nto the start position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/BulgarianSplitSquat.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/BulgarianSplitSquat.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Bulgarian Split Squat',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def low_bar_back_squat(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Pin the barbell tightly against the shelf of your\nmid back, just below your shoulder muscles. Establish\na stable tripod foot then from there generate\nexternal rotation torque at the hips. Create a\nrigid trunk by taking a big breath and\nholding it tight, remain balanced by keeping the\nbar over the mid foot during the entire\nsquat. Finally use hip drive to stand up\nfrom the bottom position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/LowBarBackSquat.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/LowBarBackSquat.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Low Bar Back Squat',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def lunges(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Bend the knees and lower your body until\nthe back knee is a few inches from\nthe floor. At the bottom of the movement,\nthe front thigh is parallel to the ground,\nthe back knee points toward the floor, and\nyour weight is evenly distributed between both legs.\nPush back up to the starting position, keeping\nyour weight on the heel of the\nfront foot.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/Lunges.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/Lunges.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Lunges',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def seated_leg_extention(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Adjust the seat so that the knees are\ndirectly in line with the axis of the\nmachine. Sit down and position both shins behind\nthe pad at the base of the machine.\nTake a deep breath and extend your leg\nas you flex your quad. As you lock\nout the knee, exhale to complete the repetition.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/SeatedLegExtention.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/SeatedLegExtention.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Seated Leg Extension',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def walking_lunges(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Step forward with your right leg, putting your\nweight into your heel. As your right foot\nstrikes the floor and stabilizes, bend the right\nknee, lowering down parallel to the floor into\na lunge position. Without moving the right leg,\nmove your left foot forward, repeating the same\nmovement on the left leg.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/WalkingLunges.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/WalkingLunges.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Walking Lunges',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def high_bar_back_squat(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Pin the barbell tightly against the shelf of\nyour upper back. Establish a stable tripod foot\nand generate external rotation torque at the hips,\nfrom there create a rigid trunk by taking\na big breath and holding it tight and\nhip hinge to engage the posterior chain. Remain balanced\nby keeping the bar over the mid foot\nduring the entire squat and use hip drive\nto stand up from the bottom position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/HighBarBackSquat.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/HighBarBackSquat.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='High Bar Back Squat',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()









#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def db_goblet_squat(self):
        
        pop = Popup(title='dumbbell goblet squat',
                  content=Label(text='Stand with your feet hip or shoulder-width apart,\ntoes pointed straight ahead. Sit your hips\nback and bend your knees to lower\nyourself into a squat. Drive through the feet\nas you stand and squeeze your glutes as\nyou return to a tall standing position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def db_squat(self):
        
        pop = Popup(title='dumbbell squat',
                  content=Label(text='Stand with your feet hip to shoulder-width apart, holding\na pair of dumbbells at arms length by your sides.\nKeeping your back flat and core braced, push your\nhips back, bend your knees, and lower your\nbody until your thighs are parallel to the\nfloor. Pause, then push yourself back up to\nthe starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def body_weight_squat(self):
        
        pop = Popup(title='body weight squat',
                  content=Label(text='Stand with your hands on the back of\nyour head and your feet shoulder-width\napart with your feet turned out slightly\nto open the hip joint. Lower your body\nuntil your thighs are parallel to the floor.\nPause, then return to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def kettlebell_squat(self):
        
        pop = Popup(title='kettlebell squat',
                  content=Label(text='Stand with your feet wider than hip width\napart and the kettlebell in between your feet.\nSquat down, placing both hands around the kettlebell\nhandle and then drive through your glutes to return\nto a standing position. Keep in this position to\nsquat, keeping your chest up and your back straight.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def single_leg_seated_extention(self):
        
        pop = Popup(title='Single Leg Seated Extension',
                  content=Label(text='Adjust the seat so that the knees are\ndirectly in line with the axis of\nthe machine. Sit down and position one\nshin behind the pad at the base of\nthe machine. Take a deep breath and extend\nyour leg as you flex your quadricep. As\nyou lock out the knee, exhale to complete the repetition.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()







#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def adductor(self):
        
        pop = Popup(title='adductor',
                  content=Label(text='Setup in an upright position with your back\nagainst the pad and your spine neutral. Exhale\nand pull the legs together as you squeeze\nthe pads inward. Once the pads touch, slowly\nreturn to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#====================================================================================================================
#====================================================================================================================
















#====================================================================================================================
#Hamstrings
#====================================================================================================================
class Hamstrings(Screen):

    def profile(self):
#calling user profile
        uProfile()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def seated_leg_curl(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'To keep tension on the hamstrings, keep the\nknees just shy of lockout. Do not allow\nthe back to arch, keep your hips pressed\ninto the pad. Keep your lower back flat\nagainst the pad throughout the movement.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/SeatedLegCurl.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/SeatedLegCurl.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Seated Leg Curl',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()







#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def romanian_deadlift(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Hold your weight (dumbbells or a barbell)\nin front of your thighs, and lower to\nthe ground by pushing your hips back. As\nyou lower the weight, keep your shoulder blades\ndrawn towards each other and your chest open\nand wide. When the weight is below your\nknees, thrust your hips forward and return to\nthe starting position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/RomanianDeadlift.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/RomanianDeadlift.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Romanian Deadlift',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def db_stiff_deadlift(self):
        
        pop = Popup(title='Dumbbell Stiff Deadlift',
                  content=Label(text='Stand upright and grab two dumbbells with an\noverhand grip and pick them up with arms\nfully extended and in front of your body. Inhale\nand lower your body by bending forward\nwhile maintaining a flat back and straight legs.\nContinue bending forward with a flat back until\nthe dumbbells pass your knees.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def single_seated_leg_curl(self):
        
        pop = Popup(title='single seated leg curl',
                  content=Label(text='To keep tension on the hamstrings, keep the\nknees just shy of lockout. Do not allow\nthe back to arch, keep your hips pressed\ninto the pad. Keep your lower back flat\nagainst the pad throughout the movement.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#====================================================================================================================
#====================================================================================================================



















#====================================================================================================================
#Calfs
#====================================================================================================================
class Calfs(Screen):

    def profile(self):
#calling user profile
        uProfile()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def calf_raises(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'To do a calf raise with dumbbells,\nhold a dumbbell in each hand and stand\nwith your feet about shoulder-width apart.\nLet your arms hang straight below your shoulders.\nRise up onto your toes, then slowly\nreturn to the starting position. You will feel\ntension in the muscles in the back of your lower legs.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/CalfRaises.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/CalfRaises.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Calf Raises',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()











#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def seated_calf_raises(self):
        
        pop = Popup(title='Seated Calf Raises',
                  content=Label(text='Sitting up tall in your chair, with your\nfeet hip width apart. Bring your \nback, so your heels are behind your knees.\nFrom this position, lifting your heels up off\nthe floor, coming up onto your\ntoes. Hold briefly and gently lower your heels back down.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def standing_barbell_calf_raises(self):
        
        pop = Popup(title='Standing Barbell Calf Raise',
                  content=Label(text='Stand tall and support a barbell on your\nupper back, with your toes facing forward. Raise\nboth heels and contract the calves on each of your legs.\nSlowly return to starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#====================================================================================================================
#====================================================================================================================

















#====================================================================================================================
#Glutes
#====================================================================================================================

class Glutes(Screen):

    def profile(self):
#calling user profile
        uProfile()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def barbell_hip_thrusts(self):
        
        pop = Popup(title='barbell hip thrusts',
                  content=Label(text='Sit on the floor, get the bar close\nand put the barbell pad on. Set yourself\nup so the mid part of your back is\nresting on the box or bench, then straighten\nyour legs and roll the bar over your\nfeet until it is over your hips. Walk\nyour feet in so they are resting flat\non the floor. Drive through your feet to\nlift your hips and the barbell until\nyour torso and thighs are parallel to the\nfloor. Lower the bar under control.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def glute_kick_back(self):
        
        pop = Popup(title='glute kick back',
                  content=Label(text='Attatch an ankle strap to a cable machine,\nthen loop it around ankle. Squeeze glute to\nactivate the muscle, then lift leg attatched\nto the machine back behind body with control.\nPause at the top of the movement,\nthen lower back to the starting position slow\nand with control.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()













#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def abductor(self):
        
        pop = Popup(title='abductor',
                  content=Label(text='Setup in an upright position with your back\nagainst the pad and your spine neutral. Exhale\nand push the legs apart as you open\nthe pads. Once your hips are fully externally\nrotated, slowly return to the starting position.', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def glute_bridge(self):
        
        pop = Popup(title='glute bridge',
                  content=Label(text='With your feet flat to the ground and\nspread hip-width apart, drop your glutes slowly\ntoward the ground. Lift your hips back up\nslowly and squeeze the muscles at the\ntop of the movement', halign = 'center'),
                  size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#====================================================================================================================
#====================================================================================================================

















#====================================================================================================================
#====================================================================================================================

class Hiit(Screen):

    def profile(self):
#calling user profile
        uProfile()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def pulsing_jump_squat(self):
    
        pop = Popup(title='Pulsing Jump Squat',
                content=Label(text='The movement is the same as a regular body\nweight squat hovever at the bottom you bounce then\njump as high as you can. Make sure to always\nland on both feet', halign = 'center'),
                size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
    




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def frog_jump(self):
    
        pop = Popup(title='frog jump',
                content=Label(text='The movement is similar to a pulsing jump sqaut\nhowever at the bottom you dont bounce. Your\ngoal is to lower and drive up with force in one fluid\nmotion. Make sure you land on both feet.', halign = 'center'),
                size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
        





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def vertical_jump(self):
    
        pop = Popup(title='vertical jump',
                content=Label(text='Bend your knees slightly and drive and jump as high as\nyou can. It is important to remember that this is not\na squat, you should only bend your knees slightly.\nMake sure to land on both feet.', halign = 'center'),
                size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
    








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def high_knees(self):
    
        pop = Popup(title='high knees',
                content=Label(text='Raise one knee to around waist height and alternate\nknees. You want to perform this at a reletive fast pace', halign = 'center'),
                size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()








#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def lunge_jumps(self):
    
        pop = Popup(title='lunge jumps',
                content=Label(text='You want to lunge down and from there\njump and switch legs in one fluid motion.\nHowever if this is too difficult just break\nthe exercise down. Simply do a lunge, stand up,\njump, then switch legs.', halign = 'center'),
                size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
    







#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def mountain_climbers(self):
    
        pop = Popup(title='mountain climbers',
                content=Label(text='Get into a straight arm plank position and\nfrom there drive your right knee to your\nleft shoulder then switch and drive your left knee\nto your right shoulder. It is importand to remember\nalthough your goal is to reach you shoulder,\nyou should not be making contact with it.', halign = 'center'),
                size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
        










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def burpees(self):
    
        pop = Popup(title='burpees',
                content=Label(text='Start standing, get down into a straight arm plank\nposition, perform a push up, then get back\nto your feet and jump. A burpee can me\nmodified in many ways, if it is too difficult\nyou can take out the pushup, if its too\neasy increase the tempo or even change the pushup\nto a clap push up.', halign = 'center'),
                size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
    










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def jumping_jacks(self):
    
        pop = Popup(title='jumping jacks',
                content=Label(text='Stand upright with your legs together, arms at\nyour sides. Bend your knees slightly, and jump into\nthe air. As you jump, spread your legs\nto be about shoulder width apart. Stretch your\narms out and over your head and then jump\nback to starting position.', halign = 'center'),
                size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()










#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def russian_twists(self):
    
        pop = Popup(title='russian twists',
                content=Label(text='Lie down with your legs bent at the\nknees, elevate your upper body so that it\ncreates a V shape with your thighs. Twist\nyour torso to the right, and then reverse\nthe motion, twisting it to the left.', halign = 'center'),
                size_hint=(None, None), size=(400, 300),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()


#=========================================================================================================================
#=========================================================================================================================

































#====================================================================================================================
#Compound
#====================================================================================================================
class Compound(Screen):


    def profile(self):
#calling user profile
        uProfile()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def conventional_deadlift(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Push the hips back and hinge forward, grasp\nthe bar, pull up slightly, set the lats,\ndrive through the whole foot, push the floor\naway, lock out the hips, return the bar\nto the floor, reset, and repeat for desired\nnumber of repetitions.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/ConventionalDeadlift.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                      image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/ConventionalDeadlift.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Conventional Deadlift',
                  content= box,          
                  size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()






#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bench_press(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'To execute the bench press first, lie on your\nback on the bench and grip the bar around shoulder\nwidth. From there press your firmly into the ground and\nmake sure that your hips are always on the bench.\nSlowly lift the bar of the rack and lower the bar to\nyour chest(Just above your sternum) allowing your\nelbows to bend out to the side at 45 degrees.\nStop lowering when your elbows are just below the\nbench, press feet into the floor and push\nthe bar back up. Remember to always warm up\nto prevent injury and have a spotter when you can.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/BenchPress.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                      image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/BenchPress.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Bench Press',
                  content= box,          
                  size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def close_bench_press(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'To execute the close grip bench press first, lie on your\nback on the bench and grip the bar around shoulder\nwidth. From there press your firmly into the ground and\nmake sure that your hips are always on the bench.\nSlowly lift the bar of the rack and lower the bar to\nyour chest(Just above your sternum) allowing your\nelbows to bend out to the side at 45 degrees.\nStop lowering when your elbows are just below the\nbench, press feet into the floor and push\nthe bar back up. Remember to always warm up\nto prevent injury and have a spotter when you can.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/CloseGripBenchPress.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                      image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/CloseGripBenchPress.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Close Grip Bench Press',
                  content= box,          
                  size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()




#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def high_bar_back_squat(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Pin the barbell tightly against the shelf of\nyour upper back. Establish a stable tripod foot\nand Generate external rotation torque at the hips\nfrom there Create a rigid trunk by taking\na big breath and holding it tight and\nhip hinge to engage the posterior chain. Remain balanced\nby keeping the bar over the mid foot\nduring the entire squat and use hip drive\nto stand up from the bottom position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/HighBarBackSquat.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/HighBarBackSquat.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='High Bar Back Squat',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is the popup for the exercise tutorial, 
#some have a video and description some only have a description 
#all of them are formatted in the same way 
#the size is smaller if there is no video
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def low_bar_back_squat(self):
        box = FloatLayout()
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.25}, text = 'Pin the barbell tightly against the shelf of your\nmid back, just below your shoulder muscles. Establish\na stable tripod foot then from there generate\nexternal rotation torque at the hips. Create a\nrigid trunk by taking a big breath and\nholding it tight, Remain balanced by keeping the\nbar over the mid foot during the entire\nsquat, Finaly use hip drive to stand up\nfrom the bottom position.', halign = 'center'))     
        box.add_widget(VideoPlayer(pos_hint = {'x': 0, 'center_y': 0.8},source = 'Vids/LowBarBackSquat.mov', row_default_height = 2,
                                    allow_fullscreen = False , image_pause = 'Graphics/pause.png', image_play = 'Graphics/play.png',
                                        image_stop = 'Graphics/stop.png', image_volumemuted = 'Graphics/mute.png', image_volumehigh ='Graphics/volhigh.png',
                                        image_volumelow = 'Graphics/vollow.png', image_volumemedium = 'Graphics/volmed.png', thumbnail = 'Vids/LowBarBackSquat.jpg', state = 'play', height = 0, size_hint_y = .6))
        pop = Popup(title='Low Bar Back Squat',
                    content= box,          
                    size_hint=(None, None), size=(400, 550),
                  separator_color = (126/255, 28/255, 19/255, 1))

        pop.open()
#====================================================================================================================
#====================================================================================================================














#====================================================================================================================
#this takes the user to the pts website where they can book a pt session
#====================================================================================================================

class PtSession(Screen):
    pass
#====================================================================================================================
#====================================================================================================================















#=============================================================================================
#the home screen is what will be holding all of the buttons/options mentiond before
#progress, pt session, training plans, and exercise tutorial
#this will also have a carousell of the featured training plans and options
#the home screen will also have a tool/task bar that will have the home button, profile button and menue button
#====================================================================================================================
class HomeScreen(Screen):
    
    def profile(self):

        uProfile()



    def img(self):
        #Carousell of avalible plans
        if self.ids.topcaro == self.picOne:
            self.ids.caro.source = 'graphics/caro1.png'

        elif self.ids.topcaro == self.picTwo:
            self.ids.caro.source = 'graphics/caro2.png'

        elif self.ids.topcaro == self.picThree:
            self.ids.caro.source = 'graphics/caro3.png'

        elif self.ids.topcaro == self.picFour:
            self.ids.caro.source = 'graphics/caro4.png'



#Link to take them to the website
    def link(self):
        webbrowser.open('https://www.mattgibsonpt.com/')

#====================================================================================================================
#====================================================================================================================
















#====================================================================================================================
#Account Information 
#====================================================================================================================
class AccountInfo(Screen):
    pass
#====================================================================================================================
#====================================================================================================================

















#====================================================================================================================
#Window Manager
#====================================================================================================================
class WindowManager(ScreenManager):
    pass

#====================================================================================================================















#Validation pop up for an invalid login

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 200),
                  separator_color = (126/255, 28/255, 19/255, 1))
    pop.open()


#Validation pop up for an invalid form
def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 200),
                  separator_color = (126/255, 28/255, 19/255, 1))

    pop.open()


#Validation pop up for a invalid input
def invalidSelection():
    pop = Popup(title='Invalid input',
                  content=Label(text='Please fill in all questions with valid information.'),
                  size_hint=(None, None), size=(400, 200),
                  separator_color = (126/255, 28/255, 19/255, 1))

    pop.open()


#Validation pop up for the email allredy being linked to an account
def usedEmail():
    pop = Popup(title='Used Email',
            content=Label(text='Email is allready linked to an account.'),
            size_hint=(None, None), size=(400, 200),
            separator_color = (126/255, 28/255, 19/255, 1))

    pop.open()
 

#Validation pop up for username allredy being linked to an account
def usedUsename():
    pop = Popup(title='Used Username',
            content=Label(text='Usename is allready linked to another account.'),
            size_hint=(None, None), size=(400, 200),
                  separator_color = (126/255, 28/255, 19/255, 1))

    pop.open()

#Validation pop up for wrong formatt for feet
def ft():
    pop = Popup(title='Invalid Input',
            content=Label(text='If you are entering your height in ft then please use the format "6.3" or "5.11"for example.'),
            size_hint=(None, None), size=(400, 200),
            separator_color = (126/255, 28/255, 19/255, 1))

    pop.open()

















global uProfile
def uProfile():
#This is the users profile





#Pulling the information from the database and using it in the pop up
    cur = conn.cursor()
    cur.execute("SELECT * FROM UserIfo WHERE Email =? ", [em])
    rows = cur.fetchall()

    box = FloatLayout()

    for row in rows:
        box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.95}, text = row[0]))
        box.add_widget(Label(pos_hint = {'x': -0.1, 'center_y': 0.87}, text = row[1]))
        box.add_widget(Label(pos_hint = {'x': -0.1, 'center_y': 0.8}, text = row[2]))
        box.add_widget(Label(pos_hint = {'x': 0.08, 'center_y': 0.73}, text = row[3]))
        box.add_widget(Label(pos_hint = {'x': -0.37, 'center_y': 0.57}, text = row[5]))
        box.add_widget(Label(pos_hint = {'x': -0.12, 'center_y': 0.57}, text = str(row[6])))
        box.add_widget(Label(pos_hint = {'x': 0.35, 'center_y': 0.57}, text = str(row[16])))
        box.add_widget(Label(pos_hint = {'x': 0.42, 'center_y': 0.57}, text = str(row[17])))
        box.add_widget(Label(pos_hint = {'x': 0.11, 'center_y': 0.57}, text = str(row[18])))
        box.add_widget(Label(pos_hint = {'x': 0.18, 'center_y': 0.57}, text = str(row[19])))


#Images to go along with the information
    box.add_widget(Image(pos_hint = {'x': 0, 'center_y': 0.87}, size_hint = {0.3, 0.1}, source = 'graphics/forename.png'))
    box.add_widget(Image(pos_hint = {'x': 0, 'center_y': 0.8}, size_hint = {0.3, 0.1}, source = 'graphics/surename.png'))
    box.add_widget(Image(pos_hint = {'x': 0, 'center_y': 0.73}, size_hint = {0.3, 0.1}, source = 'graphics/email.png'))
    box.add_widget(Image(pos_hint = {'x': 0, 'center_y': 0.65}, size_hint = {0.25, 0.1}, source = 'graphics/gender.png'))
    box.add_widget(Image(pos_hint = {'x': 0.25, 'center_y': 0.65}, size_hint = {0.25, 0.1}, source = 'graphics/age.png'))
    box.add_widget(Image(pos_hint = {'x': 0.5, 'center_y': 0.65}, size_hint = {0.25, 0.1}, source = 'graphics/weightt.png'))
    box.add_widget(Image(pos_hint = {'x': 0.75, 'center_y': 0.65}, size_hint = {0.25, 0.1}, source = 'graphics/heightt.png'))
    box.add_widget(Image(pos_hint = {'x': 0, 'center_y': 0.45}, size_hint = {0.3, 0.1}, source = 'graphics/calories.png'))
    box.add_widget(Label(pos_hint = {'x': - 0.35, 'center_y': 0.37}, text=(str(row[20]) + ' Kcals')))
    box.add_widget(Label(pos_hint = {'x': 0, 'center_y': 0.05}, text=('Train Hard, Train Smart, Train Right'), bold = True, size_hint = (1, 1)))
    

#Main part of pop up
    pop = Popup(title='Profile',
                content= box,          
                size_hint=(None, None), size=(400, 550),
                separator_color = (126/255, 28/255, 19/255, 1))

    pop.open()


#====================================================================================================================
#====================================================================================================================













#====================================================================================================================
#Main Code To Run Application
#====================================================================================================================

kv = Builder.load_file("my.kv")

sm = WindowManager()



#list of avalible windows 
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), Questions1(name ="q1"), Questions2(name ="q2"), Questions3(name ="q3")
           , Questions4(name ="q4"), Questions5(name ="q5"), HomeScreen(name="home"), TrainingPlans(name="plans"), ExerciseTutorial(name="tutorial"), Progress(name="progress")
           , PtSession(name="session"), Settings(name="settings"), Accountinfo(name="profile"), Gymplan(name="Gplan"), Homeplan(name="Hplan"), Chest(name="chest"), Back(name="back")
           , Tricep(name="tricep"), Bicep(name="bicep"), Shoulder(name="shoulder"), Trap(name="trap"), Forearm(name="forearm"), Abs(name="abs"), Quads(name="quads"), Hamstrings(name="hamstrings")
           , Calfs(name="calfs"), Glutes(name="glutes"), Compound(name="compound"), Hiit(name="hiit")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def load_screen(self, new_screen_name):
        self.root.ids.screen_manager_id.current = new_screen_name

    def build(self):
        
        return sm
        


if __name__ == "__main__":
    MyMainApp().run()
#====================================================================================================================
#====================================================================================================================