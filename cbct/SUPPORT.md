# Dental CBCT Studio support

Updated October 14, 2026 for the current native iPhone, iPad, and Apple-silicon Mac source. The Surface Export and Endo refinements described here require a build made from the October 13-14 source or later. The 1.0 (7) submission built from commit 62f8110 does not include those refinements; the same version number on a local build does not establish source parity. A GitHub or support-page update does not update an installed app.

## Endo

The Endo workspace uses bundled STSR26 inference on the device, with no separate
runtime or server. Select a tooth region and review the tooth and pulp masks
against all three acquired slice planes. Optional enhancement appears only while
navigating; painting, erasing, and placing canal points return to the acquired
single slice with an **Original · editing** label. Use **Show Original** for
immediate comparison while navigating. Manual trace length is not a clinical
working length. Tooth and pulp surfaces follow the Surface Export **Surface**
setting. Save State retains masks, traces, and notes; restored surfaces
require review before export. Notes may identify a person. See the
[Endo workflow](docs/ENDODONTICS.md).

Painting and erasing connect the points of a drag with the selected physical
brush radius, including on scans with unequal voxel spacing. One stroke has
one undo step and stays inside the selected region. Changing the slice,
region, source or brush settings before release discards the pending stroke.
Very long gestures can also be rejected; release and start a shorter stroke.

## Contact

Contact Sansar Gupta at **sansargupta10@gmail.com**. Choose **Report a Bug or Request a Feature** in Viewer Controls (Settings), Review & Help, Privacy & Licenses, or the Mac Help menu. Select Bug Report, Crash Report, or Feature Request, describe the issue, and choose **Open Email** to review and send a draft. The form includes app version/build and OS/platform only. **Copy Report** and **Copy Email Address** work when email is unavailable or a report is too long for an email link. Reports are never sent automatically; crash reporting is a description of a previous crash, with no automatic crash-log collection or attachments. Privacy & Licenses also includes the complete offline privacy policy.

Find the app version and build at the top of **Privacy & Licenses** or **Quick Start & Help**. Include both, your OS version, device model, steps to reproduce and any error message. Prefer an anonymous synthetic sample. Do not send patient names, identifiable screenshots, full DICOM studies, saved states, review files containing patient-related anatomy, or clinical records in ordinary support email. The developer receives information you choose to include; contact the same address to request deletion of correspondence, subject to applicable retention obligations.

## Opening a study

The app supports native iOS/iPadOS 18+ and Apple-silicon macOS 15+. Choose **Open CBCT Study** / **Choose DICOM File or Folder** and select one DICOM series folder or a `.dcm`/`.dicom` file. Supported transfer syntaxes are Implicit VR Little Endian, Explicit VR Little Endian, Explicit VR Big Endian, Deflated Explicit VR Little Endian, and RLE Lossless. Pixels must be single-sample MONOCHROME1 or MONOCHROME2 with 8-bit or 16-bit integer data.

Enhanced multi-frame files need valid per-frame patient positions, orientation, spacing, and consistent rescale values describing a regular spatial stack. A single-frame file also needs declared slice extent. JPEG, JPEG-LS, JPEG 2000, other compressed transfer syntaxes, color images, PACS networking, and a series-selection browser are not supported. A rejected study needs a compatible export preserving physical geometry from its source system. Model proposals and measurements are not clinically validated for diagnostic use.

If an import reports that slice positions drift from a regular spatial grid, obtain a new compatible export from the source system with consistent patient geometry. The check covers the whole stack, not just each neighboring pair. Do not change geometry tags to make a study pass.

**Quick Start & Help** is available offline, including before a study is open. It explains MPR, Slice & Panorama, Endo, Surface Export, and Media Export. Use the slice slider or the previous/next slice buttons on every platform. On iPhone and iPad, open Viewer Controls from the toolbar. On Mac, source panes also support scrolling and the app offers keyboard/menu commands; the Distance tool is **⌥⌘L**.

## Super Resolution and Metal Artifact Reduction

In **Viewer Controls → Display**, **Super Resolution** uses BoneEnhance Baseline 2D and **Metal Artifact Reduction** uses RISE-MAR Dental Preview. Both are optional, start off, and run on the device using bundled models. The selected options are retained in saved states and reviews; older files open with both off. There is no model download or upload of scan data.

These options process the visible MPR slices/slabs, arch scout, simulated panorama, tooth cross-sections, and Endo slice panes in the background. The acquired image stays visible while processing; a completed processed view is labeled **Enhanced preview**. **Show Original** instantly compares the same cut with its acquired image while retaining the processed result. This temporary comparison choice is not saved. Turn both options off or choose **Reset Display** to disable enhancement. Scrolling or changing views can restart processing. If a model is unavailable, a view is too large, or available memory is insufficient, the original view remains usable and the app explains the problem. **Clear Memory** releases enhancement models and processed views while retaining the selected options; a subsequent view interaction may process the view again.

The corrections are deliberately limited, so broad streaks may remain and the visible difference can be subtle. Compare the same cut and display settings; a visible change does not establish recovered anatomy. Enhancement is experimental and may alter anatomy and grayscale. A denser display grid does not prove improved diagnostic resolution, and CBCT gray values may differ from the model's training inputs. Source voxels, physical measurement geometry, ROI statistics, segmentation, and 3D rendering remain based on acquired data. PDF, annotated image, DICOM Secondary Capture, and media exports exclude enhancement previews. Model licenses and attribution are available offline in **Privacy & Licenses → Image enhancement models**. Clinical accuracy and physical-device performance are not established by the software checks.

## Exporting an enhanced CT copy

Choose **Export → Export Enhanced CT…**, select Bone Enhance and/or Metal Artifact Reduction, and choose a destination folder outside the open study's folder (a copy saved inside it would compete with the source series when that folder is reopened, so the app refuses it). This separately processes every axial slice and saves a derived DICOM series on the original voxel grid. The progress view reports completed slices; cancellation waits for the current calculation to finish and removes the incomplete output. If the app quits or stops during an export, a visible `…-incomplete` folder may remain; delete it, or the next export to the same folder removes it once it is a day old. **Open Saved CT** opens the completed copy with live enhancement off.

The copy includes available source patient/study information and processed grayscale. Retain the original scan for comparison and review identifiers before sharing. The processed values are not calibrated HU, and the copy is not a validated diagnostic reconstruction. Regular PNG, PDF, DICOM Secondary Capture, and media exports continue to use source data. On narrow screens and at large text sizes, scroll the export details; the destination and cancel/done controls remain available.

## Measurements

Cross-section measurements belong to the current dental arch. Switching jaw, **Use Automatic**, **Redraw Arch** from any of its buttons, or clearing the arch asks before those measurements are deleted. Cancel keeps the arch and its measurements. **Undo Last** cancels a measurement in progress, restores what the last row Delete or **Clear All** removed (Clear All asks first), and otherwise removes the newest measurement. Measurements are not clinically validated.

## Surface Export

Review the jaw, tooth, and IAN labels against the source slices, correct them, and confirm each surface before exporting STL files. The **Surface** setting is **Smooth** by default: interior spaces are filled, loose fragments removed, and each structure is smoothed and simplified into a closed solid for viewing and 3D printing. **Exact voxels** builds the source-grid label surface without filling, smoothing or simplification, and uses coarser sampling when memory is low; its STL files are not closed solids (they can have open edges and many separate pieces), so repair them before 3D printing. Changing the setting rebuilds the surfaces and clears their reviews. The Surface setting also applies to Endo tooth and pulp surfaces and clears an Endo review. With Smooth surfaces, **Combine into one STL** writes two or more reviewed structures to one STL file with one sidecar: a jaw and its teeth fuse into one solid, while upper and lower structures stay separate solids unless their teeth touch. Smoothing does not add anatomy the model did not label. Automatic segmentation is not validated for diagnostic use.

The **General surface** panel builds one surface of the whole study from the **Bone threshold**, without the model, and follows the same Surface setting; changing it there also clears segment and Endo reviews. A Smooth General surface is one closed threshold surface: teeth are not separated from the bone, thin bone can look pitted, and marrow that opens into the nerve canal or a foramen can stay hollow. The threshold starts from the study's own gray-value levels unless you move the slider or a saved state sets it. **Export STL** saves `CBCT-general-surface.stl`; **Save sidecar** then optionally saves a JSON file with the threshold and processing figures, without patient or study details. On iPhone and iPad the General surface shares the device's surface memory limit with the segment surfaces kept for the Segments panel, which stay with their reviews; when the General panel says they use part of that limit, removing segment surfaces from the 3D view on the Segments panel and rebuilding gives the General surface more room. This surface has no review step and is not validated for diagnostic use.

Cancelling or changing studies can wait for active surface work to drain;
long cavity and component traversals check cancellation during processing.
For Smooth surfaces, the reported simplification error covers the bounded
collapse passes, not the separate minimum-spacing corrections. Triangle-target
status describes the final surface after both stages.

## Images and video

Media Export creates still images and H.264 video from its captured viewer
settings. **Use Viewer Settings** takes a fresh snapshot. **3D Bone Surface**
uses the General surface built in Surface Export. If a rebuild finishes while
an export is running, that export keeps its captured surface and the preview
refreshes after it finishes or is cancelled. Review the refreshed preview
before exporting again. Leaving the workspace or changing studies cancels work;
existing output files are replaced only after a complete export is ready.

## Saving and memory

**Save State** writes `Dental-CBCT-State.cbctstate` in the selected writable CBCT folder. Reopening that folder automatically restores the last explicitly saved state only after checking the full source content and geometry. Use **Save State Copy** for a different destination, a read-only folder, or a single-file study. To open a saved-state copy, select it and provide the matching original DICOM source when prompted. Save explicitly after changes; there is no autosave, recent-folder reopening, or automatic study restoration at app launch.

A saved state is matched to the source pixels and geometry. Valid established spacing remains unchanged; if an older import represented a long decimal-rounded stack with incorrect spacing, the corrected geometry may reject that older state. Reopen the original source, review the work, and save a new state.

Saved states retain views, zoom, measurements, arches, canal traces, accepted edits, and display settings. They exclude source pixels, DICOM patient demographics and identifiers, paths, imported provenance text, media captions/timelines, generated meshes, and export approval. User-authored Endo notes and tooth designations are retained and may identify a person. Saved geometry is still study-specific and sensitive. Keep the original DICOM source: a state file is not a scan backup. The older **Save Review / Open Review** workflow remains available; `.cbctreview` files include a series identifier and sensitive anatomical work and also require the matching original source.

**Clear Memory** in Viewer Controls releases generated segmentation, surfaces, reformat caches, and the inference model after active work finishes. It keeps the loaded source and accepted work and returns to MPR with its 3D view unloaded. Choose **Load 3D View** to resume; regenerate and explicitly review segmented surfaces before exporting again. It does not discard the loaded study or free every allocation.

**Close Study** clears the visible study immediately. If you then open another study, “Finishing current study work” means canceled processing is still releasing its source buffers before replacement loading starts. This avoids overlapping large study allocations. **Cancel** in the loading view stops reading a folder that was chosen by mistake; the study that was already open stays open.

## Siri and Spotlight

**Search Guide & Siri Topics** opens eleven public app guides, including image enhancement. Siri and Shortcuts can open, search, and read these guides; Spotlight indexes only bundled public guide content. **Reset MPR View** requires the active MPR workspace, a loaded study, and no pending operation, drawing, or measurement. It resets pane focus and the MPR camera without changing records or approving an export. Patient data, filenames, pixels, measurements, saved states, and reviews are never donated to this public catalog. Availability depends on device, OS, language, and Apple settings.

Public support: https://sansar7.github.io/medical-app-support/cbct/index.html

Privacy policy: https://sansar7.github.io/medical-app-support/cbct/privacy.html

## Languages and translation feedback

**Viewer Controls → Language and translations** states that English is the primary language and translations into other languages may be inaccurate. A corrected translation is not independent native-speaker or clinical certification.

The app bundles English, Spanish, French, German, Italian, Brazilian Portuguese, Simplified Chinese, Traditional Chinese, Japanese, Korean, Hindi, Arabic, Indonesian, Turkish, and Vietnamese. It follows the system preferred-language order and supported per-app language settings, with English fallback. Russian is no longer bundled. Reopen the app after changing its system language. Bundled UI and app-authored help work offline; imported content, filenames, patient data, annotations, and saved identifiers are not translated. The language choice does not change measurements, physical geometry, or file formats.

For a translation or layout issue, include the app version, OS version, selected language/region, screen name, exact app-authored wording, and the expected wording. Use a synthetic example and remove private content from screenshots. Siri language availability and external support pages can differ from the bundled interface. Software layout checks and terminology review do not establish clinical validation or independent native-speaker review of every translation.
