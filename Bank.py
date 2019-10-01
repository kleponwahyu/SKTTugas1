import zerorpc
namaNasabah = ["Joko", "Bambang", "Bukapedia"]
saldoNasabah = [25000, 50000, 100000]

class Bank(object):
    def pindahSaldo(self, id1, id2, amount):
        hitungan = 0
        for x in namaNasabah:
            if id1 == x:
                accepted1 = 1
                break
            else:
                hitungan = hitungan + 1
        indexid1 = hitungan
        hitungan = 0
        for x in namaNasabah:
            if id2 == x:
                accepted2 = 1
                break
            else:
                hitungan = hitungan + 1
        indexid2 = hitungan
        hitungan = 0
        if accepted1 & accepted2 == 1:
            if amount < saldoNasabah[indexid1]:
                saldoNasabah[indexid1] = saldoNasabah[indexid1] - amount
                saldoNasabah[indexid2] = saldoNasabah[indexid2] + amount
                print ("Saldo", namaNasabah[indexid1], " : ", saldoNasabah[0])
                print ("Saldo", namaNasabah[indexid2], " : ", saldoNasabah[1])
                return 1
            else:
                return 2
        else:
            return 0

s = zerorpc.Server(Bank())
s.bind("tcp://0.0.0.0:9999")
s.run()