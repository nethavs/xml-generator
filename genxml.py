#!/usr/bin/env python
# 
# Script for generation of XML documents of 
# user specified size and element nesting depth
#
# author: Edmon Begoli
#
from xml.dom.minidom import Document
from optparse import OptionParser

import sys 
import string 
import random
import codecs

tree = """  <top-tree top-tree-id="1">
      <tree-level1>
       <tree-level2>
        <tree-level3>
         <tree-level4>
          <tree-level5>
           <text-node1>text1</text-node1>
           <subtext1>
            <text-node2>text2
            </text-node2>
            </subtext1>
           <text-node3>text3</text-node3>
           <text-node4>text4</text-node4>
           <text-node5>text3</text-node5>
           </append-node>
         </tree-level5>
         </tree-level4>
        </tree-level3>
       </tree-level2>
      </tree-level1>
    </top-tree>\n"""


elements = [ "address","selector","name","location","organization",
             "place","area","person","id","class","base","cost",
             "unit", "object", "track", "subject", "package"]

words =["Adult","Aeroplane","Air","Aircraft Carrier","Airforce","Airport",
"Album","Alphabet",
"Apple","Arm","Army","Baby","Baby","Backpack","Balloon","Banana",
"Bank","Barbecue","Bathroom","Bathtub","Bed","Bed","Bee","Bible",
"Bible","Bird","Bomb","Book","Boss","Bottle","Bowl","Box",
"Boy","Brain","Bridge","Butterfly","Button","Cappuccino","Car","Car-race",
"Carpet","Carrot","Cave","Chair","Chess Board","Chief","Child","Chisel",
"Chocolates","Church","Circle","Circus","Circus","Clock","Clown","Coffee",
"Coffee-shop","Comet","Compact Disc","Compass","Computer","Crystal","Cup",
"Cycle",
"Data Base","Desk","Diamond","Dress","Drill","Drink","Drum","Dung",
"Ears","Earth","Egg","Electricity","Elephant","Eraser","Explosive","Eyes",
"Family","Fan","Feather","Festival","Film","Finger","Fire","Floodlight",
"Flower","Foot","Fork","Freeway","Fruit","Fungus","Game","Garden",
"Gas","Gate","Gemstone","Girl","Gloves","God","Grapes","Guitar",
"Hammer","Hat","Hieroglyph","Highway","Horoscope","Horse","Hose","Ice",
"Ice-cream","Insect","Jet fighter","Junk","Kaleidoscope","Kitchen","Knife",
"Leather jacket",
"Leg","Library","Liquid","Magnet","Man","Map","Maze","Meat",
"Meteor","Microscope","Milk","Milkshake","Mist","Money","Monster","Mosquito",
"Mouth","Nail","Navy","Necklace","Needle","Onion","PaintBrush","Pants",
"Parachute","Passport","Pebble","Pendulum","Pepper","Perfume","Pillow",
"Plane","Planet","Pocket","Post-office","Potato","Printer","Prison","Pyramid",
"Radar","Rainbow","Record","Restaurant","Rifle","Ring","Robot","Rock",
"Rocket","Roof","Room","Rope","Saddle","Salt","Sandpaper","Sandwich",
"Satellite","School","Ship","Shoes","Shop","Shower","Signature","Skeleton",
"Slave","Snail","Software","Solid","Space Shuttle","Spectrum","Sphere",
"Spice","Spiral","Spoon","Sports-car","Spot Light","Square","Staircase",
"Star","Stomach","Sun","Sunglasses","Surveyor","Swimming Pool","Sword",
"Table","Tapestry","Teeth","Telescope",
"Television","Tennis racquet","Thermometer","Tiger","Toilet","Tongue",
"Torch","Torpedo",
"Train","Treadmill","Triangle","Tunnel","Typewriter","Umbrella","Vacuum",
"Vampire","Vulture","Water","Weapon","Web","Wheelchair","Window","Woman",
"Worm","X-ray"]

def main():
   """ """
   produced_bytes = 0

   print sys.maxunicode
   
   description = "Command line arguments for xml generation"
   parser = OptionParser( description )

   parser.add_option( "-o", "--output", dest="output",default="sample.xml",
                      help="Write output to file", metavar="FILE" )
   parser.add_option( "-s", "--size", type="float", dest="requested_bytes", 
                      default=0.1,
                      help="Size in (MB) of generated XML e.g. 1000 for"
                      " gigabyte or 0.5 for half a megabyte."
                      " Default size is 0.5 MB" )
   parser.add_option( "-r", "--random-structure", action="store_true",
                      dest="random_structure", default=False )

   (options, args) = parser.parse_args()

   out = open( options.output, "w" )
   #convert MB value into bytes 
   print options.requested_bytes
   requested_bytes = (options.requested_bytes * 1048576)

   print "size " + str( options.requested_bytes )   
   print " in bytes "  + str( requested_bytes )

   out.write( codecs.BOM_UTF8 )
   out.write( "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n" )
   out.write( "<root>\n" )
   
   while produced_bytes < requested_bytes:
      out.write( tree )
      produced_bytes = produced_bytes + len( tree )
   
   out.write( "</root>" )
   out.close()

# Creates random text node
#
#
def get_randomized_tree():
   return ""
   
def get_randomized_tree_text():
   return ""

if __name__ == "__main__":
   main()

