'''

Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message,
and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations,
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using p059.in, a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.

'''

import collections

msg = [int(i) for i in open('p059.in').read().split(',')] #file -> list

keys = []
for i in xrange(ord('a'), ord('z') + 1):
	for j in xrange(ord('a'), ord('z') + 1):
		for k in xrange(ord('a'), ord('z') + 1):
			keys.append((i,j,k))

# I should say... this method will also fail if the selection is especially atypical and doesn't include any common words
# but that's pretty unlikely
common_words = ['the','be','to','of','and','a','in','that','have','I','it','for','not','on','with','he']
common_words = [' ' + word + ' ' for word in common_words]

def main():
	for i in xrange(len(keys)):
		d_msg = []
		for n in xrange(len(msg)):
			if n%3==0:
				d_msg.append(msg[n] ^ keys[i][0])
			if n%3==1:
				d_msg.append(msg[n] ^ keys[i][1])
			if n%3==2:
				d_msg.append(msg[n] ^ keys[i][2])

		as_string = ''.join([chr(x) for x in d_msg])

		matches = 0
		for word in common_words:
			if word in as_string:
				matches += 1

		# in reality, I should just go with the score that has the most matches... but this is faster and should typically work
		if matches > len(common_words)/4: 
			return sum(d_msg)


# This would in principle be much faster... but I can't find a good way to generalize it
# (i.e. if the small sample only partially matches up with the typical frequencies, it will fail )
def freq_method():
	letter_freqs = {
		ord(" "): 0.140,
		ord("e"): 0.127,
		ord("t"): 0.090,
		ord("a"): 0.082
	}
	letter_freqs = sorted( ((v,k) for k,v in letter_freqs.iteritems()), reverse=True)
	bins = [[],[],[]]
	freqs = [{},{},{}]
	for n in xrange(len(msg)):
		if n%3==0:
			bins[0].append(msg[n])
		if n%3==1:
			bins[1].append(msg[n])
		if n%3==2:
			bins[2].append(msg[n])
	for x in xrange(len(bins)):
		for i in collections.Counter(bins[x]).most_common(len(letter_freqs)):
			freqs[x][i[0]] = (i[1]*1.0)/len(bins[x]) 
		freqs[x] = sorted( ((v,k) for k,v in freqs[x].iteritems()), reverse=True)
	for x in xrange(len(bins)):
		print "---"
		for i in xrange(len(letter_freqs)):
			for j in xrange(len(letter_freqs)):
				print x, freqs[x][i][1], letter_freqs[j][1], freqs[x][i][1] ^ letter_freqs[j][1]

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)






