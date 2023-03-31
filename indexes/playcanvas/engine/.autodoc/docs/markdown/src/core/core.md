[View code on GitHub](https://github.com/playcanvas/engine/src/core/core.js)

The code defines a root namespace for the PlayCanvas Engine and exports several variables and functions. 

The `version` and `revision` variables store the current version and revision of the PlayCanvas SDK. The `config` and `common` variables are empty objects that can be used to store configuration and common data respectively. The `apps` object is used to store information about applications that use the PlayCanvas Engine, while the `data` object is used to store exported entity data.

The `_typeLookup` function creates a lookup table for JavaScript types, which is used by the `type` function. The `type` function takes an object as an argument and returns a string representing its type. The function first checks if the object is `null` and returns `'null'` if it is. If the object is not `null`, the function uses the `typeof` operator to get the type of the object. If the type is `'undefined'`, `'number'`, `'string'`, or `'boolean'`, the function returns the type string. Otherwise, the function looks up the type string in the `_typeLookup` table based on the object's prototype.

The `extend` function takes two objects as arguments and merges their contents into a single object. The function iterates over the properties of the second object (`ex`) and copies them to the first object (`target`). If a property is an object or an array, the function recursively calls itself to copy the nested properties. The function returns the modified `target` object.

These exported variables and functions can be used by other modules in the PlayCanvas Engine to store and manipulate data, check the type of objects, and merge objects.
## Questions: 
 1. What is the purpose of the `_typeLookup` function?
    
    The `_typeLookup` function creates a lookup table for JavaScript types and their corresponding string representations.

2. What is the purpose of the `extend` function?
    
    The `extend` function merges the contents of two objects into a single object.

3. What is the purpose of the `version`, `revision`, `config`, `common`, `apps`, and `data` variables?
    
    These variables are used to store information about the PlayCanvas Engine, such as the current version and revision, configuration settings, and storage for applications and exported entity data.