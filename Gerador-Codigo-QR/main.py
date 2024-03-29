import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = input_entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

    qr_image = Image.open("qr_code.png")
    qr_image = qr_image.resize((200, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=photo)
    qr_label.photo = photo
    mesaj_label.config(text="Um código QR será gerado")

app = tk.Tk()
app.title("Gerador de código QR")

input_label = tk.Label(app, text="Introduza os dados para gerar o QR code: ", font=("Helvetica", 12))
input_label.pack()

input_entry = tk.Entry(app, font=("Helvetica", 12))
input_entry.pack()

generate_button = tk.Button(app, text="Gerar QR code", command=generate_qr, font=("Helvetica", 12))
generate_button.pack()

mesaj_label = tk.Label(app, text="", font=("Helvetica", 12))
mesaj_label.pack()

qr_label = tk.Label(app)
qr_label.pack()

app.mainloop()