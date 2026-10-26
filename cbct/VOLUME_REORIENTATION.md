# Volume reorientation

Reorient Volume rotates the study grid about the volume centre so axial slices follow the occlusal plane and the midline is vertical. It is a display and review convenience on a derived grid; it changes no source voxel and establishes no measurement accuracy. The app remains not validated for diagnostic use.

Before reorientation, the current study grid is the acquisition grid. After Apply, every workspace uses the resampled derived grid, including Endo segmentation, editing and canal points. **Show Original** disables an enhancement preview and shows the unenhanced current-grid image; it does not reverse reorientation or recover an acquired slice. **Reset to Source** rereads the original files and restores the acquisition grid, subject to the confirmation and work-replacement rules below.

## Design

- **Resampled derived volume, not oblique sampling.** `Services/VolumeReorientation.swift` builds a new `DICOMVolume` from the acquisition: isotropic voxels at the finest source spacing (rotation mixes the axes, so any per-axis spacing would undersample the finest one; for the usual isotropic CBCT the spacing is unchanged), a grid that holds the whole rotated extent centred on the source centre, trilinear samples, and a padding value for voxels outside the acquisition. Every workspace (MPR, Slice & Panorama, Endo, Surface Export, Implants, Media Export) consumes the model's volume unchanged, and Endo edits the unenhanced resampled grid.
- **Angles.** `Models/VolumeReorientationSettings.swift` holds pitch (about the patient's left–right axis), roll (anterior–posterior) and yaw (superior–inferior) in degrees, ±45°, kept to 0.1°. They compose as `Rz(yaw) · Rx(pitch) · Ry(roll)` in DICOM LPS coordinates; the new grid's axes are the acquisition's axes rotated by that matrix. Matrix entries within 1e-12 of 0 or ±1 are snapped, so a quarter turn permutes axes exactly and zero angles are the identity.
- **Geometry.** The derived `DICOMSeriesInfo` carries the new Image Orientation (row and column directions) and the Image Position of its first voxel, so direction labels, `AnatomicalFrame`, millimetre readouts, arch extraction, segmentation geometry and Enhanced CT export stay correct. Frame of Reference UID, identity, rescale and window values are kept.
- **Padding.** A study with pixel padding keeps it, and outside voxels take its value. Otherwise a stored value one step beyond the image on the air side becomes declared padding (`PixelPadding`), so the default window, histogram, 3D texture and Media Export bone statistics leave the fill out exactly as they do a scanner's. When the image already reaches the end of the encoding, that end is shared with the darkest image voxels, which the statistics then also skip; the renderer draws them unchanged.
- **Determinism.** The resample is per voxel in fixed-order Double and Float arithmetic without reductions, so the same angles rebuild the same voxels on every supported device.
- **Memory.** The resample actively samples the acquisition and writes the new derived volume. On iPhone and iPad the derived size plus a 256 MB reserve must fit `os_proc_available_memory()`, or the sheet refuses with the sizes; a Mac proceeds. Derived grids always use the same unlinked, preallocated file backing as large imports. Before replacing an existing derived grid, its mapped pages are synchronously flushed and invalidated after readers drain. The mapping remains available for rollback while the acquisition and replacement are processed; the operating system controls residency, so this is not a strict two-buffer peak-RSS guarantee. Each new grid is sampled once from the acquisition.

## Lifecycle

Apply runs through `ViewerModel.openStudy` with an acquisition loader and a transform that finishes before `install`. The `StudyWorkBarrier` drains, heavy work is cancelled, and caches and textures are released. Grid bounds and live mobile-memory preflight run before I/O and again before resampling. A failed acquisition read, rejected grid, failed transform or cancellation keeps the previous voxel storage and its anchored work, including saved views, report notes, imported implant bodies and Undo history. Cancellation and request ownership are checked again before publication, so a superseded worker cannot replace a newer study. No separate saved-state checkpoint is needed.

Only a completed replacement calls `install` and removes work anchored to the old grid. Display settings and the window (window, inversion, brightness, gamma, slabs, projections, surface style and detail, volume preset and opacity, crosshairs, canals, an operator-set bone threshold, enhancement options and the workspace) are carried over; slice indices and viewports start centred on the new grid. Successful Apply and Reset remain unsaved changes.

Apply shows a confirmation naming what the new grid removes: measurements, canal traces, arches, dental segmentation with its edits and reviews, Endo work and the implant plan. Cancel changes nothing. Reset to Source reads the acquisition again through the same path, without applying the folder's saved state.

## Save State

`StudySaveState.reorientation` stores the angles and the resampling rule as an optional field; states without it decode as before. The state's `geometry` and `sourceDigest` describe the grid the state was saved on. On restore, after the acquisition decodes, the stored reorientation is read first (`StudySaveState.reorientation(in:)`), the grid is rebuilt (memory check included), the reoriented volume is installed and only then are the fingerprint and geometry compared and the rest restored against that grid. If the state does not match, the acquisition is shown with default views and the usual "saved state not applied" message. Review files (`.cbctreview`) carry no reorientation; a review saved on a reoriented grid opens only while that grid is active.

## Suggestion

`Services/VolumeReorientationSuggestion.swift` fits the occlusal plane as the least-squares plane through the occlusal contacts: in every grid column that holds teeth of both jaws, the midpoint between the lowest upper-tooth voxel and the highest lower-tooth voxel (columns with a gap over 15 mm are skipped; at least 40 are needed). The midline follows the long axis of all teeth voxels projected onto that plane, which estimates the arch chord without depending on the distal-most teeth. The fitted frame is converted to pitch, roll and yaw relative to the acquisition. It is a starting point the operator reviews and edits, not an anatomical landmark analysis.

## Limits

- Resampling interpolates; a reoriented slice is not an acquired slice, and millimetres remain the study's geometry.
- The rotated extent grows with the angles (about 1.17× per axis at 10°), so a large rotation costs memory and time.
- Reviews are grid-specific; segmentation runs again on the new grid.
- Reset to Source re-reads the study, so the source file or folder must still be reachable.
