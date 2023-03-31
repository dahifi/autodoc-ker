[View code on GitHub](https://github.com/playcanvas/engine/scripts/posteffects/posteffect-horizontaltiltshift.js)

# PlayCanvas Engine: Horizontal Tilt-Shift Effect

The `HorizontalTiltShiftEffect` class is a post-processing effect that creates a fake tilt-shift effect by modulating a two-pass Gaussian blur by horizontal position. This effect is used to simulate a miniature scene or to create a shallow depth-of-field effect.

## How it Works

The `HorizontalTiltShiftEffect` class extends the `PostEffect` class and overrides the `render` method. The `render` method takes an input target, an output target, and a rectangle and applies the tilt-shift effect to the input target, rendering the result to the output target.

The `HorizontalTiltShiftEffect` class uses a custom fragment shader to apply the tilt-shift effect. The shader takes a color buffer texture, a horizontal offset (`uH`), and a focus value (`uR`) as input. The shader calculates a weighted sum of nine texture samples, each offset horizontally by a multiple of the focus value. The weights of the samples are determined by a Gaussian distribution.

The `HorizontalTiltShiftEffect` class also defines a `focus` property that controls the position of the "focused" vertical line. The `focus` property is used to set the `uR` uniform in the shader.

The `HorizontalTiltShift` script is a wrapper around the `HorizontalTiltShiftEffect` class that adds the effect to a camera's post-effects queue. The script defines a `focus` attribute that can be set in the editor or via script. The script creates an instance of the `HorizontalTiltShiftEffect` class and adds it to the camera's post-effects queue. The script also listens for changes to the `focus` attribute and updates the effect accordingly.

## Example

To use the `HorizontalTiltShift` script, attach it to a camera entity in your scene. You can adjust the `focus` attribute to control the position of the "focused" vertical line.

```javascript
var camera = app.root.findByName('Camera');
camera.addComponent('script');
camera.script.create('horizontalTiltShift', {
    focus: 0.5
});
```

## Limitations

The `HorizontalTiltShiftEffect` class only applies the tilt-shift effect horizontally. To apply the effect vertically, you would need to create a separate effect or modify the existing shader. Additionally, the effect is computationally expensive and may impact performance on low-end devices.
## Questions: 
 1. What is the purpose of this code?
- This code defines a post effect called HorizontalTiltShiftEffect that creates a fake tilt-shift effect by modulating a two-pass Gaussian blur by horizontal position.

2. What graphics device does this code require?
- This code requires a graphics device of the application as a parameter for creating a new instance of the post effect.

3. What is the range of values for the "focus" property?
- The "focus" property has a default value of 0.35 and a range of values from 0 to 1.