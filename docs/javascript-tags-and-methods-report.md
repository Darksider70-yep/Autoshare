# Autoshare — JavaScript Reference & Tags Report

> One-line explanation of every `<script>` tag, inline handler, keyword, DOM API, event, array method, and global object used across `index.html` and `app.js`.

---

## HTML `<script>` Tags & Inline Handlers

| Tag / Code | Source File | Line | One-Line Explanation |
|---|---|---|---|
| `<script src="https://unpkg.com/lucide@latest"></script>` | `index.html` | Line 256 | Loads the external Lucide Icons CDN library to render SVG icons dynamically across the UI. |
| `<script src="app.js"></script>` | `index.html` | Line 258 | Imports and executes the local application script containing all state, filters, and interactivity. |
| `onclick="resetFilters()"` | `app.js` (DOM template) | Line 138 | Triggers the global `resetFilters()` function when clicking the empty-state reset button. |
| `onclick="joinRideGroup(${ride.id})"` | `app.js` (DOM template) | Line 226 | Calls `joinRideGroup` with the ride's ID to claim an available seat and join that specific ride. |
| `onclick="openChatWithGroup(${ride.id})"` | `app.js` (DOM template) | Line 228 | Calls `openChatWithGroup` with the ride's ID to open the coordination chat drawer for that group. |

---

## Language Keywords & Declarations

| Keyword / Statement | One-Line Explanation |
|---|---|
| `let` | Declares mutable, block-scoped local variables (e.g., `ridesData`, `activeChatRideId`). |
| `const` | Declares immutable, block-scoped constant references (e.g., DOM handles, simulated messages). |
| `function` | Declares named, reusable blocks of code containing specific business logic. |
| `return` | Stops the execution of a function and optionally passes a value back to the caller. |
| `if...else` | Conditionally executes specific code blocks based on truthy or falsy checks. |
| `for` | Standard loop construct used to iterate over a block of code a set number of times. |
| `typeof` | Operator that returns a string indicating the data type of an unevaluated operand. |

---

## DOM Selection & Manipulation APIs

| API / Property | One-Line Explanation |
|---|---|
| `document.getElementById(id)` | Selects a single unique HTML DOM element by its ID attribute. |
| `document.querySelectorAll(selector)` | Returns a static NodeList of all elements matching a given CSS selector. |
| `document.createElement(tagName)` | Creates a new HTML element node in memory before attaching it to the document. |
| `parentElement.appendChild(childNode)` | Appends a DOM node as the last child of the specified parent element. |
| `element.innerHTML` | Gets or sets the HTML markup content rendered inside a DOM element. |
| `element.textContent` | Gets or sets the raw, unparsed text content of a DOM node. |
| `element.value` | Retrieves or updates the current text/value of an `<input>` or `<select>` element. |
| `element.classList.add(className)` | Adds a CSS class to an element's class list to trigger styling or animation changes. |
| `element.classList.remove(className)` | Removes a CSS class from an element's class list. |
| `element.getAttribute(attrName)` | Reads the value of a specified HTML attribute (e.g., `data-seats`, `data-destination`). |
| `element.scrollIntoView({ behavior })` | Scrolls the browser window smoothly until the target element is visible in the viewport. |
| `element.scrollTop` / `scrollHeight` | Measures and sets the vertical scroll position (used for auto-scrolling chat to bottom). |
| `form.reset()` | Resets all input controls inside a form back to their default values. |

---

## Event Handling APIs

| Event Method / Event Type | One-Line Explanation |
|---|---|
| `element.addEventListener(type, listener)` | Attaches an event handler callback function to run when the specified event fires. |
| `"DOMContentLoaded"` | Fires when the initial HTML document has been fully loaded and parsed. |
| `"click"` | Fires when a mouse or pointing device clicks on an element (buttons, cards, backdrop). |
| `"input"` | Fires synchronously whenever the value of an `<input>` field changes by user typing. |
| `"keypress"` | Fires when a key is pressed (used to detect the `"Enter"` key on search & chat inputs). |
| `event.preventDefault()` | Prevents the browser's default behavior (such as reloading the page on form submit). |
| `event.target` | References the exact DOM element that originally dispatched the event. |
| `event.key` | Returns the key value of the keyboard button that was pressed (e.g., `'Enter'`). |

---

##  Array & Collection Methods

| Array Method | One-Line Explanation |
|---|---|
| `Array.prototype.forEach()` | Executes a provided callback function once for every element in an array. |
| `Array.prototype.find()` | Returns the first element in an array that satisfies a given testing condition. |
| `Array.prototype.filter()` | Returns a newly created array containing only elements that pass the filtering condition. |
| `Array.prototype.map()` | Creates a new array populated with the results of calling a function on each element. |
| `Array.prototype.push()` | Appends one or more items to the end of an array and updates its length. |
| `Array.prototype.unshift()` | Inserts one or more items at the beginning of an array. |
| `Array.prototype.join()` | Joins all elements of an array into a single string separated by a specified delimiter. |

---

## String, Number & Global APIs

| Method / Global Object | One-Line Explanation |
|---|---|
| `String.prototype.toLowerCase()` | Converts a string to lowercase characters for case-insensitive filtering and matching. |
| `String.prototype.toUpperCase()` | Converts a string to uppercase characters (used to generate student avatar initials). |
| `String.prototype.trim()` | Removes whitespace from both the beginning and end of a string. |
| `String.prototype.split()` | Splits a string into an array of substrings using a specified separator. |
| `String.prototype.padStart()` | Pads a string from the start with characters until it reaches a desired length (e.g., `05` for minutes). |
| `String.prototype.includes()` | Checks whether a string contains another substring and returns a boolean. |
| `Number.prototype.toFixed()` | Formats a number to a fixed number of decimal digits as a string. |
| `parseInt()` | Parses a string argument and returns an integer. |
| `parseFloat()` | Parses a string argument and returns a floating-point number. |
| `window` | The global top-level object representing the browser window and global execution scope. |
| `setTimeout()` | Sets a timer that executes a callback function once after a specified number of milliseconds. |
| `Math.random()` | Generates a pseudo-random floating-point number between `0` (inclusive) and `1` (exclusive). |
| `Math.floor()` | Rounds down a floating-point number to the nearest lower integer. |
| `new Date()` | Creates a date instance representing the current timestamp (`getHours()`, `getMinutes()`). |
| `lucide.createIcons()` | Scans the DOM and replaces `<i data-lucide="..."></i>` placeholder elements with Lucide SVG icons. |
