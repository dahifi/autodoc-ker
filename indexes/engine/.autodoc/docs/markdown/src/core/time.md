[View code on GitHub](https://github.com/playcanvas/engine/src/core/time.js)

The code above defines a function called `now` that returns the current time in milliseconds. This function is used to measure time differences in the PlayCanvas engine project. 

The function first checks if the `window` object is defined and if the `performance` object exists within it. If both conditions are true, it checks if the `now` method exists within the `performance` object and if the `timing` property exists within the `performance` object. If all of these conditions are true, the `now` method is bound to the `performance` object and returned. 

If any of these conditions are false, the `Date.now` method is returned instead. 

This function is useful for measuring time differences in the PlayCanvas engine project, such as for calculating frame rates or animation timings. 

Here is an example of how this function could be used in the larger project:

```
const startTime = now();

// Perform some task

const endTime = now();
const elapsedTime = endTime - startTime;
console.log(`Task took ${elapsedTime} milliseconds to complete.`);
```
## Questions: 
 1. What is the purpose of this code?
   This code defines a function called `now` that returns the current time in milliseconds, which can be used to measure time differences.

2. How does the `now` function work?
   The `now` function checks if the `window` object and the `performance` object are defined, and if so, it uses the `performance.now` method to get the current time in milliseconds. Otherwise, it falls back to using the `Date.now` method.

3. Why is the `@ignore` tag used in the JSDoc comment?
   The `@ignore` tag is used to indicate that this function should not be included in the generated documentation, likely because it is an internal implementation detail that is not intended to be used directly by external code.