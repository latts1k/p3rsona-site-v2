// Lay the cards on the table as each section scrolls into view.
(function () {
  var root = document.documentElement;
  if (!root.classList.contains("anim")) return;
  function ready(fn) { if (document.readyState !== "loading") fn(); else document.addEventListener("DOMContentLoaded", fn); }
  ready(function () {
    var items = [].slice.call(document.querySelectorAll(".place"));
    function show(el, d) { el.style.setProperty("--d", d + "ms"); el.classList.add("in"); }
    if (!("IntersectionObserver" in window)) { items.forEach(function (el) { show(el, 0); }); return; }
    var io = new IntersectionObserver(function (entries) {
      // Cards arriving together are laid one after another; anything visible at load waits for the hero.
      var base = Math.max(0, 2200 - performance.now());
      entries.filter(function (en) { return en.isIntersecting; })
        .sort(function (a, b) { return items.indexOf(a.target) - items.indexOf(b.target); })
        .forEach(function (en, k) { show(en.target, base + k * 240); io.unobserve(en.target); });
    }, { threshold: 0.1, rootMargin: "0px 0px -6% 0px" });
    items.forEach(function (el) { io.observe(el); });
    // Safety net: never leave a card hidden.
    setTimeout(function () { items.forEach(function (el) { if (!el.classList.contains("in")) show(el, 0); }); }, 12000);
  });
})();

(function () {
  var F = window.P3_FORMS || {};
  var KEYS = ["utm_source", "utm_medium", "utm_campaign", "ref"];

  function store(kind) { try { return window[kind]; } catch (e) { return null; } }
  function get(kind, k) { try { var s = store(kind); return s ? s.getItem(k) : null; } catch (e) { return null; } }
  function set(kind, k, v) { try { var s = store(kind); if (s) s.setItem(k, v); } catch (e) {} }

  // Keep where the visitor came from (e.g. ?utm_source=youtube&utm_campaign=video2) for this visit.
  var qs = new URLSearchParams(location.search);
  KEYS.forEach(function (k) { if (qs.get(k)) set("sessionStorage", "p3_" + k, qs.get(k)); });

  var CARD_NAMES = { "amplified": "Amplified", "r3calibrate": "R3CALIBRATE", "next-gen": "Next Gen", "in-house": "In-House", "ai": "P3RSONA AI", "masterminds": "Masterminds", "architect": "Architect" };
  // Hidden fields sent into every Tally form: card, type, utm (one line) plus the raw UTM values.
  function hidden(card, type) {
    var h = { card: CARD_NAMES[card] || card, type: type };
    var parts = [];
    KEYS.forEach(function (k) { var v = get("sessionStorage", "p3_" + k); if (v) { h[k] = v; parts.push(k.replace("utm_", "") + "=" + v); } });
    h.utm = parts.join(" / ");
    return h;
  }

  var tallyLoading = null;
  function loadTally() {
    if (window.Tally) return Promise.resolve();
    if (tallyLoading) return tallyLoading;
    tallyLoading = new Promise(function (resolve) {
      var s = document.createElement("script");
      s.src = "https://tally.so/widgets/embed.js";
      s.async = true;
      s.onload = function () { resolve(); };
      s.onerror = function () { resolve(); };
      document.head.appendChild(s);
    });
    return tallyLoading;
  }

  // Apply and waitlist buttons
  document.querySelectorAll("[data-action]").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      var card = btn.getAttribute("data-card");
      var action = btn.getAttribute("data-action");
      var id = action === "apply" ? (F.applyFormId || {})[card] : F.waitlistFormId;
      if (!id) return; // no form yet: the link's own href (Instagram) is used
      e.preventDefault();
      loadTally().then(function () {
        if (window.Tally && window.Tally.openPopup) {
          window.Tally.openPopup(id, { layout: "modal", width: 640, overlay: true, hiddenFields: hidden(card, action === "apply" ? "Application" : "Waitlist") });
        } else {
          var p = new URLSearchParams(hidden(card, action === "apply" ? "Application" : "Waitlist"));
          location.href = "https://tally.so/r/" + id + "?" + p.toString();
        }
      });
    });
  });

  // Unlock wall on live card pages
  var wall = document.querySelector("[data-wall]");
  if (!wall) return;
  var card = wall.getAttribute("data-wall");
  var details = document.querySelector("[data-details]");
  var key = "p3_unlocked_" + card;

  function unlock(focus) {
    set("localStorage", key, "1");
    wall.hidden = true;
    details.hidden = false;
    if (focus) {
      var h = details.querySelector("h2");
      if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
      details.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
    }
  }

  if (get("localStorage", key) === "1") { unlock(false); return; }

  if (F.unlockFormId) {
    var slot = wall.querySelector(".tally-slot");
    var fallback = wall.querySelector("form");
    if (fallback) fallback.hidden = true;
    var p = new URLSearchParams(hidden(card, "Unlock"));
    var iframe = document.createElement("iframe");
    iframe.setAttribute("data-tally-src", "https://tally.so/embed/" + F.unlockFormId + "?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1&" + p.toString());
    iframe.setAttribute("loading", "lazy");
    iframe.setAttribute("title", "Unlock the card");
    iframe.height = "320";
    slot.appendChild(iframe);
    loadTally().then(function () {
      if (window.Tally && window.Tally.loadEmbeds) window.Tally.loadEmbeds();
      else iframe.src = iframe.getAttribute("data-tally-src");
    });
    window.addEventListener("message", function (e) {
      if (typeof e.data === "string" && e.data.indexOf("Tally.FormSubmitted") !== -1) unlock(true);
    });
    return;
  }

  // Temporary built-in fields until the Tally unlock form exists
  var form = wall.querySelector("form");
  var err = wall.querySelector(".err");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = form.elements.name.value.trim();
    var email = form.elements.email.value.trim();
    if (!name || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      err.textContent = "Add your name and a valid email to turn the card over.";
      return;
    }
    err.textContent = "";
    unlock(true);
  });
})();
