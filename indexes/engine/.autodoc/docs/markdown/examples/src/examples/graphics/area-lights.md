[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/area-lights.tsx)

The `AreaLightsExample` class is a part of the PlayCanvas engine project and is responsible for demonstrating the use of area lights in a 3D scene. The purpose of this code is to create a 3D scene with area lights and a statue model, and update the scene each frame. 

The `example` method is the main function of this class, which takes two parameters: a canvas element and a device type. It creates a graphics device using the `createGraphicsDevice` method and initializes the app using the `init` method. It then sets up the scene by creating a ground plane, a camera, and three area lights with different shapes and colors. The `createPrimitive` and `createAreaLight` helper functions are used to create the primitives and area lights respectively. 

The `createPrimitive` function creates a primitive with a specified shape, position, scale, and color. It also creates a material of the specified color and sets it to the primitive. The primitive is then added to the scene. 

The `createAreaLight` function creates an area light with a specified type, shape, position, scale, color, intensity, shadows, and range. It also creates a visual representation of the light source using a primitive shape and a material of the same color as the light source. The primitive shape is then added to the scene. 

The `app.on("update")` event listener is used to update the scene each frame. It updates the position and rotation of the area lights based on time and camera position. 

Overall, this code demonstrates how to create and use area lights in a 3D scene using the PlayCanvas engine. It can be used as a reference for developers who want to implement area lights in their own projects.
## Questions: 
 1. What is the purpose of the `example` method in the `AreaLightsExample` class?
- The `example` method is used to run the example code for the area lights feature of the PlayCanvas engine on a given canvas element and device type.

2. What assets are being loaded in the `assets` object?
- The `assets` object is loading several assets including textures, a 3D model, and a JSON file containing data for area light look-up tables.

3. What is the purpose of the `createAreaLight` function?
- The `createAreaLight` function is used to create an area light entity with a visual representation in the scene, including a primitive shape and emissive material. It takes parameters such as light type, shape, position, color, intensity, and range.