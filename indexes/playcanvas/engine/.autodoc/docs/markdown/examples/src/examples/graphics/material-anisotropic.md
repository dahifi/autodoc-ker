[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/material-anisotropic.tsx)

The `LightsExample` class is a part of the PlayCanvas engine project and is responsible for rendering a scene with a set of spheres and a directional light. The purpose of this code is to demonstrate the use of the PlayCanvas engine to create a 3D scene with lighting and materials.

The `example` method of the `LightsExample` class takes two parameters: a canvas element and a device type. It creates a graphics device using the `pc.createGraphicsDevice` method and initializes a new PlayCanvas application using the `pc.AppBase` constructor. It then sets the canvas to fill the window and automatically change resolution to be the same as the canvas size.

The `example` method also creates an asset list loader to load the required assets for the scene. These assets include a cubemap texture and a font. Once the assets are loaded, the method creates an entity with a camera component and an entity with a directional light component. It then creates a set of spheres with different materials and adds them to the scene.

The `createSphere` function creates a sphere entity with a `StandardMaterial` component. The material properties are set based on the position of the sphere in the grid. The `createText` function creates a text entity with a font asset and adds it to the scene.

Overall, this code demonstrates the use of the PlayCanvas engine to create a 3D scene with lighting and materials. It shows how to create entities with different components and how to set their properties. This code can be used as a starting point for creating more complex 3D scenes using the PlayCanvas engine.
## Questions: 
 1. What is the purpose of the `LightsExample` class?
- The `LightsExample` class is an example of how to use the PlayCanvas engine to create a scene with spheres and directional lighting.

2. What assets are being loaded in this code and how are they being used?
- The `helipad` texture and `font` asset are being loaded and used to create the environment map and text elements in the scene, respectively.

3. What is the significance of `WEBGPU_ENABLED` being set to `true`?
- `WEBGPU_ENABLED` being set to `true` indicates that the code is using the WebGPU API for rendering, which is a newer and more performant graphics API than WebGL.