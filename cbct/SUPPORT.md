# Dental CBCT Studio support

Updated October 26, 2026 for the current native iPhone, iPad and Apple-silicon Mac source. This guide describes builds containing the October 25 feature additions, October 26 reliability fixes, reorganized Viewer Controls and English-only resources. Those changes are not in the **1.1.1 (9)** binary submitted on October 15. The marketing version and build number alone do not establish source parity; [STATUS.md](STATUS.md) records the exact build, installation and publication evidence. Updating GitHub or this guide does not update an installed app.

The current source adds saved views, configurable PDF reports and CSV measurements; unsaved-work prompts and measurement Undo/Redo; arrows and text; Window/Level presets and 3D clipping; editable Endo canal points; model-uncertainty overlays and custom regions; JPEG Lossless import, a series picker and de-identified DICOM export; reviewed USDZ export; Universal/FDI numbers; optional recovery copies; and volume reorientation. The workflows below explain their controls and limits. The app is **not validated for diagnostic use**.

The October 26 fixes preserve existing work when reorientation fails or is cancelled, prevent stale recovery/save work from replacing newer edits, improve cancellation and memory use during import and export, and keep compact report and Endo controls usable. Synthetic and simulator checks are engineering evidence; they do not establish clinical accuracy or physical-device performance.

## Endo

The Endo workspace uses bundled STSR26 inference on the device, with no separate
runtime or server. Center the target on one tooth, select its region and review
the tooth and pulp masks against all three slice planes of the current study grid. Endo keeps
only the tooth at the target: neighbouring teeth and other predicted pieces are
removed, and the review lists the removed volume. If the tooth touches the
region boundary, enlarge the region and run again. Optional enhancement appears only while
navigating; painting, erasing, and placing canal points use one unenhanced
current-grid slice with an **Original · editing** label. Use **Show Original** for
immediate comparison with the unenhanced current-grid image while navigating.
After reorientation, that grid is resampled; **Show Original** does not return
to the acquisition. **Reset to Source** in Volume Orientation restores the
acquisition grid. Manual trace length is not a clinical
working length. Tooth and pulp surfaces follow the Surface Export **Surface**
setting. Save State retains masks, traces, and notes; restored surfaces
require review before export. Notes may identify a person. See the
[Endo workflow](docs/ENDODONTICS.md).

Painting and erasing connect the points of a drag with the selected physical
brush radius, including on scans with unequal voxel spacing. One stroke has
one undo step and stays inside the selected region. Changing the slice,
region, source or brush settings before release discards the pending stroke.
Very long gestures can also be rejected; release and start a shorter stroke.

Mask overlays update in the background for the selected tooth region; hidden
slice panes release their overlays. Cancellation also reaches component
cleanup, contact splitting, pulp closing and source-grid mapping. An active
calculation still needs to finish or reach a cancellation check before its
memory can be released.

## Contact

Contact Sansar Gupta at **sansargupta10@gmail.com**. Choose **Report a Bug or Request a Feature** in Viewer Controls (Settings), Review & Help, Privacy & Licenses, or the Mac Help menu. Select Bug Report, Crash Report, or Feature Request, describe the issue, and choose **Open Email** to review and send a draft. The form includes app version/build and OS/platform only. **Copy Report** and **Copy Email Address** work when email is unavailable or a report is too long for an email link. Reports are never sent automatically; crash reporting is a description of a previous crash, with no automatic crash-log collection or attachments. Privacy & Licenses also includes the complete offline privacy policy.

Find the app version and build at the top of **Privacy & Licenses** or **Quick Start & Help**. Include both, your OS version, device model, steps to reproduce and any error message. Prefer an anonymous synthetic sample. Do not send patient names, identifiable screenshots, full DICOM studies, saved states, review files containing patient-related anatomy, or clinical records in ordinary support email. The developer receives information you choose to include; contact the same address to request deletion of correspondence, subject to applicable retention obligations.

## Opening a study

The app supports native iOS/iPadOS 18+ and Apple-silicon macOS 15+. Choose **Open CBCT Study** / **Choose DICOM File or Folder** and select one DICOM series folder or a `.dcm`/`.dicom` file. Supported transfer syntaxes are Implicit VR Little Endian, Explicit VR Little Endian, Explicit VR Big Endian, Deflated Explicit VR Little Endian, RLE Lossless, and JPEG Lossless (Process 14, including the first-order prediction form, 1.2.840.10008.1.2.4.57 and .70). Pixels must be single-sample MONOCHROME1 or MONOCHROME2 with 8-bit or 16-bit integer data.

Enhanced multi-frame files need valid per-frame patient positions, orientation, spacing, and consistent rescale values describing a regular spatial stack. A single-frame file also needs declared slice extent. Lossy JPEG, JPEG-LS, JPEG 2000, HTJ2K, other compressed transfer syntaxes, color images, and PACS networking are not supported. When a folder holds more than one series with enough images to form a volume (at least three, and at least a quarter as many as the largest series), a **series picker** lists them with description, modality, image count, matrix and spacing and suggests the original scan (Image Type not DERIVED or LOCALIZER); **Cancel** abandons the import, and the choice is not remembered. A folder with one such series opens it directly, preferring an original scan over reformats, scout images and secondary captures. Viewer Controls notes how many other files were ignored. A clinic export folder already mounted in Finder (Go → Connect to Server) or added to Files (Connect to Server) can be selected like another folder. The operating system handles the share; the app has no PACS receiver, server login or remembered clinic location. A rejected study needs a compatible export preserving physical geometry from its source system. Model proposals and measurements are not clinically validated for diagnostic use.

If an import reports that slice positions drift from a regular spatial grid, obtain a new compatible export from the source system with consistent patient geometry. The check covers the whole stack, not just each neighboring pair. Do not change geometry tags to make a study pass.

Pixel Spacing must also remain consistent between slices, including when its
values are very small. If the app rejects differing spacing, obtain a compatible
export from the source system rather than editing calibration tags.

A short **Tutorial** opens the first time the app starts. Replay it from **Show Tutorial** on the welcome screen, in **Review & Help**, in Quick Start & Help, or in the Mac Help menu. The first time you open each workspace, a one-line tip appears under the workspace picker; **Got It** hides it and **Learn More** opens the matching help topic. **Quick Start & Help** is available offline, including before a study is open. It explains MPR, Slice & Panorama, Endo, Surface Export, Media Export, and Implants. Use the slice slider or the previous/next slice buttons on every platform. On iPhone and iPad, open Viewer Controls from the toolbar. On Mac, source panes also support scrolling and the app offers keyboard/menu commands; the Distance tool is **⌥⌘L**.

Viewer Controls puts **Display**, **Measurements**, **Saved Views** and **Save State** first while a study is open. Navigation and viewing options follow. **Image Enhancement**, **Volume Orientation**, **Preferences** and **Session & Memory** sit below the everyday controls; study information, privacy and feedback are near the bottom.

## Display, clipping and orientation

**Viewer Controls → Display** contains brightness, contrast, inversion and the **Default**, **Soft Tissue**, **Bone**, **Teeth** and **Full Range** presets. The presets come from this study's histogram and value range, not fixed Hounsfield-unit assumptions. With **Window/Level** selected (**⌥⌘W** on Mac), drag horizontally for width and vertically for level on MPR, the arch scout, panorama or cross-sections. This changes the display, not source pixels.

**Clip** on the MPR 3D tile crops its volume render using six faces or the current MPR slice positions. Media Export's **3D Volume / X-ray** can use that crop. It does not crop source slices, segmentation surfaces, measurements or voxel exports, and the crop is kept in saved display settings.

**Viewer Controls → Volume Orientation**, or **Tools → Reorient Volume…** on Mac, rotates a derived study grid by pitch, roll and yaw. **Suggest from Segmentation** provides an editable starting point. Review the preview, then confirm Apply: a completed replacement clears work anchored to the old grid, including measurements, arches, segmentation edits, Endo work and the implant plan, while retaining display settings. A failure or cancellation preserves the previous grid and its work. **Reset to Source** rereads and restores the acquisition grid; the original files must remain reachable. Until then, every workspace, including Endo, uses the resampled grid; Show Original only turns off enhancement for that grid. Save State keeps the angles and reconstructs that grid on restore. Resampling does not establish measurement accuracy. [Reorientation details](docs/VOLUME_REORIENTATION.md).

## Super Resolution and Metal Artifact Reduction

In **Viewer Controls → Image Enhancement**, **Super Resolution** uses BoneEnhance Baseline 2D and **Metal Artifact Reduction** uses RISE-MAR Dental Preview. Both are optional, start off, and run on the device using bundled models. The selected options are retained in saved states and reviews; older files open with both off. There is no model download or upload of scan data.

These options process the visible MPR slices/slabs, arch scout, simulated panorama, tooth cross-sections, and Endo slice panes in the background. The unenhanced current-grid image stays visible while processing; a completed processed view is labeled **Enhanced preview**. **Show Original** instantly compares the same cut with its unenhanced current-grid image while retaining the processed result. If the study was reoriented, this remains a resampled image; use Reset to Source to return to the acquisition. This temporary comparison choice is not saved. Turn both options off or choose **Reset Display** to disable enhancement. Scrolling or changing views can restart processing. If a model is unavailable, a view is too large, or available memory is insufficient, the original view remains usable and the app explains the problem. **Clear Memory** releases enhancement models and processed views while retaining the selected options; a subsequent view interaction may process the view again.

The corrections are deliberately limited, so broad streaks may remain and the visible difference can be subtle. Compare the same cut and display settings; a visible change does not establish recovered anatomy. Enhancement is experimental and may alter anatomy and grayscale. A denser display grid does not prove improved diagnostic resolution, and CBCT gray values may differ from the model's training inputs. Enhancement previews do not change the current study grid used for measurements, ROI statistics, segmentation and 3D rendering. That grid is acquired data before reorientation and resampled data after reorientation; the original acquisition files are unchanged. PDF, annotated image, DICOM Secondary Capture, and media exports exclude enhancement previews. Model licenses and attribution are available offline in **Privacy & Licenses → Image enhancement models**. Clinical accuracy and physical-device performance are not established by the software checks.

## Exporting an enhanced CT copy

Choose **Export → Export Enhanced CT…**, select Bone Enhance and/or Metal Artifact Reduction, and choose a destination folder outside the open study's folder (a copy saved inside it would compete with the source series when that folder is reopened, so the app refuses it). This separately processes every axial slice and saves a derived DICOM series on the original voxel grid. The progress view reports completed slices; cancellation waits for the current calculation to finish and removes the incomplete output. If the app quits or stops during an export, a visible `…-incomplete` folder may remain; delete it, or the next export to the same folder removes it once it is a day old. **Open Saved CT** opens the completed copy with live enhancement off.

The copy includes available source patient/study information and processed grayscale. Retain the original scan for comparison and review identifiers before sharing. The processed values are not calibrated HU, and the copy is not a validated diagnostic reconstruction. Regular PNG, PDF, DICOM Secondary Capture, and media exports continue to use source data. On narrow screens and at large text sizes, scroll the export details; the destination and cancel/done controls remain available.

## Exporting a de-identified copy

Choose **Export → De-identified DICOM…** and a destination folder outside the open study's folder. The app writes the open study again as uncompressed Explicit VR Little Endian CT images, one file per slice, with the identifying attributes it holds removed or emptied under the DICOM PS3.15 Basic Application Level Confidentiality Profile: patient name, ID, birth date and sex, dates and times, accession number, study ID, institution, referring/performing/operator names, series description, device identifiers and comments; private elements, curves and overlays are not carried over, and the study, series, image and frame-of-reference identifiers are replaced consistently within the export. Pixel values, geometry, rescale, window and pixel padding are unchanged; the output uses CT Image Storage with modality CT. Reset a reoriented volume to its source before exporting. The copy records Patient Identity Removed = YES with the de-identification method. **Text burned into the image pixels is not removed**; review the slices before sharing the copy. Cancellation removes the incomplete `…-incomplete` folder; one left by a quit or crash is removed by the next export to that folder once it is a day old.

## Measurements

Cross-section measurements belong to the current dental arch. Switching jaw, **Use Automatic**, **Redraw Arch** from any of its buttons, or clearing the arch asks before those measurements are deleted. Cancel keeps the arch and its measurements. **Undo** (⌘Z) and **Redo** (⇧⌘Z), also under Measurements in Viewer Controls, step through placements, row Deletes, **Clear All** (which asks first), handle and label drags, and label text, font and size edits in MPR, Slice & Panorama and the implant sections; the history holds up to 100 steps for the open study and is not saved. Measurements are not clinically validated.

**Arrow** and **Text** annotations carry no measured value. Arrow takes a tail and a head and an optional caption; Text asks for its text after one tap. Edit the text or caption under Measurements → Selected label. On the Mac, Arrow is **⌥⌘R** and Text is **⌥⌘K**. Labels are saved with states and reviews, drawn on PDF, image, DICOM SC and media exports, and listed in the report table (arrows only when they have a caption). Text you type may identify a person.

A very small oval ROI between sample centers reports the nearest current-grid or
cross-section sample. Its area still describes the drawn oval; a one-sample
value does not imply that the scan resolves anatomy at that area.

Panorama canal overlays omit points beyond either end of the drawn arch instead
of pinning them to the image edge. Review those canal portions on the source
slices or cross-sections. A cancelled canal-handle drag releases its old handle
so a later drag can begin normally.

## Surface Export

New studies start every segment at **100% opacity**. Restored studies retain saved opacity values.

Review the jaw, tooth, and IAN labels against the source slices, correct them, and confirm each surface before exporting STL files. The **Surface** setting is **Smooth** by default: interior spaces are filled, loose fragments removed, and each structure is smoothed and simplified into a closed solid for viewing and 3D printing. **Exact voxels** builds the source-grid label surface without filling, smoothing or simplification, and uses coarser sampling when memory is low; its STL files are not closed solids (they can have open edges and many separate pieces), so repair them before 3D printing. Changing the setting rebuilds the surfaces and clears their reviews. The Surface setting also applies to Endo tooth and pulp surfaces and clears an Endo review. With Smooth surfaces, **Combine into one STL** writes two or more reviewed structures to one STL file with one sidecar: a jaw and its teeth fuse into one solid, while upper and lower structures stay separate solids unless their teeth touch. Smoothing does not add anatomy the model did not label. Automatic segmentation is not validated for diagnostic use.

**Show model uncertainty** in **Surface Export → Labels** hatches the recorded voxels where the model's top two classes were closest. **Low**, **Medium** and **High** cover the lowest 5%, 10% and 20% of retained margins; **Next Uncertain Region** moves to the next region. This indicates model ambiguity, not a probability of error or a clinical finding, and is available only while the prediction retains those margins.

**Custom region** lets you paint and erase your own label on slices, then **Fill Between Slices** interpolates between two or more painted slices in the selected plane. Inspect every filled slice: interpolation follows the outlines, not the anatomy. The displayed volume is voxel count × voxel volume. Custom strokes and fills have their own Undo/Redo; their Smooth or Exact surfaces use the same review gate and STL export as other segments. Names and masks are kept in states/reviews and can be identifying; names are not written into STL files or sidecars. Custom regions are not drawn in Media Export.

**Export USDZ…** in the Segments panel saves the export-selected reviewed surfaces in their segment colors as one `.usdz` scaled to meters, optionally with the planned implants and schematic crowns (stock library crowns are never included). It opens in AR Quick Look on iPhone and iPad and in Quick Look on Mac. The same review gate and privacy notice apply as for STL; the file is a visualization, not a validated model.

**Tooth numbers** (Viewer Controls ▸ Preferences) chooses Universal (1–32) or FDI two-digit numbers for the Implants tooth chart, labels, readouts, the implant report and its export; the report names the convention. Plans and saved states keep Universal numbers. The first launch chooses Universal in the United States and FDI elsewhere.

**Colors** in the Segments panel chooses the segment palette: **Default**, **High Contrast**, **Colorblind-Safe**, or your own color for any segment. Colors apply to the 3D surfaces, the slice overlays, the legend in Viewer Controls and Media Export, and are remembered on this device for every study. **Reset Colors** returns to Default. Colors are not stored in Save State, reviews or STL files, and changing them never clears a review.

In the Segments and Endo 3D views, drag to rotate and drag with two fingers to pan. On Mac, pinch on the trackpad, use a mouse scroll wheel, or hold Option (⌥) while scrolling to zoom; a Magic Mouse scroll pans, so use ⌥-scroll to zoom with it. On iPhone and iPad, pinch to zoom; an iPad trackpad's two-finger scroll also pans. The reset camera button recenters the model.

Cancelling or changing studies can wait for active surface work to drain;
long cavity and component traversals check cancellation during processing.
For Smooth surfaces, the reported simplification error covers the bounded
collapse passes, not the separate minimum-spacing corrections. Triangle-target
status describes the final surface after both stages.

If voxel spacing would require a Smooth surface larger than the supported size,
preparation stops before making large allocations. Normal surface processing
is unchanged.

## Images and video

Media Export creates still images and H.264 video from its captured viewer
settings. **Use Viewer Settings** takes a fresh snapshot. **3D Bone Surface**
builds a threshold-derived bone surface in Media Export. Its Surface and Bone
threshold controls stay in that workspace; use Update Surface after changing
the threshold. This surface is available for images and videos. If a rebuild finishes while
an export is running, that export keeps its captured surface and the preview
refreshes after it finishes or is cancelled. Review the refreshed preview
before exporting again. Leaving the workspace or changing studies cancels work;
existing output files are replaced only after a complete export is ready.

## Saved views and reports

**Save Current View** (Viewer Controls → Saved Views, or View → Save Current View…, **⇧⌘B**, on Mac) keeps the workspace, slices, zoom, display window and 3D cameras under a name; tap a saved view to show it again, and rename, caption, reorder or delete it from its menu. **Export → Report (PDF)…** opens the report composer: choose US Letter or A4 and the sections (study header, current views, saved views as key images with their captions and measurements, a cross-section contact sheet of evenly spaced sections along the installed arch numbered on a panorama, the measurement table and notes). The title, the not-validated notice and page footers are always printed. **Measurements (CSV)…** writes the measurement table as a spreadsheet file. Source DICOM patient demographics are excluded. Text labels and arrow captions are included and may identify a person. Report notes and saved views are kept in Save State; the clinic header printed above the title stays in this device's preferences only. Measurements on contact-sheet sections are not drawn; the table lists them.

Report buttons adapt to narrow portrait windows. Saved-view names, captions and report notes remain editable study content; saving an older snapshot while you make further edits leaves the newer work marked Edited. Saved views recall their captured workspace and pane; Media Export and Endo 3D cameras and the selected implant are not captured. If a key image cannot be rendered, the report identifies that limitation instead of silently implying an image was included.

## Implants

The experimental **Implants** workspace is immediately after Endo in the workspace picker (**⌘6** on Mac) and supports full editing on Mac, iPad and iPhone using the CBCT. A source build containing this workspace is required; the submitted 1.1.1 (9) build does not include it. Its experimental-use notice appears the first time Implants opens on a device; the information button in the workspace header shows it again.

1. Wait for dental segmentation, then choose the jaw and review its arch. If the automatic arch is missing or unsuitable, draw one in Slice & Panorama.
2. Use the panorama and position slider to browse the arch. In the tooth chart, select **Implant**, choose a tooth site, then click the arch-perpendicular X-ray section. A crown is optional; select **Crown** to place one separately or place it first and propose an implant from its axis. Crown dimensions and automatic orientation remain editable starting values.
3. Adjust the implant's position, angle and size. Choose BioHorizons Tapered Pro (modeled from published dimensions with estimated details labeled), a generic body, or an implant-body STL imported under your own license. **Make Parallel to…** turns it parallel to another implant in the same jaw.
4. Inspect the implant and optional crown against the segmented maxilla and mandible in 3D, together with the CBCT sections. Jaw meshes reuse the current edited segmentation surfaces. The panorama and perpendicular section share the selected arch; tangential and axial views remain available for inspection. Expand a pane for a closer look, restore it to return to the layout, and use section measurements or editing handles as needed.

**Safety margin:** **Show safety margin** draws an operator-selected offset around every implant body, set separately at the sides and beyond the apex (0.5–4 mm): a translucent shell in 3D and dashed outlines in the X-ray views. Overlaps with another implant's margin, a traced canal or a segmented tooth are shaded. It is a display offset, not a validated safe distance.

**Readouts:** geometric measurements are shown against literature reference lines, never pass/fail results or recommendations. **Key Distances** come first: the distance to the nerve canal for a lower-jaw implant, or for an upper-jaw implant the distance to air or low-density bone as a sinus or nasal floor proxy (not a segmented sinus); the mesial and distal teeth (when DentalSegmentator teeth labels exist); the nearest implant; and facial and lingual bone at the crest. **Bone** adds the platform depth below each crest and bone thickness at mid-body and apex; **Neighbouring Implants** lists the mesial and distal implants in the same jaw with the angle between their axes; **Orientation** gives the implant's tilt from the site's occlusal axis and its angle to the crown axis; **Crown and Screw Channel** shows where the screw channel leaves the crown and the crown-to-implant ratio; **Grey Values Around the Implant** summarizes gray values in a shell around the implant. The crosshair button beside a readout shows where it was measured. Readouts refresh shortly after each edit. CBCT values are not HU unless calibrated. Implants starts or resumes segmentation and waits for it to complete before placement.

**Other workspaces:** MPR and Slice & Panorama show planned implants and crowns as display-only outlines. Turn them off with **Show Planned Implants** in Viewer Controls or the Mac View menu. **Show in MPR** and **Show in Slice & Panorama** open those workspaces with their planes through the selected implant.

**Saving and exports:** Save State and reviews keep implant and crown parameters and placements, the safety margin and measurements drawn in the implant views, never imported meshes or file names. Imported implant bodies retain only a salted digest for re-import. Export a PDF report with the disclaimer on every page, implant and schematic-crown STL surfaces, and a JSON file with volume and DICOM patient coordinates. Licensed stock crown meshes are never exported. Treat these files as sensitive.

The workspace does not create surgical guides, sleeves or drill protocols and does not recommend implants.

Implant visualization is an experimental feature. It is not a medical device, is not cleared or approved by the FDA and is not CE-marked, and it has not been validated for diagnostic use or treatment planning. Measurements are geometric readouts from the CBCT scan, its dental segmentation and the planned implant geometry, including any imported implant body file; they are not clinical recommendations. Clinical decisions must be made by a licensed clinician using cleared planning software.

## Saving and memory

**Save State** (Viewer Controls → Save State) writes `Dental-CBCT-State.cbctstate` in the selected writable CBCT folder. Reopening that folder automatically restores the last explicitly saved state only after checking the full source content and geometry. Use **Save State Copy** for a different destination, a read-only folder, or a single-file study. To open a saved-state copy, select it and provide the matching original DICOM source when prompted. Save explicitly after changes; there is no autosave into the CBCT folder, recent-folder reopening, or automatic study restoration at app launch. **Keep a recovery copy** (Viewer Controls ▸ Session & Memory, off by default) writes the same state content into the app's private storage about half a minute after your changes pause, at most once a minute, for the last three studies. When you open the same scan again and the copy is newer than the folder's saved state, the app asks whether to restore or discard it. Save State, Close Study, Discard, or turning the option off deletes the copy; it has the same contents and sensitivity as a saved state.

An **Edited** marker beside the workspace picker (and the window's edited dot on the Mac) shows that measurements, labels, arches, canal traces, segmentation edits, Endo work or the implant plan changed since the last Save State; display settings and navigation do not count. **Close Study**, opening a replacement study, opening a state or review over the current one, a file opened from the Finder or Files, and Quit on the Mac then ask whether to **Save State** (or **Save State Copy** when the study has no writable folder), **Discard** or **Cancel**. Clear Memory keeps the work and does not ask.

A saved state is matched to the source pixels and geometry. Valid established spacing remains unchanged; if an older import represented a long decimal-rounded stack with incorrect spacing, the corrected geometry may reject that older state. Reopen the original source, review the work, and save a new state.

Saved states retain views, zoom, measurements, arrows and text labels, arches, canal traces, accepted edits, display settings, saved views and report notes. They exclude source voxels, DICOM patient demographics and identifiers, paths, imported provenance text, media captions/timelines, generated meshes, and export approval. User-authored text labels, arrow captions, Endo notes, tooth designations, custom region names, saved view names and captions and report notes are retained and may identify a person; saved view thumbnails are small renderings of the scan. Saved geometry is still study-specific and sensitive. Keep the original DICOM source: a state file is not a scan backup. The older **Save Review / Open Review** workflow remains available; `.cbctreview` files include a series identifier and sensitive anatomical work and also require the matching original source.

**Clear Memory** in Viewer Controls releases generated segmentation, surfaces, reformat caches, and the inference model after active work finishes. It keeps the loaded source and accepted work and returns to MPR with its 3D view unloaded. Choose **Load 3D View** to resume; regenerate and explicitly review segmented surfaces before exporting again. It does not discard the loaded study or free every allocation.

**Close Study** clears the visible study immediately. If you then open another study, “Finishing current study work” means canceled processing is still releasing its source buffers before replacement loading starts. This avoids overlapping large study allocations. **Cancel** in the loading view stops reading a folder that was chosen by mistake; the study that was already open stays open.

## Siri and Spotlight

**Search Guide & Siri Topics** opens fourteen public app guides, including image enhancement and Implants. Siri and Shortcuts can open, search, and read these guides; Spotlight indexes only bundled public guide content. **Reset MPR View** requires the active MPR workspace, a loaded study, and no pending operation, drawing, or measurement. It resets pane focus and the MPR camera without changing records or approving an export. Patient data, filenames, pixels, measurements, saved states, and reviews are never donated to this public catalog. Availability depends on device, OS, language, and Apple settings.

Public support: https://sansar7.github.io/medical-app-support/cbct/index.html

Privacy policy: https://sansar7.github.io/medical-app-support/cbct/privacy.html

## Language and text feedback

The source updated on October 26, 2026 supports **English only**. This change takes effect in builds made from that source; previously installed or submitted builds retain their bundled languages. Interface text and app-authored help work offline. Imported content, filenames, patient data, annotations and saved identifiers are not translated. Measurements, physical geometry and file formats keep their existing definitions.

For a wording or layout issue, include the app version, OS version, screen name, exact app-authored wording and expected wording. Use a synthetic example and remove private content from screenshots. Siri availability and external support pages depend on Apple settings and their own language support.
