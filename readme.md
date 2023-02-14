# BlackJack (21)

```python
This is a game of blackjack, or 21
Followed 100 days of Code with Angela Yu on Udemy
Did by self, and used her finished code to make code more efficient and teach self better ways to use 'return'
```
### How the game works
```python
deals starting hands of two cards to each player
user decides if wants new card

after each card drawn:
    check- does either player have a blackjack
    if 11 (ace) makes bust, change to value 1
when done drawing:
    if comp under 17 and does not 'have a blackjack:'
        draw until hit 17 points
        then compare scores
compare scores:
    user with blackjack wins
    no blackjack:
        if user busted- lose
    else:
        higher score under 21 wins

```

### Future implementations

```python
Looking at other Blackjack games, they involve betting.

#I would like to implement a betting system. 
    starting money
    bet throughout game
        have to look up how the betting works in blackjack

```