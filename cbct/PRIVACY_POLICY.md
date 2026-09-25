# Dental CBCT Studio Privacy Policy

Last updated: September 24, 2026

Developer: Sansar Gupta
Contact: sansargupta10@gmail.com

## Data stays under your control

Dental CBCT Studio processes the DICOM folders you choose on your device. This includes scan pixels, DICOM metadata (which may identify a patient), measurements, annotations, and segmentation masks. The app has no account, advertising, tracking, third-party analytics SDK, remote AI, or developer-operated upload service. The developer does not receive this data through the app, sell it, or use it for advertising. No patient studies or patient identifiers are indexed in Siri or Spotlight.

## Local storage and retention

The current study and review state are held during your session. Large volumes can use private temporary disk storage. Prepared exports use private temporary files and are cleaned up after use or on a later launch. Temporary file dates are read only to identify stale app-owned export files for cleanup. Closing a study clears its active review state; it does not erase your original files or any files you saved.

Save Review explicitly writes a .cbctreview JSON file at a location you choose. It contains the DICOM series identifier and geometry, arch curves, canal traces, measurements, segmentation edits, and display settings. It contains no scan pixels, patient demographics, source-folder path, or file-access bookmark. The series identifier and anatomy can still link a review to a person; treat review files as sensitive. Open Review requires the original matching DICOM series. There is no automatic review saving or recent-study history.

Save State explicitly writes Dental-CBCT-State.cbctstate into the selected CBCT folder; Save State Copy lets you choose another location. Reopening a selected folder restores its last saved state only after checking the complete source scan and geometry using a randomly salted content fingerprint. This format excludes DICOM identifiers, patient demographics, images, source paths, bookmarks, and free-text provenance. It includes display and view settings, measurements, arches, canal traces, and segmentation edits, which remain sensitive study-specific geometry. A state file is not an anonymized clinical record. The app holds folder access only for the open session and does not remember that location between launches. Clear Memory releases generated segmentation and 3D resources while preserving the source study and accepted edits in the current session; it does not delete saved files.

Saved states, reviews, images, videos, PDF reports, DICOM captures, and mesh exports are not encrypted by the app and remain wherever you choose to save them. Delete these files in Files or Finder when they are no longer needed. The app cannot delete copies you shared or copies held by another service.

## Sharing, backups, and permissions

You choose which folders to open and where to save exports through system file dialogs. Files in an iCloud Drive or another cloud-provider folder can sync under that provider's settings. Device or computer backups may contain app files under your system settings. This is separate from a developer-operated data collection service.

Exports may contain patient names, metadata, captions, or identifying details already present in image pixels. Turning off added patient labels is not full de-identification. Review every export and its destination before sharing. The app does not request camera, microphone, location, contacts, or photo-library access.

## Siri, Shortcuts, external links, and support

The Open Dental CBCT Studio shortcut opens the app and requires device authentication. Additional Siri and Shortcuts actions open, search, and read bundled public guide topics. Only those public topics are indexed in Spotlight. Onscreen context describes the visible workspace category or guide topic. Patient names, identifiers, study pixels, measurements, annotations, review files, and filenames are not indexed or donated. These actions do not diagnose scans, select patients, change studies, or approve exports. Apple controls how Siri and Shortcuts process your requests under your device settings and Apple's privacy policy.

Source and license links open external websites, whose operators may receive ordinary browser request data under their policies. Emailing support uses your chosen mail application. The developer receives information you choose to include in that message. Do not send patient data, identifiable screenshots, or full DICOM studies for ordinary support. Support correspondence is used to respond and investigate reported problems, and retained only while needed for those purposes or applicable legal obligations. Contact the email above to request access, correction, or deletion of correspondence we hold. The developer cannot retrieve or remotely delete studies or exports stored only on your device.

## Intended use

The app has not been validated for diagnostic use. This privacy notice does not replace professional judgment or establish regulatory clearance.

## Apple diagnostics

Apple may share diagnostics and usage statistics according to your sharing settings. Any reports we receive are used to improve reliability. See Apple's App Analytics & Privacy notice (https://www.apple.com/legal/privacy/data/en/app-analytics/).

## Visiting this policy online

This policy page contains no advertising, analytics scripts, or cookies added by the developer. When hosted on GitHub Pages, GitHub logs visitors' IP addresses for security. See GitHub's privacy statement (https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Changes to this policy

We will update this policy and its date when our data practices change. The current policy will be available with the app and on its published privacy page.
