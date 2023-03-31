[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/reflection-planar.tsx)

The `ReflectionPlanarExample` class is a code example that demonstrates how to create a planar reflection effect in a 3D scene using the PlayCanvas engine. The example creates a scene with a reflective ground plane and several randomly placed 3D primitives. The reflection effect is achieved by rendering the scene from the perspective of a reflection camera and then applying the resulting texture to the ground plane using a custom shader.

The `example` method of the `ReflectionPlanarExample` class takes three arguments: a canvas element to render the scene, a string representing the type of graphics device to use (e.g. "webgl2"), and an object containing the vertex and fragment shader code for the custom shader. The method first creates a `pc.GraphicsDevice` object using the `pc.createGraphicsDevice` method and initializes a new `pc.AppBase` object with the graphics device. It then loads several assets, including a cubemap texture for the skybox, a 3D model of a statue, and a custom script for rendering the reflection texture.

The method then creates a new `pc.Entity` object for the main camera and sets its field of view and layer mask to render the world, excluded, and skybox layers. It also creates a new `pc.Entity` object for the reflection camera and sets its field of view and layer mask to render the world and skybox layers only. The reflection camera is positioned and oriented to reflect the scene from the perspective of the ground plane. A custom script component is added to the reflection camera to render the reflection texture using the `planarRenderer` script.

The method then sets up the scene by creating a reflective ground plane using a custom shader, creating several randomly placed 3D primitives, and adding them to the world layer. It also sets up the skybox and other rendering properties of the scene. Finally, the method sets up an update function to animate the scene and update the reflection texture each frame.

Overall, this code example demonstrates how to create a planar reflection effect in a 3D scene using the PlayCanvas engine. It shows how to use custom shaders, cameras, and scripts to achieve the effect and how to set up a scene with multiple layers and assets. The example can be used as a starting point for creating more complex scenes with reflective surfaces.
## Questions: 
 1. What is the purpose of the `example` method in this code?
- The `example` method is a function that takes in three parameters (canvas, deviceType, and files) and sets up a scene with various entities and cameras, and updates them each frame.

2. What is the `planarRenderer` script used for?
- The `planarRenderer` script is used to render the reflection texture for the ground material. It takes in various attributes such as the scene camera entity, scale, mipmaps, depth, plane point, and plane normal.

3. What is the purpose of the `gfxOptions` object?
- The `gfxOptions` object is used to specify various options for creating the graphics device, such as the device types to use, and the URLs for the glslang and twgsl libraries.