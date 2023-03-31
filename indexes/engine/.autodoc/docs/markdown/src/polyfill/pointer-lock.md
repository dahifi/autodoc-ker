[View code on GitHub](https://github.com/playcanvas/engine/src/polyfill/pointer-lock.js)

The code above is responsible for applying PointerLock shims to the PlayCanvas engine. PointerLock is a browser API that allows for locking the mouse cursor to a specific element on the page, which is useful for games and other interactive applications. The code checks if the browser supports PointerLock and applies shims if necessary to ensure that the API works as expected.

The code starts by checking if the `navigator` and `document` objects are defined, which indicates that the code is running in a browser environment. If not, the code returns and does nothing. Otherwise, it sets the `navigator.pointer` object to the appropriate vendor-specific implementation of the PointerLock API (`navigator.webkitPointer` or `navigator.mozPointer`).

Next, the code sets up event listeners for the `pointerlockchange` and `pointerlockerror` events, which are fired when the pointer lock state changes or an error occurs. The event listeners create custom events using the `document.createEvent()` method and dispatch them using the `document.dispatchEvent()` method.

The code then sets up `requestPointerLock` and `exitPointerLock` methods on the `Element.prototype` object. These methods are used to request and release pointer lock on an element. The code first checks if the browser supports the `mozRequestPointerLock` method, which is used by Firefox. If so, it sets the `requestPointerLock` method to call `mozRequestPointerLock()` on the element. Otherwise, it checks if the browser supports the standard `requestPointerLock` method or the vendor-specific `webkitRequestPointerLock` or `mozRequestPointerLock` methods. If none of these methods are supported and the `navigator.pointer` object is defined, the code sets the `requestPointerLock` method to manually lock the pointer using the `navigator.pointer.lock()` method.

Finally, the code sets up the `exitPointerLock` method on the `document` object. This method is used to release pointer lock on the current element. The code first checks if the browser supports the standard `exitPointerLock` method or the vendor-specific `webkitExitPointerLock` or `mozExitPointerLock` methods. If none of these methods are supported and the `navigator.pointer` object is defined, the code manually unlocks the pointer using the `navigator.pointer.unlock()` method.

Overall, this code ensures that the PointerLock API works as expected in the PlayCanvas engine, regardless of the browser being used. It sets up event listeners and shim methods to ensure that the API is consistent across different browsers and vendor-specific implementations. Here is an example of how the `requestPointerLock` method might be used in the PlayCanvas engine:

```
var canvas = document.getElementById('my-canvas');
canvas.addEventListener('click', function () {
    canvas.requestPointerLock();
});
```
## Questions: 
 1. What is the purpose of this code?
    
    This code applies PointerLock shims to the browser to enable pointer locking for mouse input in the PlayCanvas engine.

2. What browsers does this code support?
    
    This code supports browsers that implement the Pointer Lock API, including Firefox, Chrome, and Safari.

3. What is the difference between `pointerlockchange` and `pointerlockerror` events?
    
    `pointerlockchange` event is triggered when the pointer lock state changes, while `pointerlockerror` event is triggered when an error occurs while trying to acquire or release the pointer lock.