# Autoshare — HTML & CSS Tags Reference Report

> **Project:** Autoshare — Student TukTuk Ride-Sharing Web App  
> **Files Covered:** `index.html`, `style.css`  
> **Purpose:** One-line explanation of every HTML tag and CSS property/rule used in the project.

---

## 📄 HTML Tags Used (`index.html`)

| Tag | Explanation |
|-----|-------------|
| `<!DOCTYPE html>` | Tells the browser this document follows the HTML5 standard. |
| `<html>` | Root element wrapping the entire HTML document; `lang="en"` sets the language. |
| `<head>` | Container for meta-information about the page (not displayed on screen). |
| `<meta charset="UTF-8">` | Sets the character encoding to UTF-8 so special characters render correctly. |
| `<meta name="viewport">` | Controls layout on mobile devices for a responsive design. |
| `<title>` | Sets the text shown on the browser tab. |
| `<meta name="description">` | Provides a short SEO-friendly description of the page for search engines. |
| `<link>` | Links the external `style.css` stylesheet to this HTML page. |
| `<body>` | Contains all the visible content rendered in the browser. |
| `<div>` | A generic block-level container used to group and structure sections and components. |
| `<header>` | Semantic tag for the top section of the page, containing the logo and navigation. |
| `<a>` | Creates a hyperlink; used for the logo (home link) and navigation anchor links. |
| `<nav>` | Semantic tag that groups the site's navigation links together. |
| `<button>` | Creates a clickable button for actions like posting a ride, searching, and closing modals. |
| `<i>` | Inline element used here to embed Lucide SVG icons (via the `data-lucide` attribute). |
| `<main>` | Semantic tag wrapping the primary content of the page (hero + dashboard). |
| `<section>` | Semantic tag that groups related content into distinct named page sections. |
| `<h1>` | The main page heading (largest); used once in the hero section for SEO importance. |
| `<span>` | Generic inline container used to style parts of text (e.g., highlighting "TukTuks"). |
| `<p>` | A paragraph element used for descriptive body text. |
| `<label>` | Associates a text label with a form input for accessibility; `for` links it to the input's `id`. |
| `<select>` | Creates a drop-down list for choosing options like pickup location or departure time. |
| `<option>` | Defines each individual item inside a `<select>` drop-down menu. |
| `<input>` | Single-line field accepting user data; used for text, number, time, and hidden types. |
| `<h2>` | Second-level heading; used for the "Active Ride Offers" feed title. |
| `<h3>` | Third-level heading; used for sidebar card section titles. |
| `<h4>` | Fourth-level heading; used inside dynamically created ride cards for student names. |
| `<h5>` | Fifth-level heading; used for hotspot destination titles in the sidebar. |
| `<footer>` | Semantic tag for the bottom section of the page with copyright info. |
| `<form>` | Wraps all inputs for the "Post a Ride" modal; handles form submission. |
| `<small>` | Renders smaller text; used for helper hints below form fields. |
| `<script>` | Links external JavaScript files (`lucide` icons library and `app.js`). |
| `<!-- comment -->` | HTML comment used to annotate and describe sections of the code. |

---

## 🎨 CSS Properties & Rules Used (`style.css`)

### At-Rules & Selectors

| Rule / Selector | Explanation |
|----------------|-------------|
| `@import url(...)` | Imports the "Plus Jakarta Sans" Google Font from an external URL. |
| `:root { }` | Defines global CSS custom properties (variables) accessible throughout the stylesheet. |
| `*` | Universal selector that resets margin, padding, and box-sizing for every element. |
| `::before` | Pseudo-element used on `.ride-card` to inject the animated gold left-border accent. |
| `:hover` | Pseudo-class that applies styles when the user hovers their mouse over an element. |
| `:focus` | Pseudo-class applied to inputs and selects when they are clicked/tabbed into. |
| `:last-child` | Pseudo-class targeting the last sibling element (used to remove bottom border on last stat row). |
| `:first-child` | Pseudo-class targeting the first sibling element (resets left margin on first co-traveler avatar). |
| `::-webkit-scrollbar` | Pseudo-element to style the browser's scrollbar width. |
| `::-webkit-scrollbar-track` | Styles the scrollbar track (the groove the thumb slides in). |
| `::-webkit-scrollbar-thumb` | Styles the draggable scrollbar handle. |
| `@media (max-width: 992px)` | Media query that applies responsive styles on screens narrower than 992px. |

---

### Layout & Positioning Properties

| Property | Explanation |
|----------|-------------|
| `display: grid` | Activates CSS Grid layout, used for the main app container and dashboard. |
| `display: flex` | Activates Flexbox layout for aligning items in rows or columns. |
| `display: block` | Makes an element take up the full line width (used for labels). |
| `display: inline-flex` | Like flex but inline; used for buttons to flow within text. |
| `grid-template-rows` | Defines the row sizes for a grid container. |
| `grid-template-columns` | Defines column widths in a grid container; used for dashboard and search layouts. |
| `gap` | Sets the spacing between grid or flex child elements. |
| `flex-direction: column` | Stacks flex children vertically (top to bottom). |
| `flex: 1` | Makes a flex item grow to fill available space in a flex row. |
| `align-items` | Aligns flex/grid children along the cross axis (e.g., `center`, `flex-start`). |
| `justify-content` | Distributes flex/grid children along the main axis (e.g., `space-between`, `center`). |
| `position: sticky` | Keeps the header stuck to the top of the viewport while scrolling. |
| `position: fixed` | Removes an element from the page flow and fixes it at a specific screen position (modals, chat). |
| `position: relative` | Positions an element relative to itself; used as a parent for `absolute` children. |
| `position: absolute` | Positions icons or pseudo-elements relative to their nearest positioned ancestor. |
| `top / bottom / left / right` | Defines offset position for fixed, sticky, or absolute elements. |
| `z-index` | Controls the stacking order of overlapping elements (higher = on top). |
| `overflow: hidden` | Clips content that overflows the element's box. |
| `overflow-x: hidden` | Prevents horizontal scrollbar from appearing on the body. |
| `overflow-y: auto` | Adds a vertical scrollbar only when content overflows. |

---

### Sizing Properties

| Property | Explanation |
|----------|-------------|
| `width` | Sets the width of an element (px, %, rem, or `100%`). |
| `height` | Sets the height of an element. |
| `min-height` | Ensures the element is at least a minimum height (used for full-viewport layout). |
| `max-width` | Caps the width so content doesn't stretch too wide on large screens. |
| `max-height` | Caps the height, allowing scroll inside modals. |

---

### Spacing Properties

| Property | Explanation |
|----------|-------------|
| `margin` | Sets space outside an element's border (shorthand for top/right/bottom/left). |
| `margin-bottom` | Sets spacing only below an element. |
| `margin-left` | Sets spacing to the left of an element (used for negative overlap on avatars). |
| `margin-top` | Sets spacing above an element. |
| `padding` | Sets space inside an element's border (between content and edge). |
| `padding-top / padding-bottom` | Sets vertical padding individually. |

---

### Typography Properties

| Property | Explanation |
|----------|-------------|
| `font-family` | Specifies the typeface(s); uses "Plus Jakarta Sans" with system fallbacks. |
| `font-size` | Sets the size of the text (in rem, px, or other units). |
| `font-weight` | Controls text boldness (e.g., `400` = normal, `700` = bold, `800` = extra-bold). |
| `line-height` | Sets the vertical space between lines of text for readability. |
| `letter-spacing` | Adjusts the space between individual characters. |
| `text-decoration` | Removes or adds underlines (e.g., `none` removes link underlines). |
| `text-align` | Horizontally aligns text (`center`, `left`, `right`). |
| `text-transform` | Converts text case (e.g., `uppercase` for label text). |
| `-webkit-background-clip: text` | Clips a gradient background so it only shows through the text (gradient text effect). |
| `-webkit-text-fill-color: transparent` | Makes the element's text fill transparent so the background gradient shows through. |

---

### Color & Background Properties

| Property | Explanation |
|----------|-------------|
| `color` | Sets the foreground (text) colour of an element. |
| `background` | Shorthand for setting the background (colour, gradient, or image). |
| `background-color` | Sets a solid background colour. |
| `background-image` | Sets gradient(s) or image(s) as the background. |
| `background-attachment: fixed` | Makes the background stay fixed relative to the viewport as the page scrolls. |
| `linear-gradient()` | Creates a smooth transition between colours along a line (used for gradient text and cards). |
| `radial-gradient()` | Creates a circular gradient used for subtle ambient glows on the page background. |
| `opacity` | Sets how transparent an element is (0 = invisible, 1 = fully visible). |

---

### Border & Shadow Properties

| Property | Explanation |
|----------|-------------|
| `border` | Shorthand for setting a border's width, style, and colour at once. |
| `border-bottom` | Applies a border only to the bottom edge of an element. |
| `border-top` | Applies a border only to the top edge of an element. |
| `border-color` | Changes the colour of an element's border. |
| `border-radius` | Rounds the corners of an element's border (50% = circle). |
| `border-left` | Applies a border only to the left edge (used for toast accent stripe). |
| `box-shadow` | Adds shadow effects around an element (used for glow highlights and card depth). |
| `outline: none` | Removes the default browser focus outline on input elements. |

---

### Animation & Transition Properties

| Property | Explanation |
|----------|-------------|
| `transition` | Specifies how changes to CSS properties animate smoothly over time. |
| `transform: translateY()` | Moves an element vertically (up/down) without affecting page layout. |
| `transform: translateX()` | Moves an element horizontally (left/right) without affecting page layout. |
| `transform: rotate()` | Rotates an element by a given degree. |
| `transform: scale()` | Scales an element up or down proportionally. |
| `calc()` | Performs CSS calculations (e.g., `calc(100% + 3rem)` for off-screen positioning). |

---

### Visual Effect Properties

| Property | Explanation |
|----------|-------------|
| `backdrop-filter: blur()` | Applies a blur effect to the content behind an element (glassmorphism effect). |
| `-webkit-backdrop-filter` | Vendor-prefixed version of `backdrop-filter` for Safari browser support. |
| `cursor: pointer` | Changes the mouse cursor to a hand icon on hover, indicating a clickable element. |
| `appearance: none` | Removes the default browser styling of a `<select>` element. |
| `pointer-events: none` | Disables mouse interactions on an element (used to hide inactive modals). |
| `pointer-events: auto` | Re-enables mouse interactions when a modal becomes active. |
| `object-fit: cover` | Scales an image to fill its container while maintaining aspect ratio (no distortion). |
| `content: ''` | Required for `::before`/`::after` pseudo-elements to inject a (possibly empty) content box. |

---

### CSS Custom Properties (Variables)

| Variable | Explanation |
|----------|-------------|
| `--bg-primary` | Darkest background colour used for the main page body. |
| `--bg-secondary` | Mid-dark background colour for cards and panels. |
| `--bg-tertiary` | Slightly lighter dark shade used for hover states and sub-panels. |
| `--accent-gold` | Primary brand colour — a vivid yellow-gold representing TukTuk/auto aesthetic. |
| `--accent-gold-hover` | Darker shade of gold used on button hover for feedback. |
| `--accent-gold-glow` | Semi-transparent gold used for glows, borders, and badge backgrounds. |
| `--text-primary` | Near-white colour for primary readable text. |
| `--text-secondary` | Muted grey-blue for secondary descriptive text. |
| `--text-muted` | Darker muted text for labels, hints, and timestamps. |
| `--border-color` | Subtle semi-transparent white for card and input borders. |
| `--glass-bg` | Semi-transparent dark colour creating the glassmorphism panel effect. |
| `--glass-border` | Very subtle white border for glass-effect panels. |
| `--color-success` | Green colour for "seats available" / active status badges. |
| `--color-success-bg` | Transparent green background for success badge chips. |
| `--color-warning` | Amber colour for warning states (defined but available for future use). |
| `--color-error` | Red colour for "full" status badges. |
| `--color-error-bg` | Transparent red background for error badge chips. |
| `--font-main` | Font stack starting with "Plus Jakarta Sans" for all text. |
| `--border-radius-sm` | Small corner rounding (8px) used for buttons and small elements. |
| `--border-radius-md` | Medium rounding (16px) used for cards and panels. |
| `--border-radius-lg` | Large rounding (24px) used for modals and the chat drawer. |
| `--transition-smooth` | Standardised smooth cubic-bezier animation used for all hover effects. |
| `--shadow-main` | Standard dark drop-shadow for elevated cards and panels. |
| `--shadow-glow` | Soft gold glow shadow used on primary buttons and the logo icon. |

---

*Report generated for Autoshare v1.0 — August 2026*
