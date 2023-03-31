[View code on GitHub](https://github.com/playcanvas/engine/src/scene/lighting/lighting-params.js)

The code defines a class called `LightingParams` that allows configuration of global lighting parameters for the PlayCanvas engine. The class has several private properties that are used to store the current lighting settings, such as whether area lights, shadows, or cookies are enabled, the resolution of the shadow and cookie texture atlases, and the maximum number of lights per cell. 

The class also has several public properties that can be used to modify the lighting settings, such as the number of cells along each world-space axis that the space containing lights is subdivided into, the maximum number of lights a cell can store, and the resolution of the atlas texture storing all non-directional cookie and shadow textures. 

The `applySettings` method is used to apply the current lighting settings to a given render object. This method is called internally by the engine and is not intended to be called directly by users. 

The purpose of this class is to provide a way for developers to configure the global lighting parameters of the PlayCanvas engine. This allows for greater control over the lighting in a scene and can be used to optimize performance by adjusting the number of lights and the resolution of the texture atlases. 

Here is an example of how to create a new `LightingParams` object and modify its properties:

```javascript
import { LightingParams } from 'playcanvas';

const lightingParams = new LightingParams(true, 2048, () => {
    console.log('Dirty lights function called');
});

lightingParams.cells = new Vec3(20, 5, 20);
lightingParams.maxLightsPerCell = 128;
lightingParams.shadowAtlasResolution = 4096;
lightingParams.shadowType = SHADOW_PCF5;
lightingParams.cookiesEnabled = true;
lightingParams.areaLightsEnabled = true;
lightingParams.shadowsEnabled = false;
```
## Questions: 
 1. What is the purpose of the LightingParams class?
- The LightingParams class allows configuration of global lighting parameters for clustered lighting in the PlayCanvas engine.

2. What is the significance of the debugLayer property?
- The debugLayer property specifies the layer ID of a layer to contain the debug rendering of clustered lighting. It is undefined by default, which disables the debug rendering.

3. What is the purpose of the applySettings method?
- The applySettings method applies the lighting settings from a render object to the LightingParams object, allowing for dynamic changes to the lighting parameters during runtime.