import zerorpc
dataNomorHp = ["14045", "08132456", "0123456"]
pulsa = [0, 0, 0]

class Operator(object):
    def cekNomor(self, nomorhp):
    	accepted = 0
    	for x in dataNomorHp:
    		if nomorhp == x:
    			accepted = 1
    	if accepted == 1:
    		return 1
    	else:
    		return 0

    def beliPulsa(self, nomorhp, jumlahpulsa):
    	index = 0
    	for x in dataNomorHp:
    		if nomorhp == x:
    			break
    		else:
    			index = index + 1
    	pulsa[index] = pulsa[index] + jumlahpulsa
    	return pulsa[index]

Server = zerorpc.Server(Operator())
Server.bind("tcp://0.0.0.0:8082")
Server.run()