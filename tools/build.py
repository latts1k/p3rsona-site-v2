"""Builds the P3RSONA site into static HTML.

Edit the copy in CARDS below, then run:  python3 tools/build.py
It writes index.html and card/<slug>/index.html at the repo root.
"""
import html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "P3RSONA"
ANCHOR = "Whatever hand you're dealt, play content."
IG = "https://instagram.com/latts1k"

CARDS = [
  dict(slug="amplified", group="live", rank="A", rank_name="THE ACE", img="a-p3rsona-amplified.svg",
       name="P3RSONA Amplified", home_one="Build your personal brand, hands-on with me.", home_more="3 slots left · View card", hot=True,
       one="Build your personal brand, hands-on with me.",
       status="Live. Three slots left for 2026", art_label="A · MY 1:1",
       for_="Founders growing their business through their personal brand, who want to work with me directly",
       next_="Apply, then a call with me",
       what="My 1:1. Private, hands-on personal brand work with me. We get clear on who you really are on camera, what makes you different and your proof, then build your content around your real persona, not a character.",
       get=["Your positioning and personal brand strategy", "A content plan built around you", "Hands-on feedback on what you're making", "Direct access to me while we work together"],
       how=["Apply below", "We get on a call", "If it's a fit, I send your onboarding", "We start building"],
       fit="You're the face of your business, you know content is the lever, and you want to learn it properly with me before you ever hire a team.",
       faq=[("How much does it cost?", "£2,500 to start (about $3,375): £2,000 for the 90 days with me, plus a £500 P3RSONA AI setup fee. Pay in 3 is available."),
            ("Is this a course?", "No. It's 1:1, just you and me, built around your business."),
            ("Do I need a team already?", "No. This is for founders doing it themselves first. If you outgrow it, In-House and Architect are the next cards.")],
       cta_line="Let's build your persona.", cta_sub="Takes a few minutes. If it's a fit, you'll book a call with me straight after.", cta_btn="Apply for my 1:1"),
  dict(slug="r3calibrate", group="live", rank="3", rank_name="THE THREE", img="3-r3calibrate.svg",
       name="R3CALIBRATE", home_one="A Day with Latts. Your whole content ecosystem, rebuilt in a day.", home_more="Book a call · View card",
       one="A Day with Latts. Your whole content ecosystem, rebuilt in a day.",
       status="Live", art_label="3 · A DAY WITH LATTS",
       for_="Anyone whose content feels like a mess and needs it rebuilt properly",
       next_="Apply, then a call with me",
       what="One day with me, in person or online. We take your whole content strategy, the backend and the ecosystem around it, and rebuild it in a day.",
       get=["Your core transformation, the one thing your content sells", "Your offer stack, laid out clearly", "A daily roadmap, so you know exactly what to do next"],
       how=["Apply below", "We get on a call", "If it's a fit, I send your onboarding and we book the day", "We rebuild it together"],
       fit="You're putting the work in but it's not landing, and you want it fixed fast by someone who's done every job in content.",
       faq=[("How much does it cost?", "£1,500 for the day (about $2,000)."),
            ("In person or online?", "Either. London in person, or online from anywhere."),
            ("What happens after the day?", "You leave with the roadmap. If you want me hands-on after that, my 1:1 or In-House are the next cards.")],
       cta_line="Recalibrate in a day.", cta_sub="Takes a few minutes. If it's a fit, you'll book a call with me straight after.", cta_btn="Apply for R3CALIBRATE"),
  dict(slug="next-gen", group="live", rank="J", rank_name="THE JACK", img="j-next-gen.svg",
       name="Next Gen", home_one="Become the creative director founders trust with their content.", home_more="For creatives · View card",
       one="Become the creative director founders trust with their content.",
       status="Live", art_label="J · FOR CREATIVES",
       for_="Photographers and videographers learning marketing, and marketers picking up a camera",
       next_="Apply, then a call with me",
       what="My mentorship for the next generation of personal brand creative directors. There are plenty of agencies, but not enough individuals who can understand a founder and build and execute around them. I'm training those people.",
       get=["Tools and education", "The creative director role, properly", "Production and editing", "Strategy", "Emotional intelligence and working with founders", "Team leadership, systems and ops", "Hiring talent"],
       how=["Apply below", "We get on a call", "If it's a fit, I send your onboarding", "We start"],
       fit="You're good at one thing, camera or marketing, and you want to become the person a founder trusts with all of it.",
       faq=[("How much does it cost?", "Pricing is being finalised. Apply and we'll talk it through on the call."),  # PRICE TBC: confirm before launch
            ("Do I need to be a videographer already?", "No. You can come from the camera side or the marketing side. Both roads lead to the same place."),
            ("What happens after?", "The best creatives I train can get placed into founders' teams through P3RSONA Architect.")],
       cta_line="Take the next seat.", cta_sub="Takes a few minutes. If it's a fit, you'll book a call with me straight after.", cta_btn="Apply for Next Gen"),
  dict(slug="in-house", group="live", rank="K", rank_name="THE KING", img="k-p3rsona-in-house.svg",
       name="P3RSONA In-House", home_one="My most hands-on card. I join your business and run your content.", home_more="1 slot left · View card", hot=True,
       one="My most hands-on card. I join your business as Head of Content and run your content, so you can run the business.",
       status="Live. One slot left for the year", art_label="K · 1 SLOT LEFT THIS YEAR",
       for_="Founder-led businesses ready to make content their main way of bringing in clients",
       next_="Apply, then a call with me",
       what="I come on board as your Head of Content. You stay the face, I build and run the engine around you: the strategy, the team, the shoots, the edit and the numbers. It's how I work with ABG Boys right now.",
       get=["Full research and positioning: your market, your buyers, your story", "A content system built around you, with a clear plan for every week", "Me directing and shooting, plus editors and support from my talent pool", "Review and approval flow, so nothing goes out that isn't you", "Ads layered on once the content is working"],
       how=["Apply below", "We get on a call", "If it's a fit, I send your onboarding", "We rebuild your ecosystem, then the content rolls out"],
       fit="You've got a real business, you're ready to be on camera, and you want someone who's done every job on the team running it with you.",
       faq=[("How much does it cost?", "From £1,750 a month (about $2,350), with a 3-month minimum. The final number is built around your marketing budget: a leaner budget means I take on more myself, a bigger one means more people around you."),
            ("How long does it run?", "Three months to start. We review at the end of every three-month block and decide what's next together."),
            ("Do I need to be on camera?", "Yes. You're the face of the content. I handle everything behind it, so all you have to do is show up and be yourself."),
            ("Do I need my own team?", "No. I build the team around you from my talent pool, and you own what we build."),
            ("What happens in the first month?", "Research and the rebuild: your market, your buyers, your story and the system behind the content. Then the content rolls out, and ads come in once it's working."),
            ("Why is there only one slot?", "I'm hands-on in every business I take on, so I keep the numbers small. When the slot's gone, it's gone for the year.")],
       cta_line="One slot left this year.", cta_sub="Takes about 3 minutes. If it's a fit, you'll book a call with me straight after.", cta_btn="Apply for the last slot"),
  dict(slug="ai", group="soon", rank="2", rank_name="THE TWO", img="2-p3rsona-ai.svg",
       name="P3RSONA AI", home_one="Your pocket creative director. Landing soon.", home_more="Join the waitlist",
       one="Your pocket creative director.",
       status="Landing soon", art_label="2 · LANDING SOON",
       for_="Founders who aren't ready for a creative director yet but want to run their content properly",
       next_="Join the waitlist",
       what="The systems I use to run content for my bigger clients, in your pocket: tools, AI agents and prompts that help you make the content, and teach you how to run a whole content ecosystem before you ever hire.",
       fit="You're doing the content yourself and want a creative director in your corner between the posts.",
       faq=[("How much will it cost?", "Pricing announced at launch. Join the waitlist to hear first."),
            ("Can I use it alongside my 1:1?", "Yes. The two are built to work together.")],
       cta_line="Be first when it lands.", cta_sub="I'll let you know the moment it's ready.", cta_btn="Join the waitlist"),
  dict(slug="masterminds", group="soon", rank="10", rank_name="THE TEN", img="10-masterminds.svg",
       name="Masterminds", home_one="One piece of the content roadmap, in one room. Maybe one day.", home_more="Held back", held=True,
       one="One piece of the content roadmap, in one room.",
       status="Landing 2027", art_label="10 · VIA NEXT GEN",
       for_="Founders and creatives who want one part of content done properly, in a room with others doing the same",
       next_="Join the waitlist",
       what="Ticketed workshops on the creator economy. Each one takes a different piece of the content roadmap and goes deep on it, in one room. Run through Next Gen.",
       fit="You learn best in a room, and you want one piece of the puzzle solved at a time.",
       faq=[("How much will tickets cost?", "Pricing announced at launch. Join the waitlist to hear first."),
            ("When's the first one?", "2027. The waitlist hears first.")],
       cta_line="Get first pick of the seats.", cta_sub="Waitlist gets the dates before anyone else.", cta_btn="Join the waitlist"),
  dict(slug="architect", group="soon", rank="Q", rank_name="THE QUEEN", img="q-p3rsona-architect.svg",
       name="P3RSONA Architect", home_one="A media team, built around you. You own it. Landing 2027.", home_more="Join the waitlist",
       one="A media team, built around you. You own it.",
       status="Landing 2027", art_label="Q · LANDING 2027",
       for_="Founders ready for a content team of their own",
       next_="Join the waitlist",
       what="I architect a media team around you, led by a creative director I've trained through Next Gen and filled from my talent pool. The team is yours, not mine.",
       fit="You've outgrown doing it yourself and want a team that actually understands you, built by someone who's done every job on it.",
       faq=[("How much will it cost?", "Pricing announced at launch. Join the waitlist to hear first."),
            ("Who's on the team?", "A creative director I've trained, plus editors, shooters and support from my talent pool, depending on what you need.")],
       cta_line="Get on the list for 2027.", cta_sub="Waitlist hears first when the first teams are built.", cta_btn="Join the waitlist"),
]
ROMAN = ["I", "II", "III", "IV", "V", "VI"]


def e(t):
    return html.escape(t, quote=True)


def brand(t):
    """Escape text and colour the 3 in P3RSONA and R3CALIBRATE burgundy."""
    return re.sub(r"(P|R)3(R|C)", r'\1<span class="b3">3</span>\2', e(t))


IG_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1" fill="currentColor" stroke="none"/></svg>'


def ig(label="@latts1k"):
    """The Instagram link: line icon plus tracked caps."""
    return f'<a class="ig" href="{IG}" rel="noopener" aria-label="{e(label)}">{IG_ICON}<span>{e(label)}</span></a>'


THEME_BTN = ('<button class="theme" type="button" aria-label="Switch to dark mode" data-theme-toggle>'
             '<svg class="moon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></svg>'
             '<svg class="sun" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/></svg>'
             '</button>')


def words(t):
    """Split a line into words so each one can rise in turn."""
    return " ".join(f'<span class="w" style="--i:{i}">{e(w)}</span>' for i, w in enumerate(t.split()))


def head(title, desc, depth):
    return f"""<!doctype html>
<html lang="en-GB" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://p3rsona.co/assets/og.png?v=joker">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The Joker card from the P3RSONA deck: play content.">
<meta name="twitter:image" content="https://p3rsona.co/assets/og.png?v=joker">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#121110" id="tc">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Oswald:wght@400;500&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/styles.css">
<script>try{{if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('anim')}}catch(e){{}}try{{if(localStorage.getItem('p3_theme')==='light'){{delete document.documentElement.dataset.theme;document.getElementById('tc').content='#EDE7DA'}}}}catch(e){{}}</script>
</head>
<body>
"""


FOOT = f"""<footer class="wrap foot">
<a class="mark" href="/" aria-label="P3RSONA home">P<span class="b3">3</span>RSONA</a>
<span>{e(ANCHOR)}</span>
{ig("@latts1k on Instagram")}
</footer>
<script src="/assets/forms.js"></script>
<script src="/assets/app.js"></script>
</body>
</html>
"""


def item(c, i):
    if c.get("held"):
        return f"""<div class="item place held" aria-label="{e(c['name'])}, held back for now">
<div class="card"><img src="/assets/cards/{c['img']}" width="240" height="336" alt="{e(c['name'])} playing card, {e(c['rank_name'].lower())}"></div>
<div class="meta"><div class="name">{brand(c['name'])}</div><div class="one">{e(c['home_one'])}</div><div class="small more soft">{e(c['home_more'])}</div></div>
</div>"""
    cls = "more hot" if c.get("hot") else ("more soft" if c["group"] == "soon" else "more")
    return f"""<a class="item place" href="/card/{c['slug']}">
<div class="card"><img src="/assets/cards/{c['img']}" width="240" height="336" alt="{e(c['name'])} playing card, {e(c['rank_name'].lower())}"></div>
<div class="meta"><div class="name">{brand(c['name'])}</div><div class="one">{e(c['home_one'])}</div><div class="small {cls}">{e(c['home_more'])}</div></div>
</a>"""


# Order the cards appear on the home page
HOME_ORDER = dict(live=["r3calibrate", "next-gen", "amplified", "in-house"],
                  soon=["ai", "architect", "masterminds"])


def home():
    by = {c["slug"]: c for c in CARDS}
    live = [by[s] for s in HOME_ORDER["live"]]
    soon = [by[s] for s in HOME_ORDER["soon"]]
    out = head(f"P3RSONA · {ANCHOR}", "The Jack of All Trades Content Deck. Seven ways to work with Lateef, a one-of-one operator in content: pick a card.", 0)
    out += f"""<header class="wrap bar intro"><a class="wordmark" href="/" aria-label="P3RSONA home">P<span class="b3">3</span>RSONA</a><div class="tools">{THEME_BTN}{ig()}</div></header>
<main>
<section class="hero">
<svg class="fade diamond" style="--d:900ms" width="16" height="22" viewBox="0 0 14 19" aria-hidden="true"><polygon points="7,0 14,9.5 7,19 0,9.5" fill="currentColor"></polygon></svg>
<p class="eyebrow fade" style="--d:1100ms">The Jack of All Trades Content Deck</p>
<h1 class="anchor">{words(ANCHOR)}</h1>
<p class="lede fade" style="--d:2300ms">Every card below is a way to work with me.</p>
<ol class="steps fade" style="--d:2600ms"><li><b>I</b>Pick a card</li><li><b>II</b>Unlock the details</li><li><b>III</b>Apply, book a call or join the waitlist</li></ol>
</section>
<section class="wrap section" aria-labelledby="inplay">
<div class="sechead"><h2 class="label" id="inplay">In play</h2><p>Four cards on the table</p></div>
<div class="deck">{''.join(item(c, i) for i, c in enumerate(live))}</div>
</section>
<section class="wrap section" aria-labelledby="soon">
<div class="sechead"><h2 class="label" id="soon">Coming soon</h2><p>Two on the way, one held back</p></div>
<div class="deck">{''.join(item(c, i) for i, c in enumerate(soon))}</div>
</section>
<section class="wrap section" aria-labelledby="club">
<div class="sechead"><h2 class="label" id="club">Off the menu</h2><p>Handed out, never picked</p></div>
<div class="club place">
<div class="card"><img src="/assets/cards/club-p3rsona-invite.svg" width="240" height="336" alt="Club P3RSONA invitation card, private members club, by invitation only"></div>
<div class="text"><h3>CLUB P<span class="b3">3</span>RSONA</h3>
<p>A private members club for founders and creatives. You can't pick this card. If we work together and it's the right fit, it gets handed to you.</p>
<p class="small" style="color:var(--accent)">By invitation only · 2027</p></div>
</div>
</section>
<section class="wrap section">
<div class="unsure"><p class="q">Not sure what card you are?</p><p>DM me on Instagram and tell me where you're at. <a href="{IG}" rel="noopener">@latts1k</a></p></div>
</section>
</main>
"""
    return out + FOOT


def sections(c):
    s = f"""<div><h2>What it is</h2><p>{brand(c['what'])}</p></div>"""
    if c.get("get"):
        s += "<div><h2>What you get</h2><ul>" + "".join(f"<li>{brand(x)}</li>" for x in c["get"]) + "</ul></div>"
    if c.get("how"):
        s += "<div><h2>How it works</h2><ol>" + "".join(f"<li><b>{ROMAN[i]}</b>{e(x)}</li>" for i, x in enumerate(c["how"])) + "</ol></div>"
    return s


def page(c):
    live = c["group"] == "live"
    action = "apply" if live else "waitlist"
    label = ("In play · " if live else "Coming soon · ") + c["rank_name"].title()
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{brand(a)}</p></details>" for q, a in c["faq"])
    body = sections(c).replace("<h2>What it is</h2>", "<h2>What it is</h2>" if live else "<h2>What it will be</h2>")
    body += f"""<div><h2>For you if</h2><p>{brand(c['fit'])}</p></div>
<div><h2>Questions</h2><div class="faq">{faq}</div></div>
<div class="cta"><div><p class="line">{e(c['cta_line'])}</p><p class="sub">{e(c['cta_sub'])}</p></div>
<a class="btn light" href="{IG}" rel="noopener" data-action="{action}" data-card="{c['slug']}">{e(c['cta_btn'])}</a></div>"""
    if live:
        ghost = f"""<div class="ghost" aria-hidden="true"><p class="h">WHAT IT IS</p><p>{e(c['what'])}</p><p class="h">WHAT YOU GET</p><p>{e('. '.join(c['get']))}.</p></div>"""
        wall = f"""<section class="wall" data-wall="{c['slug']}" aria-labelledby="wall-h">
{ghost}
<div class="front">
<h2 id="wall-h">Turn the card over</h2>
<p>Leave your details to see the full card: what it is, what you get and how it works.</p>
<div class="tally-slot"></div>
<form novalidate>
<div class="fields">
<div class="field"><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="f-ig">Instagram</label><input id="f-ig" name="instagram" type="text" placeholder="@"></div>
</div>
<p class="err" role="alert"></p>
<button class="btn dark" type="submit" style="align-self:flex-start">Unlock the card</button>
</form>
<p class="note">No spam. I'll only reach out about this card.</p>
</div>
</section>
<section class="details" data-details hidden>{body}</section>"""
    else:
        wall = f"""<section class="details">{body}</section>"""
    out = head(f"{c['name']} · P3RSONA", f"{c['one']} {c['status']}.", 2)
    out += f"""<header class="wrap bar"><a href="/">← The deck</a><a class="mark" href="/" aria-label="P3RSONA home">P<span class="b3">3</span>RSONA</a><div class="tools">{THEME_BTN}{ig()}</div></header>
<main class="wrap page">
<div class="art rise"><div class="card"><img src="/assets/cards/{c['img']}" width="340" height="476" alt="{e(c['name'])} playing card, {e(c['rank_name'].lower())}"></div><p class="small">{e(c['art_label'])}</p></div>
<div class="content rise d1">
<p class="eyebrow">{e(label)}</p>
<h1>{brand(c['name'])}</h1>
<p class="one">{e(c['one'])}</p>
<dl class="facts"><dt>FOR</dt><dd>{e(c['for_'])}</dd><dt>STATUS</dt><dd>{e(c['status'])}</dd><dt>NEXT</dt><dd>{e(c['next_'])}</dd></dl>
{wall}
</div>
</main>
"""
    return out + FOOT


def main():
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(home())
    for c in CARDS:
        if c.get("held"):
            continue  # no page while the card is held back
        d = os.path.join(ROOT, "card", c["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w") as f:
            f.write(page(c))
    print("built", 1 + sum(1 for c in CARDS if not c.get("held")), "pages")


if __name__ == "__main__":
    main()
