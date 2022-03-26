#!/usr/bin/env python3


class Object:
	def __init__(self):
		self.x = []

objects = []


objects.append(Object())

# obj = Non


objects.append(Object())

objects[0].x.append(2)
objects[1].x.append(3)

print(objects[0].x, objects[1].x)