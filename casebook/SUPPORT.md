# Casebook Support

Casebook is a personal dental treatment tracker for dentists and dental students on iPhone, iPad, and Mac. It does not replace dental notes, the official patient record, or practice management software.

## Contact

Email Sansar Gupta at [sansargupta10@gmail.com](mailto:sansargupta10@gmail.com).

Include your Casebook version and build number, device model, operating-system version, the steps that led to the problem, and the error message. Do not send patient names, chart numbers, identifiable case photos, clinical records, or screenshots containing patient information. Reproduce problems with an alias or the fictional examples whenever possible. Public GitHub issues are visible to other people when a repository is public.

## Opening your casebook

Use the device authentication prompt to unlock Casebook. If authentication is unavailable, unlock the device and check that a device credential is configured. Canceling authentication leaves the app locked. Restarting the app does not bypass authentication. Release builds ignore developer demo arguments.

If saved cases cannot be opened, the app keeps the existing saved file. Retry after unlocking the device. Do not erase the app's storage or Keychain entries to troubleshoot: the device-only key is needed to read the local casebook. The developer cannot recover a missing encryption key or your archive passphrase.

On Mac, closing the main window leaves Casebook running. Choose **Window → Show Casebook** or press **Command-0** to open it again.

## Finding cases without an appointment

**Your cases → Unplanned** shows open cases in progress, healing or maintenance, plus open cases with a recorded start date on or before today, when no appointment is recorded on that case. A patient-level appointment, task deadline or milestone date does not schedule an individual case. Past case appointments remain visible for review until updated or removed.

## Backups and recovery

Use **Backup & CSV → Archive or restore records and photos** for a complete passphrase-protected `.casebook` backup. Store the passphrase separately. Keep the app open while preparing large archives. On another device, choose the archive, enter its passphrase, review conflicts, and import. Existing records are kept when patient, reference, or nested record IDs conflict.

Use **Settings → Recently Deleted** to restore a deleted patient. Records do not expire automatically. Permanent deletion also attempts to remove associated encrypted photos; existing exports and shared copies must be removed separately.

CSV backups are unencrypted and exclude photographs and Recently Deleted. Analysis exports may contain identifying free text even when name/reference fields are omitted. Use the encrypted archive for full recovery.

## Photos

Choose **Choose from Photos** to select existing images from your photo library, or **Choose files** to import image files. Casebook imports only the images you select. The system photo picker does not require full photo-library access. Imports are limited to 25 MB per original, 50 million pixels, and 30 photos or 250 MB of prepared images per batch. Save one batch before adding more. Source filenames and embedded metadata are removed from imported reference copies, but visible image content may still identify a person.

Saving an image to Photos requires add-only Photos permission. You can also use Share Image to choose a destination. Exported copies leave Casebook's encrypted storage and follow the destination's backup and synchronization settings.

## Reminders

Enable local reminders in Settings and permit notifications in system settings. Task reminders use 9 AM on the due date; appointment reminders use 30 minutes before the recorded time. Casebook schedules the next 60 future reminders when you open or save. Alerts contain generic counts; examples, completed tasks, and closed treatments do not create treatment reminders.

## Examples and outcomes

Settings can load 20 fictional evaluation patients. Loading a fresh log replaces both active and recently deleted examples and their photos, after confirmation. Personal patients and templates are kept. Restore missing examples preserves edited examples and skips references already in use.

Outcomes summarize your entered observations. Unreviewed records do not count as successful. A success percentage is not a survival estimate or a comparison of treatment effectiveness.

## Privacy

Read **Settings → Privacy → Privacy Policy** for the complete bundled policy, or the published policy associated with this support page. Patient data stays on your device unless you explicitly export or share it. There are no developer-operated patient accounts, analytics services, or automatic cloud synchronization.
