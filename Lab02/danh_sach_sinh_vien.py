import csv
from sinh_vien import SinhVien

class DanhSachSinhVien:
    def __init__(self):
        self.ds_sinh_vien = []

    def them_sinh_vien(self, sv: SinhVien):
        self.ds_sinh_vien.append(sv)

    def doc_tu_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                ma_sv, ho_ten, ngay_sinh, lop = row
                sv = SinhVien(ma_sv, ho_ten, ngay_sinh, lop)
                self.them_sinh_vien(sv)

    def sap_xep_tang_theo_ho_ten(self):
        self.ds_sinh_vien.sort(key=lambda sv: sv.ho_ten)

    def xuat_danh_sach(self):
        for sv in self.ds_sinh_vien:
            print(sv)
