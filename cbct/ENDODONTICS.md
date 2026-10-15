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

Paint and erase sweep the selected physical-radius brush between accepted
pointer samples on the same acquired slice. Unequal column, row and slice
spacing is respected, the stroke is clipped to the target region, and one
stroke produces one undo step. Erasing pulp returns those voxels to tooth;
erasing tooth preserves pulp. Samples from different source
planes or slices are never connected.

A change to the source, slice, target region, tool or brush settings before
release discards the pending gesture, even if the controls are later returned
to their original values. A gesture exceeding the point limit is also
discarded as a whole; release and start a shorter stroke. No retained prefix
is joined to the final release point after intermediate samples were dropped.

Wide windows show the inspector beside all four views. On iPhone and narrow
windows, use the **Axial / Coronal / Sagittal / 3D** picker for the full-width
view and **Controls** for target, trace, and review settings. On iPhone and iPad,
backgrounding cancels pending inference at the next prediction boundary;
returning to the same study starts it again from the beginning after the
cancelled work has drained.
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
- Every tile uses nnU-Net's mirrored test-time augmentation. The model runs
  on the tile and its seven mirrored copies, covering every combination of the
  three axes the checkpoint's default trainer allows. Each output is flipped
  back, and the logits are averaged before blending. This is always on and
  costs about eight times the single-pass model time. On October 12 on this Mac,
  three teeth in one example scan took 18–24 s with the default 24 mm region,
  compared with 2.4–3.2 s single-pass. The 36 mm maximum region took about 75 s.
  Mirroring reduced the tooth and pulp predicted outside the target tooth, and
  pulp inside the target tooth changed little. It does not establish accuracy
  (the app repository's `Tools/Endodontics/README.md` records the model notes). The upstream STSR26
  script runs this stage with `--disable_tta`, so the app follows nnU-Net's
  default predictor instead.
- Every editing pane uses one acquired source slice, independent of MPR slab
  thickness or image-enhancement previews. Navigation previews use a separate
  display layer; segmentation, mask edits, traces, 3D surfaces, and exports retain
  source geometry and source-based masks. Original DICOM pixels are unchanged.
- Mesh coordinates are millimetres in the DICOM patient LPS frame. Native mask
  sampling, crop boundaries, and source geometry remain part of the export.
- Tooth and pulp surfaces follow the Surface Export **Surface** setting, and the
  3D pane and the export always use the same one. **Smooth** (the default)
  smooths and simplifies each surface, puts back local shrinkage and caps each
  piece's volume change at 10%. Vertices move at most 0.25 mm from the
  unsmoothed extracted surface, plus at most about 0.03 mm from
  simplification; because that extracted surface already cuts voxel corners,
  the result can lie about 0.3 mm (0.15 mm voxels) to 0.4 mm (0.4 mm voxels)
  from the voxel-mask boundary. No piece is removed or bridged; the tooth's
  enclosed voids are filled (they have no surface), and the masks are unchanged.
  **Exact voxels** keeps the unsmoothed source-grid surface. Changing the
  setting clears the Endo surfaces and the Endo review; the surfaces are rebuilt
  at once in Endo, or when Endo is next opened.
  Long enclosed-void traversals check cancellation within the flood, so closing,
  replacement and cancellation can stop that stage before it finishes.
  `endodontic-summary.json` (schema 3) records the style and each surface's
  settings and triangle counts. Its `model` block and the Endo saved state
  (schema 2) record `mirroredInference`, which is true for every app run.
  Endo saved states from earlier versions are rejected as invalid instead of
  being migrated.
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

The October 14 audit added synthetic regressions for continuous paint/erase,
anisotropic brush radius, ROI clipping, plane changes, grouped undo and
cancellation during enclosed-void filling. The complete Mac suite passed
1,022 tests with 21 optional-input skips; the iPhone iOS 18.6 Simulator suite
passed 1,018 with 14 skips; targeted iPad simulator checks passed 148 with no
skips. All had zero failures. These checks do not establish the feel of the
final brush gesture on a physical device or clinical accuracy. No private study
was opened or enabled for this audit.

The app repository's `STATUS.md` and `docs/AUDIT_COVERAGE.tsv` record the exact
candidate, verification boundaries and per-file review. Its dated October 9
Endo validation record preserves earlier native tests, example-scan checks,
visual inspection and limitations; those private-study results were not rerun
by the October 14 audit.
