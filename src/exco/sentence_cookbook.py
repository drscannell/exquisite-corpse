
class Word:
	def __init__(self, text, tags):
		self.text = text
		self.tags = tags
	def matches(self, tag):
		return tag in self.tags
	def __str__(self):
		return self.text


class SentenceFactory:
	def __init__(self, words):
		self.words = words
	def build(self, recipe):
		sentence = []
		for tag in recipe:
			sentence.append(str(self.getword(tag)))
		return ' '.join(sentence)
	def getword(self, tag):
		for word in self.words:
			if word.matches(tag):
				return word
		
words = [
		Word('the', ['article']),
		Word('man', ['noun']),
		Word('walks', ['verb']),
		Word('away', ['preposition'])
		]

recipe1 = ['article', 'noun', 'verb', 'preposition']

sentencefactory = SentenceFactory(words)
sentence = sentencefactory.build(recipe1)
print sentence
