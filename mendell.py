#!/usr/bin/env python3
def main():
    print(dom(25,28,15))


def dom(k,m,n):
    t = k+m+n
    kk = ((k/t)*((k-1)/(t-1)))
    km = ((k/t)*((m)/(t-1)))
    kn =((k/t)*((n)/(t-1)))
    mm = ((m/t)*((m-1)/(t-1)))
    mk = ((m/t)*((k)/(t-1)))
    mn = ((m/t)*((n)/(t-1)))
    nk = ((n/t)*((k)/(t-1)))
    nm =((n/t)*((m)/(t-1)))    
    
    d_kk = 1
    d_km = 1
    d_kn = 1
    d_mm = (3/4)
    d_mk = 1
    d_mn = (1/2)
    d_nk = 1
    d_nm = (1/2)
    prob = (kk*d_kk)+(d_km*km)+(d_kn*kn)+(d_mm*mm)+(d_mk*mk)+(d_mn*mn)+(d_nk*nk)+(d_nm*nm)
    return round(prob, 5)

if __name__ == '__main__': main()