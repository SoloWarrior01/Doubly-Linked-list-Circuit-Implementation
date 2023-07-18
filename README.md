# Doubly Linked List Circuit Implementation in Proteus
This is a Proteus simulation of a circuit that is capable of traversing through a linked list stored in ROM.

## What the circuit is capable of?
The circuit has a ROM (IC 2732) which stores a doubly linked list in the form of array of elements. 
Every node at a particular address has the following components -
- Data element of 8 bits
- Address of next node at address+1
- Address of previous node at address+2

What the circuit does is that it traverses through the linked list and outputs the address as well as the data of the minimum data element.

## Circuital Solution
<img src="Circuit Diagram.png >
