[View code on GitHub](https://github.com/playcanvas/engine/src/scene/shader-lib/get-program-library.js)

The code above is a module that exports two functions: `getProgramLibrary` and `setProgramLibrary`. These functions are used to manage a cache of program libraries for different graphics devices in the PlayCanvas engine.

The `getProgramLibrary` function takes a `GraphicsDevice` object as its parameter and returns the corresponding `ProgramLibrary` object from the cache. If the library is not found in the cache, an assertion error is thrown. 

Here is an example of how `getProgramLibrary` can be used:

```javascript
import { getProgramLibrary } from 'playcanvas-engine';

const device = new GraphicsDevice();
const programLibrary = getProgramLibrary(device);
```

The `setProgramLibrary` function takes a `GraphicsDevice` object and a `ProgramLibrary` object as its parameters. It assigns the `ProgramLibrary` object to the cache for the corresponding `GraphicsDevice`. If the library is not provided, an assertion error is thrown.

Here is an example of how `setProgramLibrary` can be used:

```javascript
import { setProgramLibrary } from 'playcanvas-engine';

const device = new GraphicsDevice();
const programLibrary = new ProgramLibrary();
setProgramLibrary(device, programLibrary);
```

Overall, this module provides a way to manage program libraries for different graphics devices in the PlayCanvas engine. By caching program libraries, the engine can avoid the overhead of compiling shaders every time they are used.
## Questions: 
 1. What is the purpose of the `program-library.js` file that is being imported?
   - The `program-library.js` file contains a class called `ProgramLibrary` that is being used to create instances of program libraries.
2. What is the `DeviceCache` class and how is it being used in this code?
   - The `DeviceCache` class is a cache that stores device-specific data. In this code, it is being used to store instances of program libraries for each device.
3. Why are there `Debug.assert` statements in the code and what do they do?
   - The `Debug.assert` statements are used to check if a condition is true and throw an error if it is not. In this code, they are being used to ensure that the program library being accessed or assigned is not null.