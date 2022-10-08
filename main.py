# Sekuensial
print('Ibu berkata, "Pergi ke toko')
print('Budi menjawab , "Baik, apa yang harus saya lakukan di toko?')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')
print('Maka budi berangkat ke toko')
print ('Dan mulai belanja')

# Percabangan
milk_bottle_count = 173
egg_count = 1587
print(f'Jummlah Botol Susu {milk_bottle_count} btl' )
if milk_bottle_count >0:
    print('Budi mengecek harganya, dan ternyata uangnya cukup')
    if egg_count == 0:
        print('Budi membeli 1 botol susu')
    else:
        print('Budi membeli 6 botol susu')
else:
    print('Budi tidak jadi membeli 1 botol susu')

print('Budi pulang ke rumah menyerahkan hasil kepada Ibu')

