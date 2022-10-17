# This is a API based CoWin Availability application which will help us to find available vaccine on a particular date on your available area via Pincode

## Importing modules
from cgitb import text
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import pytz
import requests

software_version = 'v1.1'
IST = pytz.timezone('Asia/Kolkata')

# Here whatever we want to our app to function  must be written into Tk() and mainloop() 
app = Tk()

# App Geometry and components
app.geometry("700x480+600+300")
app.title(f"Vaccine Availability Checker  {software_version}")
app.iconbitmap(r"C:\Users\Asus\Downloads\covid-vaccine.ico")
app.resizable(False, False)
backcolor = "#0e344a"
app.config(background = backcolor)

## DEFAULT values
PINCODE = '110096'

# Color value reference
top_left_frame_bg  = "#2e4c58"
down_left_frame_bg = '#69ad5c'

## Frame details
frame1 = Frame(app, height = 100, width=180, bg= top_left_frame_bg, bd=1, relief = FLAT)
frame1.place(x=0,y=0)

frame2 = Frame(app, height = 520, width=180, bg= down_left_frame_bg, bd=1, relief = FLAT)
frame2.place(x=0,y=100)

frame3 = Frame(app, height = 100, width=700, bg= '#bcdcb4', bd=1, relief = RAISED)
frame3.place(x=180,y=0)

## Labels defined

label_today = Label(text="Today",bg=top_left_frame_bg, font='Opensans 10 bold')
label_today.place(x=20, y=10)

label_date_now = Label(text="Date", bg = top_left_frame_bg, font = 'Opensans 10 bold')
label_date_now.place(x=20, y=30)

label_time_now = Label(text="Time", bg = top_left_frame_bg, font = 'Opensans 10 bold')
label_time_now.place(x=20, y=50)

label_pincode = Label(text="Pincode", bg = '#bcdcb4', font = 'Opensans 10 bold')
label_pincode.place(x=220, y=15)

label_date = Label(text="Date", bg = '#bcdcb4', font = 'Opensans 10 bold')
label_date.place(x=380, y=15)

label_dateformat = Label(text="[dd-mm-yyyy]", bg = '#bcdcb4', font = 'Opensans 7')
label_dateformat.place(x=417, y=17)

label_head_result = Label(text="  Status  |      Centre-Name\t      | Age-Group |   Vaccine   | Dose_1 | Dose_2 |   Total  ", bg = 'black', fg='white', font = 'Opensans 10 bold')
label_head_result.place(x=180, y=99)

label_instructions = Label(text="Safety Instructions:", bg=down_left_frame_bg, font='Opensans 12 bold')
label_instructions.place(x=8,y=110)

label_instruct = Label(text="1. Get yourself vaccinated", bg = down_left_frame_bg, font='Opensans 9')
label_instruct.place(x=8, y=150)

label_instruct = Label(text="2. Follow distance norms", bg = down_left_frame_bg, font='Opensans 9')
label_instruct.place(x=8, y=170)

label_instruct = Label(text="3. Wash your hands frequently", bg = down_left_frame_bg, font='Opensans 9')
label_instruct.place(x=8, y=190)

label_instruct = Label(text="4. Avoid handshakes", bg = down_left_frame_bg, font='Opensans 9')
label_instruct.place(x=8, y=210)

label_instruct = Label(text="5. Isolation on observing", bg = down_left_frame_bg, font='Opensans 9')
label_instruct.place(x=8, y=230)

label_instruct = Label(text="symptoms", bg = down_left_frame_bg, font='Opensans 9')
label_instruct.place(x=21, y=245)

## Entry boxes
pincode_text_var = StringVar()
pincode_textbox = Entry(app,width = 11, bg = '#eaf2ae', fg= 'black', textvariable = pincode_text_var, font='verdana 10')
pincode_textbox['textvariable'] = pincode_text_var
pincode_textbox.place(x= 220, y=40)

date_text_var = StringVar()
date_textbox = Entry(app,width = 12, bg = '#eaf2ae', fg= 'black', textvariable = date_text_var, font='verdana 10')
date_textbox['textvariable'] = date_text_var
date_textbox.place(x= 380, y=40)


## TEXT BOX - for RESULTs
result_box_avl = Text(app, height = 20, width = 8, bg=backcolor,fg='#ecfcff', relief=FLAT, font='Opensans 8')
result_box_avl.place(x= 190 , y= 121)

result_box_cent = Text(app, height = 20, width = 30, bg=backcolor,fg='#ecfcff', relief=FLAT, font='Opensans 8')
result_box_cent.place(x= 245 , y= 121)

result_box_age = Text(app, height = 20, width = 8, bg=backcolor,fg='#ecfcff', relief=FLAT, font='Opensans 8')
result_box_age.place(x= 395 , y= 121)

result_box_vacc = Text(app, height = 20, width = 10, bg=backcolor,fg='#ecfcff', relief=FLAT, font='Opensans 8')
result_box_vacc.place(x= 456 , y= 121)

result_box_D1 = Text(app, height = 20, width = 7, bg=backcolor,fg='#ecfcff', relief=FLAT, font='Opensans 10')
result_box_D1.place(x= 536 , y= 121)

result_box_D2 = Text(app, height = 20, width = 7, bg=backcolor,fg='#ecfcff', relief=FLAT, font='Opensans 10')
result_box_D2.place(x= 590 , y= 121)

result_box_D1_D2 = Text(app, height = 20, width = 7, bg=backcolor,fg='#ecfcff', relief=FLAT, font='Opensans 10')
result_box_D1_D2.place(x= 660 , y= 121)


## Defining Functions


# Detect Automatic Pincode
def fill_pincode_with_radio():
    curr_pincode = get_pincode_ip_service(url)
    pincode_text_var.set(curr_pincode)

url = 'https://ipinfo.io/postal'
def get_pincode_ip_service(url):
    response_pincode = requests.get(url).text
    return response_pincode

# Clock function for updating contiuation date and time every second
def update_clock():
    raw_TS = datetime.now(IST)
    date_now = raw_TS.strftime("%d %b %Y")
    time_now = raw_TS.strftime("%H:%M:%S")
    formatted_now = raw_TS.strftime("%d-%m-%Y")
    label_date_now.config(text = date_now)
    # label_date_now.after(500, update_clock)
    label_time_now.config(text = time_now)
    label_time_now.after(1000, update_clock)
    return formatted_now

def insert_today_date():
    formatted_now = update_clock()
    date_text_var.set(formatted_now)
    tomorrow_date_chkbox['state'] = DISABLED

def refresh_api_call(PINCODE, DATE):
    header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
    request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={PINCODE}&date={DATE}"
    response = requests.get(request_link, headers = header)
    resp_JSON = response.json()
    return resp_JSON

def clear_result_box():
    result_box_avl.delete('1.0', END)
    result_box_cent.delete('1.0', END)
    result_box_age.delete('1.0', END)
    result_box_vacc.delete('1.0', END)
    result_box_D1.delete('1.0', END)
    result_box_D2.delete('1.0', END)
    result_box_D1_D2.delete('1.0', END)

def search_vaccine_avl():
    clear_result_box()
    PINCODE = pincode_text_var.get().strip()
    DATE = date_text_var.get()
    resp_JSON = refresh_api_call(PINCODE, DATE)

    try:
        if len(resp_JSON['sessions']) == 0:
            messagebox.showinfo("INFO","Vaccine not yet arrived for the given date")

        for sess in resp_JSON['sessions']:
            age_limit           = sess['min_age_limit']
            center_name         = sess['name']
            pincode             = sess['pincode']
            vaccine_name        = sess['vaccine']
            available_capacity  = sess['available_capacity']
            qnty_dose_1         = sess['available_capacity_dose1']
            qnty_dose_2         = sess['available_capacity_dose2']
            slot_date           = sess['date']

            if available_capacity > 0:
                curr_status = 'Available'
            else:
                curr_status = 'NA'
            
            if age_limit == 45:
                age_grp = '45+'
            else:
                age_grp = '18-44'

            result_box_avl.insert(END, f"{curr_status:^6s}")
            result_box_avl.insert(END,"\n")
            result_box_cent.insert(END, f"{center_name:<30.29s}")
            result_box_cent.insert(END,"\n")
            result_box_age.insert(END, f"{age_grp:<6s}")
            result_box_age.insert(END,"\n")
            result_box_vacc.insert(END, f"{vaccine_name:<8s}")
            result_box_vacc.insert(END,"\n")
            result_box_D1.insert(END, f"{qnty_dose_1:>5}")
            result_box_D1.insert(END,"\n")
            result_box_D2.insert(END, f"{qnty_dose_2:>5}")
            result_box_D2.insert(END,"\n")
            result_box_D1_D2.insert(END, f"{available_capacity:<5}")
            result_box_D1_D2.insert(END,"\n")

    except KeyError as KE:
        messagebox.showerror("ERROR","No Available center(s) for the given Pincode and date")
        print (pincode_text_var.get())

## Buttons

search_vaccine_image = PhotoImage(file= r"C:\Users\Asus\Downloads\searching1.png")
search_vaccine_btn = Button(app, image=search_vaccine_image, bg= down_left_frame_bg, command = search_vaccine_avl,  relief= RAISED)
#search_vaccine_avl, relief= RAISED)
search_vaccine_btn.place(x = 630,y = 30)

# Radio Button
curr_loc_var = StringVar()
radio_location = Radiobutton(app, text="Current location", bg= '#bcdcb4', variable= curr_loc_var, value = curr_loc_var, command = fill_pincode_with_radio) #state=DISABLED
radio_location.place(x=214, y=63)

# Check Box 
chkbox_today_var = IntVar()
today_date_chkbox = Checkbutton(app, text='Today', bg= '#bcdcb4', variable=chkbox_today_var, onvalue= 1, offvalue=0, command = insert_today_date)
today_date_chkbox.place(x= 375, y= 63)

chkbox_tomorrow_var = IntVar()
tomorrow_date_chkbox = Checkbutton(app, text='Tomorrow', bg= '#bcdcb4', variable=chkbox_tomorrow_var, onvalue= 1, offvalue=0, state = DISABLED)
tomorrow_date_chkbox.place(x= 435, y= 63)

update_clock()

app.mainloop()
# This is end now if we write any code below will not function into our applications
