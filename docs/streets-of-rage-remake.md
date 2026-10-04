# Streets of Rage Remake (SORR) v5.2

Fan remake of Streets of Rage 1/2/3 (BomberGames), run under Wine.
Role: `install_sorr` (opt-in). Playbook: `install-sorr.yml`, or
`ansible-playbook site.yml --tags sorr`. Vars: `group_vars/all/sorr.yml`.

## Why Wine
The engine is **BennuGD**; the shipped binary is the Windows `SorR.exe`
(a self-contained SDL 1.2 app — no MSVC runtime, so no vcrun/winetricks).
There is no clean modern native Linux engine: the AUR `streetsofrageremake`
package is only **v5.1** and pins OpenSSL-1.0-era 32-bit libs that Arch has
dropped. Running `SorR.exe` under Wine is the documented working method.

## The archive (staged on the NAS)
The only official download is a MEGA link (not pinnable/checksummable). We
use the Internet Archive mirror `SORRv52_rev550.rar` (sha1
`8e67ff02…`) — **but** that CDN throttles single connections to a crawl and
serves *corrupt* multi-connection ranges (verified: repeated downloads gave
different full-size hashes, none matching archive.org's own md5/sha1). So
the clean `.rar` is staged once on the NAS:

- `dg_sorr_archive_source` defaults to `{{ dg_roms_final_root }}/PC/SORRv52_rev550.rar`.
- The role copies it into the cache and `get_url` verifies the sha1; it only
  falls back to downloading from archive.org if the file is absent.
- To (re)fetch manually, `aria2c -x16` from the MEGA/archive mirror, verify
  the sha1, and drop it at that path.

## Fullscreen — gamescope
`SorR.exe` renders at a fixed ~640×480 and does **not** scale its own output
up; its in-game "fullscreen" only tries a display mode-change, which
XWayland on the scaled 4K DP-1 can't satisfy — so it always looks tiny.
The launcher runs it under **gamescope**, which upscales the small game to
true fullscreen:

    gamescope -W 3840 -H 2160 -f --immediate-flips --rt -- wine SorR.exe

- **Keep SORR itself in WINDOWED mode** (Options → Video). gamescope does the
  upscaling; SORR's own fullscreen fights it.
- gamescope works here for SORR even though it fails for Supermodel — SORR is
  light 2D, so it dodges the NVIDIA-compositor DRM-modifier issues that break
  gamescope's heavy-3D path (see [[project_supermodel_native_nvidia]]).
- `--immediate-flips` + `--rt` cut the compositor input latency; `--rt` needs
  `CAP_SYS_NICE`, which the role grants to the gamescope binary via `setcap`.
- Knobs: `dg_sorr_use_gamescope` (default true; `DG_SORR_GAMESCOPE=0` to
  disable per-launch), `dg_sorr_gamescope_opts`. Without gamescope it falls
  back to a Wine virtual desktop (`dg_sorr_desktop_res`).

### Host gamescope (non-Arch hosts)

On some hosts gamescope can't start **inside** the rootless box: on Ubuntu +
podman the box sees `/tmp/.X11-unix` owned by `nobody`, so gamescope fails
with `Failed to create Xwayland server`. The Wine virtual-desktop fallback
showed only a blue desktop there. Instead, the launcher runs gamescope on the
**host**.

This is automatic: with `dg_sorr_host_gamescope: auto` (the default) the role
checks the owner of the box's `/tmp/.X11-unix` and switches to host mode when
it isn't root or the box user. It then installs `gamescope` and `flatpak` on
the host (`dg_host_gamescope_tools`). Set it to `true` / `false` to force a
mode, and size the session to your panel:

```yaml
# ansible/host_vars/localhost.yml
dg_sorr_host_gamescope_opts: "-W 1920 -H 1080 -S integer -f"
```

In host mode the launcher re-enters itself inside the host gamescope session.
The desktop entry starts the launcher on the host directly, while ES-DE (which
runs inside the box) goes through `distrobox-host-exec`, which needs the
host's flatpak session helper. If the host can't be reached the launcher
prints a note and starts plain-windowed in the box.

## Saves / controls
- Saves + video/config live in `tools/sorr/game/savegame/` (persistent work
  dir, excluded from release rsync — survives rebuilds). **Start a fresh
  save**: v5.2 rejects saves from older versions.
- Controller is XInput by default; the launcher applies the shared SDL pad
  policy and opens on the main horizontal monitor.
- **Exit**: Select+Start (evsieve → Alt+F4), or gamescope's Super+Shift+Esc.
