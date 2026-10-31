# Easy3D Capture Privacy Policy

Last updated: October 31, 2026

Developer: Sansar Gupta. Contact: [sansargupta10@gmail.com](mailto:sansargupta10@gmail.com).

## Development status

Development is paused as of October 31, 2026, with no scheduled update or restart date. These instructions, privacy information and the contact address remain available. Pausing development does not remove scans from your iPhone. Export any scans you need before deleting the app; its private storage is excluded from system backups, and the developer cannot recover lost local files.

## Release coverage

This policy describes **version 1.0 (13)**, submitted for App Review on October 14, 2026. Build 13 includes optional photograph retention, interrupted-reconstruction retry, unsaved-capture recovery, renaming, thumbnails, a privacy cover and case-label exclusion from exports. Version **1.0 (13)** is available in the [US App Store](https://apps.apple.com/us/app/easy3d-capture/id6821235094), verified against App Store Connect and the public listing on October 31, 2026. Check your installed app’s version/build when applying these instructions. The earlier App Store submission **1.0 (12)**, built from `495b345`, lacks those changes and includes case labels in export manifests, as disclosed below. Earlier development copies may also report 1.0 (12) while using newer source; retain their source commit to identify their behavior.

## Information processed on your iPhone

Easy3D Capture uses rear-camera photographs and native Object Capture processing to reconstruct faces or objects on your iPhone. Saved scans can contain a case label you enter, capture dates, subject and quality metadata, 3D geometry and photographic textures. In build 13, each saved scan can also hold a small preview image of its model, created on the device for the library list; it is stored with that scan, protected and excluded from backups like the scan, never included in exports, and deleted with the scan. You can correct a case label from the scan's actions; the corrected label also stays on the device. New photogrammetry captures remove their reconstruction checkpoints after the completed model is validated, and remove their source photographs unless you turn on **Keep photographs for Mac reconstruction** for that capture. That option is included in build 13; it is off for every capture and is not remembered. Kept photographs are full-resolution images of the subject and background and can embed depth data, camera poses, capture time and the device model. Supported photo sets stay with that scan in the protected, backup-excluded library until you choose Delete photographs, delete the scan or remove the app. Sets that exceed the supported size or file limits, or contain unsupported files, are removed rather than retained partially; the model carries a warning. In build 13, photographs can also stay on the device after an interrupted reconstruction, or when a model cannot be converted to OBJ, PLY or STL, until you resume building, keep the model or discard them; see Retention and deletion below. Existing records from retired capture modes may also contain previously retained depth observations, source photographs or calibrated camera poses; those records and files are preserved until you delete them. A facial model or photograph may identify a person even when its case label does not. Obtain the subject’s informed consent and follow your professional data-handling obligations.

The app has no patient account, advertising or tracking SDK, developer-operated scan server, cloud reconstruction service, or automatic scan upload. Capture, reconstruction and local storage occur on the device. The developer does not receive your scans simply because you use the app.

## Device storage and permissions

The app requests camera access for rear-camera captures you initiate in Object or Face mode. It does not offer front-camera capture or Gaussian capture/training. You can revoke access in iPhone Settings. Saved scan storage uses iOS file protection and is excluded from operating-system backups. Protection depends on the device and lock state; it does not prevent screenshots or disclosure from an unlocked device. In build 13, a cover hides the screen when you leave the app, so the App Switcher does not show scans or labels; it does not lock the app or protect an unlocked device in someone else's hands. Keep needed exports before deleting the app.

## Languages and translation

The interface supports English, Spanish, French, German, Italian, Brazilian Portuguese, Simplified Chinese, Traditional Chinese, Japanese, Korean, Hindi, Arabic, Indonesian, Turkish, and Vietnamese. Russian is not bundled. The app follows the supported system language or per-app language setting, with English fallback.

Interface translations are bundled and work offline. The app does not send scans, photographs, case labels, file names or other private content to a translation service. It does not download a translation model. Changing language does not rewrite saved names, stored scan data, measurements or technical export identifiers.

## Exports and sharing

Sharing is initiated by you through the iOS share sheet. You choose the recipient, application or provider, whose privacy, retention, backup and synchronization rules then apply. Files copied to a cloud provider may upload according to that provider’s settings. Exported geometry and photographic textures may contain sensitive or identifying information. Model exports can include their required image textures. Legacy splat/CAD exports omit any separately retained source photograph dataset; exported representations are still potentially identifying. If you kept photographs for a scan, **Photo set for Mac (ZIP)** shares them after a confirmation: every kept capture file under its generated name, a technical manifest with scan details, photograph count, total file size and generated file names (without the case label), and reconstruction notes. The ZIP is named from the scan ID. Exported copies are outside the app and must be deleted where you shared them.

An OBJ, PLY or STL export is a ZIP containing the model file and any required material and texture images, a READ-ME.txt with units and handling notes, and a scan-manifest.json with technical details: a random scan ID, capture mode and subject, the date and time the scan was saved, the iPhone model identifier and iOS version recorded at that time, units, coordinate system, vertex and triangle counts, capture-quality counts and warnings, scale status, and internal format fields such as the record schema version. Legacy splat exports include similar splat-manifest.json and SPLAT-READ-ME.txt files. An original USDZ export is the unchanged reconstructed model file. Export file names are built from the random scan ID. Build 13 keeps the case label you enter in the app’s library on your iPhone and does not write it into exported files or their names. The earlier submitted version 1.0 (12) and earlier distributed builds include the case label as the `name` value in scan-manifest.json and splat-manifest.json; review or delete those exported copies if needed. Earlier development copies may report 1.0 (12) while using newer source, so retain their source commit to identify their export behavior.

## Retention and deletion

In build 13, a reconstruction that finished but has not been saved is kept as an unsaved capture in the protected library, without its case label, until you save or discard it from the library. An unsaved capture that cannot be opened, including any photographs kept with it, stays until you choose Discard damaged captures in the library or remove the app. Unfinished captures can temporarily retain photographs and reconstruction checkpoints. In build 13, if reconstruction stops after capture has finished (for example, the app moves to the background, the device becomes too warm or the reconstruction reports an error), or the finished model cannot be converted to OBJ, PLY or STL, the photographs and checkpoints stay in the protected, backup-excluded temporary folder. They are removed when you discard them, start a new capture, leave the capture screen, keep the model or finish building, unless you chose Keep photographs for Mac reconstruction, in which case they stay with the saved or unsaved scan. If the app is closed first, they remain until the abandoned-folder cleanup described below. On cancellation, the app waits for native processing to stop before removing those files. If removal fails, it reports the failure and retains the files for a cleanup retry. Interrupted or recently modified work can remain locally until cleanup can safely complete.

Temporary export files are removed when the share sheet reports completion or dismissal. In build 13, swiping the share sheet away also schedules removal after a 60-second grace period. If the app is interrupted before cleanup finishes, eligible temporary capture and export folders older than 24 hours are checked during a later library opening. Cleanup preserves recent, unreadable or otherwise unsafe-to-remove files; 24 hours is not a guaranteed deletion deadline. Incomplete local save stages can also remain until recovery succeeds or you remove the app.

Saved scans remain locally until you delete them. Open the scan and use Scan actions → Delete scan to remove its saved model and retained capture data from the app. Deleting the app removes its local library. Neither action removes exported copies, recipient copies, or files in another app or provider. Manage those copies separately. The developer has no remote copy from which to recover scans and cannot remotely delete data held only on your device.

## Siri, Shortcuts and Spotlight

Only the bundled public capture guides and generic app navigation are exposed. Patient scans, case labels, photographs and geometry are excluded. Siri requests and information you choose to share with Apple’s system services follow your Apple settings and Apple’s privacy terms. Availability and recognition of spoken requests depend on Apple’s language support.

## Diagnostics and support correspondence

Capture diagnostics are created locally. Share diagnostics opens the system share sheet; no report is sent automatically. The report includes app version/build, iPhone model and iOS version, capture timing and photograph counts, the chosen Object or Face subject and reconstruction mode, camera readiness, processing and thermal state, and recent diagnostic events. It excludes photographs, facial geometry, case labels and file paths. Review a report and its destination before sharing.

If you contact support, we receive your email address, message, and any attachments you choose to send. We use correspondence to respond and investigate the issue, retaining it only as needed for that purpose or applicable legal obligations. Contact the same address to request access, correction or deletion of correspondence we hold. Do not send patient identifiers, facial images, scans or clinical records by ordinary support email or public GitHub issues. Apple may provide crash or usage diagnostics according to your system sharing settings.

## This policy online

In build 13, the in-app **Privacy and storage** view links to this policy and to the support page. They open in your web browser; the app itself makes no network request.

The developer adds no advertising, tracking scripts or cookies to this policy page. Hosting providers may process connection data such as IP addresses under their own privacy terms. This policy and its date will be updated when relevant data practices change.
