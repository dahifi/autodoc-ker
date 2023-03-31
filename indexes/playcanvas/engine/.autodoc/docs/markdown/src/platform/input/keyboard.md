[View code on GitHub](https://github.com/playcanvas/engine/src/platform/input/keyboard.js)

The code defines a `Keyboard` class that represents a keyboard device bound to an HTML element. It allows the detection of the state of key presses and fires events when a key is pressed, released, or held down. 

The class extends the `EventHandler` class, which provides functionality for registering and unregistering event handlers. The `Keyboard` class constructor takes an optional `element` parameter that specifies the HTML element to attach the keyboard event handlers to. If no element is specified, the keyboard event handlers are not attached to any element.

The `Keyboard` class defines three events: `keydown`, `keyup`, and `keypress`. These events are fired when a key is pressed, released, or held down, respectively. The events are implemented using the `fire` method of the `EventHandler` class.

The `Keyboard` class provides methods for testing the state of a key. The `isPressed` method returns `true` if the specified key is currently pressed, and `false` otherwise. The `wasPressed` method returns `true` if the specified key was pressed since the last update, and `false` otherwise. The `wasReleased` method returns `true` if the specified key was released since the last update, and `false` otherwise.

The `Keyboard` class also defines several private methods that handle the browser keyboard events. These methods are `_handleKeyDown`, `_handleKeyUp`, and `_handleKeyPress`. They are called when a key is pressed, released, or held down, respectively. These methods update the internal state of the `Keyboard` object and fire the appropriate events.

The `Keyboard` class also defines several private properties that are used to store the state of the keyboard. These properties are `_keymap`, `_lastmap`, and `_element`. The `_keymap` property is an object that maps key identifiers to `true` if the key is currently pressed, and `false` otherwise. The `_lastmap` property is an object that maps key identifiers to `true` if the key was pressed since the last update, and `false` otherwise. The `_element` property is the HTML element that the keyboard event handlers are attached to.

The `Keyboard` class also defines several private helper functions. The `makeKeyboardEvent` function converts a browser keyboard event to a PlayCanvas keyboard event. The `toKeyCode` function converts a string or keycode to a keycode. The `toKeyIdentifier` function converts a keycode to a key identifier.

Overall, the `Keyboard` class provides a convenient way to handle keyboard events in a PlayCanvas application. It allows the detection of the state of key presses and provides events that can be used to trigger actions in the application.
## Questions: 
 1. What is the purpose of the `makeKeyboardEvent` function?
- The `makeKeyboardEvent` function converts a browser keyboard event to a PlayCanvas keyboard event.

2. What is the difference between `isPressed` and `wasPressed` methods in the `Keyboard` class?
- The `isPressed` method returns true if the key is currently down, while the `wasPressed` method returns true if the key was pressed since the last update.

3. What is the purpose of the `_handleVisibilityChange` method in the `Keyboard` class?
- The `_handleVisibilityChange` method handles the browser visibilitychange event and calls `_handleWindowBlur` method if the document is hidden.