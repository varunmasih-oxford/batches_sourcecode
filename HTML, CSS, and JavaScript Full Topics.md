# HTML, CSS, and JavaScript Topics

---

# HTML (HyperText Markup Language)

## 1. Basics

* What is HTML – Standard language used to structure web pages.
  Example:

```html
<h1>Hello</h1>
```

* Structure of HTML document – Basic skeleton of a webpage.
  Example:

```html
<!DOCTYPE html>
<html>
<head></head>
<body></body>
</html>
```

* Tags, Elements, Attributes – Tags define elements, attributes add extra info.
  Example:

```html
<img src="img.jpg" alt="image">
```

* Headings, Paragraphs – Used for text content.
  Example:

```html
<p>This is text</p>
```

* Formatting tags – Used to style text.
  Example:

```html
<b>Bold</b>
```

## 2. Links & Media

* Anchor tag (`<a>`) – Used to create hyperlinks.
  Example:

```html
<a href="https://google.com">Go</a>
```

* Image tag (`<img>`) – Displays images.
  Example:

```html
<img src="img.jpg">
```

* Audio & Video – Embeds media files.
  Example:

```html
<video src="video.mp4" controls></video>
```

* Iframe – Embeds another webpage.
  Example:

```html
<iframe src="https://example.com"></iframe>
```

## 3. Lists

* Ordered list – Numbered list.
  Example:

```html
<ol>
  <li>Item</li>
</ol>
```

* Unordered list – Bulleted list.
  Example:

```html
<ul>
  <li>Item</li>
</ul>
```

* Description list – Key-value list.
  Example:

```html
<dl>
  <dt>Name</dt>
  <dd>Value</dd>
</dl>
```

## 4. Tables

* Table structure – Used to display tabular data.
  Example:

```html
<table>
  <tr>
    <td>Data</td>
  </tr>
</table>
```

* `<thead>`, `<tbody>`, `<tfoot>` – Sections of a table.
  Example:

```html
<thead>
  <tr><th>Head</th></tr>
</thead>
```

* Colspan & Rowspan – Merge cells.
  Example:

```html
<td colspan="2">Merged</td>
```

## 5. Forms

* Form structure – Used to collect user input.
  Example:

```html
<form></form>
```

* Input types – Different input fields.
  Example:

```html
<input type="text">
```

* Labels – Describe inputs.
  Example:

```html
<label>Name</label>
```

* Buttons – Trigger actions.
  Example:

```html
<button>Submit</button>
```

* Select dropdown – Choose options.
  Example:

```html
<select>
  <option>A</option>
</select>
```

* Textarea – Multi-line input.
  Example:

```html
<textarea></textarea>
```

* Form validation – Ensures correct input.
  Example:

```html
<input required>
```

## 6. Semantic HTML

* `<header>`, `<footer>`, `<section>`, `<article>` – Provide meaning to layout.
  Example:

```html
<header>Top</header>
```

* `<nav>`, `<aside>` – Navigation and side content.
  Example:

```html
<nav>Menu</nav>
```

* SEO basics – Helps search engines understand content.
  Example:

```html
<title>Page</title>
```

## 7. HTML5 Features

* Local Storage – Stores data in browser.
  Example:

```js
localStorage.setItem("key","value")
```

* Session Storage – Stores data per session.
  Example:

```js
sessionStorage.setItem("k","v")
```

* Geolocation API – Gets user location.
  Example:

```js
navigator.geolocation.getCurrentPosition(()=>{})
```

* Drag & Drop – Enables dragging elements.
  Example:

```html
<div draggable="true"></div>
```

* Canvas & SVG – Used for graphics.
  Example:

```html
<canvas></canvas>
```

---

# CSS (Cascading Style Sheets)

## 1. Basics

* What is CSS – Styles HTML elements.
  Example:

```css
p { color: red; }
```

* Inline, Internal, External CSS – Ways to apply styles.
  Example:

```html
<p style="color:red">Text</p>
```

* Selectors – Target elements.
  Example:

```css
.class { }
```

* Colors, Backgrounds – Add colors and images.
  Example:

```css
background: blue;
```

## 2. Box Model

* Margin, Border, Padding, Content – Spacing around elements.
  Example:

```css
margin:10px;
```

* Width & Height – Size of elements.
  Example:

```css
width:100px;
```

* Box-sizing – Controls size calculation.
  Example:

```css
box-sizing: border-box;
```

## 3. Typography

* Fonts – Change text font.
  Example:

```css
font-family: Arial;
```

* Text styling – Style text.
  Example:

```css
text-align: center;
```

* Line height, letter spacing – Control spacing.
  Example:

```css
line-height: 1.5;
```

## 4. Layout

* Display – Defines layout type.
  Example:

```css
display: flex;
```

* Position – Controls placement.
  Example:

```css
position: absolute;
```

* Float & Clear – Old layout method.
  Example:

```css
float: left;
```

## 5. Flexbox

* Flex container & items – Flexible layout system.
  Example:

```css
display: flex;
```

* justify-content – Align horizontally.
  Example:

```css
justify-content: center;
```

* align-items – Align vertically.
  Example:

```css
align-items: center;
```

* flex-direction – Row or column.
  Example:

```css
flex-direction: column;
```

* gap – Space between items.
  Example:

```css
gap: 10px;
```

## 6. Grid

* Grid container – Defines grid layout.
  Example:

```css
display: grid;
```

* Rows & columns – Structure grid.
  Example:

```css
grid-template-columns: 1fr 1fr;
```

* Grid areas – Named layout areas.
  Example:

```css
grid-area: header;
```

* Responsive grid – Adjust grid for screens.
  Example:

```css
grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
```

## 7. Responsive Design

* Media queries – Apply styles for screen sizes.
  Example:

```css
@media (max-width:600px) {
}
```

* Mobile-first design – Design for small screens first.
  Example:

```css
/* base styles for mobile */
```

* Breakpoints – Screen size limits.
  Example:

```text
768px
```

## 8. Advanced CSS

* Transitions – Smooth changes.
  Example:

```css
transition: 0.3s;
```

* Animations – Keyframe animations.
  Example:

```css
@keyframes move {}
```

* Transform – Move/rotate elements.
  Example:

```css
transform: rotate(45deg);
```

* Shadows – Add shadow effects.
  Example:

```css
box-shadow: 2px 2px 5px;
```

* Gradients – Color transitions.
  Example:

```css
background: linear-gradient(red, blue);
```

## 9. CSS Preprocessors (Optional)

* SASS / SCSS basics – Advanced CSS with variables.
  Example:

```scss
$color: red;
```

## 10. Frameworks

* Bootstrap basics – Prebuilt CSS framework.
  Example:

```html
<div class="container"></div>
```

* Tailwind CSS basics – Utility-first CSS.
  Example:

```html
<div class="text-red-500"></div>
```

---

# JavaScript (JS)

## 1. Basics

* What is JavaScript – Adds logic to web pages.
  Example:

```js
alert("Hi")
```

* Variables – Store data.
  Example:

```js
let x = 10;
```

* Data types – Types of data.
  Example:

```js
let name = "A";
```

* Operators – Perform operations.
  Example:

```js
x + y;
```

## 2. Control Statements

* if, else, switch – Conditional logic.
  Example:

```js
if(x > 5) {}
```

* Loops – Repeat code.
  Example:

```js
for(let i = 0; i < 5; i++) {}
```

## 3. Functions

* Function declaration – Define function.
  Example:

```js
function a() {}
```

* Arrow functions – Short syntax.
  Example:

```js
const fn = () => {}
```

* Parameters & return – Input/output.
  Example:

```js
function sum(a,b){ return a+b }
```

## 4. Arrays & Objects

* Array methods – Work with arrays.
  Example:

```js
[1,2].map(x => x*2)
```

* Object properties & methods – Store key-value data.
  Example:

```js
let obj = {name:"A"}
```

## 5. DOM Manipulation

* Selecting elements – Access HTML.
  Example:

```js
document.querySelector("p")
```

* Changing content – Modify text.
  Example:

```js
elem.innerHTML = "Hi"
```

* Styling via JS – Change CSS.
  Example:

```js
elem.style.color = "red"
```

* Creating & removing elements – Modify DOM.
  Example:

```js
document.createElement("div")
```

## 6. Events

* Click, submit, change – User actions.
  Example:

```js
button.onclick = fn
```

* Event listeners – Handle events.
  Example:

```js
elem.addEventListener("click", fn)
```

* Event bubbling & capturing – Event flow.
  Example:

```text
child → parent
```

## 7. ES6+ Features

* let & const – Modern variables.
  Example:

```js
const a = 1;
```

* Arrow functions – Short functions.
  Example:

```js
()=>{}
```

* Template literals – String formatting.
  Example:

```js
`Hi ${x}`
```

* Destructuring – Extract values.
  Example:

```js
const {a} = obj
```

* Spread & Rest – Expand/collect data.
  Example:

```js
[...arr]
```

## 8. Advanced JavaScript

* Closures – Function with memory.
  Example:

```js
function outer(){ return function(){} }
```

* Hoisting – Variables moved up.
  Example:

```js
console.log(a); var a = 5;
```

* Callbacks – Function as argument.
  Example:

```js
fn(()=>{})
```

* Promises – Handle async.
  Example:

```js
new Promise(()=>{})
```

* Async/Await – Cleaner async.
  Example:

```js
await fetch(url)
```

## 9. Browser APIs

* Local Storage – Store data.
  Example:

```js
localStorage.setItem("k","v")
```

* Fetch API – Call APIs.
  Example:

```js
fetch(url)
```

* JSON handling – Data format.
  Example:

```js
JSON.parse("{}")
```

## 10. Error Handling

* try...catch – Handle errors.
  Example:

```js
try{}catch(e){}
```

* throw – Custom errors.
  Example:

```js
throw "Error"
```

## 11. OOP in JavaScript

* Classes & Objects – OOP structure.
  Example:

```js
class A {}
```

* Constructor – Initialize object.
  Example:

```js
constructor(){}
```

* Inheritance – Reuse code.
  Example:

```js
class B extends A {}
```

## 12. Modules

* Import / Export – Share code.
  Example:

```js
export default fn
```
