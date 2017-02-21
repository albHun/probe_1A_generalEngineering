import random
from probe_functions import *
from segnet import *

def credit_assignment(current_posi, goal, current_image, last_image, credits):
	"""This function upadtes the credit information according
	to the last tow images the camera captured."""

def random_select(map):
	"""This function takes the map and generates a random position
	on it."""

def select_movement(current_image, credits, probe_functions):
	"""This function selects a way of moving the probe based on
	the current_image and the credits assigned."""
	# This function is going to use segnet to analyze the image data

def initialize_credits():
	"""This fucntion initializes credits to give an even selection
	probability."""

fhand = open("map.in")
simulation_map = build_map(fhand)
current_posi = random_select(simulation_map)
goal = random_select(simulation_map)
credits = initialize_credits()
current_image = take_image()
last_image = take_image()

while (not current_posi == goal):
	# Moving in a way selected from all possible functions
	move(select_movement(current_image, credits, probe_functions))
	# Updating position and camera informaiton
	last_image = current_image
	current_image = take_image()
	current_posi = take_position()
	# Updating the credits
	credit_assignment(current_posi, goal, current_image, last_image, credits)
