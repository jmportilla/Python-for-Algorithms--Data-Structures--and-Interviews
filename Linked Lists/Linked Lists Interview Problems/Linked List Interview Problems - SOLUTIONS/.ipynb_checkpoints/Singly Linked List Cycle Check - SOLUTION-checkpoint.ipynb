{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Singly Linked List Cycle Check - SOLUTION\n",
    "\n",
    "## Problem\n",
    "\n",
    "Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a \"cycle\".\n",
    "\n",
    "A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.\n",
    "\n",
    "You've been given the Linked List Node class code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Node(object):\n",
    "    \n",
    "    def __init__(self,value):\n",
    "        \n",
    "        self.value = value\n",
    "        self.nextnode = None"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solution\n",
    "\n",
    "To solve this problem we will have two markers traversing through the list. **marker1** and **marker2**. We will have both makers begin at the first node of the list and traverse through the linked list. However the second marker, marker2, will move two nodes ahead for every one node that marker1 moves.\n",
    "\n",
    "By this logic we can imagine that the markers are \"racing\" through the linked list, with marker2 moving faster. If the linked list has a cylce and is circularly connected we will have the analogy of a track, in this case the marker2 will eventually be \"lapping\" the marker1 and they will equal each other. \n",
    "\n",
    "If the linked list has no cycle, then marker2 should be able to continue on until the very end, never equaling the first marker.\n",
    "\n",
    "Let's see this logic coded out:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def cycle_check(node):\n",
    "\n",
    "    # Begin both markers at the first node\n",
    "    marker1 = node\n",
    "    marker2 = node\n",
    "\n",
    "    # Go until end of list\n",
    "    while marker2 != None and marker2.nextnode != None:\n",
    "        \n",
    "        # Note\n",
    "        marker1 = marker1.nextnode\n",
    "        marker2 = marker2.nextnode.nextnode\n",
    "\n",
    "        # Check if the markers have matched\n",
    "        if marker2 == marker1:\n",
    "            return True\n",
    "\n",
    "    # Case where marker ahead reaches the end of the list\n",
    "    return False"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Test Your Solution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ALL TEST CASES PASSED\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "RUN THIS CELL TO TEST YOUR SOLUTION\n",
    "\"\"\"\n",
    "from nose.tools import assert_equal\n",
    "\n",
    "# CREATE CYCLE LIST\n",
    "a = Node(1)\n",
    "b = Node(2)\n",
    "c = Node(3)\n",
    "\n",
    "a.nextnode = b\n",
    "b.nextnode = c\n",
    "c.nextnode = a # Cycle Here!\n",
    "\n",
    "\n",
    "# CREATE NON CYCLE LIST\n",
    "x = Node(1)\n",
    "y = Node(2)\n",
    "z = Node(3)\n",
    "\n",
    "x.nextnode = y\n",
    "y.nextnode = z\n",
    "\n",
    "\n",
    "#############\n",
    "class TestCycleCheck(object):\n",
    "    \n",
    "    def test(self,sol):\n",
    "        assert_equal(sol(a),True)\n",
    "        assert_equal(sol(x),False)\n",
    "        \n",
    "        print \"ALL TEST CASES PASSED\"\n",
    "        \n",
    "# Run Tests\n",
    "\n",
    "t = TestCycleCheck()\n",
    "t.test(cycle_check)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Good Job!"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
