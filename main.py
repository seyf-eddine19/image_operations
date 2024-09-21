import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
import numpy as np


current_matrix = None # متغير لتخزين المصفوفة الأصلية
matrix_size = 60

# الدوال المطلوبة
def rotate_image():
    global current_matrix
    if current_matrix is not None:
        # هنا يجب إضافة الكود لتدوير الصورة بزاوية 90 درجة
        draw_matrix(current_matrix, "Image rotated 90°")

def flip_horizontal():
    global current_matrix
    if current_matrix is not None:
        # هنا يجب إضافة الكود لعكس الصورة أفقيًا
        draw_matrix(current_matrix, "Image flipped horizontally")

def flip_vertical():
    global current_matrix
    if current_matrix is not None:
        # هنا يجب إضافة الكود لعكس الصورة عموديًا
        draw_matrix(current_matrix, "Image flipped vertically")

def convert_to_bw(threshold=128):
    global current_matrix
    if current_matrix is not None:
        # هنا يجب إضافة الكود لتحويل الصورة إلى أبيض وأسود
        draw_matrix(current_matrix, f"Converted to black & white with threshold {threshold}")

def apply_blur():
    global current_matrix
    if current_matrix is not None:
        # هنا يجب إضافة الكود لتطبيق فلتر التمويه (Blur)
        draw_matrix(current_matrix, "Blur filter applied")

#__________________________________________________________________________________________________________________________
#---------------------------------------------  إنشاء واجهة المستخدم باستخدام  Tkinter  ---------------------------------------------
#__________________________________________________________________________________________________________________________
# فتح الصورة
def open_image():
    global current_matrix
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path).convert('L')
        image_resized = image.resize((matrix_size, matrix_size))
        current_matrix = np.array(image_resized)
        current_matrix = np.array(image_resized, dtype=np.uint8)
        draw_matrix(current_matrix, "Image loaded successfully")

# دالة لرسم المصفوفة الرمادية على الكانفا
def draw_matrix(matrix, status):
    canvas.delete("all")  # مسح الكانفا قبل الرسم
    pixel_size = canvas_size // matrix_size  # حجم البكسل بناءً على المصفوفة n*n
    for i in range(matrix_size):
        for j in range(matrix_size):
            color_value = matrix[i][j]
            color = f'#{color_value:02x}{color_value:02x}{color_value:02x}'  # تحويل إلى لون hex
            canvas.create_rectangle(
                j * pixel_size, i * pixel_size, (j + 1) * pixel_size, (i + 1) * pixel_size,
                outline="", fill=color
            )
    status_label.config(text=status)

# إعداد واجهة المستخدم Tkinter
window = tk.Tk()
window.title("Image Operations")
window.geometry("606x690")
window.resizable(False, False)

style = ttk.Style(window)
style.theme_use('clam')
style.configure(
    'TButton', height=2, background='#2C3E50', foreground='#FFFFFF', relief='flat', borderwidth=0,
    padding=[5, 2], font=('Dubai', 10, 'bold'), justify='right', anchor='center', compound='left'
)
style.map('TButton', foreground=[('active', '!disabled', '#FFFFFF')], background=[('active', '#1ABC9C')])

status_label = tk.Label(window, text="Welcome to Image Operations", bg='#2C3E50', fg='#FFFFFF', font=('Dubai', 14, 'bold'))
status_label.pack(side='top', fill='x')
tk.Frame(window, height=3, bg='#1ABC9C', bd=0).pack(side='top', fill='x')
canvas_size = 600
canvas = tk.Canvas(window, width=canvas_size, height=canvas_size, bg="lightgrey")
canvas.pack(side='top')

tk.Frame(window, height=3, bg='#1ABC9C', bd=0).pack(side='top', fill='x')
toolbar_frame = tk.Frame(window)
toolbar_frame.pack(side='top', pady=5)

ttk.Button(toolbar_frame, text="Open Image", command=open_image).pack(side='left', fill='x', padx=5)
ttk.Button(toolbar_frame, text="Rotate 90°", command=rotate_image).pack(side='left', fill='x', padx=5)
ttk.Button(toolbar_frame, text="Flip Horizontal", command=flip_horizontal).pack(side='left', fill='x', padx=5)
ttk.Button(toolbar_frame, text="Flip Vertical", command=flip_vertical).pack(side='left', fill='x', padx=5)
ttk.Button(toolbar_frame, text="Convert to BW", command=convert_to_bw).pack(side='left', fill='x', padx=5)
ttk.Button(toolbar_frame, text="Blur", command=apply_blur).pack(side='left', fill='x', padx=5)

window.mainloop()



