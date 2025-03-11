from sinh_vien import SinhVien

class SinhVienChinhQuy(SinhVien):
    """
    Lớp Sinh viên chính quy kế thừa từ lớp SinhVien.
    """
    def __init__(self, ma_sv, ho_ten, ngay_sinh, diem_tb, hoc_bong):
        super().__init__(ma_sv, ho_ten, ngay_sinh, diem_tb)
        self.hoc_bong = hoc_bong

    def xuat_thong_tin(self):
        base_info = super().xuat_thong_tin()
        return f"{base_info}, Học bổng: {self.hoc_bong}"