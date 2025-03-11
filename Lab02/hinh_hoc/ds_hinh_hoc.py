from hinh_hoc import HinhChuNhat, HinhTron

class DanhSachHinhHoc:
    def __init__(self):
        self.danh_sach = []

    def them_hinh(self, hinh):
        self.danh_sach.append(hinh)

    def xuat(self):
        for hinh in self.danh_sach:
            print(f"Diện tích: {hinh.tinh_dien_tich()}, Chu vi: {hinh.tinh_chu_vi()}")

    def tim_hinh_co_dien_tich_lon_nhat(self):
        return max(self.danh_sach, key=lambda h: h.tinh_dien_tich(), default=None)

    def sap_xep_giam_theo_dien_tich(self):
        self.danh_sach.sort(key=lambda h: h.tinh_dien_tich(), reverse=True)