# CMPS 2200 Assignment 4
## Answers

**Name:**_Reid Miller_


Place all written answers from `assignment-04.md` here for easier grading.

1. 

a. The greedy algorithm would work as follows
- look at how much money the individual has in USD
- find the largest coin that is less than or equal to that amount in value
- exchange it for its value in USD
- repeat until the individual has converted all their money out of USD

b. 

- goal: find the least amount of coins that equals a given value in USD
- given: every coin denomination is twice the size of the denomination before it

- each individual denomination of coin can be used at most once in an optimal solution
    - if a denomination were to be used twice, it would be unoptimal
    - the next largest denomination would serve the same function with a lower quantity of coins used

- assume some value of USD = D
- the largest usable coin denomination would be k_n, where $k_n=⌊log_2(D)⌋$
    - no larger denomination would be usable, since any larger coin value would be greater than the total value in USD

- if any other denomination coin were chosen, then there would have to be a duplicate coin at some point
    - we know this since the sum $2^{k_0}+2^{k_1}+...+2^{k_{n-1}}<2^{k_n}$
    - this shows us that, without the use of coin denomination $k_n$, we would be unable to reach any $D>2^{k_n}$ without using duplicates of smaller coin denominations

- therefore, we know that the overall optimal choice at each step would be the same as the greedy choice

c.

$W(n)=O(log(n))$

$S(n)=O(log(n))$


2. 

a. Let's say their money system has coins that are equal to $1, $4, and $5. Now let's say we have $8. The greedy choice would be to take a $5 coin followed by 3 $1 coins. However, the optimal choice would be to take 2 $4 coins. In this case, the greedy algorithm would not work since the best choice at each individual point is not necessarily the best choice in the long run.

b. The number of coins written as a function of USD will be written as $C(D)$. $k_n$ will still refer to the n-th denomination. The optimal substructure would be given by:

$C(D)=min(C(i-k_n)+1)$

In the same way as before, no coin can be chosen with a greater value than D.

c.


3. 