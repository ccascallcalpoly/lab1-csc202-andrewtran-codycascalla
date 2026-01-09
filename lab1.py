from typing import TypeAlias
from dataclasses import dataclass 
import unittest 
import sys 
sys.setrecursionlimit(10**6) 
 
#* Team-Member Intro Lines 
#   yo what's good it's andrewfsdf
#   its me cody
#* Data Definitions 
#*  okay
#* 1)
Celsius: TypeAlias = float
Fahrenheit: TypeAlias = float
#* 2) 
Cents: TypeAlias = int
#* 3) 
@dataclass(frozen = True)
class PriceRecord:
    name: str
    price: Cents
#* 4) 
@dataclass(frozen = True)
class MusicalNotes:
    pitch: float
    duration: float 




#* Design Recipe 
 
#* 1) 
def celsius_to_fahrenheit(cel: Celsius) -> Fahrenheit:
    return (cel * 9/5) + 32
#* 2) 
def up_one_octave(musicNote: MusicalNotes) -> MusicalNotes:
    return MusicalNotes(musicNote.pitch * 2, musicNote.duration)

#* 3) 
def second_largest(a: int, b: int, c: int) -> int:
    if(a <= b and a >= c) or (a >= b and a <= c):
        return a
    elif (b <= c and b >= a) or (b >= c and b <= a):
        return b
    else:
        return c
#* 4) 
def no_caps(string: str) -> bool:
    return string == string.lower()





class TestClass(unittest.TestCase): 
    delta: float = 1e-3
 
    #* 1) 
    def test_cels(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(10.0), 50.0, delta = self.delta)
        self.assertAlmostEqual(celsius_to_fahrenheit(45.4), 113.72, delta=self.delta)
        self.assertAlmostEqual(celsius_to_fahrenheit(267.0), 512.6, delta=self.delta)

    #* 2) 
    def test_octave(self):
        test1: MusicalNote = MusicalNote(10,10)
        expect1: MusicalNote = MusicalNote(20,10)
        self.assertEqual(up_one_octave(test1), expect1)

        test2: MusicalNote = MusicalNote(50.75,10)
        expect2: MusicalNote = MusicalNote(101.5,10)
        self.assertEqual(up_one_octave(test2), expect2)
        
    #* 3) 
    def test_second(self):
        self.assertEqual(second_largest(1,2,3), 2)
        self.assertEqual(second_largest(6,6,1), 6)
        self.assertEqual(second_largest(19,12,30), 19)

    #* 4) 
    def test_caps(self):
        self.assertEqual(no_caps("Caps"), False)
        self.assertEqual(no_caps("none"), True)
        self.assertEqual(no_caps("i have no Caps"), False)
        



# If this is True, means this .py file is the .py being executed  
# (rather than being imported by the .py that is being executed). 
if (__name__ == '__main__'):   
    print( "Running all defined tests:" ) 
 
    # What this does: find every class X that inherits from  
    # unittest.TestCase (there are two in this file) and runs 
    # every test defined inside X--every method whose name 
    # begins with "test". 
    unittest.main()
