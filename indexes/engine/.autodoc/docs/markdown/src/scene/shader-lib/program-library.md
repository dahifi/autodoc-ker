[View code on GitHub](https://github.com/playcanvas/engine/src/scene/shader-lib/program-library.js)

The `ProgramLibrary` class is responsible for creating and caching shaders used in the PlayCanvas engine. It has two levels of cache: the first level generates the shader based on the provided options, while the second level processes this generated shader using processing options, which in most cases modifies it to support uniform buffers. 

The class has two caches: `processedCache` and `definitionsCache`. `processedCache` is a map of shaders processed using processing options, while `definitionsCache` is a map of shader definitions before processing. 

The `ProgramLibrary` class has several methods for generating and caching shaders. The `generateShaderDefinition` method generates a shader definition for a given generator, name, key, and options. The `getProgram` method gets a shader program for a given name, options, and processing options. It generates a key for shader source code generation, a key for its further processing to work with uniform buffers, and a final key to get the processed shader from the cache. If the final processed shader is not found in the cache, it generates a new shader definition and adds it to the processed cache. 

The `storeNewProgram` method stores a new program in the unique non-cached programs collection to dump and update game shaders cache. The `dumpPrograms` method generates a script for precompiling shaders. The `clearCache` method clears the cache of processed shaders. The `removeFromCache` method removes a shader from the cache. 

The `ProgramLibrary` class is used in the PlayCanvas engine to create and cache shaders. It is used in conjunction with other classes and modules in the engine to render graphics. For example, the `Shader` class is used to create shaders, while the `StandardMaterialOptions` class is used to set options for standard materials. 

Overall, the `ProgramLibrary` class is an important part of the PlayCanvas engine, as it is responsible for generating and caching shaders used in rendering graphics.
## Questions: 
 1. What is the purpose of the `ProgramLibrary` class?
- The `ProgramLibrary` class is responsible for creating and caching required shaders for the PlayCanvas engine.
2. What are the two level caches used by the `ProgramLibrary` class?
- The first level cache generates the shader based on the provided options, while the second level processes this generated shader using processing options, in most cases modifying it to support uniform buffers.
3. What is the purpose of the `dumpPrograms` method?
- The `dumpPrograms` method is used to build a shader options script by dumping the collection of unique non-cached programs and updating the game shaders cache.