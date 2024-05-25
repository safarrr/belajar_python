def hitung_nilai(nilai):
    if nilai > 50 & nilai < 70:
        return "good"
    elif nilai > 70 & nilai < 85:
        return "baik"
    elif nilai > 85:
        return "lebih baik"
    else:
        return "tidak lulus"


print(hitung_nilai(nilai= 0))
