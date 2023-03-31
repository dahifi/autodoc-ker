[View code on GitHub](https://github.com/playcanvas/engine/src/scene/shader-lib/chunks/lit/frag/clusteredLightShadows.js)

The code above is a shader code that implements different functions for sampling shadows in a clustered omni and spot light setup. The code is written in GLSL and is used in the PlayCanvas engine project. 

The code is divided into two main sections, one for clustered omni sampling and the other for clustered spot sampling. Each section has three functions that implement different levels of Percentage Closer Filtering (PCF) for shadows. 

The first function in each section, `getShadowOmniClusteredPCF1` and `getShadowSpotClusteredPCF1`, implements no filtering and returns a binary value indicating whether a pixel is in shadow or not. The second function in each section, `getShadowOmniClusteredPCF3` and `getShadowSpotClusteredPCF3`, implements PCF3x3 filtering and returns a value between 0 and 1 indicating the level of shadowing. The third function in each section, `getShadowOmniClusteredPCF5` and `getShadowSpotClusteredPCF5`, implements PCF5x5 filtering and returns a value between 0 and 1 indicating the level of shadowing. 

The functions take as input a shadow map, a set of shadow parameters, an omni or spot light viewport, a number of shadow edge pixels, and a light direction. The shadow map is a texture that contains the depth values of the scene from the point of view of the light. The shadow parameters contain information about the resolution of the shadow map and the distance between the light and the objects in the scene. The omni or spot light viewport is a set of coordinates that define the area of the shadow map that corresponds to the light. The number of shadow edge pixels is used to adjust the size of the viewport to avoid edge artifacts. The light direction is used to compute the depth of the shadow map at a given point. 

The functions use a set of helper functions to compute the coordinates of the shadow map texels that correspond to a given point in the scene. These helper functions are not included in the code above. 

The code is used in the PlayCanvas engine project to implement shadow mapping for clustered omni and spot lights. The code is executed on the GPU and is called from the main rendering pipeline. The functions are used to compute the level of shadowing for each pixel in the scene that is affected by a clustered omni or spot light. The resulting shadow map is then combined with the color buffer to produce the final image. 

Example usage:

```glsl
// get the level of shadowing for a clustered omni light using PCF5x5 filtering
float shadowLevel = getShadowOmniClusteredPCF5(shadowMap, shadowParams, omniViewport, shadowEdgePixels, lightDir);
```
## Questions: 
 1. What is the purpose of this code?
- This code is for implementing clustered shadow mapping with different levels of PCF filtering for both omni and spot lights using an atlas.

2. What is the difference between the `getShadowOmniClusteredPCF1`, `getShadowOmniClusteredPCF3`, and `getShadowOmniClusteredPCF5` functions?
- These functions differ in the level of PCF filtering used for omni lights. `getShadowOmniClusteredPCF1` uses no filtering, `getShadowOmniClusteredPCF3` uses a 3x3 PCF filter, and `getShadowOmniClusteredPCF5` uses a 5x5 PCF filter.

3. What is the purpose of the `CLUSTER_SHADOW_TYPE_PCF1`, `CLUSTER_SHADOW_TYPE_PCF3`, and `CLUSTER_SHADOW_TYPE_PCF5` defines?
- These defines are used to conditionally compile the code for different levels of PCF filtering. `CLUSTER_SHADOW_TYPE_PCF1` is used for no filtering, `CLUSTER_SHADOW_TYPE_PCF3` is used for 3x3 PCF filtering, and `CLUSTER_SHADOW_TYPE_PCF5` is used for 5x5 PCF filtering.