[View code on GitHub](https://github.com/playcanvas/engine/extras/mini-stats/stats-timer.js)

The `StatsTimer` class is a utility class that provides a way to track and display performance statistics for a PlayCanvas application. It takes in several parameters, including the PlayCanvas `app` object, an array of `statNames` to track, the number of `decimalPlaces` to display, a `unitsName` string, and an optional `multiplier` value. 

The `constructor` method initializes the class properties and limits the `statNames` array to a maximum of 3 elements. It also defines a `resolve` function that recursively looks up properties of objects specified in a string. This function is used to read the specified stats from the `app.stats` object.

The `app.on` method is used to register a callback function that is called on every frame update. Within this callback function, the `values` array is updated with the current values of the specified stats, multiplied by the optional `multiplier` value. 

The `get timings` getter method returns the `values` array, which can be used to display the performance statistics in the application. 

Overall, the `StatsTimer` class provides a simple way to track and display performance statistics for a PlayCanvas application. It can be used in conjunction with other tools and techniques to optimize the performance of the application. 

Example usage:

```
const app = new pc.Application(canvas, options);

// create a StatsTimer object to track and display performance stats
const statsTimer = new StatsTimer(app, ['frame.ms', 'render.timings.foward', 'render.timings.deferred'], 2, 'ms', 0.001);

// add the StatsTimer object to the app's stats panel
app.stats.add(statsTimer);

// start the application
app.start();
```
## Questions: 
 1. What is the purpose of the StatsTimer class?
- The StatsTimer class is a timer interface for graph that reads specified stats from the app.stats object and stores them in an array.

2. What parameters does the constructor of the StatsTimer class take?
- The constructor of the StatsTimer class takes in an app object, an array of stat names, the number of decimal places to round to, a string for the units name, and an optional multiplier.

3. What event does the StatsTimer class listen for and what does it do when the event is triggered?
- The StatsTimer class listens for the 'frameupdate' event and when triggered, it reads the specified stats from the app.stats object and stores them in the values array, which can be accessed through the timings getter.