from exco.ambiguizer import Ambiguizer

class TestCases:

	def test_ambiguize_nouns(self):
		tests = [
				{
				 'input':'The man crosses the room',
				 'expected':'someone crosses something'
				},
				{
				 'input':'He crosses the room',
				 'expected':'someone crosses something'
				}
				]

		for test in tests:
			yield self.check_ambiguize_nouns, test
	
	def check_ambiguize_nouns(self, test):
		observed = Ambiguizer.ambiguize_nouns(test['input'])
		expected = test['expected']
		print 'input: %s' % (test['input'])
		print 'expected: %s' % (expected)
		print 'observed: %s' % (observed)
		assert expected == observed

	# ----------------------------------------------------

	def test_ambiguize_noun(self):
		tests = [
				{
				 'input':'man',
				 'expected':'someone'
				},
				{
				 'input':'car',
				 'expected':'something'
				},
				{
				 'input':'room',
				 'expected':'somewhere'
				}
				]

		for test in tests:
			yield self.check_ambiguize_noun, test
	
	def check_ambiguize_noun(self, test):
		observed = Ambiguizer.ambiguize_noun(test['input'])
		expected = test['expected']
		print 'input: %s' % (test['input'])
		print 'expected: %s' % (expected)
		print 'observed: %s' % (observed)
		assert expected == observed



