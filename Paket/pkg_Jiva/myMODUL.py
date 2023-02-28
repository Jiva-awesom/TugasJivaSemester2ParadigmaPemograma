class martabak:
    def __init__(self, tipe, RasaAtoSaus, modal, harga):
        self.tipe = tipe
        self.RasaAtoSaus = RasaAtoSaus
        self.modal = int(modal)
        self.harga = int(harga)

martabak1 = martabak("Manis", "Coklat", 17500, 26500)
martabak2 = martabak("Asin", "Tomat", 15500, 25000)

def JenisMartabak(Marta):
    print(f"Martabak {Marta.tipe}\n"
          f"Rasa {Marta.RasaAtoSaus}\n"
          f"Modal Membuat: Rp. {Marta.modal},00\n"
          f"Harga Jual: Rp. {Marta.harga},00")

JenisMartabak(martabak1)
JenisMartabak(martabak2)
