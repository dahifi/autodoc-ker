[View code on GitHub](https://github.com/playcanvas/engine/src/core/indexed-list.js)

The `IndexedList` class is a data structure that allows for the storage of items in an ordered list, with the ability to look up items by a unique key. The class contains a private `_list` property, which is an array that stores the items in the order they were added, and a private `_index` property, which is an object that maps keys to the index of the corresponding item in the `_list` array.

The `push` method is used to add a new item to the list with a unique key. If the key already exists in the index, an error is thrown. Otherwise, the item is added to the end of the `_list` array, and its index is stored in the `_index` object using the provided key.

The `has` method is used to test whether a key has been added to the index. It returns `true` if the key is in the index, and `false` otherwise.

The `get` method is used to retrieve an item from the list using its key. If the key is in the index, the method returns the corresponding item from the `_list` array. If the key is not in the index, the method returns `null`.

The `remove` method is used to remove an item from the list using its key. If the key is in the index, the corresponding item is removed from the `_list` array, and its index is removed from the `_index` object. The method returns `true` if an item was removed, and `false` otherwise.

The `list` method is used to return the entire list of items in the order they were added.

The `clear` method is used to remove all items from the list and reset the index.

This data structure can be useful in a variety of scenarios where items need to be stored in an ordered list and accessed by a unique key. For example, it could be used to store entities in a game engine, where each entity has a unique ID that can be used to look it up quickly. Here is an example of how the `IndexedList` class could be used:

```
const entities = new IndexedList();

// Add some entities
entities.push('player', { name: 'Player', health: 100 });
entities.push('enemy1', { name: 'Enemy 1', health: 50 });
entities.push('enemy2', { name: 'Enemy 2', health: 75 });

// Get an entity by key
const player = entities.get('player');
console.log(player); // { name: 'Player', health: 100 }

// Remove an entity by key
entities.remove('enemy1');

// Get the entire list of entities
const allEntities = entities.list();
console.log(allEntities); // [{ name: 'Player', health: 100 }, { name: 'Enemy 2', health: 75 }]
```
## Questions: 
 1. What is the purpose of this `IndexedList` class?
- The `IndexedList` class is a data structure that allows for item lookup by key and can also return a list.

2. What are the private properties of the `IndexedList` class?
- The private properties of the `IndexedList` class are `_list`, which is an array of objects, and `_index`, which is an object with string keys and number values.

3. What happens when a key already exists in the index during a `push` operation?
- If a key already exists in the index during a `push` operation, an error will be thrown with the message "Key already in index" followed by the key that already exists.