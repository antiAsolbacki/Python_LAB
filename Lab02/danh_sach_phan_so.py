from .phan_so import PhanSo

class DanhSachPhanSo:
    def __init__(self):
        self.ds_phan_so = []

    def them_phan_so(self, ps: PhanSo):
        self.ds_phan_so.append(ps)

    def tong_phan_so_am(self):
        tong = PhanSo(0, 1)
        for ps in self.ds_phan_so:
            if ps.tu < 0:
                tong += ps
        return tong
    
    def xoa_phan_so(self, ps: PhanSo):
        self.ds_phan_so = [x for x in self.ds_phan_so if x != ps]
    