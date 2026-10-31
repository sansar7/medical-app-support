# Foundry Call Studio — Support

Updated October 31, 2026. **Development is paused.** Foundry Call Studio remains a local Mac prototype for fictional receptionist calls, with an optional HT813/Asterisk phone-line lab. No clinic deployment, scheduling system or patient chart is connected.

This guide describes the two-tab prototype installed on October 23, 2026 (version 0.1.0, source commit `4ce2d08`) and the source preserved at the pause. Hardware testing and deployment are on hold. The October 31 cleanup removes unused UI state and styles without changing the call workflow; it does not replace the installed app.

## While development is paused

The prototype, saved practice information and setup references are retained. Quit the app when finished; if the local Asterisk lab is running, use **Setup → Phone line → Stop local Asterisk** before quitting. Quitting clears the in-memory Gemini key. Text files previously created with **Save brief** remain wherever you saved them. Before resuming, review practice details, provider availability and free-tier terms, and the unresolved microphone and phone-line checks. No new release or hardware test is scheduled.

## Start a call

These instructions are retained for supervised fictional testing when the owner resumes it.

Open Foundry Call Studio (Prototype). On first launch it opens **Setup**: under **Voice**, paste a Google Gemini API key, choose a voice, confirm the key's Google project has billing turned off, and save. The key is kept in memory and must be entered again after the app quits. Use fictional details only.

On the **Call** tab, choose **Start practice call** (microphone) or **Test with typing**. Speak or type as a caller: ask about hours or walk-ins, say you are a new patient who wants crowns, or an existing patient who needs to reschedule. The **Staff brief** fills in when the receptionist hands off; **Take over the call** ends the receptionist and keeps the brief. **Save brief** writes a text file with the brief and transcript. Shortcuts: **M** mute, **E** end, **/** type.

## Test closed-office calls

Under **Setup → Practice calls**, set **Office status** to **Always closed** to hear after-hours behavior at any time of day: the greeting says the office is closed and when it opens, nobody is handed off and no message is taken. **Always open** does the reverse. The setting resets when the app quits.

## Practice information

**Setup → Practice information → Review and edit** opens the editor: practice name, address and numbers, weekly hours and the walk-in cutoff, closure dates, prices, the answers to common questions (add, edit, remove, or mark one for review so callers who ask it go to the front desk), and the phone-line policy. **Save information** applies to the next call. If the saved information cannot be read, calls pause until you choose **Restore bundled information**; the unreadable file is kept for recovery.

## Phone line

**Setup → Phone line** starts, connects to or stops the managed Asterisk lab on this Mac, or connects to a separately configured PBX. A ringing or active line call takes over the **Call** tab with **Answer line call**, **Mute caller**, **Ring front desk now** and **End line call**; the Mac's microphone and speakers are not used. The lab on this Mac does not yet accept HT813 traffic; the gateway's networking and phones need separate setup. See [HT813 setup](docs/HT813_SETUP.md).

## Troubleshooting

- **Microphone unavailable:** allow Foundry Call Studio in macOS System Settings › Privacy & Security › Microphone, or use **Test with typing**.
- **Gemini declined the session or quota is used up:** wait a minute and start a new call; the app never retries or switches to paid usage.
- **Could not authorize the key:** check the key and its project in Google AI Studio without sharing the key.
- The setup checklist at the top of **Setup** shows what is missing. This local build is not notarized for distribution; Windows and real phone lines are untested.

## Privacy and feedback

Read the [privacy policy](PRIVACY_POLICY.md). Email [sansargupta10@gmail.com](mailto:sansargupta10@gmail.com) with the app version, macOS version and what happened. Do not send keys, patient information or call content.
