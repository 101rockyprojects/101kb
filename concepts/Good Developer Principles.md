Source: [Programming Principles NOBODY Taught Me | Shade of Code](https://www.youtube.com/watch?v=QJH0n5rMs28)
# Programming Principles NOBODY Taught Me

## Logs
First things first:
> YOUR CODE ALWAYS FAILS ON DEPLOY

Logs can be the difference between knowing what happened and spending hours guessing.
Log everything THAT MATTERS: Inputs | Output | Errors

# Tests
If you don't test, users will broke everything.
> Users are built in a way that we don't understand... Be we can foresee

Every assumption you make IS WRONG!
Test: Happy path | Common paths | Different formats | Different environment | Edge cases
> TEST FOR THE IMPOSSIBLE

# Technical Debt != sin, but a tool
You added a new little feature, WOW, but is not C L E A N.
Now you spend time in a proper abstraction, design patterns and clean architectures... Then you realize the feature have to be replaced.
> Sometimes you need to take shortcuts

Hardcoded values, copy + paste code, NOT because you are lazy.

Tech debt let you validate ideas fast:
if (newFeature.works() and  peopleLoveIt) {
	Refactor();
} else {
	timeSaved += 3 weeks;
}

Avoid P E R F E C T I O N, but usefulness.

# Naming is hard
Even for a venezuelan parent.
![Programming Fact: Naming takes time](https://miro.medium.com/v2/resize:fit:1400/1*Hgs78-x-BwXk1inYQKjyOg.jpeg)

BAD names compound FOREVER.
And DON'T USE: Data | Info | Manager | Handler

Even helps outside a legible perspective, because if you CAN'T name it properly you DON'T understand what it does.

# Localhost != Production
Your laptop is LIAR, RELIABLE and PERFECT.
Production is SLOW, UNRELIABLE and CHAOTIC.
> Different OS, different resources, different EVERYTHING.
> Deploy early and often.