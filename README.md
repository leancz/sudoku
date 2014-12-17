sudoku
======

A Sudoku solver

A very simple Sudoku solver. As this is just the first version you have to edit the Sudoku you want to solve
in the global called square. None for blank spaces.

Start Python and

<code>
import sudoku
sudoku.solver(sudoku.square)
</code>

and hopefully you get a solution.

The algorithm doesn't use recursion, rather it uses a stack (list.append(), list.pop()) to traverse the solution space
graph.

