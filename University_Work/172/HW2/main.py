from movie import Movie
from song import Song
from picture import Picture
import sys

media = []
	
def parse_command(command):

	params = command.split(' ')
	
	#print(params)
	
	#======= Start of exit =======
	if params[0] == 'exit':
		print('Closing the media library')
		sys.exit(0)
	#======= End of exit =======
	
	#======= Start of help =======
	elif params[0] == 'help':
		print('\nHere are a list of commands:')
		print('new {type} {name} {rating} [additional params]', 'will create a name media file with the corrospinding values')
		print('\t {type} of movie requires a director and runtime')
		print('\t {type} of song requires an artist and album')
		print('\t {type} of picture requires a resolution')
		print('play {type} {name}', '----> will play a song/movie with the given type, {type} and name {name}')
		print('display {picName}', '----> will display the picture with the name {picName}')
		print('list {type}', '----> will list picture, song, movie, or all media')
		print('exit', '----> will exit the media library.')
		print('')
	#======= End of help =======
	
	#======= Start of new =======
	elif params[0] == 'new':
		#======= Start of general params =======
		try:
			type = params[1]
			if type not in ['song', 'picture', 'movie']:
				print('The type must be song, picture, or movie.')
				return
		except:
			print('Missing type')
			return
			
		try:
			name = params[2]
		except:
			print('Missing name')
			return
			
		try:
			rating = params[3]
			try:
				rating = int(rating)
			except:
				print('Rating must be an integer.')
				return
		except:
			print('Missing rating')
			return
		#======= End of general params =======
		
		#======= Start of song =======
		if type == 'song':
			try:
				artist = params[4]
			except:
				print('Missing artist')
				return
				
			try:
				album = params[5]
			except:
				print('Missing album')
				return
			new_song = Song(type, name, rating, artist, album)
			media.append(new_song)
			print(new_song, '\nCreated!\n')
		#======= End of song =======
		
		#======= Start of movie =======
		elif type == 'movie':
			try:
				director = params[4]
			except:
				print('Missing director')
				return
				
			try:
				runtime = params[5]
				try:
					runtime = int(runtime)
					if runtime < 1:
						print('Runtime should be 1 or greater')
						return
				except:
					print('Runtime  must be an integer')
					return
			except:
				print('Missing runtime')
				return
			new_movie = Movie(type, name, rating, director, runtime)
			media.append(new_movie)
			print(new_movie, '\nCreated!\n')
		#======= End of movie =======
		
		#======= Start of picture =======
		elif type == 'picture':
			try:
				resolution = params[4]
				try:
					resolution = int(resolution)
					if resolution < 200:
						print('Resolution should be 200 or greater')
						return
				except:
					print('Resolution  must be an integer')
					return
			except:
				print('Missing resolution')
				return
			new_picture = Picture(type, name, rating, resolution)
			media.append(new_picture)
			print(new_picture, '\nCreated\n')
		#======= End of picture =======
		
		else:
			print('Invalid medie type. Use song, movie, or picture.')
	#======= End of new =======
	
	#======= Start of play =======
	elif params[0] == 'play':
		try:
			type = params[1]
		except:
			print('Missing type')
			return
			
		if type not in ['song', 'movie']:
			print('That is not a valid type. Use song or movie.')
			return
		
		try:
			name = params[2]
		except:
			print('Missing name')
			return
		for m in media:
			if m.get_type() == type and m.get_name() == name:
				m.play()
				return
		print('There is no', type, 'with the name', name)
	#======= End of play =======
	
	#======= Start of display =======
	elif params[0] == 'display':
		try:
			name = params[1]
		except:
			print('Missing name')
			return
		for m in media:
			if m.get_type() == 'picture' and m.get_name() == name:
				m.show()
				return
		print('There is no picture with the name', name)
	#======= End of display =======
	
	#======= Start of list =======
	elif params[0] == 'list':
		try:
			type = params[1]
			if type not in ['song', 'picture', 'movie', 'all']:
				print('The type must be all, song, picture, or movie.')
				return
		except:
			print('Missing type')
			return
		if type in ['song', 'picture', 'movie']:
			print('Your', type,'library contains:')
			for m in media:
				if m.get_type() == type:
					print(m)
		else:
			print('Your library contains:')
			for m in media:
				print(str(m))
	#======= End of list =======
	else:
		print('Invalid command. ')

def main():
	s1 = Song('song', 'Song1', 1, 'Artist 1', 'Album 1')
	s2 = Song('song', 'Song2', 2, 'Artist 2', 'Album 2')
	s3 = Song('song', 'Song3', 3, 'Artist 3', 'Album 3')
	s4 = Song('song', 'Song4', 4, 'Artist 4', 'Album 4')
	
	m1 = Movie('movie', 'Movie1', 1, 'Director 1', 120)
	m2 = Movie('movie', 'Movie2', 2, 'Director 2', 240)
	m3 = Movie('movie', 'Movie3', 3, 'Director 3', 360)
	m4 = Movie('movie', 'Movie4', 4, 'Director 4', 480)
	
	p1 = Picture('picture', 'Picture1', 1, 200)
	p2 = Picture('picture', 'Picture2', 2, 400)
	p3 = Picture('picture', 'Picture3', 3, 600)
	p4 = Picture('picture', 'Picture4', 4, 800)
	
	media.append(s1)
	media.append(s2)
	media.append(s3)
	media.append(s4)
	
	media.append(m1)
	media.append(m2)
	media.append(m3)
	media.append(m4)
	
	media.append(p1)
	media.append(p2)
	media.append(p3)
	media.append(p4)
	
	print('Welcome to your media library!')
	print('Type \'help\' for a list of commands\n')
	
	while True:
		command = input('\nEnter a command:\n')
		parse_command(command)
		



main()