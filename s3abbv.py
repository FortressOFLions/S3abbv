import stateData
import vars
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

DATA = stateData.getDataFromFile()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(vars.PATH) # hidden path to current project


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def button_clicked() -> None: 
    query: str = str(entry_1.get())
    output:stateData.StateProv = DATA[query]
    if output is None: 
        entry_2.delete(1.0,"end")
        entry_2.insert(1.0,"There is no item with that key")
    else:
        entry_2.delete(1.0,"end")
        entry_2.insert(1.0,f"""{DATA.clean_item(output.abbreviation)}
            \nIs the shorthand for: {DATA.clean_item(output.name)}
            \nIn the region: {DATA.clean_item(output.region)}
        """)



window = Tk()

window.geometry("175x250")
window.configure(bg = "#09001E")


canvas = Canvas(
    window,
    bg = "#09001E",
    height = 250,
    width = 175,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    87.0,
    25.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    87.0,
    76.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    87.0,
    76.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#9F9F9F",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=24.5,
    y=64.0,
    width=125.0,
    height=23.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_clicked(),
    relief="flat"
)
button_1.place(
    x=62.0,
    y=95.0,
    width=50.0,
    height=25.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    87.5,
    187.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#9F9F9F",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=0.0,
    y=125.0,
    width=175.0,
    height=123.0
)
entry_2.insert(1.0, "State Abbreviation will be confirmed here.")

canvas.create_rectangle(
    12.0,
    137.0,
    162.0,
    237.0,
    fill="#D9D9D9",
    outline="")
window.resizable(True, True)
window.mainloop()
