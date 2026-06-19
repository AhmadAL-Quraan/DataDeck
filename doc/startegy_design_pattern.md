# Stragtegy desing pattern 



* It's a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.


![](/pic/strategyDP.png)

## Scenario

* Imagine that you want to make a **payment service** that uses credit card.
* You want to extend it by adding a Paypal method for example.
* Adding these in one class will be hard to maintain

![](/pic/payment_example.png)
* This violates the `open/closed principle` ( closed for extension and open for modification), because everytime we want to edit this method, we will have to open this method and modify it. 
* Also it violates `single responsibility principle`, you are doing two things or more in class. 

## Solution 
* We can fix this by using **strategy DP**.
* Separate each payment logic into it's own class.

![](/pic/strategy_pattern_sol.png)

* Make a strategy interface for those classes, and abstractmethods for common behaviours(methods).

![](/pic/strategy_DP_interface.png)

* Now our context class (payment service) looks like this

![](/pic/payment_service_class.png)
* The user can use it like this
![](/pic/use_strategy.png)


- [Refactoring.guru](https://refactoring.guru/design-patterns/strategy)
- [Good vid](https://www.youtube.com/watch?v=Nrwj3gZiuJU&t=306s)

