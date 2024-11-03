import tkinter as tk
import webview
import requests
from PIL import Image, ImageTk
import io

# Načítanie počasia
def load_weather_image():
    img_url = 'https://www.imeteo.sk/images/forecast_widget/row/2193-7.png'
    response = requests.get(img_url)
    img_data = Image.open(io.BytesIO(response.content))
    img = img_data.resize((400, 200), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def open_calendar():
    with open('index.html', 'r') as f:
        html_content = f.read()
    webview.create_window('CaleDishPis Calendar', html=html_content)
    webview.start()

def run_app():
    weather_img = load_weather_image()
    weather_label.config(image=weather_img)
    weather_label.image = weather_img
    open_calendar()

root = tk.Tk()
root.title("CaleDishPis")
root.geometry("800x600")

weather_label = tk.Label(root)
weather_label.pack(pady=10)

start_button = tk.Button(root, text="Načítaj počasie a kalendár", command=run_app)
start_button.pack(pady=20)

root.mainloop()
