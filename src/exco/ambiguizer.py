from __future__ import division
import nltk
import re
import pprint
from nltk.corpus import wordnet as wn

class Ambiguizer:

	@classmethod
	def taggedtokens(cls, text):
		return nltk.pos_tag(nltk.word_tokenize(text))

	@classmethod
	def ambiguize_nouns(cls, text):
		tokens = cls.taggedtokens(text)
		print tokens
		result = []
		buffer = []
		for t in tokens:
			buffer.append(t)
			ambigule = cls.ambiguize_nouns_buffer(buffer)
			if ambigule:
				result.append(ambigule)
				buffer = []
		return ' '.join(result)

	@classmethod
	def ambiguize_nouns_buffer(cls, buffer):
		pos_list = [t[1] for t in buffer]
		if pos_list == ['DT']:
			return None
		elif pos_list == ['PRP']:
			return 'someone'
		elif pos_list == ['DT','NN']:
			return cls.ambiguize_noun(buffer[1][0])
		else:
			return ''.join([t[0] for t in buffer])

	@classmethod
	def ambiguize_noun(cls, word):
		''' TODO: determine if person, place, thing, concept
		Having difficult time figuring out how to numerically
		guess at this.
		'''
		personness = cls.personness(word)
		placeness = cls.placeness(word)
		return 'something'

	@classmethod
	def personness(cls, word):
		comparator = wn.synset('someone.n.01')
		ave = cls.ave_path_similarity(word, comparator)
		print 'personness of %s: %f' % (word, ave)
		return ave

	@classmethod
	def placeness(cls, word):
		comparator = wn.synset('somewhere.n.01')
		ave = cls.ave_path_similarity(word, comparator)
		print 'placeness of %s: %f' % (word, ave)
		return ave

	@classmethod
	def ave_path_similarity(cls, word, comparator):
		total = 0
		dividend = 0
		for synset in wn.synsets(word, pos=wn.NOUN):
			dividend += 1
			score = comparator.path_similarity(synset)
			if not score is None:
				total += score
		return total / (1.00 * dividend)


