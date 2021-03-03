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

def doWork(event):
  text = textBox.get()
  toDo = choice.get()
  ans = ""
  if text != "":
    dropdownMenu.configure(state="disabled")
  else:
    dropdownMenu.configure(state="active")
  if toDo == "Encrypt":
    ans = encrypt(text)
  elif toDo == "Decrypt":
    ans = decrypt(text)
  output_label['text'] = ""
  output_label['text'] = ans

root = tk.Tk()
root.title("Ceaser Cipher V2.0")
root.configure(background="black")
root.geometry("550x190")
root.iconbitmap('C:/Users/Ashwin/PythonApps/favicon.ico')

textBox = tk.Entry(root, width=60, bd=2, font=("Calibri",12))
textBox_label = tk.Label(root, text="Enter the text", bg="black", fg="white", font=("Helvetica",16))

output_label = tk.Label(root, bg="black", fg="white", font=("Helvetica",15))

textBox.bind("<KeyRelease>", doWork)

options = [
  "Encrypt",
  "Decrypt"
]
choice = tk.StringVar()
choice.set("Encrypt")
dropdownMenu = tk.OptionMenu(root, choice, *options)
dropdownMenu.config(bg="black", fg="white")
dropdownMenu["menu"].config(bg="black", fg="white")

textBox_label.pack(pady=15)
textBox.pack()
dropdownMenu.pack(pady=15)
output_label.pack()

root.mainloop()