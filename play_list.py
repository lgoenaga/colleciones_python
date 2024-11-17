from node_base_queue import Queue
from random import randint
import time

class Track:
  def __init__(self, title, length):
    self.title = title
    self.length = randint(3, 5)

class MediaPlayer(Queue):
  def __init__(self):
    super().__init__()
    
  def play(self, track):
    print(f"Reproduciendo: {track}")
    
  def __str__(self):
    return "MediaPlayer"

class PlayList:
  def __init__(self):
    self.queue = Queue()
    
  def add_song(self, song):
    self.queue.enqueue(song)
    
  def remove_song(self):
    return self.queue.dequeue()
    
  def show_playlist(self):
    self.queue.mostrar()
    
  def __len__(self):
    return self.queue.count
  
  def __str__(self):
    return str(self.queue)
  
play_list = PlayList()

play_list.add_song("Canción 1")
play_list.add_song("Canción 2")
play_list.add_song("Canción 3")
print()
print("Playlist")
print()
play_list.show_playlist()
print()
print(f'len: {len(play_list)}')
print()

media_player = MediaPlayer()

'''
#reproducir canciones
print("Reproduciendo canciones")
media_player.play(play_list.remove_song())
'''
print()
#reproducir todas las canciones
while play_list:
  media_player.play(play_list.remove_song())
  for i in range(randint(3, 8)):
    print("*", end=" ", flush=True)
    time.sleep(1)
  print()
print()
  