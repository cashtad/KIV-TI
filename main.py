import tkinter as tk
from PIL import Image, ImageTk

last_five_chars = []

def create_main_window():
    """Создает главное окно Tkinter и отображает начальное изображение."""
    global root, label, photo, current_stav, entry
    root = tk.Tk()
    root.title("Отображение изображения")

    # Начальное изображение
    current_stav = "stav1"
    image = Image.open(f"SVG/{current_stav}.png")
    photo = ImageTk.PhotoImage(image)

    # Метка для отображения изображения
    label = tk.Label(root, image=photo)
    label.pack()

    # Поле для ввода команд
    entry = tk.Entry(root)
    entry.pack()
    entry.bind("<Key>", disable_backspace)
    entry.bind("<KeyRelease>", on_enter_press)  # Привязываем нажатие Enter к обработке команды


def update_image():
    """Обновляет изображение в окне на основе текущего состояния."""
    global photo, label, current_stav
    image = Image.open(f"SVG/{current_stav}.png")
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # Обновляем ссылку на изображение, чтобы избежать удаления из памяти


def process_command(command):
    """Обрабатывает команду и обновляет состояние."""
    global current_stav

    # Логика смены состояний
    match current_stav:
        case "stav1":
            if command == "a":
                print("Current stav is: ", current_stav)
            elif command == "b":
                current_stav = "stav2"
            else:
                current_stav = "stav1"
        case "stav2":
            if command == "a":
                current_stav = "stav3"
            elif command == "b":
                print("Current stav is: ", current_stav)
            else:
                current_stav = "stav1"
        case "stav3":
            if command == "a":
                current_stav = "stav1"
            elif command == "b":
                current_stav = "stav4"
            else:
                current_stav = "stav1"
        case "stav4":
            if command == "a":
                current_stav = "stav3"
            elif command == "b":
                current_stav = "stav5"
            else:
                current_stav = "stav1"
        case "stav5":
            if command == "a":
                current_stav = "stav6"
            elif command == "b":
                current_stav = "stav2"
            else:
                current_stav = "stav1"
        case "stav6":
            if command == "a":
                current_stav = "stav1"
            elif command == "b":
                current_stav = "stav4"
            else:
                current_stav = "stav1"

    update_image()  # Обновляем изображение


def on_enter_press(event):
    # """Обрабатывает ввод команды."""
    global last_five_chars
    if event.keysym == 'BackSpace':
        return 'break'
    last_five_chars.append(event.char)
    if len(last_five_chars) > 5:
        last_five_chars.pop(0)
    command = ''.join(last_five_chars).upper()

    # Проверяем команды
    if command == "RESET":
        reset_stav()
    elif command == "STOP":
        root.quit()
    else:
        process_command(event.char)


def reset_stav():
    """Сбрасывает текущее состояние текстового поля."""
    entry.delete(0, tk.END)

def disable_backspace(event):
    # Если нажата клавиша Backspace, блокируем действие
    if event.keysym == 'BackSpace':
        return 'break'  # 'break' предотвращает дальнейшую обработку события


if __name__ == "__main__":
    create_main_window()

    root.mainloop()
