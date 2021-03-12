import Constants
import Node
import pygame
import Vector

from UserInterface import *
from pygame import *
from Vector import *
from Node import *
from enum import Enum
from queue import Queue
from queue import PriorityQueue

class Graph():
	def __init__(self):
		""" Initialize the Graph """
		self.nodes = []			# Set of nodes
		self.obstacles = []		# Set of obstacles - used for collision detection

		# Initialize the size of the graph based on the world size
		self.gridWidth = int(Constants.WORLD_WIDTH / Constants.GRID_SIZE)
		self.gridHeight = int(Constants.WORLD_HEIGHT / Constants.GRID_SIZE)

		# Create grid of nodes
		for i in range(self.gridHeight):
			row = []
			for j in range(self.gridWidth):
				node = Node(i, j, Vector(Constants.GRID_SIZE * j, Constants.GRID_SIZE * i), Vector(Constants.GRID_SIZE, Constants.GRID_SIZE))
				row.append(node)
			self.nodes.append(row)

		## Connect to Neighbors
		for i in range(self.gridHeight):
			for j in range(self.gridWidth):
				# Add the top row of neighbors
				if i - 1 >= 0:
					# Add the upper left
					if j - 1 >= 0:		
						self.nodes[i][j].neighbors += [self.nodes[i - 1][j - 1]]
					# Add the upper center
					self.nodes[i][j].neighbors += [self.nodes[i - 1][j]]
					# Add the upper right
					if j + 1 < self.gridWidth:
						self.nodes[i][j].neighbors += [self.nodes[i - 1][j + 1]]

				# Add the center row of neighbors
				# Add the left center
				if j - 1 >= 0:
					self.nodes[i][j].neighbors += [self.nodes[i][j - 1]]
				# Add the right center
				if j + 1 < self.gridWidth:
					self.nodes[i][j].neighbors += [self.nodes[i][j + 1]]
				
				# Add the bottom row of neighbors
				if i + 1 < self.gridHeight:
					# Add the lower left
					if j - 1 >= 0:
						self.nodes[i][j].neighbors += [self.nodes[i + 1][j - 1]]
					# Add the lower center
					self.nodes[i][j].neighbors += [self.nodes[i + 1][j]]
					# Add the lower right
					if j + 1 < self.gridWidth:
						self.nodes[i][j].neighbors += [self.nodes[i + 1][j + 1]]

	def getNodeFromPoint(self, point):
		""" Get the node in the graph that corresponds to a point in the world """
		return self.nodes[int(point.y/Constants.GRID_SIZE)][int(point.x/Constants.GRID_SIZE)]

	def placeObstacle(self, point, color):
		""" Place an obstacle on the graph """
		node = self.getNodeFromPoint(point)

		# If the node is not already an obstacle, make it one
		if node.isWalkable:
			# Indicate that this node cannot be traversed
			node.isWalkable = False		

			# Set a specific color for this obstacle
			node.color = color
			for neighbor in node.neighbors:
				neighbor.neighbors.remove(node)
			node.neighbors = []
			self.obstacles += [node]

	def reset(self):
		""" Reset all the nodes for another search """
		for i in range(self.gridHeight):
			for j in range(self.gridWidth):
				self.nodes[i][j].reset()

	def buildPath(self, endNode):
		""" Go backwards through the graph reconstructing the path """
		path = []
		node = endNode
		while node:
			node.isPath = True
			path = [node] + path
			node = node.backNode

		# If there are nodes in the path, reset the colors of start/end
		if len(path) > 0:
			path[0].isPath = False
			path[0].isStart = True 
			path[-1].isPath = False
			path[-1].isEnd = True
		return path

	# user input, finds which algorithm to switch to
	def findPath(self, start, end):
		# breadth first
		if UserInterface.CurrentSearchAlogrithm == SearchAlgorithm.BREADTH_FIRST:
			return self.findPath_Breadth(start, end)
		# djikstra
		elif UserInterface.CurrentSearchAlogrithm == SearchAlgorithm.DJIKSTRA:
			return self.findPath_Djikstra(start, end)
		# A*
		elif UserInterface.CurrentSearchAlogrithm == SearchAlgorithm.A_STAR:
			return self.findPath_AStar(start, end)
		# best first
		elif UserInterface.CurrentSearchAlogrithm == SearchAlgorithm.BEST_FIRST:
			return self.findPath_BestFirst(start, end)
		else:
			return []

	def findPath_Breadth(self, start, end):
		""" Breadth Search """
		self.reset()

		# TODO: Add your breadth-first code here!
		# used psuedo code from power point
		toVisit = Queue()
		toVisit.put(start)
		start.isVisited = True

		# while the list to visit nodes is not empty
		while not toVisit.empty():
			currentNode = toVisit.get()
			currentNode.isExplored = True

			# goes through the nodes
			for nextNode in currentNode.neighbors:
				if not nextNode.isVisited:
					toVisit.put(nextNode)
					nextNode.isVisited = True
					nextNode.backNode = currentNode

					if nextNode == end:
						return self.buildPath(end)

		return []

	def findPath_Djikstra(self, start, end):
		""" Djikstra's Search """
		self.reset()		

		# TODO: Add your Djikstra code here!
		# used psuedo code from power point
		toVisit = PriorityQueue()

		start.isVisited = True
		start.cost = 0 
		toVisit.put(start)

		# while the list to visit nodes is not empty
		while not toVisit.empty():
			currentNode = toVisit.get()
			currentNode.isExplored = True
			if currentNode == end:
				return self.buildPath(end)

			# goes through the nodes
			for nextNode in currentNode.neighbors:
				distToNext = (nextNode.center - currentNode.center).length()
				if not nextNode.isVisited:
					nextNode.isVisited = True
					nextNode.cost = distToNext + currentNode.cost
					nextNode.backNode = currentNode
					toVisit.put(nextNode)
				else:
					if distToNext + currentNode.cost < nextNode.cost:
						nextNode.cost = distToNext + currentNode.cost
						nextNode.backNode = currentNode

		return []

	def findPath_AStar(self, start, end):
		""" A Star Search """
		self.reset()

		# TODO: Add your A-star code here!
		# combination of others
		toVisit = PriorityQueue()

		start.isVisited = True
		# finds estimated and actual 
		start.costFromStart = 0
		start.costToEnd = (end.center - start.center).length()
		start.cost = start.costFromStart + start.costToEnd
		toVisit.put(start)

		# while the list to visit nodes is not empty
		while not toVisit.empty():
			currentNode = toVisit.get()
			currentNode.isExplored = True
			if currentNode == end:
				return self.buildPath(end)

			# goes through the nodes
			for nextNode in currentNode.neighbors:
				distToNext = (nextNode.center - currentNode.center).length()
				distToEnd = (end.center - nextNode.center).length()

				if not nextNode.isVisited:
					nextNode.isVisited = True
					nextNode.costFromStart = distToNext + currentNode.costFromStart
					nextNode.costToEnd = distToEnd
					nextNode.cost = nextNode.costFromStart + nextNode.costToEnd
					nextNode.backNode = currentNode
					toVisit.put(nextNode)
				else:
					if distToNext + currentNode.costFromStart < nextNode.costFromStart:
						nextNode.costFromStart = distToNext + currentNode.costFromStart
						nextNode.cost = nextNode.costFromStart + distToEnd
						nextNode.backNode = currentNode

		return []

	def findPath_BestFirst(self, start, end):
		""" Best First Search """
		self.reset()

		# TODO: Add your Best-first code here!
		# combination of others
		toVisit = PriorityQueue()

		start.isVisited = True
		start.cost = (end.center - start.center).length()
		toVisit.put(start)

		# while the list to visit nodes is not empty
		while not toVisit.empty():
			currentNode = toVisit.get()
			currentNode.isExplored = True
			if currentNode == end:
				return self.buildPath(end)

			# goes through the nodes
			for nextNode in currentNode.neighbors:
				distToEnd = (end.center - nextNode.center).length()
				if not nextNode.isVisited:
					nextNode.isVisited = True
					nextNode.cost = distToEnd
					nextNode.backNode = currentNode
					toVisit.put(nextNode)
				else:
					if distToEnd < nextNode.cost:
						nextNode.cost = distToEnd
						nextNode.backNode = currentNode
		return []

	def draw(self, screen):
		""" Draw the graph """
		for i in range(self.gridHeight):
			for j in range(self.gridWidth):
				self.nodes[i][j].draw(screen)