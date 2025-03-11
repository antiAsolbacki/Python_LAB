from sinh_vien import SinhVien

class SinhVienPhiChinhQuy(SinhVien):
    """
    Lớp Sinh viên phi chính quy kế thừa từ lớp SinhVien.
    """
    def __init__(self, ma_sv, ho_ten, ngay_sinh, diem_tb, noi_cong_tac):
        super().__init__(ma_sv, ho_ten, ngay_sinh, diem_tb)
        self.noi_cong_tac = noi_cong_tac

    def xuat_thong_tin(self):
        base_info = super().xuat_thong_tin()
        return f"{base_info}, Nơi công tác: {self.noi_cong_tac}"
