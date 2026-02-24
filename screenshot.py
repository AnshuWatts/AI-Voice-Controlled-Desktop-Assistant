import os
import datetime
import pyautogui
import editables

def screenshot():
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().strftime("%H-%M-%S")

    # ✅ Ensure screenshots folder exists
    os.makedirs(editables.screenshots, exist_ok=True)

    file_name = os.path.join(editables.screenshots, f"{date}-{time}.png")

    image = pyautogui.screenshot()
    image.save(file_name)
    print(f"Screenshot saved to {file_name}")


# import pyautogui
# import editables
# import datetime
# import speak


# def screenshot():
#     date = datetime.datetime.now().date()
#     time = datetime.datetime.now().strftime("%H-%M-%S")

#     image = pyautogui.screenshot()
#     image.save(editables.screenshots + '/' + str(date) + '-' + str(time) + '.png')

#     speak.speak('Screenshot saved successfully')
