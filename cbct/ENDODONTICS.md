# Endo Workspace

Endo adds a tooth-region source review workflow on Mac, iPhone, and iPad. It uses
the STSR26 Dataset513 PulpSegPretrain checkpoint requested for this workspace.
The checkpoint predicts whole-tooth and pulp regions independently. TIPs is not
part of this implementation. This reference describes the October 26 source,
including canal-point editing, grouped Undo/Redo, canal-distance readouts and
bounded STL serialization; [STATUS.md](../STATUS.md) records exact verification
and delivery evidence. The interface and guide text are English only.

## Workflow

1. Open the original DICOM study and choose **Endo** (Command-5 on Mac).
2. Align the crosshairs on the tooth, set the target, and enter a tooth identifier.
   Adjust the region to include the tooth. The target is manually localized;
   the app does not assign or verify a tooth number.
3. Run **Segment Tooth & Pulp**. The bundled Core ML model runs locally.
4. Compare the colored masks with axial, coronal and sagittal slices of the
   current unenhanced study grid. Optional Super Resolution and Metal Artifact Reduction apply while
   navigating; **Show Original** compares the same current-grid slice without enhancement.
   Painting, erasing, or placing canal points displays **Original · editing**
   and uses one unenhanced current-grid slice. Paint or erase masks as needed; undo and restoration of the original
   prediction are available. The 3D view shows tooth and pulp independently.
5. Record manual canal paths, a reference landmark, and review notes. A path's
   length is the sum of straight segments between the placed 3D points in
   millimetres. It is not an established working length. With the Trace tool,
   pressing a point on a slice selects it, dragging moves it (the path changes
   when the drag ends), tapping between two points on the same slice inserts a
   point there, and tapping elsewhere adds one at the end. The inspector steps
   through the points, inserts after the selected point at the crosshair,
   deletes the selected point (also the Delete key on Mac) and removes the
   last point. The 3D view marks the selected point.
6. Review the current result and export separate tooth and pulp STL objects
   with a JSON record of geometry, model provenance, edits, traces, and notes.
7. Use **Save State** or **Save State Copy** to retain the workspace. Reopening
   requires the matching original scan. Export approval is never restored.

Before volume reorientation, the current grid is the acquisition grid. After
reorientation, every workspace, including Endo, uses the resampled derived grid.
**Show Original** and **Original · editing** mean unenhanced pixels of that
current grid; they do not restore acquired slices. Use **Reset to Source** in
Volume Orientation if you want to return to the acquisition grid. Reset follows
the same confirmation and work-replacement rules as reorientation.

Replacing a target or region with existing masks or traces requires explicit
confirmation. Mask edits and changes to recorded information invalidate export
review. Closing or replacing a study cancels pending work.

Undo and Redo are one grouped history for the workspace: a brush stroke, a
placed, inserted, moved, deleted or removed trace point, a new or deleted
trace, and a change to a trace's name or landmark (typing into one field is
one step) are undone in the order they were made. A new prediction or Restore
Prediction drops the mask steps and keeps the trace steps; replacing the
target drops both.

**Distance to the nerve canal.** When an inferior alveolar canal has been
traced in Slice & Panorama and the tooth is segmented, the Target tab's Nerve
Canal Distance shows, for each traced canal, the closest distance from the
tooth mask boundary to that canal's radius envelope
(`CanalCenterline.clearance(from:)`), in the volume's millimetre frame. The
boundary is every tooth voxel (tooth or pulp label) with a six-neighbour
outside the mask or on a face of the region; the search bounds each voxel by
its distance to boxes around 4 mm runs of the centreline and evaluates the
exact clearance in that order, so it gives the same minimum as an exhaustive
search in a fraction of the time. When the boundary touches or enters the
envelope the readout says "0.0 mm (within the canal envelope)". The
measurement runs off the main actor, is superseded by a mask edit or a canal
change, and is recorded nowhere: it is not part of the saved state, the
review or the export. Show Where moves the three slices to the tooth point and
marks both points on the slice overlays, with the measured segment projected
onto each plane, until the slices move again. It is a geometric distance
between two reviewed geometries, not a validated safe distance, and nothing
in the workspace judges it.

Paint and erase sweep the selected physical-radius brush between accepted
pointer samples on the same current-grid slice. Unequal column, row and slice
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
view and **Controls** for target, trace, and review settings. The compact Controls
sheet keeps segmentation progress and Cancel above the inspector while work
runs. On iPhone and iPad,
backgrounding requests cancellation of pending inference and postprocessing;
returning to the same study starts it again from the beginning after the
cancelled work has drained.
Explicit cancellation and changing studies discard that pending restart.

Mask overlays rasterize off the UI actor and retain only the target region's
pixels, positioned on the current-grid slice without changing its geometry or
colors. Hidden slice panes cancel and release their overlays; source, slice,
mask revision and visibility checks reject obsolete results. Brush commits
and undo update tooth, pulp and edit counts from the changed indices rather
than recounting the entire region. Component floods, contact splitting, pulp
closing and source-grid mapping observe cancellation in addition to the
prediction and minimum-cut boundaries. Current synthetic verification and
performance limits are recorded in [STATUS.md](../STATUS.md).

## Model and Geometry

- Upstream: [STSR26](https://github.com/longls1810/STSR26-nnUNet-for-Teeth-and-Pulp-Segmentation),
  commit `f2af8d41cb1d1760ce9009befa0117f2ed4706b0`.
- Checkpoint SHA-256: `13180dc59f3e28cd0fabe8b07947abf5052a9f6d8cac327a8802adf986a8d094`.
- Single-tooth stage: `Dataset513_PulpSegPretrain`, `3d_fullres`, `fold_all`,
  `checkpoint_best.pth`; 0.3 mm model sampling, YZX patch shape 56 x 88 x 48.
- User localization replaces the upstream jaw and numbered-tooth cascade.
  This is an adaptation of the single-tooth stage, not the complete 64-class
  pipeline. The target point decides which tooth is kept, so center it on the
  tooth.
- Native preprocessing adds 2 mm context where scan coverage allows and
  resamples in canonical LPS coordinates. Each model crop is z-scored on its
  own (the checkpoint's `ZScoreNormalization`), and overlapping tiles are
  blended with nnU-Net's Gaussian weights. Each tile is predicted once; there
  is no test-time mirroring, matching the upstream script's `--disable_tta`.
- **Target tooth (since October 15, 2026).** The released stage was trained on
  crops of one tooth: its bounding box plus 2 mm, which is about
  14 × 16 × 25 mm (left–right × anterior–posterior × superior–inferior). Given a 24 mm or larger region, it also segments
  neighbouring teeth, and sometimes bone or soft tissue, as "tooth". The app
  therefore runs it in passes:
  1. A tooth-sized crop centred on the target (up to 20 × 20 × 28 mm, long
     axis superior–inferior, inside the region) is predicted, and the piece
     at the target (or within 3 mm of it) is chosen. Starting from this crop
     rather than the whole region keeps a large region from pulling in bone
     and neighbouring teeth.
  2. That piece's bounding box plus 2 mm is cropped, normalized on its own and
     predicted again, like the upstream crop. The piece at the target is kept.
  3. Step 2 repeats until the crop stops changing (up to six crops; most
     teeth settle after one or two). This
     separates a neighbour that the first pass merged and regrows a root an
     earlier crop cut.
  4. After every pass, teeth joined at a contact are separated by eroding the
     piece up to 1.8 mm until it falls apart into tooth-sized parts (at least
     25 mm³). Each voxel then goes back to the part it reaches first, and the
     part at the target is kept. A single tooth whose thin roots erode first
     stays whole.
  5. An opposing crown joined where the teeth bite together touches over too
     broad an area for erosion. When the piece holds a second pulp chamber (a
     predicted pulp piece of at least 2 mm³ besides the target's), the app
     finds the cheapest surface separating the two pulps (a minimum cut).
     Cutting through a voxel costs more the brighter it is, from the target
     pulp's level up to the tooth's median, so the cut follows the darker seam
     where the crowns meet and crosses enamel only at real contacts. The far
     side is removed only when the cut ran mostly through that seam (mean cost
     at most half that of tooth tissue), holds at least 25 mm³ and lies on the
     target's occlusal side. The occlusal side is where the target pulp is
     widest, because the chamber sits in the crown. A cut that would keep the
     other tooth and drop the target is refused. A part removed this way stays
     removed in later passes, so a tighter crop that no longer holds the
     opposing pulp cannot merge that crown back. A multi-rooted tooth stays
     whole: its canal fragments are small, lie on the apical side, and a cut
     to them runs through dentin. *(Since October 15, 2026.)*
  6. Pulp is kept only inside the kept tooth and closed once with a
     six-connected closing, as upstream `06_postprocess_pulp_connectivity.py`
     does.
  7. Everything else the first pass predicted is removed, and the review
     warning reports its volume. When no tooth lies near the target, the
     result is empty and the review asks you to center the target on the tooth.
- **Source resolution.** The blended logits are linearly resampled to the
  scan's own voxels and then thresholded, as nnU-Net exports a prediction.
  Boundaries therefore fall between model voxels instead of on the 0.3 mm grid
  faces. The interpolation stays within one model voxel of the kept tooth and
  pulp, and only the source piece that overlaps the model-grid tooth is kept.
  Where a neighbour or opposing crown was cut away in the final pass, the
  boundary stays at the cut instead of reaching back into the removed side.
  Pulp specks under 0.1 mm³ (about four model voxels) that the resampling
  leaves return to tooth; every larger pulp piece is kept. This does not add
  anatomical detail the model did not predict.
- Every editing pane uses one unenhanced current-grid slice, independent of MPR slab
  thickness or image-enhancement previews. Navigation previews use a separate
  display layer; segmentation, mask edits, traces, 3D surfaces, and exports retain
  source geometry and source-based masks. Original DICOM pixels are unchanged.
- Mesh coordinates are millimetres in the DICOM patient LPS frame. Native mask
  sampling, crop boundaries, and source geometry remain part of the export.
  STL serialization transforms vertices into that frame in its bounded facet
  buffer and derives each face normal there, avoiding a second full copy of
  the mesh's vertex and shading-normal buffers.
- Tooth and pulp surfaces follow the Surface Export **Surface** setting, and the
  3D pane and the export always use the same one. **Smooth** (the default)
  smooths and simplifies each surface, puts back local shrinkage and caps each
  piece's volume change at 10%. Vertices move at most 0.25 mm from the
  unsmoothed extracted surface, plus at most about 0.03 mm from
  simplification; because that extracted surface already cuts voxel corners,
  the result can lie about 0.3 mm (0.15 mm voxels) to 0.4 mm (0.4 mm voxels)
  from the voxel-mask boundary. Since October 15, 2026, the smoothed surface
  is then moved onto the CT's own edge before simplification, as the jaw
  surfaces are: up to 0.35 mm along the surface normal, wherever the image
  shows one clear edge (for the pulp, the dentin wall around it). Where it
  does not (a narrow canal, a thin wall, another structure just beyond,
  enamel or metal much brighter than the rest), the surface holds still.
  Voxels you painted or erased vote to stay, so the move fades out near them,
  but beside a narrow edit (one or two brush slices) a vertex can still take
  up to about half of its neighbours' move. Where it
  follows the CT edge it can therefore lie up to about 0.75 mm from the
  voxel-mask boundary. No piece is removed or bridged; the tooth's enclosed
  voids are filled (they have no surface), and the masks are unchanged.
  **Exact voxels** keeps the unsmoothed source-grid surface. Changing the
  setting clears the Endo surfaces and the Endo review; the surfaces are rebuilt
  at once in Endo, or when Endo is next opened.
  Long enclosed-void traversals check cancellation within the flood, so closing,
  replacement and cancellation can stop that stage before it finishes.
  `endodontic-summary.json` (schema 5) records the style and each surface's
  settings, triangle counts and CT-edge refinement (`edgeRefinement`: vertices
  moved and their mean move); its `model` block keeps the model provenance
  and warnings. The Endo saved state is schema 3. Endo saved states from
  earlier versions (including schema 2, which recorded mirrored inference) are
  rejected as invalid instead of being migrated.
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

Predictions outside the target tooth, including pulp outside it, are removed
and their volume is reported for review. Pulp or tooth touching the region
boundary is flagged because the region can truncate the tooth and exported crop
surfaces can be artificially closed; enlarge the region and run again. Apart
from the upstream one-voxel pulp closing, no bridging or invented canal
completion is performed.

Saved states and reviews contain Endo masks and user-authored text as well as
sensitive anatomical geometry. Text can identify a person. Endo exports do not
automatically copy DICOM demographics, but they are not anonymized records.
The workspace is experimental and has not been validated for diagnosis, access
preparation, or treatment decisions. Upstream's MIT license is preserved;
its README also describes research and academic use.

## Verification

The public verification record is limited to synthetic engineering checks and implementation limits. Regression tests exercise target-region geometry, editing and undo behavior, cancellation, surface preparation and export. The current Endo STL serializer uses bounded output buffers; synthetic triangle fixtures verified byte parity and source-buffer preservation. These checks establish software behavior for those fixtures, not anatomical accuracy, clinical performance, or equivalence to another viewer.

The tooth/pulp model and CT-edge refinement require independent evaluation on appropriately authorized data with expert reference annotations. No reference-based diagnostic accuracy or treatment-planning validity is established. Physical-device memory, thermal behavior and learned-inference performance remain separate checks. Private study-derived evaluation details are excluded from public support documentation. [STATUS.md](../STATUS.md) records dated engineering runs and their scope.

**October 14 audit.**

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
