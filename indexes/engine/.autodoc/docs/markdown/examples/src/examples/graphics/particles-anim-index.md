[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/particles-anim-index.tsx)

The `ParticlesAnimIndexExample` class is an example of how to use the PlayCanvas engine to create a particle system with animated textures. The purpose of this code is to demonstrate how to create a particle system with multiple entities, each with a different animation index, and display the full particle texture on a panel.

The `example` method takes in a canvas element and a device type as parameters. It creates a new PlayCanvas application and sets the canvas to fill the window and automatically change resolution to be the same as the canvas size. It then creates an entity with a camera component, a directional light entity, a screen entity, and a panel entity. The camera entity is positioned at (0, 0, 20) and the light entity is rotated to (45, 0, 0). The screen entity is set to have a resolution of (640, 480) and a reference resolution of (1280, 720). The panel entity is added as a child of the screen entity.

Four particle entities are created and added as children of the root entity. Each particle entity is positioned at a different location. The `particleSystemConfiguration` object is created with properties for the particle system, such as the number of particles, lifetime, rate, color map, initial velocity, emitter shape, emitter radius, animation loop, animation tiles, animation speed, and scale graph. A `scaleCurve` object is created with a curve that gradually makes sparks bigger.

For each particle entity, an `options` object is created by merging the `particleSystemConfiguration` object with an object that specifies the animation index and number of frames for that entity. The `options` object is then passed to the `addComponent` method of the particle entity with the `particlesystem` component type.

Finally, the full particle texture is added to the panel entity as an image element. The application is started and the particle system is displayed on the canvas.

This code can be used as a starting point for creating more complex particle systems with animated textures in the PlayCanvas engine. Developers can modify the properties of the `particleSystemConfiguration` object to create different effects, and add more particle entities with different animation indices to create more complex animations. The `scaleCurve` object can also be modified to create different scaling effects for the particles.
## Questions: 
 1. What is the purpose of this code?
- This code is an example of how to create and display particle systems using the PlayCanvas engine.

2. What assets are being used in this code?
- This code is using a texture asset called 'particlesNumbers' located at '/static/assets/textures/particles-numbers.png'.

3. What is the significance of the 'animIndex' property in the particle system configuration?
- The 'animIndex' property sets the animation index of the particle system, which determines which animation in the sprite sheet to use. In this code, each of the four particle systems has a different 'animIndex' value to display a different animation.