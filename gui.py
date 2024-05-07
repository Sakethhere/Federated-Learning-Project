import pyautogui
import time
import random
import datetime
from tkinter import Tk
from tkinter.messagebox import showinfo, showwarning
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from email_feature import send_email

model = load_model("ssmodel", compile=False)

classes = {0:'Education Classroom', 1:'Games', 2:'Movies', 3 : 'Screen shots programming', 4 : 'Youtube Education'}
def take_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    pyautogui.screenshot(filename)
    print(f"Screenshot taken and saved as {filename}")
    return filename

def show_alert(class_name):
    root = Tk()
    root.withdraw()
    message = f"{class_name} found. Keep going"
    showinfo("Screenshot Taken", message)
    root.destroy()

def show_error(class_name):
    root = Tk()
    root.withdraw()
    message = f"{class_name} found, arent you being productive today?"
    showwarning("Screenshot Taken", message)
    root.destroy()

def main():
    while True:
        interval = random.randint(5, 10)
        print(f"Waiting for {interval} seconds.")
        time.sleep(interval)
        filename = take_screenshot()
        img = Image.open(filename)
        img = img.resize((256, 256))
        img = img.convert("RGB")
        img = np.array(img).astype('float32') / 255
        img = img.reshape((1, 256, 256, 3))
        pred = model.predict(img)
        pred_class = np.argmax(pred)
        act_class = classes[pred_class]
        if pred_class == 2 or pred_class == 1 or pred_class == 4:
            show_error(act_class)
            send_email('saketha1299@gmail.com', filename, 'Warning for student', f'we found your child watching {act_class}. attached the screenshot below')
        else:
            show_alert(act_class)

if __name__ == "__main__":
    main()
