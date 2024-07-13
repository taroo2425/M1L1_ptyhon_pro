meme_dict = {
            "key" : "value",
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SHEESH" : "sedikit ketidaksetujuan",
            "CREEPY" : "menakutkan/tidak menyenangkan",
            "AGGRO"  : "untuk menjadi agresif/marah",
            "ROLF" : "tanggapan terhadap lelucon"
            }
            
#print(meme_dict["CRINGE"])

for i in range(len(meme_dict)):
    meme = input("masukkan key:")
    print(meme_dict[meme])
