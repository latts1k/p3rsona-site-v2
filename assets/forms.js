// Paste your Tally form IDs here once the forms are built.
// A form's ID is the last part of its link: tally.so/r/ABC123 -> "ABC123".
// Leave a value empty and the site falls back (built-in unlock fields, or Instagram for buttons).
window.P3_FORMS = {
  unlockFormId: "",     // one form for the "Turn the card over" wall on the four live cards
  waitlistFormId: "",   // one form for every waitlist (P3RSONA AI, Masterminds, Architect)
  applyFormId: {        // one form per live card (each redirects to its own Calendly call type)
    "amplified": "",
    "r3calibrate": "",
    "next-gen": "",
    "in-house": ""
  },
  fallbackUrl: "https://instagram.com/latts1k"
};
