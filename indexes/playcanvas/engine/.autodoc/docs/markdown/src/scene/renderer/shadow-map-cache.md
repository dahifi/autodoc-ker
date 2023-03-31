[View code on GitHub](https://github.com/playcanvas/engine/src/scene/renderer/shadow-map-cache.js)

The `ShadowMapCache` class is responsible for managing a cache of shadow maps used by lights in the PlayCanvas engine. In the normal case, each light has a unique shadow map. However, in two specific cases, the `ShadowMapCache` is used to limit allocations and re-use shadow maps. 

The first case is when lights are baked to lightmaps one at a time by the `Lightmapper`. In this case, shadow maps are re-used to limit allocations and are deleted when baking is done. The second case is when VSM (Variance Shadow Mapping) blur is done by the `ShadowRenderer`. In this case, a temporary buffer is grabbed from the cache.

The `ShadowMapCache` class has a `cache` property that is a `Map` object that maps a shadow map key to an array of shadow maps in the cache. The `getKey` method generates a string key for the shadow map required by the light. The key is based on the light's type, shadow type, and shadow resolution. If a matching shadow buffer is found in the cache, it is returned. Otherwise, a new shadow map is created and added to the cache.

The `ShadowMapCache` class has a `clear` method that removes all shadow maps from the cache. It also has a `destroy` method that clears the cache and sets it to null.

This class is used in the PlayCanvas engine to optimize the use of shadow maps and reduce memory allocations. It is used by the `Lightmapper` and `ShadowRenderer` to re-use shadow maps and limit allocations. 

Example usage:

```javascript
import { ShadowMapCache } from './shadow-map-cache.js';

const shadowMapCache = new ShadowMapCache();

// get shadow map for a light
const shadowMap = shadowMapCache.get(device, light);

// use shadow map for rendering

// return shadow map to cache
shadowMapCache.add(light, shadowMap);

// clear cache
shadowMapCache.clear();

// destroy cache
shadowMapCache.destroy();
```
## Questions: 
 1. What is the purpose of the `ShadowMapCache` class?
- The `ShadowMapCache` class is used to store and manage shadow maps for lights in the PlayCanvas engine, and can be used to re-use shadow maps to limit allocations.

2. What is the `getKey` method used for?
- The `getKey` method is used to generate a unique string key for a shadow map based on the light's properties, such as whether it is a cube map, its shadow type, and its resolution.

3. What is the difference between using the `get` and `add` methods of the `ShadowMapCache` class?
- The `get` method is used to retrieve a shadow map from the cache, or create a new one if none are available, while the `add` method is used to add a shadow map back to the cache for reuse.