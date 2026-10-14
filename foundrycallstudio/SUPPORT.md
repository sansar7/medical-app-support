# Foundry Call Studio — Support

Updated October 14, 2026. Foundry Call Studio 0.1.0 is a local Mac prototype for fictional receptionist practice calls. It is not connected to a clinic phone line, scheduling system or patient chart.

## Start a practice call

Open Foundry Call Studio (Prototype) in Applications. Choose a provider in Voice setup, supply its API key and confirm the required free-usage conditions. Google Gemini requires an unbilled project; OpenAI requires verified available free API credits. The app cannot verify account balances. Do not use real patient information.

Use Start practice call with a microphone or Test with typing. End the call to review the brief; Save brief creates a text or JSON export that includes the transcript. Quitting clears the app's in-memory call content and keys, but does not delete exported files or provider-held data.

## Practice controls

Office status can follow the current Bessemer time or be set open or closed for testing. The phone-line audio option simulates narrowband telephone audio. A handoff or callback only prepares an in-app brief; it does not contact anyone. One call can run for up to five minutes. Errors and exhausted quota end the call without an automatic provider switch.

## Troubleshooting

If the microphone is unavailable, check this app's permission in macOS Privacy & Security and try typing-only practice. If provider setup fails, check your own provider account and key permissions without sharing the key. No live provider call is required to open the app. This local test build is not notarized for public distribution. Windows and real phone-line integration remain untested.

## Privacy and feedback

Read the [privacy policy](PRIVACY_POLICY.md) for provider processing, exports and local retention. Email [sansargupta10@gmail.com](mailto:sansargupta10@gmail.com) with the app version, macOS version and a description of the problem. Do not send keys, patient information or unredacted call content.
