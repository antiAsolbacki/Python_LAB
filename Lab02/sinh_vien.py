class SinhVien:
    """
    Lớp Sinh viên cơ bản với các thuộc tính và phương thức cần thiết.
    """
    def __init__(self, ma_sv, ho_ten, ngay_sinh, diem_tb):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.diem_tb = diem_tb

    def xuat_thong_tin(self):
        """Xuất thông tin sinh viên."""
        return f"Mã SV: {self.ma_sv}, Họ tên: {self.ho_ten}, Ngày sinh: {self.ngay_sinh}, Điểm TB: {self.diem_tb}"
    