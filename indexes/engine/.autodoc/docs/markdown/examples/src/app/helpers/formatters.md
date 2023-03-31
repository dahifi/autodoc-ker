[View code on GitHub](https://github.com/playcanvas/engine/examples/src/app/helpers/formatters.mjs)

The code provided is a module that exports several utility functions used in the PlayCanvas engine project. These functions are used to extract information from text files containing JavaScript or TypeScript code.

The `findClosingBracketMatchIndex` function takes a string and a position and returns the index of the closing bracket that matches the opening bracket at the given position. This function is used to find the end of a function definition in a text file.

The `getTypeScriptFunctionFromText` function takes a string of TypeScript code and returns the text of the function that matches a specific signature. This function is used to extract the example function from a TypeScript file.

The `getInnerFunctionText` function takes a string of JavaScript code and returns the text of the inner function. This function is used to extract the inner function from a JavaScript file.

The `getExampleClassFromTextFile` function takes a Babel object and a string of JavaScript or TypeScript code and returns the transformed code as a string. This function is used to transform the example class code to be compatible with the PlayCanvas engine.

The `getEngineTypeFromClass` function takes a string of JavaScript or TypeScript code and returns the engine type used in the example class. This function is used to determine whether the engine is in debug or performance mode.

The `getWebgpuEnabledFromClass` function takes a string of JavaScript or TypeScript code and returns a boolean indicating whether WebGPU is enabled in the example class. This function is used to determine whether WebGPU is enabled in the example.

The `classIncludesMiniStats` function takes a string of JavaScript or TypeScript code and returns a boolean indicating whether the example class includes MiniStats. This function is used to determine whether MiniStats is included in the example.

The `retrieveStaticObject` function takes a string of JavaScript or TypeScript code and a name and returns the static object with the given name. This function is used to retrieve static objects from the example class.

Overall, these functions are used to extract information from example code files and transform them to be compatible with the PlayCanvas engine. They are used to provide examples and documentation for the engine's features and capabilities.
## Questions: 
 1. What does the `findClosingBracketMatchIndex` function do?
- This function finds the index of the closing bracket that matches the opening bracket at the given position in the input string.

2. What is the purpose of the `getExampleClassFromTextFile` function?
- This function transforms the input text using Babel and returns the transformed text, with certain replacements and modifications made to the original text.

3. What does the `retrieveStaticObject` function do?
- This function retrieves a static object from the input text by finding the start and end indices of the object and returning the substring that represents the object.