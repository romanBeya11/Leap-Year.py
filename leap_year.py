'''
Created by: Roman Beya
Created on: 14-oct-2017
Created for: ICS3U
This program determines whether or not the year inputted by a user is a leap year using 'nested if statements'
'''
import ui

def calculate_if_leapyear_touch_up_inside(sender):
	# determines whether the year that the user types in is a leap year or not
	year = int(view['calculate_if_leapyear_textfield'].text)
	if year % 100 == 0:
		if year % 400 == 0:
			view['output_label'].text = "{} is a leap year!!".format(year)
		else:
			view['output_label'].text = "{} is not a leap year!!".format(year)
	else:
		if year % 4 == 0:
			view['output_label'].text = "{} is a leap year!!".format(year)
		else: 
			view['output_label'].text = "{} is not a leap year...".format(year)

view = ui.load_view()
view.present('sheet')
