import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:9999")

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
    	accepted = c.pindahSaldo(namaclient, "Bukapedia", amount)
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

    #def beliPulsa(self, namaclient, amount):


s = zerorpc.Server(Marketplace())
s.bind("tcp://0.0.0.0:10000")
s.run()
