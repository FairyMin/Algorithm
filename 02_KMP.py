class My_kmp(object):
	def __init__(self,s1,s2):
		self.s1 = s1
		self.s2 = s2
		self.n = len(s1)
		self.m = len(s2)

	def strStr(self):
		self.F = [0 for x in range(0,self.m)]
		self.F[0] = -1

		for i in range(1,self.m):
			j = self.F[i-1]
			while ((self.s2[j+1]!=self.s2[i]) and (j>=0)):
				j=self.F[j]
			if self.s2[j+1] == self.s2[i]:
				self.F[i] = j+1
			else:
				self.F[i] = -1
		#for i in self.F:
		#	print(i)
	
	def str_match(self):
		i=0
		j=0
		while i<self.n:
			if self.s1[i]==self.s2[j]:
				i+=1
				j+=1
				if j==self.m:
					print("%d\n"%(i-self.m+1))
					j=self.F[j-1]+1
			else:
				if j==0:
					i+=1
				else:
					j=self.F[j-1]+1
#		k1 = 0
#		p2 = 0
#		while p2<self.n-self.m:
#			for m_i in range(k1,self.m):
#				if self.s1[p2+m_i] == self.s2[m_i]:
#					m_i += 1
#					if m_i == self.m:
#						print(p2)
#						p2 += 1
#						k1 = 0
#						break
#
#				else:
#					k1 = self.F[m_i]	
#					p2 = m_i - k1
#				#	if self.F[m_i]<0:
#					#	p2 += 1
#					#	k1 = 0
#

s1="asdbcdqvvqabcdq"
s2="cdq"
t = My_kmp(s1,s2)
t.strStr()
t.str_match()
