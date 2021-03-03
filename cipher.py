import tkinter as tk

def encrypt(text):
  ans=""
  text = text.upper()
  for char in text:
    if char>='A' and char<='Z':
      z = (ord(char)+3-ord('A'))%26
      z = z+ord('A')
      ans = ans+chr(z)
    else:
      ans = ans+char
  return ans

def decrypt(text):
  ans=""
  text = text.lower()
  for char in text:
    if char>='a' and char<='z':
      z = (ord(char)-ord('a')+26-3)%26
      z = z+ord('a')
      ans = ans+chr(z)
    else:
      ans = ans+char
  return ans

def ceaser():
  toDo = choice.get()
  text = textBox.get()
  ans = ""
  count = 0
  if toDo == "Encrypt":
    ans = encrypt(text)
    count = 10
  elif toDo == "Decrypt":
    ans = decrypt(text)
    count = 5
  infoWindow = tk.Toplevel()
  infoWindow.iconbitmap('C:/Users/Ashwin/PythonApps/favicon.ico')
  infoWindow.title("Message Window")
  infoWindow.geometry("600x100")
  label1 = tk.Label(infoWindow, text=toDo+"ed Text: ", font=("Helvetica",15), anchor=tk.W)
  label2 = tk.Label(infoWindow, text=ans, font=("Helvetica",15))
  label3 = tk.Label(infoWindow, text="This window will automatically close in "+str(count)+" seconds.", fg="red")
  label1.pack()
  label2.pack()
  label3.pack()
  infoWindow.after(count*1000, infoWindow.destroy)

root = tk.Tk()
root.title("Ceaser Cipher")
root.geometry("600x200")
root.iconbitmap('C:/Users/Ashwin/PythonApps/favicon.ico')
root.configure(background="black")

# Creating Entry Field and Label
textBox_label = tk.Label(root, text="Enter the text", font=("Helvetica", 15), bg="black", fg="white")
textBox = tk.Entry(root, width=50)

textBox_label.grid(row=0, column=0, padx=30, pady=30)
textBox.grid(row=0, column=1, padx=30, pady=30)

# Creating dropdown menu
options = [
  "Encrypt",
  "Decrypt"
]
choice = tk.StringVar()
choice.set("Encrypt")
dropdownMenu = tk.OptionMenu(root, choice, *options)
dropdownMenu.config(bg="black", fg="white")
dropdownMenu["menu"].config(bg="black", fg="white")
dropdownMenu.grid(row=1, column=0)

# Creating button
go_btn = tk.Button(root, text="Continue", command=ceaser)
go_btn.grid(row=1, column=1, ipadx=50)

root.mainloop()