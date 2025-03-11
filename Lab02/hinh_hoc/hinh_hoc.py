from math import pi

class HinhHoc:
    """
    Lớp cơ bản cho các hình học.
    """
    def tinh_dien_tich(self):
        pass

    def tinh_chu_vi(self):
        pass

class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return pi * self.ban_kinh ** 2

    def tinh_chu_vi(self):
        return 2 * pi * self.ban_kinh