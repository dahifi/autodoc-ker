[View code on GitHub](https://github.com/playcanvas/engine/src/platform/input/keyboard-event.js)

The code defines a class called `KeyboardEvent` which represents a key press or release event on a keyboard. This class is used in the PlayCanvas engine to handle keyboard input events. 

The `KeyboardEvent` class has a constructor that takes two parameters: a `keyboard` object and an `event` object. The `keyboard` object is the instance of the `Keyboard` class that is firing the event. The `event` object is the original browser event that was fired. 

The `KeyboardEvent` class has three properties: `key`, `element`, and `event`. The `key` property represents the keyCode of the key that has changed. The `element` property represents the element that fired the keyboard event. The `event` property represents the original browser event which was fired. 

The `KeyboardEvent` class is used in the PlayCanvas engine to handle keyboard input events. For example, the following code shows how to use the `KeyboardEvent` class to handle a key down event for the space key:

```
var onKeyDown = function (e) {
    if (e.key === pc.KEY_SPACE) {
        // space key pressed
    }
    e.event.preventDefault(); // Use original browser event to prevent browser action.
};
app.keyboard.on("keydown", onKeyDown, this);
```

In this code, the `onKeyDown` function is called when a key down event is fired on the keyboard. The `e` parameter is an instance of the `KeyboardEvent` class. The `if` statement checks if the `key` property of the `KeyboardEvent` instance is equal to the `pc.KEY_SPACE` constant, which represents the space key. If the space key is pressed, the code inside the `if` statement is executed. The `e.event.preventDefault()` line prevents the default browser action for the key down event.
## Questions: 
 1. What is the purpose of the KeyboardEvent class?
    
    The KeyboardEvent class is used to represent a key press or release event and is passed into all event callbacks from the Keyboard.

2. What parameters are required to create a new KeyboardEvent instance?
    
    A new KeyboardEvent instance requires a keyboard object and the original browser event that was fired.

3. What properties are available on a KeyboardEvent instance?
    
    A KeyboardEvent instance has three properties: key (the keyCode of the key that has changed), element (the element that fired the keyboard event), and event (the original browser event which was fired).