import tkinter as tk

PerClick = 1
Clicks = 0
Multiplier = 1
MultiplierCost = 100
PerClickCost = 20

def Update():
    label.config(text=f"Clicks: {Clicks}")

def AddClick():
    global Clicks
    global PerClick

    Clicks = Clicks + PerClick * Multiplier
    Update()

def BuyMultiplier():
    global Multiplier
    global Clicks
    global MultiplierCost

    if Clicks >= MultiplierCost:
        Clicks = Clicks - MultiplierCost
        Multiplier = Multiplier + 1
        MultiplierCost = MultiplierCost * 2
        multiplier_label.config(text=f"Multiplier: {Multiplier}")
        multiplier_button.config(text=f"Buy Multiplier ({MultiplierCost} clicks)")
        Update()

def BuyPerClick():
    global PerClick
    global Clicks
    global PerClickCost

    if Clicks >= PerClickCost:
        Clicks = Clicks - PerClickCost
        PerClick = PerClick + 1
        PerClickCost = PerClickCost + 10
        perclick_label.config(text=f"Per Click: {PerClick}")
        perclick_button.config(text=f"Buy Per Click ({PerClickCost} clicks)")
        Update()

def CloseApp():
    root.destroy()

root = tk.Tk()
root.title("Kazoo's totally W game")
root.geometry("1920x1080")

label = tk.Label(root, text="Clicks: 0")
label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

click_button = tk.Button(button_frame, text='Click Me!', width=15, command=AddClick)
click_button.pack(side=tk.LEFT)

close_button = tk.Button(button_frame, text='Close', width=15, command=CloseApp)
close_button.pack(side=tk.LEFT)

shop_frame = tk.Frame(root)
shop_frame.pack(pady=10)

multiplier_label = tk.Label(shop_frame, text=f"Multiplier: {Multiplier}")
multiplier_label.grid(row=0, column=0, padx=10)

multiplier_button = tk.Button(shop_frame, text=f"Buy Multiplier ({MultiplierCost} clicks)", command=BuyMultiplier)
multiplier_button.grid(row=0, column=1, padx=10)

perclick_label = tk.Label(shop_frame, text=f"Per Click: {PerClick}")
perclick_label.grid(row=1, column=0, padx=10)

perclick_button = tk.Button(shop_frame, text=f"Buy Per Click ({PerClickCost} clicks)", command=BuyPerClick)
perclick_button.grid(row=1, column=1, padx=10)

made_by_label = tk.Label(root, text="Made by Ducky", anchor="se")
made_by_label.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()