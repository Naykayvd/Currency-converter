from tkinter import *
import requests

root = Tk()
root.title("Currency Converter")
root.geometry("500x400")

value = IntVar()

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']

value_label = Label(root, text="Enter amount(USD)")
value_label.pack()

value_entry = Entry(root, textvariable=value)
value_entry.pack()

convert = Label(root, text="Select your currency")
convert.pack()

convert_list = Listbox(root)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
    convert_list.pack()

convert_label = Label(root, text="Converted to: ")
convert_label.pack()


def conversion():
    num = float(value_entry.get())
    print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    convert_label['text'] = ans


convert_btn = Button(root, command=conversion, text="Calculate")
convert_btn.pack()

root.mainloop()
