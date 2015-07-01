# Find the value of d < 1000 for which 1/d
# contains the longest recurring cycle in its decimal fraction part.

'''
hm... I originally wanted to convert the floats for 1/d -> strings -> int arrays,
thinking then I could traverse these arrays to look for cycles...
but I'm only getting 15 digits of precision by default, and beyond that, I can't be
certain that how many digits of precision I actually need. All the inputs are rational,
so fractional part will contain some repetition, but can I find a bound on it?

Here's an interesting question that speaks to a larger principle:

Which fractions are most difficult to represent in base 10? In converting from one base
to another, where are we most likely to run into these unterminating representations?



went on a bit of a tangent here... was wondering about drawing text using PIL,
to create an image of text for emphasizing certain patterns.
well, now I know a bit more about that.

'''

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from collections import Counter
a=str(14285714285714285)
times=2


def find_repeating_pattern(a):
	a=str(a)
	for i in xrange(len(a),1,-1):
		chunks, chunk_size = len(a), i
		substrings = [ a[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
		freqs = Counter(substrings)
		pattern = freqs.most_common()[0]
		if (pattern[1]) > 1:
			return pattern[0], len(pattern[0])


num_lines = 20;
image = Image.new("RGBA", (301,600), (255,255,255))
d_usr = ImageDraw.Draw(image)

font_size = 30
current_position = 0
for i in xrange(1,30):
	mult = 1000000000000000000000000000000000000000000000000000000000
	test_val = mult/i
	
	font = ImageFont.truetype('Monaco.dfont', font_size)
	current_position += font_size
	d_usr.text((1,current_position), str(test_val),(0,0,0), font=font)
	font_size -= 1




image.show()



'''
for n in range(1,len(a)):
    substrings=[a[i:i+n] for i in range(len(a)-n+1)]
    freqs=Counter(substrings)
    #print substrings
    d = dict(freqs)
    for i in substrings:
    	if d[i] > 1:
    		print i
    		print 'break'
    		break
    		'''



def main():
	return 0

def repeating_pattern(num):
	arr = [int(i) for i in str(num)]
	print arr
	largest_repeat = 0
	 

#repeating_pattern(14285714285714285)

def to_string(n):
	f = float(1)/n
	a = str(f).split('.')[1][:-1]
	print f, a

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
