[View code on GitHub](https://github.com/playcanvas/engine/src/core/sorted-loop-array.js)

The `SortedLoopArray` class is a helper class used to hold an array of items in a specific order. The class is designed to hold objects that need to be sorted based on one of their fields. The class is safe to modify while looping through it. 

The class has several properties and methods. The `items` property is an internal array that holds the actual array elements. The `length` property is the number of elements in the array. The `loopIndex` property is the current index used to loop through the array. This gets modified if we add or remove elements from the array while looping. 

The class has a constructor that takes an object with a `sortBy` property. The `sortBy` property is the name of the field that each element in the array is going to be sorted by. The class has an `_binarySearch` method that searches for the right spot to insert the specified item. The method uses a binary search algorithm to find the right index. 

The class has an `insert` method that inserts the specified item into the array at the right index based on the `sortBy` field passed into the constructor. This also adjusts the `loopIndex` accordingly. The class has an `append` method that appends the specified item to the end of the array. This method is faster than `insert()` as it does not binary search for the right index. This also adjusts the `loopIndex` accordingly. The class has a `remove` method that removes the specified item from the array.

The class has a `sort` method that sorts elements in the array based on the `sortBy` field passed into the constructor. This also updates the `loopIndex` if we are currently looping. The method uses the `_doSort` method to sort the array. The `_doSort` method is a private method that takes two items and compares them based on the `sortBy` field. 

The `SortedLoopArray` class can be used in the larger project to hold an array of objects that need to be sorted based on one of their fields. The class can be used to insert, append, and remove items from the array while looping through it. The class can also be used to sort the array based on the `sortBy` field. 

Example usage:

```
var array = new SortedLoopArray({ sortBy: 'priority' });
array.insert(item); // adds item to the right slot based on item.priority
array.append(item); // adds item to the end of the array
array.remove(item); // removes item from array
for (array.loopIndex = 0; array.loopIndex < array.length; array.loopIndex++) {
  // do things with array elements
  // safe to remove and add elements into the array while looping
}
```
## Questions: 
 1. What is the purpose of this class and how is it used?
- This class is a helper class used to hold an array of items in a specific order that is safe to modify while looping through it. It assumes that it holds objects that need to be sorted based on one of their fields. It can be used to insert, append, and remove items from the array, as well as sort the elements based on the specified field.
2. What is the significance of the `_binarySearch` method?
- The `_binarySearch` method is used to search for the right spot to insert the specified item into the array based on the `sortBy` field passed into the constructor. It performs a binary search on the array to find the correct index to insert the item, which makes it more efficient than a linear search.
3. What is the potential issue with sorting the array while iterating through it?
- If the array is sorted while iterating through it, the element that is currently being processed might be moved behind other elements, which could cause it to be iterated over more than once. This can lead to unexpected behavior and should be avoided.