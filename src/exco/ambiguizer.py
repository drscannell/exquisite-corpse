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
				result += ambigule
				buffer = []
		return ' '.join(result)

	@classmethod
	def ambiguize_nouns_buffer(cls, buffer):
		pos_list = [t[1] for t in buffer]
		if not pos_list[-1] in ['NN', 'PRP']:
			return None
		else:
			return cls.ambiguize_terminal_noun_buffer(buffer)
	
	@classmethod
	def ambiguize_terminal_noun_buffer(cls, buffer):
		pos_list = [t[1] for t in buffer]
		word_list = [t[0] for t in buffer]
		lexname_list = cls.get_lexname_list(buffer)
		print lexname_list
		transform = 'something'
		if pos_list[-1] in ['PRP']:
			transform = 'someone'
		elif lexname_list[-1] in ['noun.person']:
			print 'found person noun!'
			transform = 'someone'
		elif 'verb.motion' in lexname_list:
			transform = 'somewhere'
		word_list[-1] = transform
		if len(word_list) > 1:
			if pos_list[-2] in ['DT']:
				word_list.pop(-2)
		return word_list

	@classmethod
	def get_lexname_list(cls, buffer):
		lexnames = []
		for b in buffer:
			if b[1] in ['NN', 'NNP', 'NNPS']:
				synsets = wn.synsets(b[0], pos=wn.NOUN)
				lexnames.append(synsets[0].lexname)
			elif b[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
				synsets = wn.synsets(b[0], pos=wn.VERB)
				lexnames.append(synsets[0].lexname)
		return lexnames


