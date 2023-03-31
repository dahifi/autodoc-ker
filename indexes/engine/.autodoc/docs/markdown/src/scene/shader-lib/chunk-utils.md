[View code on GitHub](https://github.com/playcanvas/engine/src/scene/shader-lib/chunk-utils.js)

The code above defines two tables, `decodeTable` and `encodeTable`, which map texture encodings to their corresponding decoding and encoding functions, respectively. The `ChunkUtils` class provides two static methods, `decodeFunc` and `encodeFunc`, which take an encoding string as input and return the name of the corresponding decoding or encoding function from the appropriate table. If the input encoding is not found in the table, the default function `decodeGamma` or `encodeGamma` is returned.

This code is likely used in the larger PlayCanvas engine project to facilitate the decoding and encoding of textures with different encodings. By providing a mapping between encodings and their corresponding functions, this code allows other parts of the engine to easily access the appropriate decoding or encoding function for a given texture. For example, if a texture is encoded with the `rgbm` encoding, another part of the engine could use `ChunkUtils.decodeFunc('rgbm')` to retrieve the name of the corresponding decoding function, `decodeRGBM`, and then use that function to decode the texture.

Here is an example of how this code might be used in the larger PlayCanvas engine project:

```
import { ChunkUtils } from 'playcanvas-engine';

// assume we have a texture with the encoding 'srgb'
const textureEncoding = 'srgb';

// get the name of the decoding function for the texture encoding
const decodeFuncName = ChunkUtils.decodeFunc(textureEncoding);

// retrieve the actual decoding function from the appropriate module
const decodeFunc = require(`playcanvas-engine/decoders/${decodeFuncName}`);

// use the decoding function to decode the texture
const decodedTexture = decodeFunc(textureData);
```
## Questions: 
 1. What is the purpose of the `decodeTable` and `encodeTable` objects?
    - The `decodeTable` and `encodeTable` objects map texture encodings to their corresponding decode and encode functions, respectively.

2. What is the significance of the `ChunkUtils` class?
    - The `ChunkUtils` class provides static methods for retrieving the appropriate decode and encode functions based on a given texture encoding.

3. What happens if an unknown texture encoding is passed to the `decodeFunc` or `encodeFunc` methods?
    - If an unknown texture encoding is passed to the `decodeFunc` or `encodeFunc` methods, the default `decodeGamma` or `encodeGamma` function will be returned, respectively.