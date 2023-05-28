def ikili_arama(dizi, hedef):
    baslangic = 0
    son = len(dizi) - 1

    while baslangic <= son:
        orta = (baslangic + son) // 2

        if dizi[orta] == hedef:
            return orta
        
        if dizi[orta] < hedef:
            baslangic = orta + 1

        else:
            son = orta - 1

    return -1

print(ikili_arama([9,8,75,35,14], 8))