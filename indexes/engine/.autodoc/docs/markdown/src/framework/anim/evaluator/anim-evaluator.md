[View code on GitHub](https://github.com/playcanvas/engine/src/framework/anim/evaluator/anim-evaluator.js)

The `AnimEvaluator` class is responsible for blending multiple sets of animation clips together. It is a part of the PlayCanvas engine project. The purpose of this class is to evaluate and blend animation clips and set the results on the animation targets. 

The `AnimEvaluator` class has a constructor that takes an instance of `AnimBinder` as a parameter. The `AnimBinder` interface resolves curve paths to instances of `AnimTarget`. The class has a list of animation clips, inputs, outputs, and targets. The `addClip` method adds a clip to the evaluator. It stores a list of input/output arrays, curves, and snapshots. It creates a new target if it doesn't exist yet. It also sets the mask for the animation component. The `removeClip` method removes a clip from the evaluator. The `removeClips` method removes all clips from the evaluator. The `updateClipTrack` method updates the clip track. The `findClip` method finds the first clip that matches the given name. The `rebind` method rebinds the evaluator. The `assignMask` method assigns a mask. The `update` method updates the evaluator. It updates the clip, blends the results, and sets the results on the animation targets. 

The `AnimEvaluator` class is used in the PlayCanvas engine project to blend multiple sets of animation clips together. It is used to evaluate and blend animation clips and set the results on the animation targets. It is a part of the animation system in the PlayCanvas engine project. 

Example usage:

```javascript
const animEvaluator = new AnimEvaluator(animBinder);
animEvaluator.addClip(animClip);
animEvaluator.update(deltaTime);
```
## Questions: 
 1. What is the purpose of the `AnimEvaluator` class?
- The `AnimEvaluator` class blends multiple sets of animation clips together.

2. What is the role of the `binder` parameter in the `AnimEvaluator` constructor?
- The `binder` parameter is an interface that resolves curve paths to instances of `AnimTarget`.

3. What is the purpose of the `update` method in the `AnimEvaluator` class?
- The `update` method is the evaluator frame update function that evaluates, blends, and sets the results of the update to the `AnimTarget`.