[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/physics/falling-shapes.tsx)

The `FallingShapesExample` class is a demonstration of how to use the PlayCanvas engine to create a physics simulation of falling shapes. The purpose of this code is to show how to create a scene with a floor, lights, camera, and various shapes that fall from above and collide with the floor. The code uses the PlayCanvas engine to create a 3D graphics application that runs in a web browser.

The `example` method is the main entry point for the code. It takes two arguments: a canvas element and a device type. The canvas element is the HTML canvas element that the graphics will be rendered to. The device type is a string that specifies the type of graphics device to use, such as "webgl2" or "webgpu". The method sets up the physics engine and creates the scene with the floor, lights, camera, and falling shapes.

The `demo` function is called after the physics engine is set up. It loads the assets needed for the scene, creates the graphics device, and initializes the application. The `createOptions` object is used to specify the graphics device, keyboard, and component systems. The `resourceHandlers` array is used to specify the handlers for loading different types of resources, such as textures, scripts, and fonts.

The `app` object is an instance of the `pc.AppBase` class, which represents the 3D graphics application. The `setCanvasFillMode` and `setCanvasResolution` methods are used to set the canvas to fill the window and automatically change resolution to be the same as the canvas size. The `app.start` method is called to start the application.

The `createMaterial` function is used to create a material with a given color. The `red` and `gray` materials are created using this function. The `floor` entity is created with a render component, rigidbody component, and collision component. The `light` entity is created with a light component. The `camera` entity is created with a camera component. The `createTemplate` function is used to create templates for the falling shapes. The `boxTemplate`, `sphereTemplate`, `capsuleTemplate`, `cylinderTemplate`, and `meshTemplate` templates are created using this function.

The `app.on("update")` method is used to set an update function that is called every frame. The update function creates a falling shape every 0.2 seconds and positions it above the floor. The `clone` of the falling shape is created by cloning a random template and enabling it. The `teleport` method is used to position the clone above the floor. The `angularVelocity` property is used to give the clone a random spin. The `isActive` method is used to determine if a rigidbody is active or frozen, and the material of the mesh instance is set accordingly.

In summary, the `FallingShapesExample` class is a demonstration of how to use the PlayCanvas engine to create a physics simulation of falling shapes. The code creates a scene with a floor, lights, camera, and various shapes that fall from above and collide with the floor. The code uses the PlayCanvas engine to create a 3D graphics application that runs in a web browser.
## Questions: 
 1. What is the purpose of the `FallingShapesExample` class?
- The `FallingShapesExample` class is an example of a physics simulation that creates falling shapes and demonstrates the use of the PlayCanvas engine.

2. What is the significance of the `WasmModule` object and its `setConfig` and `getInstance` methods?
- The `WasmModule` object is used to configure and instantiate the Ammo physics engine, which is used by the PlayCanvas engine. The `setConfig` method sets the configuration options for the Ammo engine, and the `getInstance` method instantiates the engine.

3. What is the purpose of the `createTemplate` function and how is it used?
- The `createTemplate` function is a helper function that creates a template for a physics collider. It is used to create templates for falling shapes such as boxes, spheres, capsules, cylinders, and meshes. These templates are then cloned and used to create the actual falling shapes in the physics simulation.