from danh_sach_sinh_vien import DanhSachSinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiChinhQuy
from ds_hinh_hoc import DanhSachHinhHoc
from hinh_hoc import HinhChuNhat, HinhTron

if __name__ == "__main__":
    print("=== Quản lý Sinh Viên Kế Thừa ===")
    sv1 = SinhVienChinhQuy("001", "Nguyen Van A", "2000-01-01", 8.5, "1000000")
    sv2 = SinhVienPhiChinhQuy("002", "Le Thi B", "1999-05-12", 7.5, "Công ty ABC")
    print(sv1.xuat_thong_tin())
    print(sv2.xuat_thong_tin())

    print("\n=== Quản lý Hình Học ===")
    ds_hh = DanhSachHinhHoc()
    hcn = HinhChuNhat(5, 10)
    htr = HinhTron(7)

    ds_hh.them_hinh(hcn)
    ds_hh.them_hinh(htr)

    ds_hh.xuat()
    print("\nHình có diện tích lớn nhất:", ds_hh.tim_hinh_co_dien_tich_lon_nhat().tinh_dien_tich())

    ds_hh.sap_xep_giam_theo_dien_tich()
    print("\nDanh sách sau khi sắp xếp giảm theo diện tích:")
    ds_hh.xuat()
