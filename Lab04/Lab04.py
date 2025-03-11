import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import openpyxl

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        email TEXT,
                        phone TEXT,
                        dob TEXT,
                        semester TEXT,
                        year TEXT,
                        subjects TEXT)''')
    conn.commit()
    conn.close()

def save_data():
    student_id = entry_id.get()
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    dob = entry_dob.get()
    semester = combo_semester.get()
    year = combo_year.get()

    #Lấy danh sách môn học đã chọn
    subjects = [subjects_list[i] for i in range(len(subject_vars)) if subject_vars[i].get() == 1]
    subjects_str = ", ".join(subjects)

    #Kiểm tra dữ liệu hợp lệ
    if not student_id.isdigit() or len(student_id) != 7:
        messagebox.showerror("Lỗi", "Mã số sinh viên phải có 7 chữ số")
        return
    
    if "@" not in email or "." not in email:
        messagebox.showerror("Lỗi", "Email không hợp lệ")
        return
    
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (student_id, name, email, phone, dob, semester, year, subjects_str))
    conn.commit()
    conn.close()
    messagebox.showinfo("Thành công", "Đăng ký thành công!")
    clear_fields()

def export_to_excel():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["ID", "Họ tên", "Email", "Số điện thoại", "Ngày sinh", "Học kỳ", "Năm học", "Môn học"])
    for row in data:
        sheet.append(row)
    
    workbook.save("students.xlsx")
    messagebox.showinfo("Xuất Excel", "Dữ liệu đã được lưu vào students.xlsx")

def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    combo_semester.set("")
    combo_year.set("")
    
    #Bỏ chọn tất cả môn học
    for var in subject_vars:
        var.set(0)

create_database()

root = tk.Tk()
root.title("Đăng ký học phần")
root.geometry("500x400")
root.configure(bg="lightgreen")

#Tiêu đề
title_label = tk.Label(root, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", font=("Arial", 14, "bold"), fg="red", bg="lightgreen")
title_label.grid(row=0, column=0, columnspan=2, pady=5)

#Các trường nhập liệu
labels = ["Mã số sinh viên", "Họ tên", "Email", "Số điện thoại", "Ngày sinh", "Học kỳ", "Năm học"]
entries = {}

for i, text in enumerate(labels):
    tk.Label(root, text=text, font=("Arial", 10), bg="lightgreen").grid(row=i + 1, column=0, sticky="w", padx=10, pady=2)
    if "Năm học" in text:
        entries[text] = ttk.Combobox(root, values=["2023", "2024", "2025"])
    else:
        entries[text] = tk.Entry(root)
    entries[text].grid(row=i + 1, column=1, padx=10, pady=2, sticky="ew")

entry_values = list(entries.values())
entry_id, entry_name, entry_email, entry_phone, entry_dob = entry_values[:5]
combo_semester, combo_year = entries["Học kỳ"], entries["Năm học"]

#Danh sách môn học
tk.Label(root, text="Chọn môn học", font=("Arial", 10), bg="lightgreen").grid(row=len(labels) + 1, column=0, sticky="w", padx=10, pady=2)
subjects_list = ["Lập trình Python", "Lập trình Java", "Công nghệ phần mềm", "Phát triển ứng dụng web"]
subject_vars = [tk.IntVar() for _ in subjects_list]

for i, subject in enumerate(subjects_list):
    tk.Checkbutton(root, text=subject, variable=subject_vars[i], bg="lightgreen").grid(row=len(labels) + 2 + (i // 2), column=i % 2, sticky="w", padx=10)

#Nút bấm
frame_buttons = tk.Frame(root, bg="lightgreen")
frame_buttons.grid(row=len(labels) + 4, column=0, columnspan=2, pady=10)

btn_register = tk.Button(frame_buttons, text="Đăng ký", bg="green", fg="white", width=10, command=save_data)
btn_register.grid(row=0, column=0, padx=10)

btn_export = tk.Button(frame_buttons, text="Xuất Excel", bg="blue", fg="white", width=10, command=export_to_excel)
btn_export.grid(row=0, column=1, padx=10)

btn_exit = tk.Button(frame_buttons, text="Thoát", bg="red", fg="white", width=10, command=root.quit)
btn_exit.grid(row=0, column=2, padx=10)

#Chạy giao diện
root.mainloop()
