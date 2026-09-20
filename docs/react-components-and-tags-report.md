# Autoshare — React Components & HTML/JSX Tags Reference

> Comprehensive reference guide providing one-line definitions for every React component, Lucide icon component, HTML/JSX tag, and React hook used across the **Autoshare** frontend application.

---

## ⚛️ 1. React Application Components

| Component | File Path | One-Line Definition |
|---|---|---|
| `<App />` | [`src/App.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/App.jsx) | Root orchestrator component managing global application state, search filters, ride bookings, chat channels, and toast notifications. |
| `<Navbar />` | [`src/components/Navbar.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/Navbar.jsx) | Sticky top navigation bar providing branding, on-page anchor navigation links, and the primary "Post a Ride" modal trigger. |
| `<HeroSearch />` | [`src/components/HeroSearch.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/HeroSearch.jsx) | Hero banner component combining promotional campus copy with a multi-criteria search bar (Pickup, Destination, Departure Time). |
| `<RidesFeed />` | [`src/components/RidesFeed.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/RidesFeed.jsx) | Live feed container rendering active ride cards, real-time offer count badge, and empty state when no rides match filters. |
| `<RideCard />` | [`src/components/RideCard.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/RideCard.jsx) | Individual ride card displaying student creator details, route path, departure time, live per-student cost split, capacity dots, co-traveler avatars, and join/chat actions. |
| `<SidebarStats />` | [`src/components/SidebarStats.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/SidebarStats.jsx) | Sidebar widget presenting live campus statistics including active daily groups, average student fare savings, and popular gates. |
| `<HotspotClusters />` | [`src/components/HotspotClusters.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/HotspotClusters.jsx) | Interactive sidebar module showcasing high-density student hostel/PG destinations with one-click quick-filtering. |
| `<PostRideModal />` | [`src/components/PostRideModal.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/PostRideModal.jsx) | Accessible dialog popup containing the ride creation form with interactive seat selector buttons and real-time per-person split calculator. |
| `<ChatDrawer />` | [`src/components/ChatDrawer.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/ChatDrawer.jsx) | Slide-in coordination chat drawer providing instant messaging, simulated auto-replies from ride hosts, and auto-scrolling message streams. |
| `<Toast />` | [`src/components/Toast.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/Toast.jsx) | Animated feedback pill notifying users when they join rides, publish offers, or encounter validation alerts. |
| `<Footer />` | [`src/components/Footer.jsx`](file:///c:/Users/Daksh%20Gehlot/OneDrive/Desktop/Autoshare/src/components/Footer.jsx) | Bottom footer component displaying copyright notices and campus safe-travel guidelines. |

---

## 🎨 2. Lucide Icon Components

| Icon Component | Package | One-Line Definition |
|---|---|---|
| `<PlusCircle />` | `lucide-react` | Circular plus icon representing the action to create or post a new ride offer. |
| `<Sparkles />` | `lucide-react` | Star sparkle icon highlighting the campus ride-sharing banner badge. |
| `<MapPin />` | `lucide-react` | Geographic pin icon representing pickup spots and destination clusters. |
| `<Navigation />` | `lucide-react` | Compass navigation arrow icon indicating destination input fields. |
| `<Clock />` | `lucide-react` | Clock face icon indicating departure schedules and departure time filters. |
| `<Search />` | `lucide-react` | Magnifying glass icon for executing search and filter operations on rides. |
| `<ArrowRight />` | `lucide-react` | Directional arrow icon showing travel route progression from pickup to drop-off. |
| `<UserPlus />` | `lucide-react` | Person icon with a plus sign for joining an available ride share. |
| `<MessageSquare />` | `lucide-react` | Chat bubble icon for opening ride coordination communication drawers. |
| `<CheckCircle />` | `lucide-react` | Checkmark circle icon indicating confirmed ride participation or successful actions. |
| `<RefreshCw />` | `lucide-react` | Rotating arrows icon representing the action to reset active search filters. |
| `<Info />` | `lucide-react` | Informational 'i' icon displayed when no matching rides are found in search. |
| `<Activity />` | `lucide-react` | Pulse waveform icon denoting live activity and dynamic statistics. |
| `<X />` | `lucide-react` | Close cross icon for dismissing modals and chat panels. |
| `<Send />` | `lucide-react` | Paper plane arrow icon for submitting new rides or dispatching chat messages. |
| `<AlertCircle />` | `lucide-react` | Warning exclamation icon used for error alerts in toast notifications. |

---

## 📄 3. HTML & JSX Tags

| Tag / Element | Semantic Category | One-Line Definition |
|---|---|---|
| `<!DOCTYPE html>` | Document Declaration | Informs the web browser that the document follows the HTML5 standard specification. |
| `<html lang="en">` | Root Element | Root container that wraps the entire document tree; `lang="en"` defines English as the primary language. |
| `<head>` | Document Metadata | Container for non-rendered page configuration such as character set, title, viewport rules, and font links. |
| `<meta charset="UTF-8">` | Encoding Metadata | Declares UTF-8 character encoding to ensure proper rendering of international text and symbols. |
| `<meta name="viewport">` | Responsive Metadata | Configures viewport width and scaling for optimal display across mobile, tablet, and desktop screens. |
| `<meta name="description">` | SEO Metadata | Provides a concise textual description of the app used by search engines for index previews. |
| `<title>` | Document Title | Specifies the web page title displayed on browser tabs and bookmark bars. |
| `<link>` | External Resource | Connects external assets like Google Fonts stylesheets, preconnect domains, and favicons to the page. |
| `<body>` | Visible Document Body | Contains all visible elements and user interface markup rendered in the browser viewport. |
| `<header>` | Semantic Header | Landmark container representing top-level brand identification and main navigation. |
| `<nav>` | Semantic Navigation | Landmark element grouping primary navigational links and high-priority action buttons. |
| `<main>` | Semantic Main | Landmark container enclosing the central, unique functional content of the web application. |
| `<section>` | Semantic Section | Generic thematic section grouping related content units such as hero search and live dashboard. |
| `<aside>` | Semantic Aside | Landmark element representing auxiliary sidebar content including live stats and destination cards. |
| `<footer>` | Semantic Footer | Landmark container displaying copyright information and campus student community notices. |
| `<h1>` | Heading 1 | Primary top-level page heading communicating the core mission of the Autoshare platform. |
| `<h2>` | Heading 2 | Second-tier heading introducing major functional sections like the active rides feed. |
| `<h3>` | Heading 3 | Third-tier heading used for sidebar card titles, modal dialog headers, and statistics banners. |
| `<h4>` | Heading 4 | Fourth-tier heading used for student host names on ride cards and chat panel participant headers. |
| `<h5>` | Heading 5 | Fifth-tier heading used for individual destination cluster names in hotspot widgets. |
| `<p>` | Paragraph | Standard block element containing explanatory text passages, subtitles, and descriptions. |
| `<span>` | Inline Container | Generic inline element used for badge labels, status indicators, and styled sub-strings. |
| `<div>` | Block Container | Generic block-level division used for structuring layouts, flex containers, grids, and card wrappers. |
| `<a>` | Hyperlink Anchor | Interactive anchor element facilitating navigation to on-page anchors or external web URLs. |
| `<button>` | Action Button | Interactive clickable button triggering state changes, modal openings, join requests, or form submissions. |
| `<form>` | Input Form | Container capturing user inputs and dispatching submit events for search and ride creation. |
| `<label>` | Accessible Label | Associates accessible text descriptions with form input controls to improve screen-reader usability. |
| `<input>` | Form Input | Interactive data entry field accepting textual, numeric, or time data (`text`, `number`, `time`). |
| `<select>` | Dropdown Select | Dropdown control allowing users to pick from predefined lists of campus gates and departure windows. |
| `<option>` | Dropdown Option | Defines an individual selectable item inside a `<select>` dropdown menu. |
| `<small>` | Small Text | Renders supplementary helper notes, pricing guidelines, or fine print below input controls. |
| `<script>` | JavaScript Script | References and executes JavaScript code modules such as the Vite React application entry point. |

---

## 🪝 4. React Hooks Used

| Hook | Source | One-Line Definition |
|---|---|---|
| `useState` | `react` | Manages local reactive component state for rides data, search inputs, modal visibility, and chat messages. |
| `useMemo` | `react` | Memoizes filtered ride calculations so searching only re-evaluates when rides or filter criteria change. |
| `useEffect` | `react` | Handles side effects like listening for keyboard `Escape` keys to close modals and auto-scrolling chat history. |
| `useRef` | `react` | Holds a direct mutable reference to the chat message container DOM node for smooth programmatic scrolling. |

---

*Documentation generated for Autoshare React Frontend.*
