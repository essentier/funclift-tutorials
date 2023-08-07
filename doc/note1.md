Functional programming patterns

referential transparency

##

The tutorials consist of toy examples as well as practical ones. The toy examples are for showing the core concepts and basic usages of funclift. The practical examples are for demonstrating funclift in real-world scenarios.

Function composition is a foundational pillar of functional programming. Here's an example of function composition. In the example, we have two functions: Composing pure functions is straightforward. Pure functions are like math functions. They are total and they always return the same output for the same input with no side effects.

However, besides pure functions, we also have non-pure functions such as partial functions, functions that perform I/O, functions that throw exceptions and so on. We call those 'effectful' functions and we would like to compose them the way we compose pure functions.

in addition to composing pure functions, we often need to compose 'effectful' functions. Pure functions A key driving force
