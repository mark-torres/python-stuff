import random, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

logging.debug('Start of program')

guess = ''
opts = ['tails', 'heads']

toss = opts[ random.randint(0, 1) ] # 0 is tails, 1 is heads
logging.debug( 'Toss value: %s' % (toss) )

while guess not in opts:
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()
	logging.debug( 'User guess: %s' % (guess) )
if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guess = input()
	logging.debug( 'User guess: %s' % (guess) )
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')

logging.debug('End of program')
