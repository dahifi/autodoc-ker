[View code on GitHub](https://github.com/playcanvas/engine/src/core/shape/frustum.js)

# PlayCanvas Engine - Frustum Class

The `Frustum` class is a shape that defines the viewing space of a camera. It can be used to determine visibility of points and bounding spheres. Typically, you would not create a Frustum shape directly, but instead query `CameraComponent#frustum`.

The `Frustum` class has the following methods:

## constructor()

The constructor creates a new `Frustum` instance. It initializes the `planes` array with six empty arrays.

```javascript
var frustum = new pc.Frustum();
```

## setFromMat4(matrix)

The `setFromMat4` method updates the frustum shape based on the supplied 4x4 matrix. It extracts the numbers for the six planes of the frustum and normalizes the result. The `matrix` parameter is an instance of `Mat4` class.

```javascript
// Create a perspective projection matrix
var projMat = pc.Mat4();
projMat.setPerspective(45, 16 / 9, 1, 1000);

// Create a frustum shape that is represented by the matrix
var frustum = new pc.Frustum();
frustum.setFromMat4(projMat);
```

## containsPoint(point)

The `containsPoint` method tests whether a point is inside the frustum. Note that points lying in a frustum plane are considered to be outside the frustum. The `point` parameter is an instance of `Vec3` class.

```javascript
var point = new pc.Vec3(1, 2, 3);
var isInside = frustum.containsPoint(point);
```

## containsSphere(sphere)

The `containsSphere` method tests whether a bounding sphere intersects the frustum. If the sphere is outside the frustum, zero is returned. If the sphere intersects the frustum, 1 is returned. If the sphere is completely inside the frustum, 2 is returned. Note that a sphere touching a frustum plane from the outside is considered to be outside the frustum. The `sphere` parameter is an instance of `BoundingSphere` class.

```javascript
var sphere = new pc.BoundingSphere(new pc.Vec3(1, 2, 3), 4);
var result = frustum.containsSphere(sphere);
```
## Questions: 
 1. What is a Frustum and how is it used in PlayCanvas engine?
- A Frustum is a shape that defines the viewing space of a camera and is used to determine visibility of points and bounding spheres. It is typically queried through the CameraComponent#frustum method.
2. What does the setFromMat4 method do?
- The setFromMat4 method updates the frustum shape based on the supplied 4x4 matrix. It extracts the numbers for each plane of the frustum and normalizes the result.
3. How does the containsSphere method determine if a sphere intersects the frustum?
- The containsSphere method checks if the sphere is outside the frustum by calculating the distance between the sphere center and each plane of the frustum. If the distance is less than or equal to the negative radius of the sphere, it is outside the frustum. If the distance is greater than the radius, it intersects the frustum. If the sphere is completely inside the frustum, it is contained by the frustum.