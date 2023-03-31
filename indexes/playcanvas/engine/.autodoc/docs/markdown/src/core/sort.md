[View code on GitHub](https://github.com/playcanvas/engine/src/core/sort.js)

The code above defines two functions, `cmpPriority` and `sortPriority`, which are used to sort an array of objects based on their `priority` property. 

The `cmpPriority` function takes two objects as parameters, each with a `priority` property, and returns a number indicating their relative position. It does this by subtracting the `priority` property of `b` from the `priority` property of `a`. If `a` has a higher priority than `b`, the result will be a positive number, indicating that `a` should come before `b` in the sorted array. If `b` has a higher priority, the result will be negative, indicating that `b` should come before `a`. If the priorities are equal, the result will be zero, indicating that their relative position doesn't matter.

The `sortPriority` function takes an array of objects as a parameter, where each object has at least a `priority` property. It then sorts the array in place based on the `priority` property of each object, using the `cmpPriority` function. The sorted array is then returned.

This code is likely used in the larger PlayCanvas engine project to sort arrays of objects based on their priority. This could be useful in a variety of contexts, such as rendering objects in a scene based on their distance from the camera, or updating game objects based on their importance to the gameplay. 

Here is an example of how this code could be used:

```
const objects = [
  { name: 'object1', priority: 2 },
  { name: 'object2', priority: 1 },
  { name: 'object3', priority: 3 }
];

sortPriority(objects);

console.log(objects);
// Output: [{ name: 'object2', priority: 1 }, { name: 'object1', priority: 2 }, { name: 'object3', priority: 3 }]
```

In this example, an array of objects is defined, each with a `name` and `priority` property. The `sortPriority` function is then called on the array, which sorts the objects based on their `priority` property. The sorted array is then logged to the console.
## Questions: 
 1. What is the purpose of the `cmpPriority` function?
   - The `cmpPriority` function is used to compare two objects based on their `priority` property and return a number indicating their relative position.

2. What is the input and output of the `sortPriority` function?
   - The `sortPriority` function takes an array of objects, each containing at least a `priority` property, and sorts the array in place based on the `priority` property. The function returns the sorted array.

3. Why is the `@ignore` tag used in the JSDoc comments?
   - The `@ignore` tag is used to indicate that the function should be ignored by the documentation generator. This is likely because the functions are internal and not intended to be used or documented externally.