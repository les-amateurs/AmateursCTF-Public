<?php
$nonce = base64_encode(random_bytes(16));
header("Content-Security-Policy: default-src 'none'; script-src 'nonce-$nonce'; style-src 'nonce-$nonce'; img-src 'self'; font-src https://fonts.googleapis.com https://fonts.gstatic.com; frame-ancestors 'none'; base-uri 'none'; form-action 'self';");

// determine Trailblazer name from query
$username = 'Trailblazer';
if (!empty($_GET['username'])) {
    $tmp = trim($_GET['username']);
    if ($tmp !== '') {
        $username = mb_substr($tmp, 0, 128, 'UTF-8');
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Ripples of Past Reverie · Cyrene</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet" nonce="<?php echo $nonce; ?>" />
  
  <style nonce="<?php echo $nonce; ?>">
   :root {
    --bg-dark: #050318;
    --accent-pink: #f8a7ff;
    --accent-blue: #88e4ff;
    --accent-violet: #c7a4ff;
    --accent-soft: #fdf1ff;
    --glass: rgba(16, 10, 35, 0.72);
    --border-glow: rgba(255, 255, 255, 0.42);
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  /* make sure the root is never white + smooth scroll for anchors */
  html {
    height: 100%;
    background: #050318;
    scroll-behavior: smooth;
  }

  body {
    height: 100vh;                 /* lock viewport height */
    font-family: "Poppins", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    background: radial-gradient(circle at top, #4131a8 0, #050318 45%, #050318 100%);
    color: #fdf9ff;
    overflow: hidden;              /* page itself doesn't scroll */
  }

  .page {
    max-width: 1200px;
    margin: 0 auto;
    padding: 32px 18px 64px;
    height: 100%;                  /* take full viewport height */
    overflow-y: auto;              /* scroll only inside .page */
    overflow-x: hidden;
    scroll-behavior: smooth;       /* smooth scrolling inside container */
  }

  /* Floating petals / particles */
  .petal {
    position: fixed;
    width: 18px;
    height: 32px;
    border-radius: 999px 999px 999px 999px;
    background: linear-gradient(145deg, rgba(248, 167, 255, 0.9), rgba(136, 228, 255, 0.15));
    filter: blur(0.3px);
    opacity: 0.4;
    animation: floatUp 26s linear infinite;
    pointer-events: none;
    mix-blend-mode: screen;
    z-index: -1;
  }
  .petal:nth-child(2) { left: 8%; animation-duration: 21s; animation-delay: -4s; transform: rotate(-16deg); }
  .petal:nth-child(3) { left: 22%; animation-duration: 29s; animation-delay: -11s; transform: rotate(11deg); }
  .petal:nth-child(4) { left: 47%; animation-duration: 24s; animation-delay: -7s; transform: rotate(-8deg); }
  .petal:nth-child(5) { left: 68%; animation-duration: 33s; animation-delay: -18s; transform: rotate(17deg); }
  .petal:nth-child(6) { left: 86%; animation-duration: 28s; animation-delay: -14s; transform: rotate(-12deg); }

  @keyframes floatUp {
    0%   { top: 110vh; transform: translateX(0) scale(1) rotate(0deg); opacity: 0; }
    15%  { opacity: 0.45; }
    50%  { transform: translateX(-30px) scale(1.05) rotate(12deg); }
    100% { top: -20vh; transform: translateX(36px) scale(0.9) rotate(-18deg); opacity: 0; }
  }

  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    margin-bottom: 32px;
  }

  .logo-cluster {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 0.9rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.8;
  }

  .logo-pill {
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.28);
    background: radial-gradient(circle at top left, rgba(248, 167, 255, 0.35), rgba(8, 2, 30, 0.9));
    font-size: 0.75rem;
  }

  .nav {
    display: flex;
    gap: 20px;
    font-size: 0.9rem;
    opacity: 0.8;
  }

  .nav a {
    text-decoration: none;
    color: inherit;
    position: relative;
    padding-bottom: 4px;
  }

  .nav a::after {
    content: "";
    position: absolute;
    left: 0;
    right: 100%;
    bottom: 0;
    height: 2px;
    border-radius: 999px;
    background: linear-gradient(90deg, var(--accent-pink), var(--accent-blue));
    transition: right 0.3s ease;
  }
  .nav a:hover::after { right: 0; }

  /* HERO */
  .hero {
    display: grid;
    grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
    gap: 32px;
    align-items: center;
    margin-bottom: 52px;
  }
  .mta{
    margin-top:6px;
  }
  .hero-copy {
    position: relative;
    padding: 16px 0;
  }

  .eyebrow {
    font-size: 0.85rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    opacity: 0.75;
    margin-bottom: 8px;
  }

  .title-main {
    font-family: "Playfair Display", serif;
    font-weight: 700;
    font-size: clamp(2.4rem, 4vw, 3.2rem);
    line-height: 1.06;
    color: var(--accent-soft);
    text-shadow: 0 0 18px rgba(199, 164, 255, 0.55);
  }
  .title-main span:nth-child(2) {
    display: block;
    font-size: 0.7em;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-top: 8px;
    color: rgba(255, 255, 255, 0.8);
  }

  .subtitle {
    margin-top: 14px;
    font-size: 0.95rem;
    max-width: 34rem;
    color: rgba(240, 229, 255, 0.86);
  }

  .cyrene-name {
    margin-top: 18px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.25);
    background: linear-gradient(120deg, rgba(248, 167, 255, 0.14), rgba(136, 228, 255, 0.09));
    font-size: 0.9rem;
  }

  .cyrene-dot {
    width: 8px;
    height: 8px;
    border-radius: 999px;
    background: radial-gradient(circle, var(--accent-pink), var(--accent-violet));
    box-shadow: 0 0 10px rgba(248, 167, 255, 0.9);
  }

  .hero-actions {
    margin-top: 24px;
    display: flex;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
  }

  .btn-primary,
  .btn-ghost {
    position: relative;
    border-radius: 999px;
    padding: 10px 20px;
    font-size: 0.9rem;
    border: 1px solid transparent;
    cursor: pointer;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    overflow: hidden;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease, background 0.18s ease;
  }

  .btn-primary {
    background: radial-gradient(circle at top left, var(--accent-pink), var(--accent-blue));
    border-color: rgba(255, 255, 255, 0.4);
    box-shadow: 0 0 24px rgba(199, 164, 255, 0.75);
    animation: buttonGlow 3.2s ease-in-out infinite;
  }

  /* ripple sheen on primary button */
  .btn-primary::before {
    content: "";
    position: absolute;
    top: 0;
    left: -120%;
    width: 70%;
    height: 100%;
    background: linear-gradient(
      110deg,
      transparent,
      rgba(255, 255, 255, 0.4),
      transparent
    );
    transform: skewX(-18deg);
    opacity: 0;
    animation: buttonSheen 4.5s ease-in-out infinite;
  }

  .btn-primary:hover {
    transform: translateY(-1px) scale(1.02);
    box-shadow: 0 0 32px rgba(199, 164, 255, 0.95);
  }

  .btn-primary.is-playing {
    transform: scale(0.96);
    box-shadow: 0 0 40px rgba(199, 164, 255, 1);
  }

  .btn-ghost {
    background: rgba(12, 7, 40, 0.75);
    border-color: rgba(255, 255, 255, 0.2);
    color: rgba(250, 244, 255, 0.9);
  }
  .btn-ghost:hover {
    transform: translateY(-1px);
    background: rgba(22, 14, 70, 0.9);
    border-color: rgba(255, 255, 255, 0.32);
  }

  .btn-small {
    padding: 8px 16px;
    font-size: 0.85rem;
  }

  .pill-text {
    font-size: 0.75rem;
    opacity: 0.8;
  }
  .pill-text--spaced {
    margin-bottom: 8px;
  }

  /* Hero art card */
  .hero-art {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .hero-orbit {
    position: absolute;
    width: 360px;
    height: 360px;
    border-radius: 999px;
    background:
      radial-gradient(circle at 20% 0, rgba(248, 167, 255, 0.9), transparent 70%),
      radial-gradient(circle at 80% 100%, rgba(136, 228, 255, 0.85), transparent 70%);
    filter: blur(26px);
    opacity: 0.9;
    z-index: -1;
    animation: orbitPulse 14s ease-in-out infinite alternate;
  }

  .hero-card {
    position: relative;
    border-radius: 28px;
    padding: 10px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.12), rgba(16, 9, 42, 0.9));
    box-shadow:
      0 0 0 1px rgba(255, 255, 255, 0.15),
      0 24px 60px rgba(0, 0, 0, 0.8);
    overflow: hidden;
    max-width: 420px;
    transform-origin: center;
    animation: floatCard 7s ease-in-out infinite;
  }

  @keyframes floatCard {
    0%,100% { transform: translateY(0) rotate(-0.7deg); }
    50%     { transform: translateY(-6px) rotate(0.7deg); }
  }

  /* shimmering highlight around the card */
  .hero-card::before {
    content: "";
    position: absolute;
    inset: -40%;
    background:
      radial-gradient(circle at 0 0, rgba(248, 167, 255, 0.35), transparent 55%),
      radial-gradient(circle at 100% 100%, rgba(136, 228, 255, 0.3), transparent 55%);
    opacity: 0;
    animation: cardHalo 6s ease-in-out infinite;
    mix-blend-mode: screen;
    pointer-events: none;
  }

  .hero-card img {
    display: block;
    width: 100%;
    border-radius: 24px;
  }

  .hero-card-footer {
    margin-top: 10px;
    padding: 8px 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.75rem;
    color: rgba(243, 232, 255, 0.88);
  }

  .hero-card-footer span {
    opacity: 0.85;
  }

  .badge-stars {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 10px;
    border-radius: 999px;
    background: rgba(5, 3, 24, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.22);
  }
  .badge-meta {
    opacity: 0.7;
  }

  /* Content grid */
  .content-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr);
    gap: 24px;
    margin-bottom: 40px;
  }

  .panel {
    border-radius: 24px;
    padding: 18px 18px 20px;
    background: linear-gradient(140deg, rgba(11, 6, 40, 0.9), rgba(101, 70, 184, 0.32));
    border: 1px solid rgba(255, 255, 255, 0.16);
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.7);
    position: relative;
    overflow: hidden;
    margin-bottom: 24px;
  }

  .panel::before {
    content: "";
    position: absolute;
    inset: -40%;
    background:
      radial-gradient(circle at 10% 10%, rgba(248, 167, 255, 0.14), transparent 55%),
      radial-gradient(circle at 90% 0, rgba(136, 228, 255, 0.18), transparent 55%);
    opacity: 0.8;
    mix-blend-mode: screen;
    pointer-events: none;
  }

  .panel-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
    position: relative;
    z-index: 1;
  }

  .panel-title {
    font-size: 0.95rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.85;
  }

  .panel-tag {
    font-size: 0.75rem;
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.22);
    background: rgba(13, 7, 48, 0.9);
  }

  .panel-body {
    position: relative;
    z-index: 1;
    font-size: 0.9rem;
    opacity: 0.93;
  }

  .panel-body strong {
    color: var(--accent-soft);
    font-weight: 500;
  }

  .traits {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 14px;
  }
  .traits--compact {
    margin-top: 12px;
  }

  .chip {
    font-size: 0.78rem;
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.26);
    background: rgba(5, 3, 24, 0.9);
    backdrop-filter: blur(12px);
  }

  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
    gap: 10px;
    margin-top: 14px;
  }

  .stat-card {
    border-radius: 16px;
    padding: 10px 12px;
    background: rgba(7, 4, 26, 0.92);
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 0.8rem;
  }

  .stat-label {
    text-transform: uppercase;
    letter-spacing: 0.12em;
    opacity: 0.7;
    margin-bottom: 4px;
    font-size: 0.72rem;
  }

  .stat-value {
    font-weight: 500;
    color: var(--accent-soft);
  }
  .stat-description {
    opacity: 0.78;
    margin-top: 4px;
  }

  .panel-art {
    margin-top: 10px;
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.22);
  }
  .panel-art--spaced {
    margin-top: 16px;
  }

  .panel-art img {
    display: block;
    width: 100%;
  }

  /* Tracklist */
  .tracklist {
    margin-bottom: 14px;
  }

  .track {
    display: grid;
    grid-template-columns: 18px minmax(0, 1fr) auto;
    gap: 10px;
    align-items: center;
    padding: 6px 0;
    border-bottom: 1px dashed rgba(255, 255, 255, 0.12);
    font-size: 0.86rem;
  }

  .track:last-child {
    border-bottom: none;
  }

  .track-index {
    font-size: 0.72rem;
    opacity: 0.7;
  }

  .track-title {
    font-weight: 500;
  }

  .track-meta {
    font-size: 0.75rem;
    opacity: 0.75;
  }

  footer {
    margin-top: 32px;
    padding-top: 18px;
    border-top: 1px solid rgba(255, 255, 255, 0.14);
    font-size: 0.78rem;
    display: flex;
    justify-content: space-between;
    gap: 10px;
    flex-wrap: wrap;
    opacity: 0.8;
  }

  /* Art generator section */
  .art-generator {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  .art-form {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
  }

  .art-form input[type="text"] {
    flex: 1 1 180px;
    min-width: 0;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.24);
    background: rgba(5, 3, 24, 0.9);
    color: #fdf9ff;
    padding: 8px 14px;
    font-size: 0.9rem;
    outline: none;
  }

  .art-form input[type="text"]::placeholder {
    color: rgba(255, 255, 255, 0.5);
  }

  /* Reveal-on-scroll animation */
  .js-reveal {
    opacity: 0;
    transform: translateY(22px);
    transition: opacity 0.9s ease-out, transform 0.9s ease-out;
  }
  .js-reveal.in-view {
    opacity: 1;
    transform: translateY(0);
  }
  .js-reveal[data-delay="1"] { transition-delay: 0.15s; }
  .js-reveal[data-delay="2"] { transition-delay: 0.3s; }
  .js-reveal[data-delay="3"] { transition-delay: 0.45s; }

  /* Keyframes for extra motion */
  @keyframes orbitPulse {
    0%   { transform: scale(0.98) translateY(4px); opacity: 0.85; }
    50%  { transform: scale(1.02) translateY(-2px); opacity: 1; }
    100% { transform: scale(1.05) translateY(0); opacity: 0.9; }
  }

  @keyframes buttonGlow {
    0%, 100% { box-shadow: 0 0 24px rgba(199, 164, 255, 0.75); }
    50%      { box-shadow: 0 0 36px rgba(199, 164, 255, 1); }
  }

  @keyframes buttonSheen {
    0%   { opacity: 0; left: -120%; }
    20%  { opacity: 1; }
    40%  { left: 130%; opacity: 0; }
    100% { opacity: 0; left: 130%; }
  }

  @keyframes cardHalo {
    0%, 100% { opacity: 0; }
    40%      { opacity: 0.45; }
    60%      { opacity: 0.15; }
  }

  /* Responsive */
  @media (max-width: 880px) {
    header {
      flex-direction: column;
      align-items: flex-start;
      gap: 18px;
    }
    .hero {
      grid-template-columns: 1fr;
    }
    .hero-art {
      order: -1;
    }
  }

  @media (max-width: 720px) {
    .content-grid {
      grid-template-columns: 1fr;
    }
    .page {
      padding-inline: 14px;
    }
  }
  </style>
</head>
<body>
  <!-- floating petals -->
  <div class="petal"></div>
  <div class="petal"></div>
  <div class="petal"></div>
  <div class="petal"></div>
  <div class="petal"></div>

  <main class="page">
    <header class="js-reveal" data-delay="0">
      <div class="logo-cluster">
        <span class="logo-pill">Honkai: Star Rail</span>
        <span>HoYo-MiX · Cyrene Character Single</span>
      </div>
      <nav class="nav">
        <a href="#top">Overview</a>
        <a href="#about">About Cyrene</a>
        <a href="#memories">Memories</a>
        <a href="#tracks">Tracklist</a>
        <a href="#art">Trailblazer</a>
      </nav>
    </header>

    <!-- HERO -->
    <section class="hero" id="top">
      <div class="hero-copy js-reveal" data-delay="1">
        <div class="eyebrow">5★ Ice · Path of Remembrance</div>
        <h1 class="title-main">
          Ripples of Past Reverie
          <span>CYRENE · CHRYSOS HEIR OF REMEMBRANCE</span>
        </h1>
        <p class="subtitle">
          A meteor once crossed Amphoreus’ sky and stirred thirteen-colored ripples in the river of life. 
          From that light was born Cyrene, daughter of Aedes Elysiae and Chrysos Heir who tends the Seed of Memory so flowers of yesterday can bloom again tomorrow.
        </p>

        <div class="cyrene-name">
          <span class="cyrene-dot"></span>
          <span>Personal page for Trailblazer: <?php echo $username; ?></span>
        </div>

        <div class="hero-actions">
          <!-- PLAY BUTTON NOW GOES TO SPOTIFY -->
          <a
            href="https://open.spotify.com/album/1ZCtXSL5vBELipzP4PRWbi"
            id="playButton"
            class="btn-primary"
          >
            ▶ Play album
            <span class="pill-text">Listen to Ripples of Past Reverie</span>
          </a>
          <a href="#about" class="btn-ghost">
            ❋ View character story
          </a>
        </div>
      </div>

      <div class="hero-art js-reveal" data-delay="2">
        <div class="hero-orbit"></div>
        <div class="hero-card">
          <!-- Album cover -->
          <img src="/static/Ripples_of_Past_Reverie.webp" alt="Cyrene - Ripples of Past Reverie album art" />
          <div class="hero-card-footer">
            <span>Cyrene · Ripples of Past Reverie Animated Short</span>
            <span class="badge-stars">
              ✦✦✦✦✦
              <span class="badge-meta">5★ Remembrance · Ice</span>
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- CONTENT GRID -->
    <section class="content-grid" id="about">
      <!-- Left: character spotlight -->
      <article class="panel js-reveal" data-delay="0">
        <div class="panel-header">
          <h2 class="panel-title">Character Spotlight</h2>
          <span class="panel-tag">Path · Harmony of Memories</span>
        </div>
        <div class="panel-body">
          <p>
            <strong>Cyrene</strong> is Phainon’s childhood friend from Aedes Elysiae and the Chrysos Heir who guides Amphoreus’ cycles of remembrance. 
            After the Trailblazer awakens the Path of Remembrance, she greets them first as the fairy Mem, then returns in her true form to shoulder the stories of a world caught in endless repetition.
          </p>
          <p style="margin-top:10px;">
            In the Amphoreus saga she becomes the Demiurge of the Scepter, the one who records every sacrifice and gently rewrites fate so that Irontomb can be sealed away and the people she loves can finally walk toward a tomorrow of their own making.
          </p>
          <p style="margin-top:10px;">
            She likes to ask if a meeting is fate or a reunion long delayed, and invites others to write a different kind of poem together, one where memories do not end in regret but ripple forward into new lives.
          </p>

          <div class="traits">
            <span class="chip">Element · Ice</span>
            <span class="chip">Path · Remembrance</span>
            <span class="chip">Origin · Aedes Elysiae, Amphoreus</span>
            <span class="chip">Alias · Mem · Demiurge</span>
            <span class="chip">Role · True DMG support / healer</span>
            <span class="chip">Special · Recollection &amp; Future stacks</span>
          </div>

          <div class="stats-grid">
            <div class="stat-card">
              <div class="stat-label">Ultimate</div>
              <div class="stat-value">Verse ◦ Vow ∞</div>
              <div class="stat-description">
                Consumes Recollection instead of energy to summon her memosprite and enter the Ripples of Past Reverie state. 
                All allies’ Ultimates are activated, her Skill’s True DMG zone becomes permanent, and her Basic ATK is enhanced into To Love and Tomorrow ♪.
              </div>
            </div>
            <div class="stat-card">
              <div class="stat-label">Talent</div>
              <div class="stat-value">Hearts Gather as One</div>
              <div class="stat-description">
                At the start of battle and after Cyrene acts, allies and their memosprites gain Future. 
                When they take action, Future is consumed to grant Cyrene Recollection, letting the whole team’s turns feed into her next Ultimate.
              </div>
            </div>
            <div class="stat-card">
              <div class="stat-label">Technique</div>
              <div class="stat-value">Peace at West Wind's End</div>
              <div class="stat-description">
                Creates a special dimension that hastens allies’ movement and deploys her True DMG zone at battle start, 
                turning an approaching encounter into a small oasis of stillness where the past is already watching over the fight.
              </div>
            </div>
          </div>

          <div class="panel-art panel-art--spaced">
            <!-- Intro style artwork -->
            <img src="/static/Character_Cyrene_Introduction.webp" alt="Cyrene introduction artwork from Honkai: Star Rail" />
          </div>
        </div>
      </article>

      <!-- Right: memories / splash art -->
      <article class="panel js-reveal" id="memories" data-delay="1">
        <div class="panel-header">
          <h2 class="panel-title">Memories in Bloom</h2>
          <span class="panel-tag">Amphoreus &amp; Chrysos Heirs</span>
        </div>
        <div class="panel-body">
          <p>
            Amphoreus is a world built from cycles and stories. 
            In one era, Cyrene names Phainon the Deliverer and walks beside him through a flame-chasing journey; 
            in another, she becomes a memosprite who watches the same river of life from outside the flow.
          </p>
          <p style="margin-top:10px;">
            She carries the scenery they once wished to see together, still gazing at it long after goodbyes. 
            Spring, she believes, will always return to the land entangled by fate, as long as someone remains who remembers.
          </p>

          <div class="traits traits--compact">
            <span class="chip">Bond · Phainon &amp; Chrysos Heirs</span>
            <span class="chip">Form · Human · Mem · Demiurge</span>
            <span class="chip">Theme · Farewell that becomes reunion</span>
          </div>

          <div class="panel-art panel-art--spaced">
            <!-- Full splash illustration -->
            <img src="/static/Character_Cyrene_Splash_Art.webp" alt="Cyrene full splash art illustration" />
          </div>
        </div>
      </article>
    </section>

    <!-- TRACKLIST -->
    <section class="panel js-reveal" id="tracks" data-delay="0">
      <div class="panel-header">
        <h2 class="panel-title">Album Tracklist</h2>
        <span class="panel-tag">Ripples of Past Reverie · EP</span>
      </div>
      <div class="panel-body">
        <p class="pill-text pill-text--spaced">
          Official tracklist for the character single Ripples of Past Reverie (Honkai: Star Rail Cyrene Animated Short Single).
        </p>
        <div class="tracklist">
          <div class="track">
            <span class="track-index">01</span>
            <span class="track-title">昔涟</span>
            <span class="track-meta">3:06 · CN vocal · HOYO-MiX</span>
          </div>
          <div class="track">
            <span class="track-index">02</span>
            <span class="track-title">Ripples of Past Reverie</span>
            <span class="track-meta">3:06 · EN vocal · HOYO-MiX</span>
          </div>
          <div class="track">
            <span class="track-index">03</span>
            <span class="track-title">昔涟 · Instrumental</span>
            <span class="track-meta">3:06 · orchestral / backing</span>
          </div>
          <div class="track">
            <span class="track-index">04</span>
            <span class="track-title">昔涟 · Chinese Harmony Instrumental</span>
            <span class="track-meta">3:06 · harmony backing</span>
          </div>
          <div class="track">
            <span class="track-index">05</span>
            <span class="track-title">Ripples of Past Reverie · English Harmony Instrumental</span>
            <span class="track-meta">3:06 · harmony backing</span>
          </div>
        </div>
        <p class="pill-text" style="margin-top:10px;">
          Vocals by Angela Chang (CN ver.) and Cassie Wei (EN ver.), composed and produced by HOYO-MiX for Cyrene’s animated short.
        </p>
      </div>
    </section>

    <!-- TRAILBLAZER SECTION (greeting + input) -->
    <section class="panel js-reveal" id="art" data-delay="0">
      <div class="panel-header">
        <h2 class="panel-title">Trailblazer</h2>
        <span class="panel-tag">Personal Greeting</span>
      </div>
      <div class="panel-body art-generator">
        <p class="pill-text pill-text--spaced">
          Hi there! This page is tuned to your journey aboard the Astral Express and your encounter with Cyrene on Amphoreus.
        </p>
        <form class="art-form" method="get" action="index.php">
          <input
            type="text"
            name="username"
            id="artNameInput"
            maxlength="24"
            placeholder="Enter your Trailblazer name"
            autocomplete="off"
            value="TrailBlazer"
          />
          <button type="submit" class="btn-primary btn-small">
            ✦ Update greeting
          </button>
        </form>
        <p class="pill-text mta">
          Tip: Share a link like <code>?username=TrailBlazer</code> to show this page as “Hi TrailBlazer!”.
        </p>
      </div>
    </section>

    <footer class="js-reveal" data-delay="0">
      <span>Fan-made front-end concept for Cyrene · “Ripples of Past Reverie”.</span>
      <span>Adjust copy and links as official story updates in future versions.</span>
    </footer>
  </main>

  <!-- small script for scroll reveal + play button animation / redirect -->
  <script nonce="<?php echo $nonce; ?>">
    document.addEventListener("DOMContentLoaded", function () {
      // Reveal-on-scroll using IntersectionObserver
      var revealEls = document.querySelectorAll(".js-reveal");
      if ("IntersectionObserver" in window) {
        var observer = new IntersectionObserver(function (entries, obs) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add("in-view");
              obs.unobserve(entry.target);
            }
          });
        }, { threshold: 0.2 });

        revealEls.forEach(function (el) {
          observer.observe(el);
        });
      } else {
        // Fallback: show all if no IO support
        revealEls.forEach(function (el) {
          el.classList.add("in-view");
        });
      }

      // Play button → Spotify with small animation delay
      var playButton = document.getElementById("playButton");
      if (playButton) {
        playButton.addEventListener("click", function (e) {
          e.preventDefault();
          playButton.classList.add("is-playing");
          setTimeout(function () {
            window.location.href = "https://open.spotify.com/album/1ZCtXSL5vBELipzP4PRWbi";
          }, 350);
        });
      }
    });
  </script>
</body>
</html>
