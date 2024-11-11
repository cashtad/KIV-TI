import tkinter as tk
import PIL.ImageTk as ImageTk
import PIL.Image as Image

last_five_chars = []


def create_main_window():
    """Создает главное окно Tkinter и отображает начальное изображение."""
    global root, label, photo, current_stav, entry
    root = tk.Tk()
    root.title("Отображение изображения")

    # Начальное изображение
    current_stav = "stav1"
    image = Image.open(f"PNG/{current_stav}.png")
    photo = ImageTk.PhotoImage(image)

    # Метка для отображения изображения
    label = tk.Label(root, image=photo)
    label.pack()

    # Считыватель клавиш
    root.bind("<KeyRelease>", on_press)  # Привязываем нажатие Enter к обработке команды


def update_image():
    """Обновляет изображение в окне на основе текущего состояния."""
    global photo, label, current_stav
    image = Image.open(f"PNG/{current_stav}.png")
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # Обновляем ссылку на изображение, чтобы избежать удаления из памяти


def process_command(command):
    """Обрабатывает команду и обновляет состояние."""
    global current_stav

    if command == "ф":
        command = "a"
    if command == "и":
        command = "b"

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
    if event.char == 'r' or event.char == 'к':
        reset_stav()
    elif event.char == 's' or event.char == 'ыифи':
        root.quit()
    else:
        process_command(event.char)


def reset_stav():
    """Сбрасывает текущее состояние и обновляет изображение."""
    global current_stav
    current_stav = "stav1"
    update_image()


if __name__ == "__main__":
    create_main_window()

    root.mainloop()
