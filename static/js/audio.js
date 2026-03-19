// ============================================================
//  audio.js — Forgotten Among the Fallen
//  Named SoundEngine to avoid shadowing window.Audio.
// ============================================================

const SoundEngine = (() => {

  const SCENE_MUSIC = {
    "title":                "ambient_title",
    "name_entry":           "ambient_cairn",       // introspective, not battlefield
    "battlefield":          "ambient_battlefield",
    "leif":                 "ambient_leif",
    "longhouse":            "ambient_forge",
    "cairn":                "ambient_cairn",
    "mound":                "ambient_mound",
    "gunnar":               "ambient_mound",       // dialogue — ominous, not combat yet
    "gunnar_combat":        "combat_boss",          // only the actual fight
    "scavenge":             "ambient_battlefield",
    "combat_draugar":       "combat_draugar",
    "act_break":            "ambient_void",
  };

  const SFX_MAP = {
    choice:       "sfx_choice",
    confirm:      "sfx_confirm",
    memory:       "sfx_memory",
    death:        "sfx_death",
    shards:       "sfx_shards",
    combat_hit:   "sfx_hit",
    combat_miss:  "sfx_miss",
    combat_parry: "sfx_parry",
  };

  let currentTrack   = null;
  let currentTrackId = null;
  let musicVolume    = 0.45;
  let sfxVolume      = 0.7;
  let muted          = false;

  const FADE_STEPS    = 30;
  const FADE_DURATION = 2000;
  const MUSIC_BASE    = "/static/audio/music/";
  const SFX_BASE      = "/static/audio/music/";  // sfx in same folder for now

  // ── Crossfade ─────────────────────────────────────────────
  let _fadeTimer = null;   // track active fade so we can cancel it

  function _crossfade(incoming, outgoing) {
    // Cancel any in-progress fade
    if (_fadeTimer) { clearInterval(_fadeTimer); _fadeTimer = null; }
    const interval = FADE_DURATION / FADE_STEPS;
    let step = 0;
    _fadeTimer = setInterval(() => {
      step++;
      const r = step / FADE_STEPS;
      if (outgoing && !outgoing.paused) outgoing.volume = Math.max(0, musicVolume * (1 - r));
      if (incoming) incoming.volume = Math.min(musicVolume, musicVolume * r);
      if (step >= FADE_STEPS) {
        clearInterval(_fadeTimer);
        _fadeTimer = null;
        if (outgoing) { outgoing.pause(); outgoing.currentTime = 0; }
      }
    }, interval);
  }

  // ── Core switch — SYNCHRONOUS, no await ───────────────────
  function _switchTo(trackName) {
    if (trackName === currentTrackId) return;

    // Immediately stop any previous track to prevent overlap
    if (currentTrack) {
      if (_fadeTimer) { clearInterval(_fadeTimer); _fadeTimer = null; }
      currentTrack.pause();
      currentTrack.currentTime = 0;
    }

    const track    = new window.Audio();
    track.loop     = true;
    track.volume   = muted ? 0 : musicVolume;
    track.src      = MUSIC_BASE + trackName + ".mp3";
    track.onerror  = () => { track.src = MUSIC_BASE + trackName + ".ogg"; };

    currentTrack   = track;
    currentTrackId = trackName;

    track.play()
      .then(() => {})
      .catch(err => {
        console.warn("Audio blocked:", err.message);
      });
  }

  // ── Public API ────────────────────────────────────────────
  function playTitle()  { if (!muted) _switchTo("ambient_title"); }

  function playScene(artKey) {
    if (muted) return;
    const t = SCENE_MUSIC[artKey];
    if (t) _switchTo(t);
  }

  function stopMusic(fade = true) {
    if (!currentTrack) return;
    if (_fadeTimer) { clearInterval(_fadeTimer); _fadeTimer = null; }
    if (fade) {
      _crossfade(null, currentTrack);
    } else {
      currentTrack.pause();
      currentTrack.currentTime = 0;
    }
    currentTrack   = null;
    currentTrackId = null;
  }

  function playSfx(name) {
    if (muted) return;
    const sfxName = SFX_MAP[name];
    if (!sfxName) return;
    try {
      const a   = new window.Audio(SFX_BASE + sfxName + ".mp3");
      a.volume  = sfxVolume;
      a.onerror = () => { a.src = SFX_BASE + sfxName + ".ogg"; a.play().catch(() => {}); };
      a.play().catch(() => {});
    } catch(e) {}
  }

  function toggleMute() {
    muted = !muted;
    if (currentTrack) currentTrack.volume = muted ? 0 : musicVolume;
    return muted;
  }

  function setMusicVolume(v) {
    musicVolume = Math.max(0, Math.min(1, v));
    if (currentTrack && !muted) currentTrack.volume = musicVolume;
  }

  function setSfxVolume(v) { sfxVolume = Math.max(0, Math.min(1, v)); }
  function isMuted()       { return muted; }

  return { playTitle, playScene, stopMusic, playSfx,
           toggleMute, isMuted, setMusicVolume, setSfxVolume };

})();
