[View code on GitHub](https://github.com/playcanvas/engine/src/platform/input/controller.js)

The `Controller` class is a general input handler that handles both mouse and keyboard input assigned to named actions. This allows you to define input handlers separately from defining keyboard/mouse configurations. The class is part of the PlayCanvas engine project and is located in a file that imports `type` and several constants from other files. It also imports `Keyboard` and `Mouse` classes from other files.

The `Controller` class has several methods that allow you to attach and detach the controller to an element, enable and disable the context menu, update the keyboard and mouse handlers, register actions against a controller axis, and check if an action is enabled or was enabled since the last update. 

The `Controller` class constructor takes an optional `element` parameter and an optional `options` object that can contain a `keyboard`, `mouse`, or `gamepads` object. If an `element` is provided, the `attach` method is called to attach the keyboard and mouse event handlers to the element. 

The `registerKeys`, `registerMouse`, and `registerPadButton` methods allow you to create or update an action that is enabled when the supplied keys, mouse button, or gamepad button is pressed. The `registerAxis` method allows you to register an action against a controller axis. 

The `isPressed` and `wasPressed` methods allow you to check if an action is currently enabled or was enabled since the last update. The `getAxis` method returns the value of the specified controller axis.

Overall, the `Controller` class provides a way to handle input from multiple sources and assign it to named actions, making it easier to manage input in a larger project. 

Example usage:

```
import { Controller } from 'playcanvas';

const controller = new Controller(document);

controller.registerKeys('move_forward', [pc.KEY_W]);
controller.registerKeys('move_backward', [pc.KEY_S]);
controller.registerKeys('strafe_left', [pc.KEY_A]);
controller.registerKeys('strafe_right', [pc.KEY_D]);

controller.registerMouse('shoot', pc.MOUSEBUTTON_LEFT);

controller.registerPadButton('jump', PAD_1, pc.PAD_FACE_1);

controller.registerAxis({
    name: 'move',
    positive: 'key',
    positiveKey: pc.KEY_W,
    negative: 'key',
    negativeKey: pc.KEY_S
});

controller.update(dt);

if (controller.isPressed('move_forward')) {
    // move forward
}

if (controller.wasPressed('shoot')) {
    // shoot
}

const moveValue = controller.getAxis('move');
if (moveValue !== 0) {
    // move left or right
}
```
## Questions: 
 1. What is the purpose of the `Controller` class?
- The `Controller` class is a general input handler that handles both mouse and keyboard input assigned to named actions, allowing developers to define input handlers separately from defining keyboard/mouse configurations.

2. What are the different types of input actions that can be registered with the `Controller` class?
- The different types of input actions that can be registered with the `Controller` class are keyboard, mouse, and gamepad actions.

3. How can a developer check if a specific action is enabled or was enabled since the last update?
- A developer can check if a specific action is enabled or was enabled since the last update by calling the `isPressed` or `wasPressed` method of the `Controller` class and passing in the name of the action as a parameter.