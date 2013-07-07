import sys
pipe = open('/dev/input/js0','r')
action = []
spacing = 0
while 1:
	for character in pipe.read(1):
		action += ['%02X' % ord(character)]
		if len(action) == 8:

			num = int(action[5], 16) # Translate back to integer form
			percent254 = str(((float(num)-128.0)/126.0)-100)[4:6] # Calculate the percentage of push
			percent128 = str((float(num)/127.0))[2:4]

			if percent254 == '.0':
				percent254 = '100'
			if percent128 == '0':
				percent128 = '100'

			if action[6] == '01': # Button
				if action[4] == '01':
					print 'You pressed button: ' + action[7]
				else:
					print 'You released button: ' + action[7]

			elif action[7] == '00': # D-pad left/right
				if action[4] == 'FF':
					print 'You pressed right on the D-pad'
				elif action[4] == '01':
					print 'You pressed left on the D-pad'
				else:
					print 'You released the D-pad'


			elif action[7] == '01': # D-pad up/down
				if action[4] == 'FF':
					print 'You pressed down on the D-pad'
				elif action[4] == '01':
					print  'You pressed up on the D-pad'
				else:
					print 'You released the D-pad'


			elif action[7] == '04': # Left Joystick left/right
				if action[4] == 'FF':
					print 'You pressed right on the left joystick'
				elif action[4] == '01':
					print 'You pressed left on the left joystick'
				else:
					print 'You released the left joystick'

			elif action[7] == '05': # Left Joystick up/down
				if action[4] == 'FF':
					print 'You pressed down on the left joystick'
				elif action[4] == '01':
					print 'You pressed up on the left joystick'
				else:
					print 'You released the left joystick'

			elif action[7] == '02': # Right Joystick left/right
				num = int(action[5], 16) # Translate back into integer form
				if num >= 128:
					print 'You moved the right joystick left to %' + percent254
				elif num <= 127 \
				and num != 0:
					print 'You moved the right joystick right to %' + percent128
				else:
					print 'You stopped moving the right joystick'

			elif action[7] == '03': # Right Joystick up/ down
				if num >= 128:
					print 'You moved the right joystick upward to %' + percent254
				elif num <= 127 \
				and num != 0:
					print 'You moved the right joystick downward to %' + percent128
				else:
					print 'You stopped moving the right joystick' 
			action = []

