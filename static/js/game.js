// ============================================================
//  game.js — Forgotten Among the Fallen
//  Frontend controller. Talks to Flask API, renders scenes.
// ============================================================

const ART_BASE = "/static/svg/";
const ART_FALLBACK = "battlefield";

// ── DOM refs ──────────────────────────────────────────────────
const $ = id => document.getElementById(id);

const screens = {
  title:   $("title-screen"),
  game:    $("game-screen"),
  credits: $("credits-screen"),
};

// ── State ─────────────────────────────────────────────────────
let currentScene = null;
let inCombat     = false;

// ═══════════════════════════════════════════════════════════
//  INIT
// ═══════════════════════════════════════════════════════════

async function init() {
  // Check for existing save
  try {
    const res  = await fetch("/api/status");
    const data = await res.json();
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
  });
  $("name-submit").addEventListener("click", submitName);
  $("name-input").addEventListener("keydown", e => {
    if (e.key === "Enter") submitName();
  });
}

// ═══════════════════════════════════════════════════════════
//  NAVIGATION
// ═══════════════════════════════════════════════════════════

function show(screenId) {
  Object.values(screens).forEach(s => s.classList.add("hidden"));
  screens[screenId].classList.remove("hidden");
}

function hide(id) { $(id).classList.add("hidden"); }
function unhide(id) { $(id).classList.remove("hidden"); }

// ═══════════════════════════════════════════════════════════
//  NEW GAME / LOAD
// ═══════════════════════════════════════════════════════════

async function startNewGame() {
  await fetch("/api/new", { method: "POST" });
  show("game");
  loadScene();
}

async function loadGame() {
  const res  = await fetch("/api/load", { method: "POST" });
  const data = await res.json();
  if (data.error) { alert("No save found."); return; }
  show("game");
  loadScene();
}

// ═══════════════════════════════════════════════════════════
//  SCENE LOADING
// ═══════════════════════════════════════════════════════════

async function loadScene() {
  showLoading(true);
  try {
    const res  = await fetch("/api/scene");
    const data = await res.json();

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
  // ── Illustration ──────────────────────────────────────────
  const artKey = data.art_key || ART_FALLBACK;
  const artEl  = $("scene-art");
  artEl.style.opacity = "0";
  artEl.src = `${ART_BASE}${artKey}.svg`;
  artEl.onload = () => { artEl.style.opacity = "1"; };
  artEl.onerror = () => {
    artEl.src = `${ART_BASE}${ART_FALLBACK}.svg`;
    artEl.style.opacity = "1";
  };

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
  if (data.name_prompt) {
    nameWrap.classList.remove("hidden");
    setTimeout(() => $("name-input").focus(), 200);
  } else {
    nameWrap.classList.add("hidden");
  }

  // ── Choices ───────────────────────────────────────────────
  renderChoices(data.choices || [], data.next);
}

function renderChoices(choices, autoNext) {
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
    btn.addEventListener("click", () => makeChoice(choice.id));
    wrap.appendChild(btn);
  });
}

async function advanceScene(nextKey) {
  showLoading(true);
  try {
    // Tell the server to advance to the next scene
    const res  = await fetch("/api/advance", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ next_scene: nextKey }),
    });
    const data = await res.json();
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
    const res  = await fetch("/api/choose", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ choice_id: choiceId }),
    });
    const data = await res.json();
    if (data.game_over) { show("credits"); unhide("credits-screen"); return; }
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
    await fetch("/api/choose", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });
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

  // Set combat art
  const artKey = data.art_key || "combat_draugar";
  $("combat-art").src = `${ART_BASE}${artKey}.svg`;

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
    const res  = await fetch("/api/combat/action", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action_id: actionId }),
    });
    const data = await res.json();

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
  // Auto-classify messages
  if (!type) {
    if (msg.includes("taken") || msg.includes("wound") || msg.includes("fall"))
      div.classList.add("damage");
    else if (msg.includes("miss") || msg.includes("wide") || msg.includes("step aside"))
      div.classList.add("miss");
    else if (msg.includes("parry") || msg.includes("PARRY") || msg.includes("shard"))
      div.classList.add("parry");
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
