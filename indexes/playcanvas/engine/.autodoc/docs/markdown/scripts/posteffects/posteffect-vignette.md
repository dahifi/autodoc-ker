[View code on GitHub](https://github.com/playcanvas/engine/scripts/posteffects/posteffect-vignette.js)

# PlayCanvas Engine - Vignette Effect

The `VignetteEffect` class is a post-processing effect that adds a vignette to the screen. It is a part of the PlayCanvas engine project and is used to enhance the visual quality of the game. 

## How it Works

The `VignetteEffect` class extends the `PostEffect` class and overrides its `render` method. The `render` method takes an input target, an output target, and a rectangle as parameters. It sets the values of the `uColorBuffer`, `uOffset`, and `uDarkness` uniforms in the shader and then draws a quad using the `vignetteShader`. The `vignetteShader` is a fragment shader that applies the vignette effect to the screen.

The `Vignette` script is a wrapper around the `VignetteEffect` class that makes it easier to use in a PlayCanvas project. It adds two attributes to the script: `offset` and `darkness`. These attributes control the offset and darkness of the vignette effect. The `initialize` method of the script creates a new instance of the `VignetteEffect` class and sets its `offset` and `darkness` properties to the values of the `offset` and `darkness` attributes. It then adds the effect to the camera's post-effects queue. 

The `Vignette` script also listens for changes to the `offset` and `darkness` attributes and updates the `effect` object accordingly. It also listens for changes to the `state` of the script and adds or removes the effect from the camera's post-effects queue accordingly. Finally, it listens for the `destroy` event and removes the effect from the camera's post-effects queue.

## Example Usage

To use the `Vignette` script in a PlayCanvas project, you can attach it to a camera entity. You can then adjust the `offset` and `darkness` attributes to achieve the desired effect. For example:

```javascript
var cameraEntity = app.root.findByName('Camera');
cameraEntity.addComponent('script');
cameraEntity.script.create('vignette', {
    offset: 0.5,
    darkness: 0.5
});
```

This will add a vignette effect to the camera with an offset of 0.5 and a darkness of 0.5.
## Questions: 
 1. What is the purpose of this code?
- This code implements the VignetteEffect post processing effect in the PlayCanvas engine.

2. What are the properties of the VignetteEffect?
- The VignetteEffect has two properties: offset, which controls the offset of the effect, and darkness, which controls the darkness of the effect.

3. How is the VignetteEffect applied to an entity's camera?
- The VignetteEffect is added to an entity's camera postEffects queue in the initialize function of the Vignette script, and can be enabled or disabled using the state attribute.