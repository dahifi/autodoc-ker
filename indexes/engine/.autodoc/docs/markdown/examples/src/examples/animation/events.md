[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/animation/events.tsx)

The code is an example of how to use the PlayCanvas engine to create a 3D scene with animation and event handling. The purpose of the code is to demonstrate how to load assets, create entities, add components, and handle events in a PlayCanvas application. 

The `EventsExample` class is a static class that contains a single method called `example`. This method takes two parameters: a canvas element and a device type. The canvas element is used to create a graphics device, and the device type is used to specify the type of device to create. 

The `example` method begins by defining a set of assets that will be used in the scene. These assets include a 3D model, an animation, a texture, and a script. The method then creates a graphics device using the `pc.createGraphicsDevice` function, passing in the canvas element and device type. Once the graphics device is created, the method creates an instance of the `pc.AppBase` class and initializes it with the graphics device and other options. 

The method then loads the assets using the `pc.AssetListLoader` class and starts the application. Once the application is started, the method sets up the scene by creating a skydome, adding a camera entity, creating a floor made up of box models, and adding a loaded model with an animation component. 

The method then adds two animation events to the walk animation, one for each footstep. These events occur just as each foot touches the ground. When an event occurs, the method highlights the box that is under the foot's bone position. 

Finally, the method sets up an update loop that iterates over any currently highlighted boxes and reduces their emissive property. It also removes old highlighted boxes from the update loop. The method then sets the camera to follow the model. 

Overall, this code demonstrates how to use the PlayCanvas engine to create a 3D scene with animation and event handling. It shows how to load assets, create entities, add components, and handle events in a PlayCanvas application.
## Questions: 
 1. What is the purpose of the `EventsExample` class?
- The `EventsExample` class is an example class that demonstrates how to use events in the PlayCanvas engine.

2. What assets are being loaded in the `example` method?
- The `example` method loads a 3D model, an animation, a texture, and a script.

3. What does the `highlightBox` function do?
- The `highlightBox` function lights up a box at a given position with a random color using the emissive material property and adds the box to an array of highlighted boxes.