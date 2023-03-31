[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/physics/compound-collision.tsx)

The `CompoundCollisionExample` class is a part of the PlayCanvas engine project and is responsible for demonstrating the use of compound collision shapes in a physics simulation. The purpose of this code is to create a scene with a chair and a ground, where the chair has a compound collision shape that is made up of several child entities. The scene is rendered using WebGL and the physics simulation is powered by the Ammo.js physics engine.

The `example` method of the `CompoundCollisionExample` class takes two arguments: a canvas element and a device type. It first sets the configuration for the Ammo.js physics engine by specifying the URLs for the JavaScript and WebAssembly files. It then creates a graphics device using the `createGraphicsDevice` method of the PlayCanvas engine, passing in the canvas element and device type. The graphics device is used to render the scene.

The `example` method then creates an instance of the Ammo.js physics engine using the `getInstance` method of the `WasmModule` class. It initializes the PlayCanvas application by creating an instance of the `AppBase` class and passing in an instance of the `AppOptions` class. The `AppOptions` class is used to specify the graphics device, keyboard, component systems, and resource handlers for the application.

The `example` method then defines a scene hierarchy in JSON format, which is loaded and parsed using the `parseScene` function. The scene hierarchy consists of a chair entity with a compound collision shape and several child entities, a ground entity with a box collision shape, a directional light entity, and a camera entity. The `parseEntity` function is used to convert an entity definition in the JSON structure to a `pc.Entity` object.

The `example` method then sets an update function on the application's update event. The update function is responsible for adding new chair entities to the scene every 250 milliseconds and changing the material of the chair entities based on whether they are active or frozen.

Overall, the `CompoundCollisionExample` class demonstrates how to create a physics simulation with compound collision shapes in the PlayCanvas engine. It shows how to define a scene hierarchy in JSON format, how to convert an entity definition to a `pc.Entity` object, and how to set an update function on the application's update event.
## Questions: 
 1. What is the purpose of the `example` method in the `CompoundCollisionExample` class?
- The `example` method is used to run a demo of the compound collision feature of the PlayCanvas engine, using the specified canvas and device type.

2. What is the significance of the `pc.WasmModule` calls in the `demo` function?
- The `pc.WasmModule` calls are used to configure and initialize the Ammo physics engine, which is used for the compound collision feature.

3. What is the purpose of the `parseEntity` and `parseScene` functions?
- The `parseEntity` function is used to convert an entity definition in JSON format to a `pc.Entity` object, while the `parseScene` function is used to parse a scene hierarchy in JSON format and add the entities to the scene's root entity.