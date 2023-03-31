[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/camera/first-person.tsx)

The `FirstPersonExample` class is a code example that demonstrates how to create a first-person camera controller in the PlayCanvas engine. The purpose of this code is to provide developers with a starting point for creating their own first-person camera controllers in their projects. 

The `example` method is the main entry point for the code example. It takes two parameters: a `canvas` element and a `deviceType` string. The `canvas` element is used to create a new `pc.Application` instance, which is the main object that manages the PlayCanvas engine. The `deviceType` string is not used in this code example.

The `example` method creates a new `pc.Application` instance with a set of input devices, including a mouse, touch device, gamepads, and keyboard. It then loads two assets: a 3D model of a statue and a script that defines the first-person camera controller. Once the assets are loaded, the `run` function is called, which starts the application and creates the scene.

The `run` function creates a physical floor, a model entity, a camera entity, a character controller, and a directional light. The physical floor is created using a `pc.Entity` instance with a `collision` component and a `rigidbody` component. The model entity is created using the `assets.statue.resource.instantiateRenderEntity` method, which instantiates a new entity with the 3D model of the statue. The camera entity is created using a `pc.Entity` instance with a `camera` component. The character controller is created using a `pc.Entity` instance with a `collision` component, a `rigidbody` component, and several script components that define the first-person camera controller. Finally, the directional light is created using a `pc.Entity` instance with a `light` component.

The `FirstPersonExample` class can be used as a starting point for creating a first-person camera controller in a PlayCanvas project. Developers can modify the code to suit their specific needs, such as changing the 3D model, adjusting the camera settings, or adding additional input devices. Overall, this code example demonstrates how to create a basic first-person camera controller in the PlayCanvas engine.
## Questions: 
 1. What is the purpose of this code?
- This code is an example of a first-person camera implementation in the PlayCanvas engine, which creates a 3D environment with a physical floor, a model entity, a camera, a character controller, and a directional light.

2. What external dependencies does this code have?
- This code depends on the PlayCanvas engine, which is imported using the wildcard syntax, as well as on the Ammo physics engine, which is loaded using WebAssembly.

3. What is the expected output of this code?
- The expected output of this code is a playable 3D scene with a first-person camera that can be controlled using various input devices, such as a keyboard, a mouse, or a gamepad. The scene includes a physical floor, a model entity, a camera, a character controller, and a directional light, all of which are rendered using the PlayCanvas engine.