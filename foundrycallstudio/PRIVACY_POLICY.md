# Foundry Call Studio — Privacy Policy

Updated October 31, 2026. **Development is paused.** Applies to the two-tab desktop prototype installed on October 23, 2026 (version 0.1.0, source commit `4ce2d08`) and the source preserved at the pause. The October 31 removal of unused UI code does not change data handling or replace the installed app. It is for fictional practice calls only, including an optional isolated HT813/Asterisk phone-line lab. Patient use and clinic deployment are not authorized.

## What the app processes

A call sends the caller's audio (this Mac's microphone, or a test call on the phone line) or typed messages to Google Gemini, the app's only voice service. Gemini also receives the receptionist's instructions: the practice information, the current date and office status, and the conversation so far. Replies, captions, the handoff note (patient type, reason, and the caller's name only if they gave it), the office status, reply timing and token counts appear on the Call tab. Typing tests never request microphone access. The phone-line audio option changes the sound on this Mac only; it records nothing.

## What is stored on this Mac

- **No automatic call storage.** There is no call log. The transcript and brief stay on the Call tab until the next call starts or the app closes. Audio is never recorded. Choosing **Save brief** creates a text file, described below.
- **Practice information** you edit in Setup is saved as `practice-information.json` in the app's user-data folder and used for later calls. It must hold practice policies, never patient information. **Restore bundled information** replaces it with the bundled copy; an unreadable file is kept beside it as a recovery copy.
- **The chime choice** uses local browser storage within the packaged app's temporary browser session and resets when the app quits. A development preview in a regular browser can retain it in that browser.
- The Gemini API key, the free-tier confirmation, the voice and the testing office status are kept in memory and cleared when the app quits. The app does not write keys or audio to its settings, logs or files.

The service inside the app listens only on this computer, at a random loopback port, and requires the app's temporary token. The interface loads only local files and has no advertising, analytics or tracking. The optional Asterisk lab is a local Linux VM; its SIP/RTP traffic and audio WebSocket carry fictional test-call audio, and its generated PBX credential stays in its private runtime outside the source, never shown to the app's window. A manually entered PBX password stays in memory until you disconnect or quit. The supplied lab configuration does not record audio or call details. Normal network requests reveal connection metadata to Google.

## Saving a brief

**Save brief** writes a text file only when you choose: the brief, the call's date, length and office status, the caller ID for a line call, and the transcript. It contains no key and no audio, but it contains whatever the caller said, which is why only fictional details belong in this prototype. You control the file and its copies; deleting the app does not delete them, and a synchronized folder follows that service's rules.

## Provider handling

Google's unpaid Gemini service uses submitted content and generated responses to improve its products and may have human reviewers process it. Do not submit personal, confidential or sensitive information. See the [Gemini API terms](https://ai.google.dev/gemini-api/terms), reviewed on October 31, 2026; they can change, and the app's local handling does not override them. Deleting anything on this Mac does not delete content Google retains.

## Operator controls

You supply your own Gemini key and confirm that its Google project has billing turned off; the app cannot check your account. One call runs at a time, for up to five minutes, with explicit microphone, mute and end controls. No request reaches Gemini until a call starts or a line call is answered, and nothing is retried automatically. On a practice call a handoff only shows the brief; on a line call it continues the same call to the front desk phone after closing Gemini and its media channel. The app does not schedule appointments, take messages, take payments or open patient charts.

## Contact

Questions: [sansargupta10@gmail.com](mailto:sansargupta10@gmail.com). Do not include patient information, API keys or call transcripts.
