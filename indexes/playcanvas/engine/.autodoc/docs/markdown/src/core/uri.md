[View code on GitHub](https://github.com/playcanvas/engine/src/core/uri.js)

## Code Explanation: PlayCanvas Engine - URI

The `createURI` function and `URI` class are part of the PlayCanvas engine project. The purpose of this code is to provide a way to create and manipulate URI objects. 

The `createURI` function takes an object as an argument, which contains the different parts of a URI. It then constructs a URI string from these parts and returns it. The different parts of the URI that can be passed as options include the scheme, authority, host, path, hostpath, query, and fragment. 

The `URI` class is used to represent a URI object. It takes a URI string as an argument and parses it into its constituent parts. The different parts of the URI are then stored as properties of the `URI` object. The `toString` method is used to convert the `URI` object back into a URI string. 

The `getQuery` method is used to extract the query parameters from the URI and return them as an object. The `setQuery` method is used to set the query parameters of the URI from an object. 

Overall, this code provides a way to create, parse, and manipulate URI objects in the PlayCanvas engine project. 

Example usage:

```javascript
const uriString = 'https://www.example.com/path/to/resource?key=value#fragment';
const uri = new URI(uriString);

console.log(uri.scheme); // logs "https"
console.log(uri.authority); // logs "www.example.com"
console.log(uri.path); // logs "/path/to/resource"
console.log(uri.query); // logs "key=value"
console.log(uri.fragment); // logs "fragment"

uri.setQuery({ key: 'newvalue' });
console.log(uri.toString()); // logs "https://www.example.com/path/to/resource?key=newvalue#fragment"
```
## Questions: 
 1. What is the purpose of the `createURI` function?
- The `createURI` function is used to create a URI string from constituent parts such as scheme, authority, host, path, query, and fragment.

2. What is the purpose of the `URI` class?
- The `URI` class is used to represent a URI object and provides methods to manipulate and retrieve information from the URI.

3. What is the purpose of the `getQuery` method in the `URI` class?
- The `getQuery` method is used to extract the query parameters from the URI and return them as an object.