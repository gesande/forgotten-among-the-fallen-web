// ============================================================
//  game.js — Forgotten Among the Fallen
//  Frontend controller. Talks to Flask API, renders scenes.
// ============================================================

const ART_BASE = "/static/svg/";
const ART_FALLBACK = "battlefield";

// ── DOM refs ──────────────────────────────────────────────────
const $ = id => document.getElementById(id);

// ── DOM refs — resolved after DOMContentLoaded ───────────────
let screens = {};

// ── State ─────────────────────────────────────────────────────
let currentScene = null;
let inCombat     = false;

// ── Central fetch helper — always sends session cookie ────────
async function api(path, body = null) {
  const opts = {
    credentials: "include",
    headers: {},
  };
  if (body !== null) {
    opts.method  = "POST";
    opts.headers["Content-Type"] = "application/json";
    opts.body    = JSON.stringify(body);
  } else {
    opts.method = "GET";
  }
  const res = await fetch(path, opts);
  return res.json();
}

// ═══════════════════════════════════════════════════════════
//  INIT
// ═══════════════════════════════════════════════════════════

async function init() {
  // Resolve all DOM refs now that the document is ready
  screens.title   = $("title-screen");
  screens.game    = $("game-screen");
  screens.credits = $("credits-screen");

  // Check for existing save
  try {
    const data = await api("/api/status");
    if (data.has_save) {
      $("btn-load").style.display = "block";
    }
  } catch(e) {}

  $("btn-new").addEventListener("click", startNewGame);
  $("btn-load").addEventListener("click", loadGame);
  $("btn-quit").addEventListener("click", () => window.close());
  $("btn-rise").addEventListener("click", riseAgain);
  $("btn-credits-back").addEventListener("click", () => {
    show("title"); hide("credits-screen");
    SoundEngine.playTitle();
  });
  $("name-submit").addEventListener("click", submitName);
  $("name-input").addEventListener("keydown", e => {
    if (e.key === "Enter") submitName();
  });

  // ── Audio controls ─────────────────────────────────────────

  // Helper: sync in-game audio UI to current engine state
  function syncAudioUI(musicPct, sfxPct, muted) {
    const muteEl = $("mute-btn");
    if (muteEl) {
      muteEl.textContent = muted ? "♪ muted" : "♪ sound on";
      muteEl.classList.toggle("muted", muted);
    }
    const mv = $("music-vol"); if (mv) mv.value = musicPct;
    const mv2 = $("music-val"); if (mv2) mv2.textContent = musicPct;
    const sv = $("sfx-vol");   if (sv) sv.value = sfxPct;
    const sv2 = $("sfx-val");  if (sv2) sv2.textContent = sfxPct;
  }

  let musicPct = 45, sfxPct = 70, isMuted = false;

  // Mute button — in-game only
  const muteBtn = $("mute-btn");
  if (muteBtn) {
    muteBtn.addEventListener("click", () => {
      isMuted = SoundEngine.toggleMute();
      syncAudioUI(musicPct, sfxPct, isMuted);
    });
  }

  // In-game audio panel toggle
  const audioPanel = $("audio-panel");
  if (muteBtn && audioPanel) {
    muteBtn.addEventListener("click", () => {
      audioPanel.classList.toggle("hidden");
    });
  }

  // Music volume slider — in-game only
  const musicVolEl = $("music-vol");
  if (musicVolEl) {
    musicVolEl.addEventListener("input", () => {
      musicPct = parseInt(musicVolEl.value);
      SoundEngine.setMusicVolume(musicPct / 100);
      syncAudioUI(musicPct, sfxPct, isMuted);
    });
  }

  // SFX volume slider — in-game only
  const sfxVolEl = $("sfx-vol");
  if (sfxVolEl) {
    sfxVolEl.addEventListener("input", () => {
      sfxPct = parseInt(sfxVolEl.value);
      SoundEngine.setSfxVolume(sfxPct / 100);
      syncAudioUI(musicPct, sfxPct, isMuted);
    });
  }

  // Initial UI state
  syncAudioUI(musicPct, sfxPct, false);
}

// ── Enter overlay — at module level for clean gesture call stack ──────
// Browsers require play() to be in the direct call stack of a user event.
// Keeping this outside init() / DOMContentLoaded avoids async chain breaks.
(function() {
  function attachOverlay() {
    const overlay = document.getElementById("enter-overlay");
    if (!overlay) return;
    function dismiss() {
      if (overlay.classList.contains("fade-out")) return;
      overlay.classList.add("fade-out");
      SoundEngine.playTitle();           // direct gesture → play()
      setTimeout(() => overlay.remove(), 900);
    }
    overlay.addEventListener("click",       dismiss);
    document.addEventListener("keydown",    dismiss, { once: true });
    document.addEventListener("touchstart", dismiss, { once: true });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", attachOverlay);
  } else {
    attachOverlay();
  }
})();

// ═══════════════════════════════════════════════════════════
//  NAVIGATION
// ═══════════════════════════════════════════════════════════

function show(screenId) {
  Object.values(screens).forEach(s => s && s.classList.add("hidden"));
  if (screens[screenId]) screens[screenId].classList.remove("hidden");
}

function hide(id) { $(id).classList.add("hidden"); }
function unhide(id) { $(id).classList.remove("hidden"); }

// ═══════════════════════════════════════════════════════════
//  NEW GAME / LOAD
// ═══════════════════════════════════════════════════════════

async function startNewGame() {
  await api("/api/new", {});
  SoundEngine.stopMusic(true);
  show("game");
  loadScene();
}

async function loadGame() {
  const data = await api("/api/load", {});
  if (data.error) { alert("No save found."); return; }
  SoundEngine.stopMusic(true);
  show("game");
  loadScene();
}

// ═══════════════════════════════════════════════════════════
//  SCENE LOADING
// ═══════════════════════════════════════════════════════════

async function loadScene() {
  showLoading(true);
  try {
    const data = await api("/api/scene");

    if (data.game_over) {
      if (data.credits) { show("credits"); hide("credits-screen"); unhide("credits-screen"); }
      return;
    }

    currentScene = data;
    renderScene(data);

    if (data.combat) {
      startCombat(data);
    }
  } catch(e) {
    console.error("Scene load error:", e);
  } finally {
    showLoading(false);
  }
}

// ═══════════════════════════════════════════════════════════
//  SCENE RENDERING
// ═══════════════════════════════════════════════════════════

function renderScene(data) {
  // ── Illustration — try .png first, fall back to .svg ────────
  const artKey = data.art_key || ART_FALLBACK;
  const artEl  = $("scene-art");
  artEl.style.opacity = "0";

  function tryLoad(exts, idx) {
    if (idx >= exts.length) { artEl.style.opacity = "1"; return; }
    artEl.src = `${ART_BASE}${artKey}.${exts[idx]}`;
    artEl.onload  = () => { artEl.style.opacity = "1"; };
    artEl.onerror = () => tryLoad(exts, idx + 1);
  }
  tryLoad(["png", "jpg", "svg"], 0);

  // ── Scene music ───────────────────────────────────────────
  SoundEngine.playScene(artKey);

  // ── HUD ───────────────────────────────────────────────────
  if (data.hud) renderHUD(data.hud);

  // ── Header ────────────────────────────────────────────────
  const hdr = $("scene-header");
  if (data.header) {
    $("scene-title").textContent    = data.header.title    || "";
    $("scene-subtitle").textContent = data.header.subtitle || "";
    hdr.classList.remove("hidden");
  } else {
    hdr.classList.add("hidden");
  }

  // ── Notifications (items / shards) ────────────────────────
  const notif = $("notification");
  const notifParts = [];
  if (data.shards  > 0) notifParts.push(`+ ${data.shards} echo shards`);
  if (data.items?.length) notifParts.push(...data.items.map(i => `+ ${i}`));
  if (notifParts.length) {
    notif.innerHTML = notifParts.join("<br>");
    notif.classList.remove("hidden");
  } else {
    notif.classList.add("hidden");
  }

  // ── Memory flash ──────────────────────────────────────────
  const memFlash = $("memory-flash");
  if (data.memories?.length) {
    $("memory-text").textContent = data.memories[0];
    memFlash.classList.remove("hidden");
    SoundEngine.playSfx("memory");
  } else {
    memFlash.classList.add("hidden");
  }

  // ── Prose body ────────────────────────────────────────────
  const proseEl = $("prose-body");
  proseEl.innerHTML = "";
  (data.paragraphs || []).forEach((p, i) => {
    if (p.type === "memory") return; // shown in memory flash
    const div = document.createElement("div");
    div.className = "prose-block" + (p.type === "italic" ? " italic" : "");
    div.textContent = p.type === "italic" ? `"${p.text}"` : p.text;
    div.style.animationDelay = `${i * 0.08}s`;
    div.style.opacity = "0";
    div.style.animation = `fadeIn 0.5s ease ${i * 0.08}s forwards`;
    proseEl.appendChild(div);
  });

  // ── Name input ────────────────────────────────────────────
  const nameWrap = $("name-input-wrap");
  if (data.name_prompt && (data.choices || []).length === 0) {
    // name_entry scene: show immediately, no choices to pick first
    nameWrap.classList.remove("hidden");
    setTimeout(() => $("name-input").focus(), 200);
  } else {
    nameWrap.classList.add("hidden");
  }
  $("name-input").value = "";

  // ── Choices ───────────────────────────────────────────────
  renderChoices(data.choices || [], data.next, data.name_prompt);
}

let pendingChoiceId = null;  // remembers which choice was clicked before name input

function renderChoices(choices, autoNext, hasNamePrompt) {
  const wrap = $("choices-wrap");
  wrap.innerHTML = "";

  if (autoNext) {
    const btn = document.createElement("button");
    btn.className = "choice-btn";
    btn.dataset.num = "·";
    btn.textContent = "Continue";
    btn.addEventListener("click", () => advanceScene(autoNext));
    wrap.appendChild(btn);
    return;
  }

  choices.forEach((choice, i) => {
    const btn = document.createElement("button");
    btn.className = "choice-btn";
    btn.dataset.num = i + 1;
    btn.textContent = choice.label;
    btn.addEventListener("mouseenter", () => SoundEngine.playSfx("choice"));
    btn.addEventListener("click", () => {
      SoundEngine.playSfx("confirm");
      makeChoice(choice.id);
    });
    wrap.appendChild(btn);
  });
}

async function advanceScene(nextKey) {
  showLoading(true);
  try {
    const payload = nextKey
      ? { next_scene: nextKey }
      : { next_scene: "__scene_next__", scene_key: currentScene ? currentScene.scene_key : "" };
    const data = await api("/api/advance", payload);
    if (data.game_over) { unhide("credits-screen"); return; }
    loadScene();
  } catch(e) {
    console.error("Advance error:", e);
    showLoading(false);
  }
}

// ═══════════════════════════════════════════════════════════
//  CHOICES
// ═══════════════════════════════════════════════════════════

async function makeChoice(choiceId) {
  showLoading(true);
  disableChoices(true);
  try {
    // __next__ is a synthetic Continue for prose-only auto-next scenes
    if (choiceId === "__next__") {
      await advanceScene(null);
      return;
    }
    const data = await api("/api/choose", { choice_id: choiceId });
    if (data.game_over) { show("credits"); unhide("credits-screen"); return; }
    if (data.narration) {
      const proseEl = $("prose-body");
      proseEl.innerHTML = "";
      const div = document.createElement("div");
      div.className = "prose-block";
      div.textContent = data.narration;
      proseEl.appendChild(div);
      $("choices-wrap").innerHTML = "";
      $("notification").classList.add("hidden");
      showLoading(false);
      await sleep(1800);
    }
    loadScene();
  } catch(e) {
    console.error("Choice error:", e);
    showLoading(false);
    disableChoices(false);
  }
}

async function submitName() {
  const name = $("name-input").value.trim();
  if (!name) return;
  showLoading(true);
  try {
    await api("/api/choose", { name });
    pendingChoiceId = null;
    loadScene();
  } catch(e) { showLoading(false); }
}

// ═══════════════════════════════════════════════════════════
//  HUD
// ═══════════════════════════════════════════════════════════

function renderHUD(hud) {
  $("hp-bar").style.width    = (hud.hp_ratio * 100) + "%";
  $("wrath-bar").style.width = ((hud.wrath / (hud.max_wrath || 100)) * 100) + "%";
  $("hud-hp-desc").textContent = hud.hp_desc || "";
  $("hud-shards").innerHTML   = `${hud.shards} <span>shards</span>`;

  // Curse dots
  const curseEl = $("hud-curse");
  curseEl.innerHTML = "";
  if (hud.curse > 0) {
    const dots = "●".repeat(hud.curse) + "○".repeat(5 - hud.curse);
    curseEl.textContent = `Curse ${dots}`;
  }

  // Memories
  const memEl = $("hud-memories");
  if (hud.memories > 0) {
    memEl.textContent = `${hud.memories} ${hud.memories === 1 ? "memory" : "memories"} recovered`;
  }
}

// ═══════════════════════════════════════════════════════════
//  COMBAT
// ═══════════════════════════════════════════════════════════

function startCombat(data) {
  inCombat = true;
  const c = data.combat;

  // Switch to combat music and set art — one declaration
  const artKey = data.art_key || "combat_draugar";
  SoundEngine.playScene(artKey);

  // Set combat art
  // Set combat art — try png/jpg before svg
  const combatArtEl = $("combat-art");
  combatArtEl.style.opacity = "0";
  function tryCombatLoad(exts, idx) {
    if (idx >= exts.length) { combatArtEl.style.opacity = "1"; return; }
    combatArtEl.src = `${ART_BASE}${artKey}.${exts[idx]}`;
    combatArtEl.onload  = () => { combatArtEl.style.opacity = "1"; };
    combatArtEl.onerror = () => tryCombatLoad(exts, idx + 1);
  }
  tryCombatLoad(["png", "jpg", "svg"], 0);

  // Enemy name & HP bar
  $("combat-enemy-name").textContent = c.enemy_name || "Enemy";
  $("enemy-hp-bar").style.width = (c.enemy_hp_ratio * 100) + "%";

  // Initial log
  const logEl = $("combat-log");
  logEl.innerHTML = "";
  (c.log || []).forEach(msg => appendCombatLog(msg));

  // Actions
  renderCombatActions(c.actions || []);

  // Show combat panel
  unhide("combat-panel");
}

function renderCombatActions(actions) {
  const wrap = $("combat-actions");
  wrap.innerHTML = "";
  actions.forEach(a => {
    const btn = document.createElement("button");
    btn.className     = "combat-btn";
    btn.textContent   = a.label;
    btn.dataset.id    = a.id;
    btn.addEventListener("click", () => doCombatAction(a.id));
    wrap.appendChild(btn);
  });
}

async function doCombatAction(actionId) {
  disableCombatBtns(true);
  try {
    const data = await api("/api/combat/action", { action_id: actionId });

    // Update enemy HP bar
    $("enemy-hp-bar").style.width = (data.enemy_hp_ratio * 100) + "%";
    if (data.hud) renderHUD(data.hud);

    // Append log entries
    (data.log || []).forEach(msg => appendCombatLog(msg));

    if (data.over) {
      await handleCombatEnd(data);
    } else {
      renderCombatActions(data.actions || []);
    }
  } catch(e) {
    console.error("Combat error:", e);
    disableCombatBtns(false);
  }
}

async function handleCombatEnd(data) {
  if (data.died) {
    // Show death overlay
    SoundEngine.playSfx("death");
    SoundEngine.stopMusic(true);
    hide("combat-panel");
    inCombat = false;
    const curseStacks = data.hud?.curse || 0;
    $("death-curse").textContent = curseStacks > 0
      ? `Curse: ${"●".repeat(curseStacks)}${"○".repeat(5 - curseStacks)}`
      : "";
    unhide("death-overlay");
    return;
  }

  // Won or fled — show rewards briefly then advance
  if (data.shards_gained > 0) {
    SoundEngine.playSfx("shards");
    appendCombatLog(`+ ${data.shards_gained} echo shards`, "system");
  }
  (data.items_gained || []).forEach(item => appendCombatLog(`+ ${item}`, "system"));

  await sleep(1800);
  hide("combat-panel");
  inCombat = false;
  loadScene();
}

function appendCombatLog(msg, type = "") {
  const logEl = $("combat-log");
  const div   = document.createElement("div");
  div.className = "log-entry" + (type ? ` ${type}` : "");
  // Auto-classify messages and play sfx
  if (!type) {
    if (msg.includes("taken") || msg.includes("wound") || msg.includes("fall")) {
      div.classList.add("damage");
      SoundEngine.playSfx("combat_hit");
    } else if (msg.includes("miss") || msg.includes("wide") || msg.includes("step aside")) {
      div.classList.add("miss");
      SoundEngine.playSfx("combat_miss");
    } else if (msg.includes("parry") || msg.includes("PARRY")) {
      div.classList.add("parry");
      SoundEngine.playSfx("combat_parry");
    }
  }
  div.textContent = msg;
  logEl.appendChild(div);
  logEl.scrollTop = logEl.scrollHeight;
}

async function riseAgain() {
  hide("death-overlay");
  loadScene();
}

// ═══════════════════════════════════════════════════════════
//  HELPERS
// ═══════════════════════════════════════════════════════════

function showLoading(on) {
  const el = $("loading");
  if (on) el.classList.remove("hidden");
  else    el.classList.add("hidden");
}

function disableChoices(on) {
  document.querySelectorAll(".choice-btn").forEach(b => b.disabled = on);
}

function disableCombatBtns(on) {
  document.querySelectorAll(".combat-btn").forEach(b => b.disabled = on);
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

// ── Boot ──────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", init);
