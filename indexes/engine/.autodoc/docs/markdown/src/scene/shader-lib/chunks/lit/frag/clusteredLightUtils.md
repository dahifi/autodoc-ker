[View code on GitHub](https://github.com/playcanvas/engine/src/scene/shader-lib/chunks/lit/frag/clusteredLightUtils.js)

The code provided is a set of two functions that are used to convert a direction vector into cubemap face coordinates and texture coordinates for a cubemap face stored within a texture atlas. 

The first function, `getCubemapFaceCoordinates`, takes a direction vector `dir` and returns the corresponding cubemap face index in the range of [0..5] and the UV coordinates within the face in the range of [0..1]. Additionally, an offset to a tile in the atlas within a 3x3 subdivision is provided. The function first calculates the absolute values of the direction vector components and then determines which face of the cubemap the vector is pointing towards. If the absolute value of the z-component is greater than or equal to the absolute values of the x and y components, the vector is pointing towards the front or back face of the cubemap. If the absolute value of the y-component is greater than or equal to the absolute value of the x-component, the vector is pointing towards the top or bottom face of the cubemap. Otherwise, the vector is pointing towards the left or right face of the cubemap. Based on the determined face, the function sets the face index, calculates the UV coordinates, and sets the tile offset. The UV coordinates are then scaled and offset to the range of [0..1] and returned along with the face index and tile offset.

The second function, `getCubemapAtlasCoordinates`, takes an omniAtlasViewport, shadowEdgePixels, shadowTextureResolution, and a direction vector dir. The function first calls `getCubemapFaceCoordinates` to get the UV coordinates and face index for the direction vector. It then moves the UV coordinates inwards to compensate for the larger field of view when rendering shadows into the atlas. The function then scales the UV coordinates to the cube face area within the viewport and offsets them into the face of the atlas (3x3 grid) and the atlas viewport. The final UV coordinates are returned.

These functions are likely used in the PlayCanvas engine to convert direction vectors into cubemap face coordinates and texture coordinates for rendering cubemaps and shadows. The `getCubemapFaceCoordinates` function is used to determine which face of the cubemap a direction vector is pointing towards, which is necessary for rendering cubemaps. The `getCubemapAtlasCoordinates` function is used to convert direction vectors into texture coordinates for a cubemap face stored within a texture atlas, which is necessary for rendering shadows.
## Questions: 
 1. What does this code do?
- This code contains two functions that convert an unnormalized direction vector to cubemap face and texture coordinates within the face, and to texture coordinates for a cubemap face stored within a texture atlas.

2. What are the input parameters for the `getCubemapAtlasCoordinates` function?
- The `getCubemapAtlasCoordinates` function takes in four parameters: `omniAtlasViewport`, `shadowEdgePixels`, `shadowTextureResolution`, and `dir`. 

3. What is the purpose of the `tileOffset` variable in the `getCubemapFaceCoordinates` function?
- The `tileOffset` variable provides an offset to a tile in the atlas within a 3x3 subdivision.