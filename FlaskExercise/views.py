from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
	log = request.values.get('log_button')
	# TODO: Appropriately log the different button presses
	#   with the appropriate log level.

	if log == 'info':
		app.logger.info('The INFO button was pushed')
	elif log == 'warning':
		app.logger.warning('The WARNING button was pushed')
	elif log == 'warning':
		app.logger.error('The ERROR button was pushed')
	elif log == 'warning':
		app.logger.critical('The CRITICAL button was pushed')

	return render_template(
		'index.html',
		log=log
	)
