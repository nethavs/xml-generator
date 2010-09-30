#!/usr/bin/env python
# 
# Script for generation of XML documents of 
# user specified size and element nesting depth
#
# author: Edmon Begoli
#
from xml.dom.minidom import Document

import sys 
import string 
import random


elements = [ "address","selector","name","location","organization",
             "place","area","person","id","class","base","cost",
             "unit", "object", "track", "subject", "package"]

words =["Adult","Aeroplane","Air","Aircraft Carrier","Airforce","Airport","Album","Alphabet",
"Apple","Arm","Army","Baby","Baby","Backpack","Balloon","Banana",
"Bank","Barbecue","Bathroom","Bathtub","Bed","Bed","Bee","Bible",
"Bible","Bird","Bomb","Book","Boss","Bottle","Bowl","Box",
"Boy","Brain","Bridge","Butterfly","Button","Cappuccino","Car","Car-race",
"Carpet","Carrot","Cave","Chair","Chess Board","Chief","Child","Chisel",
"Chocolates","Church","Circle","Circus","Circus","Clock","Clown","Coffee",
"Coffee-shop","Comet","Compact Disc","Compass","Computer","Crystal","Cup","Cycle",
"Data Base","Desk","Diamond","Dress","Drill","Drink","Drum","Dung",
"Ears","Earth","Egg","Electricity","Elephant","Eraser","Explosive","Eyes",
"Family","Fan","Feather","Festival","Film","Finger","Fire","Floodlight",
"Flower","Foot","Fork","Freeway","Fruit","Fungus","Game","Garden",
"Gas","Gate","Gemstone","Girl","Gloves","God","Grapes","Guitar",
"Hammer","Hat","Hieroglyph","Highway","Horoscope","Horse","Hose","Ice",
"Ice-cream","Insect","Jet fighter","Junk","Kaleidoscope","Kitchen","Knife","Leather jacket",
"Leg","Library","Liquid","Magnet","Man","Map","Maze","Meat",
"Meteor","Microscope","Milk","Milkshake","Mist","Money $$$$","Monster","Mosquito",
"Mouth","Nail","Navy","Necklace","Needle","Onion","PaintBrush","Pants",
"Parachute","Passport","Pebble","Pendulum","Pepper","Perfume","Pillow","Plane",
"Planet","Pocket","Post-office","Potato","Printer","Prison","Pyramid","Radar",
"Rainbow","Record","Restaurant","Rifle","Ring","Robot","Rock","Rocket",
"Roof","Room","Rope","Saddle","Salt","Sandpaper","Sandwich","Satellite",
"School","Ship","Shoes","Shop","Shower","Signature","Skeleton","Slave",
"Snail","Software","Solid","Space Shuttle","Spectrum","Sphere","Spice","Spiral",
"Spoon","Sports-car","Spot Light","Square","Staircase","Star","Stomach","Sun",
"Sunglasses","Surveyor","Swimming Pool","Sword","Table","Tapestry","Teeth","Telescope",
"Television","Tennis racquet","Thermometer","Tiger","Toilet","Tongue","Torch","Torpedo",
"Train","Treadmill","Triangle","Tunnel","Typewriter","Umbrella","Vacuum","Vampire",
"Vulture","Water","Weapon","Web","Wheelchair","Window","Woman","Worm",
"X-ray"]

def main():
""" """

   requested_bytes = 5000
   produced_bytes = 0

   # Create the minidom document
   doc = Document()
   root = doc.createElement( "root" )
   doc.appendChild( root )

   while produced_bytes < requested_bytes:

      top_id = 1

      # Create the <top> base element
      top = doc.createElement( "level-top" )
      top.setAttribute( "top-id", str( top_id ) )
      root.appendChild( top )

      # Create the first level element
      level1 = doc.createElement( "level1" )
      level1.setAttribute( "level-id", "1" )
      top.appendChild( level1 )

      # Create a second level element
      level2 = doc.createElement( "level2" )
      level2.setAttribute( "level-id", "2" )
      level1.appendChild( level2 )

      # Create the next element as some text
      for i in range( 5 ):
         elem_name = "sub-level" + str( i )
         sub_level = doc.createElement( elem_name )
         text1 = doc.createTextNode( words[ random.randint( 0, len( words ) - 1 ) ] )
         sub_level.appendChild( text1 )
         level2.appendChild( sub_level )

      # Print our newly created XML
      result = doc.toprettyxml( indent="  " )
      produced_bytes = produced_bytes + len( result )
      top_id = top_id + 1  

   f = open( "sample.xml", "w" )
   print "writing result of size " + str( len( result ) )
   f.write( result )   
   f.close()

# Creates random text node
#
#
def txtnode( doc ):
    elem_name = elements[ random.randint( 0, len( elements ) - 1 ) ] 
    sub_tree  =  doc.createElement( elem_name )
    text_node = doc.createTextNode( words[ random.randint( 0, len( words ) - 1 ) ] )
    sub_tree.appendChild( text_node )      
    return sub_tree

if __name__ == "__main__":
   main()

