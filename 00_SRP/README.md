# SRP: The Single Responsibility Principle

```
A module should be responsible to one, and only one, actor.
```
<cite>Robert C.Martin: Clean Architecture</cite>

------------------------------------
## Example 1
The first example introduces the Employee class containing three methods: `calculate_pay()`, `report_hours()` and `save()`. Now this alone violates the SRP since all three functions serve a different actor. `calculate_pay()` is defined by accounting, `report_hours()` is defined by operations and `save()` is defined by the database administration. This coupling can cause problems when one actor changes the scope. A possible solution could be the implementation using a facade implementation pattern.