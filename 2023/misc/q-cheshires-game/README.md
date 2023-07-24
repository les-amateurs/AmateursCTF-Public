# q-CHeSHire's game

## Author: flocto

**Solves:** 8

**Points:** 496

---

A friendly cat approaches you with an interesting game. If you can win enough times, maybe it'll give you the flag?

This challenge was done on Qiskit version 0.42.1. See `template.py` for an example of server interaction.

`nc amt.rs 31011`

---

**Provided Files:**

- [q-cheshires-game.py](./q-cheshires-game.py)
- [template.py](./template.py)

## Solution

Originally, I intended this challenge to be a copy paste of the CHSH Game, but realized that my setup allowed for an interesting "vulnerability". Typically, you aren't
given access to both qubits, so there should be a way to get higher than the 85% optimal win rate from the original CHSH Game.

After finicking with gates for a while, I stumbled upon a 87.5% win rate combination (seen below), which I felt was a decent improvement and left it at that. Unfortunately, I probably should have bumped up the required win rate just a little since there were still quite a few solves from people just brute forcing.

For example:
```
T1BFTlFBU00gMi4wOwppbmNsdWRlICJxZWxpYjEuaW5jIjsKcXJlZyBxWzJdOwpjcmVnIGNbMV07Cg==
T1BFTlFBU00gMi4wOwppbmNsdWRlICJxZWxpYjEuaW5jIjsKcXJlZyBxWzJdOwpjcmVnIGNbMV07CmN4IHFbMF0scVsxXTsKaCBxWzBdOwp4IHFbMF07CmggcVswXTsKY3ggcVswXSxxWzFdOwo=
T1BFTlFBU00gMi4wOwppbmNsdWRlICJxZWxpYjEuaW5jIjsKcXJlZyBxWzJdOwpjcmVnIGNbMV07Cg==
T1BFTlFBU00gMi4wOwppbmNsdWRlICJxZWxpYjEuaW5jIjsKcXJlZyBxWzJdOwpjcmVnIGNbMV07CmN4IHFbMF0scVsxXTsKaCBxWzBdOwpjeCBxWzBdLHFbMV07CmggcVswXTsKY3ggcVswXSxxWzFdOwo=
```
and
```
T1BFTlFBU00gMi4wOwppbmNsdWRlICJxZWxpYjEuaW5jIjsKcXJlZyBxWzJdOwpjcmVnIGNbMV07Cg==
T1BFTlFBU00gMi4wOwppbmNsdWRlICJxZWxpYjEuaW5jIjsKcXJlZyBxWzJdOwpjcmVnIGNbMV07CmN4IHFbMF0scVsxXTsKaCBxWzBdOwp4IHFbMF07CmggcVswXTsKY3ggcVswXSxxWzFdOwo=
T1BFTlFBU00gMi4wOwppbmNsdWRlICJxZWxpYjEuaW5jIjsKcXJlZyBxWzJdOwpjcmVnIGNbMV07Cg==
T1BFTlFBU00gMi4wOwppbmNsdWRlICJxZWxpYjEuaW5jIjsKcXJlZyBxWzJdOwpjcmVnIGNbMV07CmN4IHFbMF0scVsxXTsKaCBxWzBdOwpjeCBxWzBdLHFbMV07CmggcVswXTsKY3ggcVswXSxxWzFdOwo=
```

Update: Someone found a 100% solution :scream:. Alice and Bob use the same strategy. 
```py
circ_0 = QuantumCircuit(2, 1)

circ_1 = QuantumCircuit(2, 1)
# Z axis control
# If Z was applied to qubit 0, its state will be |0>-|1> instead of |0>+|1>,
# use the phase difference to conditionally flip the second qubit iff both
# input bits are 1 (that is, if this circuit is applied twice).
circ_1.ry(pi/2, 0)
circ_1.cx(0, 1)
circ_1.ry(-pi/2, 0)
# Apply Z
# This doesn't affect measurement probabilities
circ_1.z(0)
```