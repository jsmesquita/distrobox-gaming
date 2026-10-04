# ES-DE Ports (native ports & fan games)

ES-DE organizes games by system and ROM file, so the standalone games the
opt-in roles install (fan games, source ports, recomps) have no ROM to scan.
They get their own **Ports** system instead: one tiny launcher script per game
in `dg_esde_ports_dir` (default `~/ES-DE/ports` in the box home), which ES-DE
lists and runs like any other game, so everything is playable from the
controller-driven front-end, not only from the desktop menu.

Each script just execs the game's existing box launcher:

```sh
#!/bin/sh
# Managed by Ansible (configure_esde/port.yml) - ES-DE Ports entry.
exec "/path/to/box/home/bin/sorr-launch" "$@"
```

The scripts live in the box home, not in the ROM library: they are generated
files, and the EmuDeck tree is mounted read-only inside the box.

## Registered games

| Game | Role |
|---|---|
| Streets of Rage Remake | `install_sorr` |
| ProjectR - SF Rush | `install_project_r` (removed again on `dg_projectr_revert=true`) |

## Adding a game

After a role deploys its launcher, register it with the shared task file:

```yaml
- name: Register <game> in the ES-DE Ports system
  ansible.builtin.include_role:
    name: configure_esde
    tasks_from: port.yml
  vars:
    esde_port_name: "<Name shown in ES-DE>"
    esde_port_cmd: "{{ dg_box_home }}/bin/<launcher>"
```

Pass `esde_port_state: absent` (with the same `esde_port_name`) from the
role's revert path to remove the entry.

## Notes

- New entries appear on the next ES-DE start, since ES-DE rescans its
  directories by default. With fast startup
  (`dg_esde_parse_gamelist_only: true`) run `esde-rescan` once. See
  `docs/esde-fast-startup.md`.
- ES-DE's scraper supports the `ports` platform, so cover art and
  descriptions can be scraped like any other system.
