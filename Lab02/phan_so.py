from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        self.rut_gon()

    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def __add__(self, other):
        tu = self.tu * other.mau + self.mau * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __sub__(self, other):
        tu = self.tu * other.mau - self.mau * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __mul__(self, other):
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __truediv__(self, other):
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        return PhanSo(tu, mau)

    def __str__(self):
        return f"{self.tu}/{self.mau}"