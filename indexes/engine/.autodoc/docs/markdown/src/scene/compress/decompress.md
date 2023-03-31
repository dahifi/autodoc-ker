[View code on GitHub](https://github.com/playcanvas/engine/src/scene/compress/decompress.js)

The `Decompress` class is used to reconstruct the original object field names in a compressed scene. This class is part of the PlayCanvas engine project. The purpose of this class is to decompress a compressed scene by reconstructing the original object field names. This is done by iterating over the compressed scene and replacing the compressed keys with their original names.

The `Decompress` class has a constructor that takes two parameters: `node` and `data`. The `node` parameter is the current node of the object being decompressed, initially the 'entities' field of a scene. The `data` parameter is the compression metadata. The `run` method is used to start the decompression process. It checks the type of the current node and calls the appropriate method to handle it. If the node is an object, it calls the `_handleMap` method. If the node is an array, it calls the `_handleArray` method. If the node is neither an object nor an array, it sets the result to the node.

The `_handleMap` method is called when the current node is an object. It creates a new object and iterates over the keys of the current node. For each key, it calls the `_handleKey` method to replace the compressed key with the original key and recursively decompresses the value of the key.

The `_handleKey` method is called for each key in the `_handleMap` method. It takes the original key as a parameter and replaces it with the original key if the length of the key is greater than 2. If the length of the key is 1, it calls the `oneCharToKey` method of the `CompressUtils` class to replace the compressed key with the original key. If the length of the key is 2, it calls the `multCharToKey` method of the `CompressUtils` class to replace the compressed key with the original key. It then recursively decompresses the value of the key.

The `_handleArray` method is called when the current node is an array. It creates a new array and iterates over the elements of the current node. For each element, it calls the `_handleArElt` method to recursively decompress the element.

The `_handleArElt` method is called for each element in the `_handleArray` method. It takes the element as a parameter and recursively decompresses it.

This class is used in the larger PlayCanvas engine project to decompress compressed scenes. It is used to reconstruct the original object field names in a compressed scene. This class can be used as follows:

```
const decompressedScene = new Decompress(compressedScene, compressionMetadata).run();
```
## Questions: 
 1. What is the purpose of this code?
- This code defines a class called `Decompress` that is used to reconstruct original object field names in a compressed scene.

2. What parameters does the `Decompress` constructor take?
- The `Decompress` constructor takes two parameters: `node`, which is the current node of the object being decompressed, and `data`, which is compression metadata.

3. What is the output of the `run` method?
- The output of the `run` method is the result of decompressing the input object. The output is determined by the type of the input object: if it is an object, the output is a new object with decompressed keys and values; if it is an array, the output is a new array with decompressed elements; otherwise, the output is the input object itself.