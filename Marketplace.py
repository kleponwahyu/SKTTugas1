import zerorpc

Bank = zerorpc.Client()
Bank.connect("tcp://127.0.0.1:8080")

Operator = zerorpc.Client()
Operator.connect("tcp://127.0.0.1:8082")

namaClientMarketplace =  ["Joko", "Bambang"]
saldoClientMarketplace = [0, 0]

class Marketplace(object):
    def cekNama(self, namaclient):
        global namaClientMarketplace
        for x in namaClientMarketplace:
            if namaclient == x:
                return 1
                break

    def topUp(self, namaclient, amount):
    	accepted = Bank.pindahSaldo(namaclient, "Bukapedia", amount)
    	if accepted == 1:
    		index = 0
    		for x in namaClientMarketplace:
    			if namaclient == x:
    				break
    			else:
    				index = index + 1
    		saldoClientMarketplace[index] = saldoClientMarketplace[index] + amount
    		print (namaClientMarketplace[index], "berhasil TopUp sebesar: ", amount , "Total saldo sebesar: ", saldoClientMarketplace[index])
    		return "Berhasil bro! Saldo e-money mu = %s" % saldoClientMarketplace[index]
    	elif accepted == 2:
    		return "Gagal TopUp karena saldo di bank tidak mencukupi"
    	elif accepted == 0:
    		return "Gagal TopUp karena nasabah tidak terdaftar di bank"

    def cekNomor(self, nomorhp):
        return (Operator.cekNomor(nomorhp))

    def beliPulsa(self, namaclient, nomorhp, jumlahpulsa):
        index = 0
        for x in namaClientMarketplace:
                if namaclient == x:
                    break
                else:
                    index = index + 1
        saldoClientMarketplace[index] = saldoClientMarketplace[index] - jumlahpulsa;
        hasil = Operator.beliPulsa(nomorhp, jumlahpulsa)
        print(namaClientMarketplace[index] + " beli pulsa sebesar " + str(hasil))
        #return "Berhasil menambahkan pulsa, pulsa saat ini %s" % hasil

Server = zerorpc.Server(Marketplace())
Server.bind("tcp://0.0.0.0:8081")
Server.run()
