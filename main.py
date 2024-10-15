import tkinter as tk
import keyboard
from PIL  import Image, ImageTk

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

    # # Поле для ввода команд
    entry = tk.Entry(root)
    entry.pack()
    entry.bind("<Key>", disable_keys)
    entry.bind("<KeyRelease>", on_press)  # Привязываем нажатие Enter к обработке команды


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
            if command == "b":
                current_stav = "stav2"
        case "stav2":
            if command == "a":
                current_stav = "stav3"
        case "stav3":
            if command == "a":
                current_stav = "stav1"
            elif command == "b":
                current_stav = "stav4"
        case "stav4":
            if command == "a":
                current_stav = "stav3"
            elif command == "b":
                current_stav = "stav5"
        case "stav5":
            if command == "a":
                current_stav = "stav6"
            elif command == "b":
                current_stav = "stav2"
        case "stav6":
            if command == "a":
                current_stav = "stav1"
            elif command == "b":
                current_stav = "stav4"

    update_image()  # Обновляем изображение


def on_press(event):
    """Обрабатывает ввод команды."""
    if event.char == 'r':
        reset_stav()
    elif event.char == 's':
        root.quit()
    else:
        process_command(event.char)


def reset_stav():
    """Сбрасывает текущее состояние и обновляет изображение."""
    global current_stav
    current_stav = "stav1"
    update_image()

def disable_keys(event):
    # Если нажата клавиша Backspace, блокируем действие
    if event.keysym == 'BackSpace':
        return 'break'  # 'break' предотвращает дальнейшую обработку события
    if event.keysym != 'a' or event.keysym != 'b' or event.keysym != 's' or event.keysym != 'r':
        return 'break'


if __name__ == "__main__":
    create_main_window()

    root.mainloop()
