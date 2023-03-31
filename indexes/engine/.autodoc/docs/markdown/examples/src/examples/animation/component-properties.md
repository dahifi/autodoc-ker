[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/animation/component-properties.tsx)

The code defines a class called `ComponentPropertiesExample` that demonstrates how to use the PlayCanvas engine to create an animation of two spotlights. The class has two methods: `controls` and `example`. 

The `controls` method returns a React component that renders a button with the text "Flash". When the button is clicked, it toggles the value of a boolean property called `flash` in the `data` object passed as an argument to the method. 

The `example` method creates a PlayCanvas application that renders a 3D scene with a box, a plane, and two spotlights. The method first creates a `GraphicsDevice` object using the `createGraphicsDevice` method of the `pc` module. It then creates an `AppBase` object and initializes it with the `GraphicsDevice` object and other options such as mouse and touch input handlers. 

The method then loads a texture asset and creates two animation clips: one for static lights and one for flashing lights. Each clip contains keyframe data for the color and rotation of the spotlights. The method creates entities for the camera, box, plane, and spotlights, and adds them to the scene hierarchy. It also adds an `AnimComponent` to the entity that contains the spotlights and assigns the animation clips to the appropriate states. 

Finally, the method starts the PlayCanvas application and listens for changes to the `flash` property in the `data` object. When the property changes, the method transitions the animation state of the spotlights between "Static" and "Flash" using the `transition` method of the `AnimComponent`. 

Overall, the `ComponentPropertiesExample` class demonstrates how to use the PlayCanvas engine to create an animated 3D scene with user interaction. The class can be used as a starting point for creating more complex applications that use the PlayCanvas engine.
## Questions: 
 1. What is the purpose of the `controls` method in the `ComponentPropertiesExample` class?
- The `controls` method returns a React component that includes a button with a `Flash` label. When clicked, the button toggles the `flash` property of the `data` object.

2. What is the `anim` component added to the `lightsEntity` entity for?
- The `anim` component is added to the `lightsEntity` entity to enable animation of the spot lights. It is configured with two animation clips, `Static` and `Flash`, which are assigned to the appropriate states.

3. What is the purpose of the `WEBGPU_ENABLED` static property in the `ComponentPropertiesExample` class?
- The `WEBGPU_ENABLED` static property is used to indicate whether the example supports the WebGPU graphics API. If set to `true`, the example will use WebGPU if available, otherwise it will use WebGL.