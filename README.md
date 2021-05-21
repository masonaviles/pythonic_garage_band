# pythonic_garage_band
# by Mason Aviles

## Summary
Creating a Garage Band with Object Oriented Programming.

## Feature Tasks
- Use Python classes to model a Band made up of different kinds of musicians.
- Start with Guitarist,Bassist, and Drummer.
- Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

## Documentation

### Tests
#### Band Tests
- A Band instance should have a name attribute which is a string.
- A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
- A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
- A Band instance should have appropriate __str__ and __repr__ methods.
- A Band should have a class method to_list which returns a list of previously created Band instances
#### Musician Subclass Tests
- Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
- Each kind of Musician instance should have a get_instrument method that returns string.
- Each kind of Musician instance should have a play_solo method that returns string.

## Data Architecture (which includes a UML/WRRC)

## References & Links
- [Python docs](https://docs.python.org/3/)
- [Team Treehouse Python Basic OOP](https://teamtreehouse.com/library/basic-objectoriented-python)

