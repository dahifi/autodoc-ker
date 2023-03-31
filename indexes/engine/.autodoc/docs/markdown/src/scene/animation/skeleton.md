[View code on GitHub](https://github.com/playcanvas/engine/src/scene/animation/skeleton.js)

The code defines a class called `Skeleton` that represents a skeleton used to play animations. The class contains methods to add time to the animation, blend two skeletons together, link a skeleton to a node hierarchy, and synchronize the linked node hierarchy with the current state of the skeleton. 

The `Skeleton` class has a constructor that takes a `graph` parameter, which is the root `GraphNode` of the skeleton. The constructor creates an array of `InterpolatedKey` objects, which represent the interpolated keyframes for each node in the skeleton. The `addInterpolatedKeys` method is called recursively to add an `InterpolatedKey` object for each node in the skeleton hierarchy. 

The `animation` property is a setter that sets the current animation for the skeleton and resets the current time to zero. The `currentTime` property is a getter and setter that gets or sets the current time of the animation in seconds. The `addTime` method progresses the animation by the supplied time delta and updates the interpolated keyframes for each node in the skeleton. The `blend` method blends two skeletons together using a specified alpha value. The `setGraph` method links the skeleton to a node hierarchy, and the `updateGraph` method synchronizes the linked node hierarchy with the current state of the skeleton.

Overall, the `Skeleton` class is an important part of the PlayCanvas engine, as it provides the functionality to animate 3D models and synchronize their animations with the node hierarchy. Here is an example of how to use the `Skeleton` class to animate a 3D model:

```javascript
const model = app.root.findByName('MyModel');
const skeleton = model.model.skeleton;
skeleton.animation = model.model.animations[0];
skeleton.currentTime = 0;
skeleton.looping = true;

app.on('update', (deltaTime) => {
    skeleton.addTime(deltaTime);
    skeleton.updateGraph();
});
```
## Questions: 
 1. What is the purpose of the `InterpolatedKey` class?
- The `InterpolatedKey` class represents a keyframe that has been interpolated from two other keyframes. It stores the resulting position, rotation, and scale values, as well as the name of the node it corresponds to and an optional target node.

2. How does the `addTime` method handle looping animations?
- If the animation is set to loop, and the time delta takes the animation past its end point, the method will wrap around to the beginning of the animation. Otherwise, the animation's current time will remain at its duration.

3. What is the purpose of the `updateGraph` method?
- The `updateGraph` method synchronizes the currently linked node hierarchy with the current state of the skeleton. It converts the interpolated keyframe at each node in the skeleton into the local transformation matrix at each corresponding node in the linked node hierarchy.