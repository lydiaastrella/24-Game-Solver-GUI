import globalvar 
import backend1 as bk

import sys
import random
import kivy
kivy.require('1.9.1')

from globalvar import Nilai, Operan, string, Operator, Solusi, Bracket, Hasil
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

def shuffle():
	global SymbolsList, SpadesCard, HeartCard, ClubCard, DiamondCard

	Symbol = random.choice(SymbolsList)
	if (Symbol =='S'):
		Card = random.choice(SpadesCard)
		SpadesCard.remove(Card)
		if (len(SpadesCard) == 0):
			SymbolsList.remove('S')
	elif (Symbol =='H'):
		Card = random.choice(HeartCard)
		HeartCard.remove(Card)
		if (len(HeartCard) == 0):
			SymbolsList.remove('H')
	elif (Symbol =='C'):
		Card = random.choice(ClubCard)
		ClubCard.remove(Card)
		if (len(ClubCard) == 0):
			SymbolsList.remove('C')
	elif (Symbol =='D'):
		Card = random.choice(DiamondCard)
		DiamondCard.remove(Card)
		if (len(DiamondCard) == 0):
			SymbolsList.remove('D')
	return Card,Symbol

def shuffleAll():
	global SymbolsList, SpadesCard, HeartCard, ClubCard, DiamondCard,Card
	Card = []
	for i in range(4):
		C,S = shuffle()
		Card.append(str(C) + S)
	return Card

def countDeck():
	global SpadesCard, HeartCard, ClubCard, DiamondCard
	return (len(SpadesCard) + len(HeartCard) + len(ClubCard) + len(DiamondCard))

def set():
	global SpadesCard, HeartCard, ClubCard, DiamondCard
	A =  ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
	for x in A:
		if not x in SpadesCard:
			SpadesCard.append(x)
		if not x in HeartCard:
			HeartCard.append(x)
		if not x in ClubCard:
			ClubCard.append(x)
		if not x in DiamondCard:
			DiamondCard.append(x)
	B = ['S','H','C','D']	
	for x in B:
		if not x in SymbolsList:
			SymbolsList.append(x)

class start(Screen):
	def exit(self):
		sys.exit()		

class play(Screen):
	def draw(self):
		global SymbolsList, SpadesCard, HeartCard, ClubCard, DiamondCard, Card,Solution,countDeck,Card,Operator,Solusi,Bracket,Hasil,Operan, string, Nilai
		if (countDeck() > 0):
			self.ids.Card1.source = './PNG/gray_back.png'
			self.ids.Card2.source = './PNG/gray_back.png'
			self.ids.Card3.source = './PNG/gray_back.png'
			self.ids.Card4.source = './PNG/gray_back.png'
			Card = shuffleAll()
			Operan = []
			for i in range(4):
				if (Card[i][0]=='A'):
					Operan.append(1)
				elif (Card[i][0]=='J'):
					Operan.append(11)
				elif (Card[i][0]=='Q'):
					Operan.append(12)
				elif (Card[i][0]=='K'):
					Operan.append(13)
				elif(Card[i][0]== '1'):
					Operan.append(10)
				else:
					Operan.append(int(Card[i][0]))
			bk.SortNilai(Operan)
			bk.Greedy(Operan,Operator,Solusi)
			bk.PrintSolusi(Solusi)
			Solution = ''
			equation =' '.join(string)
			try :
				Nilai = eval(equation)
			except ZeroDivisionError:
				Nilai =0
			Solution = ''.join(string) + ' = ' + str(Nilai)
			source = []
			for i in range(4):
				source.append ('./PNG/' + str(Card[i]) + '.PNG')
			self.ids.Card1.source = str(source[0])
			self.ids.Card2.source = str(source[1])
			self.ids.Card3.source = str(source[2])
			self.ids.Card4.source = str(source[3])
			self.current = 'play'
			self.ids.Card_on_Deck.text =  str(countDeck())
			self.ids.Solution.text = Solution
			del Solusi[:]
			del string[:]
			Solution = ''

		else:
			box = BoxLayout(orientation = 'vertical', padding = (10))
			box.add_widget(Label(text = "Card on Deck is empty !\n Please Reset or Exit",halign = 'center'))
			btn = Button(text = "Got it",size_hint= (0.95,0.5))
			box.add_widget(btn)

			popup = Popup(title='Card on Deck is empty',content= box ,size_hint=(0.25, 0.3),auto_dismiss = False)
			btn.bind(on_press=(popup.dismiss))
			popup.open()


	def reset(self):
		global SymbolsList, SpadesCard, HeartCard, ClubCard, DiamondCard,countDeck
		set()
		self.ids.Card1.source = './PNG/gray_back.png'
		self.ids.Card2.source = './PNG/gray_back.png'
		self.ids.Card3.source = './PNG/gray_back.png'
		self.ids.Card4.source = './PNG/gray_back.png'
		self.ids.Card_on_Deck.text =  str(countDeck())
		self.ids.Solution.text = '-'
		self.current = 'play'

	def exit(self):
		sys.exit()

class main(App):
	global SymbolsList, SpadesCard, HeartCard, ClubCard, DiamondCard, Card,Solution,countDeck
	Builder.load_file("GUItest.kv")
	def build(self):
		sm = ScreenManager()
		sm.add_widget(start(name='start'))
		sm.add_widget(play(name='play'))
		return sm

SpadesCard = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
HeartCard = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
ClubCard = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
DiamondCard = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
SymbolsList = ['S','H','C','D']

if __name__ == '__main__':
	aString = 'this is a test'
	aString = aString[:6] + 'Python!'
	aString = 'different string altogether'
	Solution = ''
	main().run()