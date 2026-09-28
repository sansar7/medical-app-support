# Dental CBCT Studio support

Updated September 27, 2026 for the current native iPhone, iPad, and Apple-silicon Mac source.

## Contact

Contact Sansar Gupta at **sansargupta10@gmail.com**. Choose **Report a Bug or Request a Feature** in Viewer Controls (Settings), Review & Help, Privacy & Licenses, or the Mac Help menu. Select Bug Report, Crash Report, or Feature Request, describe the issue, and choose **Open Email** to review and send a draft. The form includes app version/build and OS/platform only. **Copy Report** and **Copy Email Address** work when email is unavailable or a report is too long for an email link. Reports are never sent automatically; crash reporting is a description of a previous crash, with no automatic crash-log collection or attachments. Privacy & Licenses also includes the complete offline privacy policy.

Find the app version and build at the top of **Privacy & Licenses** or **Quick Start & Help**. Include both, your OS version, device model, steps to reproduce and any error message. Prefer an anonymous synthetic sample. Do not send patient names, identifiable screenshots, full DICOM studies, saved states, review files containing patient-related anatomy, or clinical records in ordinary support email. The developer receives information you choose to include; contact the same address to request deletion of correspondence, subject to applicable retention obligations.

## Opening a study

The app supports native iOS/iPadOS 18+ and Apple-silicon macOS 15+. Choose **Open CBCT Study** / **Choose DICOM File or Folder** and select one DICOM series folder or a `.dcm`/`.dicom` file. Supported transfer syntaxes are Implicit VR Little Endian, Explicit VR Little Endian, Explicit VR Big Endian, Deflated Explicit VR Little Endian, and RLE Lossless. Pixels must be single-sample MONOCHROME1 or MONOCHROME2 with 8-bit or 16-bit integer data.

Enhanced multi-frame files need valid per-frame patient positions, orientation, spacing, and consistent rescale values describing a regular spatial stack. A single-frame file also needs declared slice extent. JPEG, JPEG-LS, JPEG 2000, other compressed transfer syntaxes, color images, PACS networking, and a series-selection browser are not supported. A rejected study needs a compatible export preserving physical geometry from its source system. Model proposals and measurements are not clinically validated for diagnostic use.

If an import reports that slice positions drift from a regular spatial grid, obtain a new compatible export from the source system with consistent patient geometry. The check covers the whole stack, not just each neighboring pair. Do not change geometry tags to make a study pass.

**Quick Start & Help** is available offline, including before a study is open. It explains MPR, Slice & Panorama, Surface Export, and Media Export. On iPhone and iPad, use the slice slider or previous/next slice buttons and open Viewer Controls from the toolbar. On Mac, source panes also support scrolling and the app offers keyboard/menu commands.

## Saving and memory

**Save State** writes `Dental-CBCT-State.cbctstate` in the selected writable CBCT folder. Reopening that folder automatically restores the last explicitly saved state only after checking the full source content and geometry. Use **Save State Copy** for a different destination, a read-only folder, or a single-file study. To open a saved-state copy, select it and provide the matching original DICOM source when prompted. Save explicitly after changes; there is no autosave, recent-folder reopening, or automatic study restoration at app launch.

A saved state is matched to the source pixels and geometry. Valid established spacing remains unchanged; if an older import represented a long decimal-rounded stack with incorrect spacing, the corrected geometry may reject that older state. Reopen the original source, review the work, and save a new state.

Saved states retain views, zoom, measurements, arches, canal traces, accepted edits, and display settings. They exclude source pixels, patient names, DICOM identifiers, paths, arbitrary provenance text, media captions/timelines, generated meshes, and export approval. Saved geometry is still study-specific and sensitive. Keep the original DICOM source: a state file is not a scan backup. The older **Save Review / Open Review** workflow remains available; `.cbctreview` files include a series identifier and sensitive anatomical work and also require the matching original source.

**Clear Memory** in Viewer Controls releases generated segmentation, surfaces, reformat caches, and the inference model after active work finishes. It keeps the loaded source and accepted work and returns to MPR with its 3D view unloaded. Choose **Load 3D View** to resume; regenerate and explicitly review segmented surfaces before exporting again. It does not discard the loaded study or free every allocation.

**Close Study** clears the visible study immediately. If you then open another study, “Finishing current study work” means canceled processing is still releasing its source buffers before replacement loading starts. This avoids overlapping large study allocations.

## Siri and Spotlight

**Search Guide & Siri Topics** opens nine public app guides. Siri and Shortcuts can open, search, and read these guides; Spotlight indexes only bundled public guide content. **Reset MPR View** requires the active MPR workspace, a loaded study, and no pending operation, drawing, or measurement. It resets pane focus and the MPR camera without changing records or approving an export. Patient data, filenames, pixels, measurements, saved states, and reviews are never donated to this public catalog. Availability depends on device, OS, language, and Apple settings.

Public support: https://sansar7.github.io/medical-app-support/cbct/index.html

Privacy policy: https://sansar7.github.io/medical-app-support/cbct/privacy.html
