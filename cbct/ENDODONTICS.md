# Endo Workspace

Endo adds a tooth-region source review workflow on Mac, iPhone, and iPad. It uses
the STSR26 Dataset513 PulpSegPretrain checkpoint requested for this workspace.
The checkpoint predicts whole-tooth and pulp regions independently. TIPs is not
part of this implementation.

## Workflow

1. Open the original DICOM study and choose **Endo** (Command-5 on Mac).
2. Align the crosshairs on the tooth, set the target, and enter a tooth identifier.
   Adjust the region to include the tooth. The target is manually localized;
   the app does not assign or verify a tooth number.
3. Run **Segment Tooth & Pulp**. The bundled Core ML model runs locally.
4. Compare the colored masks with the acquired axial, coronal, and sagittal
   slices. Optional Super Resolution and Metal Artifact Reduction apply while
   navigating; **Show Original** compares the same acquired slice instantly.
   Painting, erasing, or placing canal points displays **Original · editing**
   and uses the acquired single slice. Paint or erase masks as needed; undo and restoration of the original
   prediction are available. The 3D view shows tooth and pulp independently.
5. Record manual canal paths, a reference landmark, and review notes. A path's
   length is the sum of straight segments between the placed 3D points in
   millimetres. It is not an established working length.
6. Review the current result and export separate tooth and pulp STL objects
   with a JSON record of geometry, model provenance, edits, traces, and notes.
7. Use **Save State** or **Save State Copy** to retain the workspace. Reopening
   requires the matching original scan. Export approval is never restored.

Replacing a target or region with existing masks or traces requires explicit
confirmation. Mask edits and changes to recorded information invalidate export
review. Closing or replacing a study cancels pending work.

Wide windows show the inspector beside all four views. On iPhone and narrow
windows, use the **Axial / Coronal / Sagittal / 3D** picker for the full-width
view and **Controls** for target, trace, and review settings. On iPhone and iPad,
backgrounding cancels pending inference at the next prediction boundary;
returning to the same study resumes it after the cancelled work has drained.
Explicit cancellation and changing studies discard that pending restart.

## Model and Geometry

- Upstream: [STSR26](https://github.com/longls1810/STSR26-nnUNet-for-Teeth-and-Pulp-Segmentation),
  commit `f2af8d41cb1d1760ce9009befa0117f2ed4706b0`.
- Checkpoint SHA-256: `13180dc59f3e28cd0fabe8b07947abf5052a9f6d8cac327a8802adf986a8d094`.
- Single-tooth stage: `Dataset513_PulpSegPretrain`, `3d_fullres`, `fold_all`,
  `checkpoint_best.pth`; 0.3 mm model sampling, YZX patch shape 56 x 88 x 48.
- User localization replaces the upstream jaw and numbered-tooth cascade.
  This is an adaptation of the single-tooth stage, not the complete 64-class
  pipeline. Neighboring teeth can be included and require manual review.
- Native preprocessing adds 2 mm context where scan coverage allows,
  resamples in canonical LPS coordinates, normalizes the crop, and blends
  overlapping model logits. Predictions map back to the original source ROI.
- Every editing pane uses one acquired source slice, independent of MPR slab
  thickness or image-enhancement previews. Navigation previews use a separate
  display layer; segmentation, mask edits, traces, 3D surfaces, and exports retain
  source geometry and source-based masks. Original DICOM pixels are unchanged.
- Mesh coordinates are millimetres in the DICOM patient LPS frame. Native mask
  sampling, crop boundaries, and source geometry remain part of the export.
- Numerical conversion checks compare Core ML against the original PyTorch
  checkpoint. They do not measure anatomical accuracy.

The reproducible converter is `Tools/Endodontics/convert_stsr26.py`. Python is
development tooling only. The app uses its bundled model without a Python
install, server, account, or network access.

## Interpretation and Privacy

No expert reference masks were supplied for the example studies. Predicted
chambers, fine branches, and apical or accessory canals can be incomplete or
incorrect. Metal, motion, scan resolution, and cropping affect the result.
Disconnected pieces are not a canal count, and a missing prediction does not
establish absence of a canal. A smaller output voxel pitch cannot create
anatomical information absent from the source.

Pulp predicted outside the independent tooth region is preserved and reported
for review. Pulp contacting the ROI boundary is flagged because exported crop
surfaces can be artificially closed. No automatic bridging or invented canal
completion is performed.

Saved states and reviews contain Endo masks and user-authored text as well as
sensitive anatomical geometry. Text can identify a person. Endo exports do not
automatically copy DICOM demographics, but they are not anonymized records.
The workspace is experimental and has not been validated for diagnosis, access
preparation, or treatment decisions. Upstream's MIT license is preserved;
its README also describes research and academic use.

## Verification

See the [October 9 Endo validation record](history/ENDODONTICS_VALIDATION_2026-10-09.md)
for completed native tests, example-scan checks, visual inspection, and their
limitations. Current verification is in [STATUS.md](../STATUS.md).
