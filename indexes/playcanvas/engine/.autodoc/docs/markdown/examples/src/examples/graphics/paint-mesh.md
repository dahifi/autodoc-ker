[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/paint-mesh.tsx)

The `PaintMeshExample` class is an example of how to use the PlayCanvas engine to create a custom shader that can be used to paint a texture onto a 3D mesh. The example demonstrates how to create a high-quality sphere mesh, apply a texture to it, and then use a custom shader to paint a decal texture onto the surface of the sphere.

The `example` method of the `PaintMeshExample` class takes three arguments: a canvas element, a device type, and an object containing two shader files. The method creates a new PlayCanvas application, loads several assets (including the sphere texture, the decal texture, and a cubemap), and sets up two cameras: one for rendering the sphere with the decal texture, and one for rendering the scene with the sphere and the decal camera. 

The method then creates a high-quality sphere mesh using the `createHighQualitySphere` function, which takes a material and a layer as arguments. The function creates a new entity, adds a render component to it with the sphere mesh and the provided material, and returns the entity. The method also creates a new layer for rendering decals, a new camera for rendering the decal texture, and a new directional light entity.

The custom shader used to paint the decal texture onto the sphere is defined in the `FILES` object, which contains two shader files: `shader.vert` and `shader.frag`. The vertex shader transforms the vertex position to world space and then to decal space, and passes it to the fragment shader to sample the decal texture. The fragment shader calculates the decal space position of each pixel, checks if it is within the bounds of the projection box, and then samples the decal texture at that position.

The method creates a new `pc.Shader` object from the vertex and fragment shaders, and then creates a new `pc.Material` object with the shader. The method then creates a new entity that is a child of the sphere entity, and adds a render component to it with the sphere mesh and the decal material. The method also updates the decal projection position and direction each frame, and renders the decal texture to a texture every half second.

Overall, this code demonstrates how to use the PlayCanvas engine to create a custom shader that can be used to paint a decal texture onto a 3D mesh. The example shows how to create a high-quality sphere mesh, apply a texture to it, and then use a custom shader to paint a decal texture onto the surface of the sphere. This technique can be used to add detailed textures and decals to 3D models in PlayCanvas projects.
## Questions: 
 1. What does this code do?
- This code is an example of how to use a custom shader to render decals onto a mesh in the PlayCanvas engine. It creates a high-resolution sphere with a texture, and then renders decals onto it using a custom shader.

2. What are the inputs and outputs of the `example` function?
- The `example` function takes in an HTML canvas element, a device type string, and an object containing two shader files as strings. It does not have any outputs.

3. What is the purpose of the `decalLayer` and `decalCamera` entities?
- The `decalLayer` entity is a layer used for rendering decals onto the mesh. The `decalCamera` entity is a camera that renders the decals using the `decalLayer`, and renders before the main camera.