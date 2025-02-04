
## v1.2.0   (14th September 2008)

 * The license has been changed to the ISC license.
 * Support for compiling with gcc coverage options and running tests in
   valgrind.
 * All headers now have extern "C" definitions for use in C++ programs.
 * Trie free function uses a non-recursive algorithm to avoid the possibility
   of stack overflow.

Test suite:
 * Framework added for testing memory allocation/free.
 * Tests have been fixed to properly free any memory allocated during
   execution of the test.
 * Tests have been expanded to increase the code coverage.
 * A test case has been added for testing use of the program in C++
   programs.

Bugs fixed:
 * Memory leak in hash table.
 * Bugs with the AVL tree.
 * Trie responds to out of memory scenarios correctly.

## v1.1.0   (1st June 2008)

 * Added data structures:
   - Binary Heap
   - Binomial Heap
   - Bloom Filter
 * Iterator functions changed to a model based around an iterator structure
   rather than callback functions.
 * Void pointers used for keys/values replaced by typedefs to void pointers.
   This allows the type to be changed to something else if desired.
 * Hash table sizes changed to use a set of recommended prime numbers that are
   mathematically good for use in hash tables:
     http://planetmath.org/encyclopedia/GoodHashTablePrimes.html
 * Tests added for some code that was not covered by the test suite.
 * Failed malloc() calls are now checked for.
 * Bugs fixed:
   - Lockup with set_remove function.
   - set_to_array did not include all values.

## v1.0.0   (30th January 2006)

First release.

