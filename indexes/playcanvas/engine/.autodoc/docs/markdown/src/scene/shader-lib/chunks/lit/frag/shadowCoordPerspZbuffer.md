[View code on GitHub](https://github.com/playcanvas/engine/src/scene/shader-lib/chunks/lit/frag/shadowCoordPerspZbuffer.js)

The code provided is a GLSL shader code that contains three functions: `_getShadowCoordPerspZbuffer`, `getShadowCoordPerspZbufferNormalOffset`, and `getShadowCoordPerspZbuffer`. These functions are used to calculate the shadow coordinates for a perspective projection with a z-buffer. 

The `_getShadowCoordPerspZbuffer` function takes in a `shadowMatrix`, `shadowParams`, and `wPos` as parameters. The `shadowMatrix` is a matrix that transforms the world coordinates to shadow map coordinates. The `shadowParams` is a vector that contains the parameters for the shadow map, including the bias and the strength. The `wPos` is the world position of the vertex. The function first transforms the `wPos` to the shadow map coordinates using the `shadowMatrix`. Then, it divides the `xyz` components of the resulting vector by its `w` component to obtain the normalized device coordinates. Finally, it sets the `dShadowCoord` variable to the normalized device coordinates. 

The `getShadowCoordPerspZbufferNormalOffset` function takes in a `shadowMatrix`, `shadowParams`, and `normal` as parameters. The `normal` is the normal vector of the vertex. The function first calculates the world position of the vertex by adding the `normal` vector multiplied by the `y` component of the `shadowParams` vector to the `vPositionW` vector. Then, it calls the `_getShadowCoordPerspZbuffer` function with the `shadowMatrix`, `shadowParams`, and the calculated `wPos`. 

The `getShadowCoordPerspZbuffer` function takes in a `shadowMatrix` and `shadowParams` as parameters. It calls the `_getShadowCoordPerspZbuffer` function with the `shadowMatrix`, `shadowParams`, and the `vPositionW` vector. 

These functions are used to calculate the shadow coordinates for a perspective projection with a z-buffer. They are likely used in the rendering pipeline of the PlayCanvas engine to generate shadows for 3D objects in a scene. For example, the `getShadowCoordPerspZbuffer` function may be called in the vertex shader to calculate the shadow coordinates for each vertex, which can then be used in the fragment shader to determine the amount of shadowing for each pixel. 

Example usage:

```glsl
uniform mat4 shadowMatrix;
uniform vec4 shadowParams;

void main() {
  getShadowCoordPerspZbuffer(shadowMatrix, shadowParams);
  // use dShadowCoord to determine shadowing
}
```
## Questions: 
 1. What does this code do?
    
    This code defines three functions related to calculating shadow coordinates for a perspective z-buffer shadow map.

2. What are the input parameters for each function?
    
    Each function takes a `shadowMatrix` (a matrix used to transform the position into shadow map space), `shadowParams` (a vec4 containing shadow map parameters), and either a `wPos` (a vec3 world position) or `normal` (a vec3 surface normal).

3. What is the purpose of the `getShadowCoordPerspZbufferNormalOffset` function?
    
    This function calculates the shadow coordinate for a position offset by a given surface normal, which can be used to apply a depth bias to prevent self-shadowing artifacts.