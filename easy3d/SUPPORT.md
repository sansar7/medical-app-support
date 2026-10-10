# Dental 3D Support

Updated October 9, 2026 for the prepared Dental 3D 2.0 update. The import, file-color, camera, and project-restoration improvements described below require version 2.0 or a build containing those changes. Earlier installed versions can behave differently; publishing these instructions does not update your app.

Email: **sansargupta10@gmail.com**

Supported platforms: iOS/iPadOS 17 or newer and macOS 15 or newer on Apple silicon (M-series). Intel Macs are not supported.

For a problem report, include the Dental 3D version/build, device model, OS version, file format, and the steps that led to the issue. A screenshot of the error can help. Do not send patient files or private dental or medical information. Use a synthetic or de-identified example only when needed to explain a file-format issue.

## Send feedback from the app

Open **Settings → Report a Bug or Request a Feature** and choose Bug Report, Crash Report, or Feature Request. Describe the issue or suggestion, then review the included app/version/build, OS, and platform information. **Open Email** prepares a draft addressed to the support email above; review and send it in your email app. The app sends nothing automatically and attaches no models, files, screenshots, identifiers, or crash logs. For a crash report, describe what happened before the app closed.

If no email app opens, or the report is too long for an email link, use **Copy Report** and **Copy Email Address**, then paste into your preferred email service. Feedback drafts are not saved in Dental 3D; closing a draft with text asks whether to discard it. A draft already opened in an email app or copied remains there.

## Opening models

Choose Open in the app, select a supported local model, or share a file from Files/Finder. For OBJ/WRL textures, select companion files together or place the complete model and companions in a ZIP archive. Files from iCloud Drive or another provider may need to finish downloading first. Supported formats include STL, OBJ/MTL, PLY, a bounded 3MF core subset, WRL, OFF/EOFF, XYZ variants, ASC, and ZIP archives containing those formats. See the app's Help for format and measurement guidance. Unsupported formats and files that exceed device resource limits report an import error.

For OBJ files with several included MTL libraries, the app looks for a usable diffuse texture in declaration order. An included material filename containing spaces takes precedence over splitting that name into separate libraries. Dental 3D displays one diffuse texture per imported OBJ; separate material groups, procedural maps, and MTL material colors are not reproduced. Missing companions appear as import notes while geometry can still open.

If an import reports incomplete geometry, export a repaired or triangulated model from the source application. PLY files that declare faces without a supported vertex-index list are rejected. Large selections and ZIPs share the same file-count and resource limits. Try a smaller selection or lower-resolution export when a limit is reported; the app’s Help explains the supported format subsets and resource limits.

## File colors

Choose the model's file-color appearance to use imported colors and textures, or apply a tint to override them. Explicitly white source colors remain white. Newly saved projects preserve whether source colors were supplied; older projects whose white buffers lack that information retain the earlier tint behavior. Reimport the original model and save a new project to preserve explicitly white source colors in that case.

## Public guides and Siri

Open the bundled guide from Help or use the app's Siri/Shortcuts actions to open, read or search its nine public topics. The five App Shortcuts include Open 3D Workspace and Reset 3D View. Reset only centers an active, ready workspace and refuses unfinished measurements/drawings, file operations and modal dialogs. Private model contents, annotations and measurements are not indexed or returned by guide actions. Siri and Spotlight availability depend on the device, OS and system settings.

## Default opening app

Install the current app, then select a supported model in Finder and choose **Get Info → Open with → Dental 3D → Change All**. Repeat for each model format. In the app, **Set Up…** opens instructions; **Not Now** dismisses the welcome offer, and Settings keeps the instructions available. This is the standard [macOS default-app workflow](https://support.apple.com/guide/mac-help/mh35597/mac). If an OBJ or WRL uses companion materials/textures, open the complete set together or use a ZIP.

On iPhone/iPad with iOS/iPadOS 26 or newer, touch and hold a supported model in Files, choose **Get Info → Always Open With → Dental 3D**, then confirm the file-type choice. The app provides instructions and does not change system associations itself. Earlier supported iOS versions can use Open or the share sheet.

## Saved work

Save a Dental 3D project to preserve models, annotations, measurements, appearance, and saved views together. Reopening a project restores the document's saved annotations and measurements for its included models and saved views for its exact scene. Newer cached records in those scopes are replaced, so save current work before reopening an older project. Records belonging to other models or scenes remain available.

Saved cameras retain their projection and framing, including immediately after Reset to Center or a standard-view change. A wide-screen saved view can crop on a narrow display; use Reset to Center to fit the current viewport. Preferences, measurements, views, and annotations can be cleared from Settings. Project files are managed separately in Files or Finder.

## Measurements

Verify the source scale and alignment before interpreting a measurement. Readout precision does not establish clinical accuracy. Clinical or diagnostic suitability has not been established by the engineering tests in this repository.

## Picture and video exports

Use the Export preview to check framing and annotation visibility before saving. If HEIC encoding is unavailable, choose JPG. Large exports depend on available device resources; choose a smaller output size if an export cannot finish. Canceling or failing an export does not publish a partial output. Visible model content and annotations remain in exported media, so review them before sharing.

## Privacy

The complete [privacy policy](PRIVACY_POLICY.md) is also available in Settings. Support correspondence is handled as described there.

## Languages and translation feedback

The app bundles English, Spanish, French, German, Italian, Brazilian Portuguese, Simplified Chinese, Traditional Chinese, Japanese, Korean, Hindi, Arabic, Indonesian, Turkish, and Vietnamese. It follows the system preferred-language order and supported per-app language settings, with English fallback. Russian is no longer bundled. Reopen the app after changing its system language. Bundled UI and app-authored help work offline; imported content, filenames, patient data, annotations, and saved identifiers are not translated. The language choice does not change measurements, physical geometry, or file formats.

English is the primary language of Dental 3D. Translations into other languages may be inaccurate; this notice is also available in **Settings → Language and translations**. Verify unfamiliar measurement and file-format wording against the English guidance.

For a translation or layout issue, include the app version, OS version, selected language/region, screen name, exact app-authored wording, and the expected wording. Use a synthetic example and remove private content from screenshots. Siri language availability and external support pages can differ from the bundled interface. Software layout checks and terminology review do not establish clinical validation or independent native-speaker review of every translation.
