# ToothForm: Dental Anatomy 3D Support

Updated October 14, 2026. ToothForm: Dental Anatomy 3D (ToothForm) is a prototype educational 3D tooth atlas for dental students. It is not on the App Store yet; this page describes builds that contain the October 2026 changes. The app's display name and Mac application menu use **ToothForm**.

Email: **sansargupta10@gmail.com**

Supported platforms: iPhone and iPad with iOS/iPadOS 26 or newer, and Macs with Apple silicon (M-series) running macOS 26 or newer. Intel Macs are not supported.

For a problem report, include the app version and build, device model, operating system version, the tooth or specimen you were viewing, and the steps that led to the issue. A screenshot can help. Do not send patient information.

## Exploring the atlas

The app opens on a complete permanent dentition. Tap or click a tooth, or use **Choose tooth**, to study it. **All teeth** returns to the full arch, and the reset button restores the camera.

| | Rotate | Move | Zoom |
|---|---|---|---|
| Mac | Drag | Right-drag, Option-drag, middle-drag, or Shift-scroll | Scroll or pinch on the trackpad, toward the pointer |
| iPhone and iPad | Drag with one finger | Drag with two fingers; on iPad, also a trackpad two-finger scroll or a secondary-button drag | Pinch, toward your fingers; on iPad, also a mouse wheel, toward the pointer |

A rotation glides briefly after you let go, except with Reduce Motion. A tap or click that stops a moving model does not open a tooth.

Each numbered position shows separately segmented enamel, dentin and pulp from a micro-CT specimen. Use **Enamel**, **Dentin** and **Pulp** to show or hide each tissue without moving the model; hide enamel and dentin to inspect the pulp chamber and canals. **Tissue opacity**, near the top of a tooth's details, has a slider for each tissue: lower the dentin's opacity, for example, to see the canals inside the root. 0% hides a tissue. Opacity applies to the standard view; with ray tracing on, shown tissues are opaque. **Additional scan specimens** at the end of a tooth's details opens four separate micro-CT demonstrations. Two of them offer **Endo**, which isolates that specimen's own pulp.

On a Mac, and on an iPad with a hardware keyboard, the **Atlas** menu lists every tooth and specimen. Escape returns to all teeth, Command-0 resets the camera, Command-= and Command-− zoom, Command-Option-arrow keys rotate and tilt, and Shift-Command-R opens Sources & credits.

## What the models and colors represent

Each model is an individual anatomical example, not a standard for every patient. Some positions are mirrored counterparts or class examples where the source does not document the original side; the app labels these. The sources include author-prepared tissue surfaces and locally inferred automatic segmentations; the complete atlas has not been reviewed by an anatomy educator or endodontist. Some prototype display surfaces also use inferred repair or simplification. Fine apical anatomy and fissure detail may be incomplete, and the models are not a calibrated measurement tool.

Enamel and dentin colors and translucency are an illustrative rendering. The shading uses thickness estimates ray-cast from each display mesh and published optical data with calibrated display constants; those estimates are not independently measured enamel thickness. Micro-CT records structure, not the tooth's real color. Enamel is shown slightly whiter than dentin to make the tissues easy to tell apart.

On devices whose graphics support hardware ray tracing, a **Ray tracing** switch appears in the full arch and in every study with enamel, dentin and pulp layers. It draws the same view with ray-traced lighting, light scattering in enamel and dentin, and the gloss of wet enamel. This is also an illustrative rendering, not a measured color. The standard view is the default and returns automatically if ray tracing stops. In the full arch, and in a study on slower graphics, the standard view shows while the model moves and the ray-traced image returns once it is still. Ray-tracing performance on iPhone and iPad has not yet been verified on devices.

Anatomy summaries and canal-configuration percentages come from cited textbooks and studies. Percentages describe study populations, not a particular patient. Sources & credits lists every reference and model source.

## Accessibility

Every tooth can be chosen from a list, without using the 3D view. VoiceOver reads tooth names and layer states, and the 3D view offers rotate, tilt, move, zoom and Reset View actions. The app follows Reduce Motion, Reduce Transparency, Increase Contrast and Dynamic Type.

## Troubleshooting

- **"3D model unavailable"**: choose another tooth or reopen the app. If it persists, reinstall the app and send a report.
- **The model looks too small or off-center** after rotating or resizing: press the reset button.
- **A tooth takes a moment to appear**: detailed specimens are large and load in the background the first time they are opened.

## Privacy

The atlas works offline and sends no app data to the developer. Tooth selections, tissue opacity, ray-tracing choices and camera positions are local to the window; a generated lighting cache contains no personal data. Optional web links and support email are covered in the [privacy policy](PRIVACY_POLICY.md).
