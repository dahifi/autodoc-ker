[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/animation/blend-trees-2d-cartesian.tsx)

The `BlendTrees2DCartesianExample` class is a React component that demonstrates how to use blend trees in PlayCanvas engine to create 2D animations. The component contains two methods: `controls()` and `example()`. 

The `controls()` method is responsible for rendering a canvas element that allows the user to control the position of the model in the 2D blend tree. The method uses the `useEffect()` hook to listen for the `start` event of the PlayCanvas app and then sets up event listeners for mouse and touch events on the canvas. When the user interacts with the canvas, the method updates the position of the model in the blend tree and redraws the canvas to reflect the new position.

The `example()` method is responsible for setting up the PlayCanvas app and loading the assets required for the example. The method creates a new `pc.AppBase` instance and sets up the graphics device, camera, light, and model entities. It also creates an animation state graph for the model entity and loads the required animations. Finally, the method starts the PlayCanvas app.

Overall, the `BlendTrees2DCartesianExample` class demonstrates how to use blend trees in PlayCanvas engine to create 2D animations and provides an interactive example for users to experiment with.
## Questions: 
 1. What is the purpose of the `controls()` method?
- The `controls()` method sets up a canvas element and event listeners for mouse and touch events, which allow the user to control the position of an animated model using a 2D blend tree.

2. What assets are loaded in the `example()` method?
- The `example()` method loads several assets, including a 3D model, multiple animations, a texture for a skybox, and a post-processing script for bloom effects.

3. What is the purpose of the `BlendTrees2DCartesianExample` class?
- The `BlendTrees2DCartesianExample` class is an example implementation of a 2D blend tree animation system using the PlayCanvas engine. It includes methods for setting up user controls and loading assets, as well as a static category and name for the example.