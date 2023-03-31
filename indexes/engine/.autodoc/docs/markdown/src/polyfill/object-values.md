[View code on GitHub](https://github.com/playcanvas/engine/src/polyfill/object-values.js)

The code above is a polyfill for the `Object.values()` method, which is used to extract the values of an object and return them as an array. This method is not supported in all browsers, so this code provides a fallback for those that do not support it.

The `Object.values()` method takes an object as its parameter and returns an array containing the values of all the enumerable properties of the object. This is useful when you need to extract the values of an object and use them in an array format.

The code above checks if the `Object.values()` method is already defined. If it is not defined, it creates a new function that uses the `Object.keys()` method to extract the keys of the object and then uses the `map()` method to return an array of the values of each key.

Here is an example of how this code can be used:

```
const myObject = { a: 1, b: 2, c: 3 };
const myArray = Object.values(myObject);
console.log(myArray); // [1, 2, 3]
```

In this example, the `Object.values()` method is used to extract the values of the `myObject` object and store them in the `myArray` array.

Overall, this code is a useful addition to the PlayCanvas engine project as it provides a fallback for the `Object.values()` method in browsers that do not support it. This ensures that the project can be used in a wider range of environments without encountering errors.
## Questions: 
 1. **What does this code do?** 
This code is defining a polyfill for the `Object.values()` method, which returns an array of the values of an object's enumerable properties.

2. **Why is a polyfill necessary for `Object.values()`?** 
The `Object.values()` method was introduced in ECMAScript 2017 and may not be supported by all browsers or environments. This polyfill ensures that the method is available even if it is not natively supported.

3. **How does this polyfill work?** 
The polyfill checks if `Object.values()` is already defined and, if not, defines it as a function that uses `Object.keys()` to get an array of the object's keys and then maps over that array to return an array of the corresponding values.