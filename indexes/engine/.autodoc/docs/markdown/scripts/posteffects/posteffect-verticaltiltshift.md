[View code on GitHub](https://github.com/playcanvas/engine/scripts/posteffects/posteffect-verticaltiltshift.js)

# PlayCanvas Engine: VerticalTiltShiftEffect

The `VerticalTiltShiftEffect` is a post-processing effect that creates a fake tilt-shift effect by modulating a two-pass Gaussian blur by vertical position. This effect is used to simulate a miniature scene by blurring the top and bottom of the image, creating a shallow depth of field effect. 

The `VerticalTiltShiftEffect` is a class that extends the `PostEffect` class, which is a base class for all post-processing effects in the PlayCanvas engine. The `VerticalTiltShiftEffect` constructor takes a `GraphicsDevice` object as a parameter and creates a new instance of the post effect. The `focus` property controls where the "focused" horizontal line lies.

The `VerticalTiltShiftEffect` uses a fragment shader to apply the effect. The shader takes a color buffer texture as input and applies a vertical blur to it. The amount of blur is controlled by the `focus` property. The shader code is written in GLSL and is compiled at runtime using the `createShaderFromCode` method of the `pc` object.

The `render` method of the `VerticalTiltShiftEffect` class is responsible for rendering the effect. It takes an input target, an output target, and a rectangle as parameters. The method sets the values of the shader uniforms and draws a quad using the shader.

The `VerticalTiltShift` script is a wrapper around the `VerticalTiltShiftEffect` class that can be attached to a camera entity in the scene. The script adds the effect to the camera's post-effects queue and provides a user interface for controlling the `focus` property. The `initialize` method of the script creates a new instance of the `VerticalTiltShiftEffect` class and adds it to the camera's post-effects queue. The `on` method is used to listen for changes to the `focus` property and update the effect accordingly. The `on` method is also used to listen for changes to the script's state and enable or disable the effect accordingly. Finally, the `on` method is used to remove the effect from the post-effects queue when the script is destroyed.

Example usage:

```javascript
var cameraEntity = new pc.Entity();
cameraEntity.addComponent('camera', {
    postEffects: new pc.PostEffectQueue()
});
cameraEntity.addComponent('script');
cameraEntity.script.create('verticalTiltShift', {
    focus: 0.5
});
```
## Questions: 
 1. What does this code do?
- This code defines a post effect called VerticalTiltShiftEffect that creates a fake tilt-shift effect by modulating two pass Gaussian blur by vertical position. It also defines a script called VerticalTiltShift that initializes the effect and adds it to the camera's post effects queue.

2. What is the purpose of the `focus` property?
- The `focus` property controls where the "focused" horizontal line lies in the tilt-shift effect.

3. Who is the author of the shader used in this code?
- The shader author is alteredq from http://alteredqualia.com/.