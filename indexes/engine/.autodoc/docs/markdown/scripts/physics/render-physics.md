[View code on GitHub](https://github.com/playcanvas/engine/scripts/physics/render-physics.js)

The `RenderPhysics` script is responsible for rendering debug shapes for physics collision components in the PlayCanvas engine. The script is attached to an entity and has three attributes: `drawShapes`, `opacity`, and `castShadows`. 

The `initialize` function is called once per entity and sets up event listeners for attribute changes and script enable/disable events. When the `castShadows` attribute changes, the script updates the `castShadows` property of each child model in the `debugRoot` entity. When the `opacity` attribute changes, the script updates the `opacity` property of each material in each child mesh instance in the `debugRoot` entity. When the script is enabled, a new `debugRoot` entity is created and added to the app root. When the script is disabled, the `debugRoot` entity is destroyed and any `_debugShape` properties on collision components are deleted.

The `createModel` function creates a new model with a single mesh instance using the provided mesh and material.

The `postUpdate` function is called once per frame and is responsible for updating the debug shapes. First, it marks all existing debug shapes as not updated. If `drawShapes` is true, it finds all collision components in the app root and updates their debug shapes. If a collision component does not have a `_debugShape` property, a new debug shape is created and added to the `debugRoot` entity. The debug shape is created using a random color material and a mesh created using the collision component's properties. If the collision component has a rigid body, the debug shape is positioned and rotated using the rigid body's position and rotation. Otherwise, the debug shape is positioned and rotated using the collision component's entity's position and rotation. If the collision component is a capsule, cone, or cylinder, the debug shape is rotated to take into account the component's axis. If a debug shape was not updated during this frame, it is assumed that the corresponding collision component no longer exists and the debug shape is deleted.

Overall, the `RenderPhysics` script provides a way to visualize physics collision components in the PlayCanvas engine, which can be useful for debugging and testing physics interactions. Developers can attach this script to entities with collision components and adjust the `drawShapes`, `opacity`, and `castShadows` attributes to customize the debug shapes.
## Questions: 
 1. What does this code do?
- This code defines a script called `RenderPhysics` that can be attached to entities in a PlayCanvas project to render physics collision shapes. It has attributes for controlling the appearance of the shapes and handles events for changing those attributes.

2. What are the possible values for the `type` property of the `drawShapes` attribute?
- The `drawShapes` attribute is a boolean type, so it can only have the values `true` or `false`. 

3. What happens when the `disable` event is triggered on an entity with the `RenderPhysics` script?
- When the `disable` event is triggered, the script removes any debug shapes associated with collision components on the entity and destroys the `debugRoot` entity that contains them.