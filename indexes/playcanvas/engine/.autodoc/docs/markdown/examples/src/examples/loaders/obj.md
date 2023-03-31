[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/loaders/obj.tsx)

The `ObjExample` class is a code example that demonstrates how to load and display a 3D model in the PlayCanvas engine using the OBJ file format. The purpose of this code is to provide developers with a working example of how to use the PlayCanvas engine to load and display 3D models in their applications.

The `example` method is the main entry point for this code example. It takes two parameters: a `canvas` element and a `deviceType` string. The `canvas` element is used to create a new PlayCanvas application, while the `deviceType` string is not used in this example.

The code first creates a new PlayCanvas application using the `pc.Application` constructor. It then sets the ambient light of the scene to a dark gray color using the `pc.Color` constructor.

The code then defines the URLs for the OBJ file and the OBJ model parser script. It loads the OBJ model parser script using the `app.assets.loadFromUrl` method and adds the OBJ parser to the model resource handler using the `app.loader.getHandler("model").addParser` method. This enables the PlayCanvas engine to parse OBJ files and load them as 3D models.

The code then loads the OBJ file using the `app.assets.loadFromUrl` method and creates a new entity to display the model. It adds a `model` component to the entity and sets the `model` property to the loaded model resource. It also generates a random material for each mesh instance in the model and assigns it to the `material` property of the mesh instance.

The code then creates a new entity with a `camera` component and adds it to the scene. It also creates a new entity with an `omni` light component and adds it to the scene.

Finally, the code sets up an update loop using the `app.on("update")` method. In the update loop, it rotates the model entity around the y-axis if it exists.

This code example demonstrates how to load and display a 3D model in the PlayCanvas engine using the OBJ file format. Developers can use this code as a starting point for their own applications that require 3D models. They can modify the code to load different models, use different materials, and add more entities to the scene.
## Questions: 
 1. What is the purpose of the `ObjExample` class?
- The `ObjExample` class is an example class that demonstrates how to load and display an OBJ model using the PlayCanvas engine.

2. What are the URLs for the OBJ model and the OBJ model parser script?
- The URLs for the OBJ model and the OBJ model parser script are `/static/assets/models/monkey.obj` and `/static/scripts/parsers/obj-model.js`, respectively.

3. What components are added to the camera and light entities?
- The camera entity has a `camera` component with a clear color of `new pc.Color(0.4, 0.45, 0.5)`, while the light entity has a `light` component with a type of `"omni"`, a color of `new pc.Color(1, 1, 1)`, and a range of `100`.