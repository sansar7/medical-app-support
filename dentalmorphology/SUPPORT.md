# ToothForm: Dental Anatomy 3D Support

Updated October 15, 2026. ToothForm: Dental Anatomy 3D (ToothForm) is a prototype educational 3D tooth atlas for dental students. It is not on the App Store yet. This page describes the current source and local builds containing the October 15 model and reliability changes. The **1.0 (4)** builds prepared in App Store Connect on October 14 predate these changes; newer local builds can still display the same version and build number. The app's display name and Mac application menu use **ToothForm**.

Email: **sansargupta10@gmail.com**

Supported platforms: iPhone and iPad with iOS/iPadOS 26 or newer, and Macs with Apple silicon (M-series) running macOS 26 or newer. Intel Macs are not supported.

For a problem report, include the app version and build, whether it is a developer-provided local build, device model, operating system version, the tooth or specimen you were viewing, and the steps that led to the issue. A screenshot can help. Do not send patient information.

## Exploring the atlas

The app opens on a complete permanent dentition. Tap or click a tooth, or use **Choose tooth**, to study it. **All teeth** returns to the full arch, and the reset button restores the camera.

Right and left in tooth names refer to the patient's anatomical sides, regardless of how you rotate the view. The patient's lower-right central and lateral incisors are **#25 (FDI 41)** and **#26 (FDI 42)**; the lower-left counterparts are **#24 (FDI 31)** and **#23 (FDI 32)**. **About this model** explains the source specimen and any mirrored or representative placement.

| | Rotate | Move | Zoom |
|---|---|---|---|
| Mac | Drag | Right-drag, Option-drag, middle-drag, or Shift-scroll | Scroll or pinch on the trackpad, toward the pointer |
| iPhone and iPad | Drag with one finger | Drag with two fingers; on iPad, also a trackpad two-finger scroll or a secondary-button drag | Pinch, toward your fingers; on iPad, also a mouse wheel, toward the pointer |

A rotation glides briefly after you let go, except with Reduce Motion. A tap or click that stops a moving model does not open a tooth. Reset and opening another tooth cancel the previous drag, pinch or trackpad scroll, including its remaining glide. Start a new gesture to move the newly fitted model.

Each numbered position shows separately segmented enamel, dentin and pulp from a micro-CT specimen. Use **Enamel**, **Dentin** and **Pulp** to show or hide each tissue without moving the model; hide enamel and dentin to inspect the pulp chamber and canals. **Tissue opacity**, near the top of a tooth's details, has a slider for each tissue: lower the dentin's opacity, for example, to see the canals inside the root. 0% hides a tissue. Opacity applies to the standard view; with ray tracing on, shown tissues are opaque. **Additional scan specimens** at the end of a tooth's details opens four separate micro-CT demonstrations. Two of them offer **Endo**, which isolates that specimen's own pulp.

On a Mac, and on an iPad with a hardware keyboard, the **Atlas** menu lists every tooth and specimen. Escape returns to all teeth, Command-0 resets the camera, Command-= and Command-− zoom, Command-Option-arrow keys rotate and tilt, and Shift-Command-R opens Sources & credits.

## What the models and colors represent

Each model is an individual anatomical example, not a standard for every patient. Some positions are mirrored counterparts or class examples where the source does not document the original side; the app labels these. The sources include author-prepared tissue surfaces and locally inferred automatic segmentations; the complete atlas has not been reviewed by an anatomy educator or endodontist. Some prototype display surfaces also use inferred repair or simplification. Fine apical anatomy and fissure detail may be incomplete, and the models are not a calibrated measurement tool.

The lower-incisor teaching models use reviewed patient-right placements at **#25/#26** and explicit patient-left mirrors at **#24/#23**, with all three tissues kept together. The source authors label those original forms as left-sided; the app discloses their reviewed right-side placement. The source also contains repeated central/lateral enamel forms. These reviewed placements retain that limitation and do not establish distinct, independently verified central- and lateral-incisor anatomy.

The Root Canal Anatomy Project (RCAP) upper-premolar specimens do not document their original side, so their four positions remain class representatives. The six ACTA-DIRECT specimens used for twelve positions do not document tooth class or side; those were inferred as imaged during an in-house review. Their source notes disclose that uncertainty for each placement, including the mirrored counterparts. The lower first molars **#19/#30** now use the two-rooted ACTA-DIRECT tooth 0039, with its short roots and other source limits disclosed in About this model.

Enamel and dentin colors and translucency are an illustrative rendering. The shading uses thickness estimates ray-cast from each display mesh and published optical data with calibrated display constants; those estimates are not independently measured enamel thickness. Micro-CT records structure, not the tooth's real color. Enamel is shown slightly whiter than dentin to make the tissues easy to tell apart.

On devices with Metal ray tracing and Apple GPU family 9 or newer, a **Ray tracing** switch appears in every tooth study with enamel, dentin and pulp layers; the full arch always uses the standard view. It draws the same view with ray-traced lighting, light scattering in enamel and dentin, and the gloss of wet enamel. This is also an illustrative rendering, not a measured color. The standard view is the default and returns automatically if ray tracing stops. On slower graphics, the standard view shows while the model moves and the ray-traced image returns once it is still. The choice stays with the window as you move between teeth, including through the full arch, and resets when the window closes. Ray-tracing performance on iPhone and iPad has not yet been verified on devices.

Anatomy summaries and canal-configuration percentages come from cited textbooks, university teaching resources and research studies. Percentages describe study populations, not a particular patient. Sources & credits lists every reference and model source; textbook and course-note full texts and images are not bundled or offered for download.

## Licensing and model notices

The [Licensing and model notices](LICENSES.md) page explains the distinction between ToothForm's original application-code rights and the independent licenses or permission requirements of its model sources. It provides all 14 bundled model notices as readable pages and unchanged text copies, with historical and upstream notices identified separately. These documents preserve source-license rights; they do not supply missing redistribution permissions or amend the selected App Store EULA.

## Accessibility

Every tooth can be chosen from a list, without using the 3D view. VoiceOver reads tooth names and layer states, and the 3D view offers rotate, tilt, move, zoom and Reset View actions. The app follows Reduce Motion, Reduce Transparency, Increase Contrast and Dynamic Type.

## Troubleshooting

- **"3D model unavailable"**: choose another tooth or reopen the app. If it persists, reinstall the app and send a report.
- **The model looks too small or off-center** after rotating or resizing: press the reset button.
- **A tooth takes a moment to appear**: detailed specimens are large and load in the background the first time they are opened.
- **No Ray tracing switch**: open a layered tooth study on supported graphics hardware. The full arch and the two combined-hard-tissue demos use the standard view.
- **Rendering was interrupted while the app was inactive**: the standard view remains available. After a temporary system refusal of ray-tracing work, ray tracing retries when the window can draw again, keeping the camera and the window's choice. If it reports a permanent failure, continue in the standard view and include the message in a report.
- **A side or shape looks wrong**: use Reset camera, confirm the tooth number, and read About this model. Include the tooth number and viewing angle in a report so the displayed orientation can be checked against its source.

## Privacy

The atlas works offline and sends no app data to the developer. Tooth selections, tissue opacity, ray-tracing choices and camera positions are local to the window; a generated lighting cache contains no personal data. Optional web links and support email are covered in the [privacy policy](PRIVACY_POLICY.md).
