from tkinter import *
from  configparser import ConfigParser
from tkinter import  messagebox
import requests

url_api = "enter api key"

api_file = 'weather.key'
file_a = ConfigParser()
file_a.read(api_file)
api_key = file_a['api_key']['key'] #in the format of json file

def weather_find(city):
    final = requests.get(url_api.format(city,api_key))
    if final :
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        # Convert Kelvin to Fahrenheit
        k_temperature = json_file["main"]['temp']
        c_temperature = k_temperature - 273.15
        f_temperature = (k_temperature-273.15)*9/5+32
        weather_display = json_file['weather'][0]['main']
        result = (city,country_name,c_temperature,f_temperature,weather_display)
        return result
    else:
        return None

def print_weather():
    city = search_city.get()
    weather = weather_find(city)
    if weather:
        location_entry['text']= '{},{}'.format(weather[0],weather[1])
        temperature_entry['text'] = '{:.2f} C, {:.2f} F'.format(weather[2],weather[3])
        weather_entry['text'] = weather[4]
    else:
        messagebox.showerror('Error','Please Enter Valid City Name')


#make a root window
root =Tk()
#give your window a title#
root.title("My own weather app")

# root is our variable to mention our tkinter window
#that is why we will be using it multiple times

root.config(background="blue")
root.geometry("700x400")

#making the input section  for place

search_city = StringVar() # variable name for city

# we are now taking the entry bo that will take the preferred country name
enter_city = Entry(root , textvariable=search_city, bg="green",fg="black",font=("Arial",30,"bold"))
# We are using root [ Our Tkinter root window ]
# And the variable we just created  as parameters

# Pack is a function that will allow you to put out all of these things
enter_city.pack()

# Now we will make our search button with button function
# Put whatever should appear in the middle of the search button into text
search_button = Button(root, text = 'SEARCH WEATHER !' , width= 20 , bg="red",fg="white",font=("Arial",25,"bold"),command=print_weather)
search_button.pack()

# we are leaving the text part empty because we will be writing some code to print the text
location_entry = Label(root , text='',font=("Arial",35,"bold"),bg="lightblue")
location_entry.pack()

temperature_entry = Label(root ,text='',font=("Arial",35,"bold"),bg="lightpink")
temperature_entry.pack()

weather_entry = Label(root , text = '' , font =("Arial",35,"bold"),bg="lightgreen")
weather_entry.pack()

# After we write write the functions you will be able to see the changes we made here

# Now it is time for the APİ

# use this to see the output #
root.mainloop()
