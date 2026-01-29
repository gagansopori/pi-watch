# pi-watch client

This file: `client/README.md`

## Purpose
Client runs on the Raspberry Pi with the Pirate Audio board. It is responsible for local UI, hardware control (audio, display, buttons), and minimal offline behavior. Server handles persistence, the web dashboard, and heavy external integrations.

## Responsibilities

\*Client responsibilities
- Render local screens (clock, radio, combined).
- Drive Pirate Audio hardware: display, audio output, buttons, LEDs.
- Local audio playback and FM/stream control.
- Read buttons and map to UI/actions.
- Sync configuration with server and use a local cache if server unavailable.
- Provide a small HTTP/WebSocket API for real-time updates and remote control from the server or web UI.

\*Server responsibilities
- Persist user configuration (styles, station list, schedules).
- Host web dashboard for editing styles, stations, and global settings.
- Authenticate users and devices.
- Fetch external data (weather, timezones, metadata) and optionally push it to clients.
- Serve configuration and push real-time updates via WebSocket or push endpoints.

## Modes
- `clock` \- show clock, weather and clock styles.
- `radio` \- show currently playing station metadata and radio controls.
- `both` \- combined UI; small clock + radio info.
The client should allow switching modes locally and accept mode changes from the server.

## UI screens (client)
- Clock screen: large time, optional weather, selected style.
- Radio screen: station name, metadata, play/pause, volume.
- Combined screen: condensed clock + radio.
- Settings/Info screen: current mode, WiFi, sync status, local IP.

Navigation: simple stack or finite-state machine; default screen = last-used.

## Buttons (4 buttons)
Map buttons to simple actions so physical controls always work.

- Button A (short press): Toggle between screens (clock -> radio -> combined -> clock)  
  Button A (long press, 1s): Cycle modes (clock / radio / both) and send mode update to server.
- Button B (short press): Previous station / rewind metadata  
  Button B (long press): Seek backward in stream (if supported) or decrease brightness.
- Button C (short press): Next station / forward metadata  
  Button C (long press): Seek forward in stream or increase brightness.
- Button D (short press): Play / Pause / Mute toggle  
  Button D (long press): Open local settings menu (WiFi, sync now, reboot).

Buttons generate events locally and also post events to the server for logging / remote control.

## Data model (client local cache)
Store a small `state.json` locally with:
- mode: `clock|radio|both`
- display_style: id
- stations: [ { id, name, url, metadata } ]
- selected_station_id
- volume (0-100)
- last_sync_timestamp

On boot: load `state.json`, attempt server sync, then apply local cache.

## API (client exposes)
- GET `/api/state` \- current state (mode, station, volume)
- POST `/api/state` \- update state (body: partial state)
- GET `/api/stations` \- station list
- POST `/api/controls` \- control actions (play/pause, next, prev, volume)
- WebSocket `/ws` \- real-time updates from server

Server should authenticate calls. Client accepts server updates and applies them immediately.

## Web dashboard integration (server)
- Server UI edits station list, styles, and pushes changes to specific device via `/api/state` or `/ws`.
- When user changes a style or station on web UI, server pushes to client; client persists to `state.json`.

## Offline behavior
- If server unreachable: run fully from `state.json`. Queue outbound events and retry sync.
- Provide user feedback via LEDs or a small text line on screen for sync status.

## Security
- Use token-based auth for client-server API.
- Keep tokens in `~/.pi-watch/credentials.json` with filesystem permissions set to owner-only.
- Consider HTTPS or VPN for remote access.

## Development / Run (client)
1. Create virtualenv and install deps:
   - `python -m venv .venv && source .venv/bin/activate`
   - `pip install -r requirements.txt`
2. Configure device:
   - Create `~/.pi-watch/state.json` (example included in repo).
   - Create `~/.pi-watch/credentials.json` with server URL and token.
3. Run:
   - `python -m client.main` (or use the provided systemd service)
4. Logs: `journalctl -u pi-watch-client -f` (if using systemd) or stdout for dev.

## Notes for refactor
- Keep hardware bindings (display, audio, GPIO) confined to a small hardware layer module.
- UI logic should be testable and independent of hardware (inject hardware drivers).
- Keep networking code in a sync module with clear retry/backoff.
- Keep business logic (modes, button handling, playlist logic) in separate modules so server can reuse some logic if needed.

## Example files to add in `client/`
- `client/main.py` \- app entry
- `client/ui.py` \- UI state machine and rendering
- `client/hardware.py` \- Pirate Audio wrappers (display/audio/buttons)
- `client/sync.py` \- HTTP + WebSocket client to server
- `client/state_store.py` \- local JSON cache management
