def cal_propinas(vt_cuenta, p_propina=10):
    return vt_cuenta * (p_propina/100)
print(cal_propinas(180000))
print(cal_propinas(180000,15))