[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/clustered-omni-shadows.tsx)

The code is an example of how to use the PlayCanvas engine to create a 3D scene with clustered omni shadows. The purpose of the code is to demonstrate how to use the PlayCanvas engine to create a 3D scene with clustered omni shadows, which is a technique used to optimize the rendering of many lights in a scene. The code imports several modules from the PlayCanvas engine, as well as some modules from the @playcanvas/pcui/react and @playcanvas/observer libraries. 

The ClusteredOmniShadowsExample class contains two methods: controls and example. The controls method returns a React component that renders a panel with several input fields that allow the user to adjust the settings of the scene, such as the shadow resolution, the shadow filter type, and whether shadows and cookies are enabled. The example method takes a canvas element, a device type, and some data as arguments, and creates a 3D scene with clustered omni shadows. 

The example method first creates an object that contains several assets, such as textures and scripts, that are used in the scene. It then creates a graphics device using the createGraphicsDevice method of the PlayCanvas engine, and initializes an app using the AppBase class. The app is configured to use the graphics device, and several component systems and resource handlers are added to it. 

The example method then sets up the scene by creating several primitives, such as boxes and spheres, and adding them to the scene. It also creates several omni lights, which are lights that emit light in all directions, and adds them to the scene. The lights are configured to cast shadows and use a cookie texture, which is a texture that is projected onto the scene to create a pattern of light and shadow. 

The example method also sets up the clustered lighting system by enabling clustered lighting and adjusting the default clustered lighting parameters to handle many lights. It also enables clustered shadows and cookies, and sets the resolution of the shadow and cookie atlases. 

Finally, the example method sets up an update function that is called every frame, and updates the position of the omni lights. It also provides some debug features that allow the user to display the shadow and cookie textures. 

Overall, the code demonstrates how to use the PlayCanvas engine to create a 3D scene with clustered omni shadows, and provides an example of how to use the engine's API to create and configure lights, shadows, and cookies.
## Questions: 
 1. What is the purpose of the `controls` method in the `ClusteredOmniShadowsExample` class?
- The `controls` method returns a JSX element that contains UI controls for adjusting settings related to shadows and cookies in the example.
2. What type of graphics device is created in the `example` method?
- The `example` method creates a WebGL graphics device using the `pc.createGraphicsDevice` function.
3. What is the purpose of the `Observer` class imported from `@playcanvas/observer`?
- The `Observer` class is used to create an observable data object that can be used to track changes to the settings in the example and update the scene accordingly.