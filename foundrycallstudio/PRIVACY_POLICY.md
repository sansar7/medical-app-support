# Foundry Call Studio — Privacy Policy

Updated October 14, 2026. Applies to the local 0.1.0 desktop prototype and its current source. This app is for fictional practice calls only; it is not connected to clinic phones or patient records.

## What the app processes

A call you start sends microphone audio or typed practice messages to the voice provider you select, Google Gemini or OpenAI. The provider also receives the bundled clinic instructions, current office-status context, conversation and tool messages needed to answer and prepare the simulated brief. Replies, streaming captions, fictional intake details, handoff or callback notes, timing and provider usage counts appear in the app. Typing-only practice does not request microphone access. The phone-line test processes audio locally before transmission or playback; it does not record a telephone call.

## Local storage and access

Provider API keys, settings and practice-call content are kept in application memory. The application does not deliberately write keys, audio recordings or transcripts to its settings, server logs or an application database. Its browser session is nonpersistent. Ending a call stops its streams but keeps the current brief visible for review and export; quitting the app clears its in-memory keys and call content. Operating-system diagnostics, swap and files you export are separate from this in-memory design.

The desktop service listens only on this computer at a random loopback port and requires the app's temporary token. The interface loads local resources and has no advertising, analytics or tracking SDK. There is no developer-operated relay receiving call content. Normal network requests still reveal connection metadata to the selected provider. Links you choose to open in your browser are governed by those websites' policies.

## Exports and deletion

Save brief writes a text or JSON file only when you request it. These files include the conversation transcript, any entered name and callback number, intake and simulated handoff or callback details, and call metadata such as time, provider, office status, response delay and usage counts. Exports do not include the API key or an audio recording. They can contain sensitive information if you type or say it, which is why only fictional details belong in this prototype.

You control the saved file and its destination. Delete exported files and any copies or backups separately; quitting or uninstalling the app does not delete them. A destination in iCloud, Google Drive or another synchronized folder follows that service's rules. Deleting a local export does not delete content retained by a model provider.

## Provider handling

Google's unpaid Gemini service uses submitted content and generated responses to improve its products and may have human reviewers process that content. Do not submit personal, confidential or sensitive information. See the [Gemini API terms](https://ai.google.dev/gemini-api/terms).

OpenAI states that API content is not used for model training unless the account opts in. Provider-side retention can still apply, including abuse-monitoring logs and account-specific storage settings. This prototype does not establish that your account has zero data retention. See [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data).

Provider terms were reviewed on October 14, 2026 and can change. Local in-memory handling does not override them. This prototype is not configured or validated for real patient information.

## Operator controls

You choose the provider and supply your own key. Each provider has a separate usage confirmation. There is one active practice call, limited to five minutes, with explicit microphone, mute and end controls. The app makes no provider call until you start one and does not automatically switch providers. It cannot independently verify your account balance or billing status.

The app does not place calls, transfer a real line, schedule appointments, send messages to staff, take payments or access patient charts. Handoffs and callbacks are simulations inside the app.

## Contact

For questions, contact [sansargupta10@gmail.com](mailto:sansargupta10@gmail.com). Do not include patient information, API keys or unredacted practice transcripts in support requests.
